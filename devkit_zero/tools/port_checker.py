"""
端口检查工具
检查端口占用情况和对应进程
"""

import argparse
import socket
import subprocess
import sys
import os
from typing import List, Dict, Any, Optional


def check_port(host: str, port: int, timeout: int = 3) -> Dict[str, Any]:
    """
    检查端口是否被占用
    
    Args:
        host: 主机地址
        port: 端口号
        timeout: 连接超时时间
        
    Returns:
        端口检查结果
    """
    result = {
        'host': host,
        'port': port,
        'is_open': False,
        'is_listening': False,
        'process_info': None
    }
    
    # 检查端口是否可连接
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        connection_result = sock.connect_ex((host, port))
        sock.close()
        
        result['is_open'] = connection_result == 0
    except socket.error:
        result['is_open'] = False
    
    # 检查端口是否在监听
    try:
        if sys.platform.startswith('win'):
            # Windows 系统
            cmd = f'netstat -ano | findstr :{port}'
            output = subprocess.check_output(cmd, shell=True, text=True, encoding='gbk')
            if output:
                result['is_listening'] = True
                result['process_info'] = parse_windows_netstat(output)
        else:
            # Unix/Linux 系统
            cmd = f'netstat -tulpn | grep :{port}'
            output = subprocess.check_output(cmd, shell=True, text=True)
            if output:
                result['is_listening'] = True
                result['process_info'] = parse_unix_netstat(output)
    except subprocess.CalledProcessError:
        pass
    except Exception:
        pass
    
    return result


def parse_windows_netstat(output: str) -> List[Dict[str, str]]:
    """解析 Windows netstat 输出"""
    processes = []
    lines = output.strip().split('\n')
    
    for line in lines:
        parts = line.split()
        if len(parts) >= 5:
            pid = parts[-1]
            try:
                # 获取进程名
                cmd = f'tasklist /FI "PID eq {pid}" /FO CSV /NH'
                task_output = subprocess.check_output(cmd, shell=True, text=True, encoding='gbk')
                if task_output:
                    process_name = task_output.split(',')[0].strip('"')
                else:
                    process_name = "Unknown"
            except:
                process_name = "Unknown"
            
            processes.append({
                'pid': pid,
                'name': process_name,
                'protocol': parts[0],
                'local_address': parts[1],
                'state': parts[3] if len(parts) > 3 else 'N/A'
            })
    
    return processes


def parse_unix_netstat(output: str) -> List[Dict[str, str]]:
    """解析 Unix/Linux netstat 输出"""
    processes = []
    lines = output.strip().split('\n')
    
    for line in lines:
        parts = line.split()
        if len(parts) >= 7:
            pid_program = parts[-1]
            if '/' in pid_program:
                pid, program = pid_program.split('/', 1)
            else:
                pid = pid_program
                program = "Unknown"
            
            processes.append({
                'pid': pid,
                'name': program,
                'protocol': parts[0],
                'local_address': parts[3],
                'state': parts[5] if len(parts) > 5 else 'N/A'
            })
    
    return processes


def scan_ports(host: str, start_port: int, end_port: int) -> List[Dict[str, Any]]:
    """
    扫描端口范围
    
    Args:
        host: 主机地址
        start_port: 起始端口
        end_port: 结束端口
        
    Returns:
        开放端口列表
    """
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        result = check_port(host, port, timeout=1)
        if result['is_open']:
            open_ports.append(result)
    
    return open_ports


def get_common_ports() -> Dict[int, str]:
    """获取常见端口及其服务"""
    return {
        21: "FTP",
        22: "SSH", 
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        993: "IMAPS",
        995: "POP3S",
        1433: "SQL Server",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        6379: "Redis",
        8080: "HTTP Alt",
        8443: "HTTPS Alt",
        9200: "Elasticsearch",
        27017: "MongoDB"
    }


def format_port_result(result: Dict[str, Any]) -> str:
    """格式化端口检查结果"""
    lines = []
    
    host = result['host']
    port = result['port']
    
    # 获取常见端口服务名
    common_ports = get_common_ports()
    service = common_ports.get(port, "Unknown Service")
    
    lines.append(f"🌐 主机: {host}")
    lines.append(f"🔌 端口: {port} ({service})")
    
    if result['is_open']:
        lines.append("✅ 端口状态: 开放")
    else:
        lines.append("❌ 端口状态: 关闭或未响应")
    
    if result['is_listening']:
        lines.append("👂 监听状态: 正在监听")
        
        if result['process_info']:
            lines.append("\n📋 进程信息:")
            for proc in result['process_info']:
                lines.append(f"  • PID: {proc['pid']}")
                lines.append(f"  • 进程名: {proc['name']}")
                lines.append(f"  • 协议: {proc['protocol']}")
                lines.append(f"  • 本地地址: {proc['local_address']}")
                lines.append(f"  • 状态: {proc['state']}")
                lines.append("")
    else:
        lines.append("👂 监听状态: 未监听")
    
    return '\n'.join(lines)


def format_scan_results(results: List[Dict[str, Any]]) -> str:
    """格式化端口扫描结果"""
    if not results:
        return "❌ 扫描范围内没有发现开放的端口"
    
    lines = []
    lines.append(f"🔍 发现 {len(results)} 个开放端口:\n")
    
    common_ports = get_common_ports()
    
    for result in results:
        port = result['port']
        service = common_ports.get(port, "Unknown")
        lines.append(f"✅ 端口 {port} - {service}")
        
        if result['process_info']:
            for proc in result['process_info']:
                lines.append(f"    📋 {proc['name']} (PID: {proc['pid']})")
    
    return '\n'.join(lines)


def register_parser(subparsers):
    """注册 port-checker 命令的参数解析器"""
    parser = subparsers.add_parser('port', help='端口检查工具')
    
    subcommands = parser.add_subparsers(dest='action', help='操作类型')
    
    # 检查单个端口
    check_parser = subcommands.add_parser('check', help='检查指定端口')
    check_parser.add_argument('port', type=int, help='端口号')
    check_parser.add_argument('--host', default='localhost', help='主机地址 (默认: localhost)')
    check_parser.add_argument('--timeout', type=int, default=3, help='连接超时时间 (秒)')
    
    # 扫描端口范围
    scan_parser = subcommands.add_parser('scan', help='扫描端口范围')
    scan_parser.add_argument('--host', default='localhost', help='主机地址 (默认: localhost)')
    scan_parser.add_argument('--start', type=int, default=1, help='起始端口 (默认: 1)')
    scan_parser.add_argument('--end', type=int, default=1000, help='结束端口 (默认: 1000)')
    
    # 列出常见端口
    list_parser = subcommands.add_parser('list', help='列出常见端口')
    
    parser.set_defaults(func=main)


def main(args):
    """port-checker 工具的主函数"""
    try:
        if args.action == 'check':
            result = check_port(args.host, args.port, args.timeout)
            return format_port_result(result)
            
        elif args.action == 'scan':
            if args.end <= args.start:
                raise ValueError("结束端口必须大于起始端口")
            
            results = scan_ports(args.host, args.start, args.end)
            return format_scan_results(results)
            
        elif args.action == 'list':
            common_ports = get_common_ports()
            lines = ["🔌 常见端口列表:\n"]
            
            for port, service in sorted(common_ports.items()):
                lines.append(f"  {port:5d} - {service}")
            
            return '\n'.join(lines)
            
        else:
            raise ValueError("请选择操作类型: check, scan, list")
            
    except Exception as e:
        raise RuntimeError(f"端口检查失败: {e}")


if __name__ == "__main__":
    # 测试代码
    print("端口检查工具测试:")
    result = check_port('localhost', 80)
    print(format_port_result(result))
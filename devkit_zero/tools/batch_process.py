"""
批量文件处理工具
批量重命名、复制、移动文件
"""

import argparse
import os
import shutil
import glob
import re
from typing import List, Dict, Any, Optional
from pathlib import Path


def batch_rename(directory: str, pattern: str, replacement: str, 
                preview: bool = False, recursive: bool = False) -> List[Dict[str, str]]:
    """
    批量重命名文件
    
    Args:
        directory: 目标目录
        pattern: 匹配模式 (支持通配符或正则表达式)
        replacement: 替换字符串
        preview: 是否仅预览
        recursive: 是否递归处理子目录
        
    Returns:
        操作结果列表
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"目录不存在: {directory}")
    
    results = []
    
    if recursive:
        file_pattern = os.path.join(directory, '**', pattern)
        files = glob.glob(file_pattern, recursive=True)
    else:
        file_pattern = os.path.join(directory, pattern)
        files = glob.glob(file_pattern)
    
    for file_path in files:
        if os.path.isfile(file_path):
            dir_name = os.path.dirname(file_path)
            old_name = os.path.basename(file_path)
            
            # 使用正则表达式替换
            new_name = re.sub(pattern.replace('*', '.*'), replacement, old_name)
            new_path = os.path.join(dir_name, new_name)
            
            result = {
                'old_path': file_path,
                'new_path': new_path,
                'old_name': old_name,
                'new_name': new_name,
                'status': 'preview' if preview else 'pending'
            }
            
            if not preview:
                try:
                    os.rename(file_path, new_path)
                    result['status'] = 'success'
                except OSError as e:
                    result['status'] = 'error'
                    result['error'] = str(e)
            
            results.append(result)
    
    return results


def batch_copy(source_pattern: str, destination: str, 
               preserve_structure: bool = False) -> List[Dict[str, str]]:
    """
    批量复制文件
    
    Args:
        source_pattern: 源文件模式
        destination: 目标目录
        preserve_structure: 是否保持目录结构
        
    Returns:
        操作结果列表
    """
    files = glob.glob(source_pattern, recursive=True)
    results = []
    
    # 确保目标目录存在
    os.makedirs(destination, exist_ok=True)
    
    for source_file in files:
        if os.path.isfile(source_file):
            if preserve_structure:
                # 保持相对路径结构
                rel_path = os.path.relpath(source_file)
                dest_file = os.path.join(destination, rel_path)
                dest_dir = os.path.dirname(dest_file)
                os.makedirs(dest_dir, exist_ok=True)
            else:
                # 直接复制到目标目录
                filename = os.path.basename(source_file)
                dest_file = os.path.join(destination, filename)
            
            result = {
                'source': source_file,
                'destination': dest_file,
                'status': 'pending'
            }
            
            try:
                shutil.copy2(source_file, dest_file)
                result['status'] = 'success'
            except OSError as e:
                result['status'] = 'error'
                result['error'] = str(e)
            
            results.append(result)
    
    return results


def batch_move(source_pattern: str, destination: str) -> List[Dict[str, str]]:
    """
    批量移动文件
    
    Args:
        source_pattern: 源文件模式
        destination: 目标目录
        
    Returns:
        操作结果列表
    """
    files = glob.glob(source_pattern, recursive=True)
    results = []
    
    # 确保目标目录存在
    os.makedirs(destination, exist_ok=True)
    
    for source_file in files:
        if os.path.isfile(source_file):
            filename = os.path.basename(source_file)
            dest_file = os.path.join(destination, filename)
            
            result = {
                'source': source_file,
                'destination': dest_file,
                'status': 'pending'
            }
            
            try:
                shutil.move(source_file, dest_file)
                result['status'] = 'success'
            except OSError as e:
                result['status'] = 'error'
                result['error'] = str(e)
            
            results.append(result)
    
    return results


def format_results(results: List[Dict[str, str]], operation: str) -> str:
    """格式化操作结果"""
    if not results:
        return f"❌ 未找到匹配的文件进行{operation}"
    
    lines = []
    lines.append(f"📁 {operation}结果 (共 {len(results)} 个文件):\n")
    
    success_count = 0
    error_count = 0
    
    for result in results:
        if result['status'] == 'success':
            success_count += 1
            if operation == '重命名':
                lines.append(f"✅ {result['old_name']} → {result['new_name']}")
            else:
                lines.append(f"✅ {result['source']} → {result['destination']}")
        elif result['status'] == 'error':
            error_count += 1
            lines.append(f"❌ 失败: {result.get('error', '未知错误')}")
        elif result['status'] == 'preview':
            if operation == '重命名':
                lines.append(f"👀 预览: {result['old_name']} → {result['new_name']}")
            else:
                lines.append(f"👀 预览: {result['source']} → {result['destination']}")
    
    lines.append(f"\n📊 总计: {success_count} 成功, {error_count} 失败")
    
    return '\n'.join(lines)


def register_parser(subparsers):
    """注册 batch-process 命令的参数解析器"""
    parser = subparsers.add_parser('batch', help='批量文件处理工具')
    
    subcommands = parser.add_subparsers(dest='operation', help='操作类型')
    
    # 批量重命名
    rename_parser = subcommands.add_parser('rename', help='批量重命名')
    rename_parser.add_argument('directory', help='目标目录')
    rename_parser.add_argument('pattern', help='文件名匹配模式')
    rename_parser.add_argument('replacement', help='替换字符串')
    rename_parser.add_argument('--preview', action='store_true', help='仅预览，不实际执行')
    rename_parser.add_argument('--recursive', '-r', action='store_true', help='递归处理子目录')
    
    # 批量复制
    copy_parser = subcommands.add_parser('copy', help='批量复制')
    copy_parser.add_argument('source', help='源文件模式')
    copy_parser.add_argument('destination', help='目标目录')
    copy_parser.add_argument('--preserve-structure', action='store_true', help='保持目录结构')
    
    # 批量移动
    move_parser = subcommands.add_parser('move', help='批量移动')
    move_parser.add_argument('source', help='源文件模式')
    move_parser.add_argument('destination', help='目标目录')
    
    parser.set_defaults(func=main)


def main(args):
    """batch-process 工具的主函数"""
    try:
        if args.operation == 'rename':
            results = batch_rename(
                args.directory, 
                args.pattern, 
                args.replacement,
                preview=args.preview,
                recursive=args.recursive
            )
            return format_results(results, '重命名')
            
        elif args.operation == 'copy':
            results = batch_copy(
                args.source,
                args.destination,
                preserve_structure=args.preserve_structure
            )
            return format_results(results, '复制')
            
        elif args.operation == 'move':
            results = batch_move(args.source, args.destination)
            return format_results(results, '移动')
            
        else:
            raise ValueError("请选择操作类型: rename, copy, move")
            
    except Exception as e:
        raise RuntimeError(f"批量处理失败: {e}")


if __name__ == "__main__":
    # 测试代码
    print("批量文件处理工具测试")
    # 这里可以添加测试代码
"""
正则表达式测试工具
交互式测试正则表达式
"""

import argparse
import re
from typing import List, Dict, Any, Optional


def test_regex(pattern: str, text: str, flags: int = 0) -> Dict[str, Any]:
    """
    测试正则表达式
    
    Args:
        pattern: 正则表达式模式
        text: 要匹配的文本
        flags: 正则表达式标志
        
    Returns:
        测试结果字典
    """
    try:
        compiled_pattern = re.compile(pattern, flags)
        
        # 查找所有匹配
        matches = []
        for match in compiled_pattern.finditer(text):
            match_info = {
                'match': match.group(),
                'start': match.start(),
                'end': match.end(),
                'groups': match.groups(),
                'groupdict': match.groupdict()
            }
            matches.append(match_info)
        
        # 替换测试（用于演示）
        replacement_test = compiled_pattern.sub('[MATCH]', text)
        
        return {
            'pattern': pattern,
            'flags': flags,
            'is_valid': True,
            'match_count': len(matches),
            'matches': matches,
            'replacement_preview': replacement_test,
            'full_match': compiled_pattern.fullmatch(text) is not None
        }
        
    except re.error as e:
        return {
            'pattern': pattern,
            'flags': flags,
            'is_valid': False,
            'error': str(e),
            'match_count': 0,
            'matches': []
        }


def get_regex_flags(flag_names: List[str]) -> int:
    """
    从标志名称列表获取标志值
    
    Args:
        flag_names: 标志名称列表
        
    Returns:
        组合的标志值
    """
    flag_map = {
        'i': re.IGNORECASE,
        'ignorecase': re.IGNORECASE,
        'm': re.MULTILINE,
        'multiline': re.MULTILINE,
        's': re.DOTALL,
        'dotall': re.DOTALL,
        'x': re.VERBOSE,
        'verbose': re.VERBOSE,
        'a': re.ASCII,
        'ascii': re.ASCII
    }
    
    flags = 0
    for flag_name in flag_names:
        flag_name = flag_name.lower()
        if flag_name in flag_map:
            flags |= flag_map[flag_name]
    
    return flags


def format_test_result(result: Dict[str, Any]) -> str:
    """格式化测试结果"""
    if not result['is_valid']:
        return f"❌ 正则表达式语法错误: {result['error']}"
    
    lines = []
    lines.append(f"✅ 正则表达式: {result['pattern']}")
    lines.append(f"📊 匹配数量: {result['match_count']}")
    
    if result['matches']:
        lines.append("\n🎯 匹配结果:")
        for i, match in enumerate(result['matches'], 1):
            lines.append(f"  {i}. '{match['match']}' (位置: {match['start']}-{match['end']})")
            
            if match['groups']:
                lines.append(f"     分组: {match['groups']}")
            
            if match['groupdict']:
                lines.append(f"     命名分组: {match['groupdict']}")
    
    if result['replacement_preview']:
        lines.append(f"\n🔄 替换预览: {result['replacement_preview']}")
    
    lines.append(f"\n✅ 完全匹配: {'是' if result['full_match'] else '否'}")
    
    return '\n'.join(lines)


def generate_regex_examples() -> Dict[str, str]:
    """生成常用正则表达式示例"""
    return {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'phone': r'^1[3-9]\d{9}$',  # 中国手机号
        'url': r'https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?',
        'ip': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
        'date': r'^\d{4}-\d{2}-\d{2}$',  # YYYY-MM-DD
        'time': r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$',  # HH:MM or HH:MM:SS
        'chinese': r'[\u4e00-\u9fa5]+',  # 中文字符
        'number': r'^-?\d+(\.\d+)?$',  # 数字 (整数或小数)
        'password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$'  # 强密码
    }


def register_parser(subparsers):
    """注册 regex-tester 命令的参数解析器"""
    parser = subparsers.add_parser('regex', help='正则表达式测试工具')
    parser.add_argument('pattern', help='正则表达式模式')
    parser.add_argument('text', help='要匹配的文本')
    parser.add_argument('--flags', '-f', nargs='*', default=[],
                       help='正则表达式标志 (i, m, s, x, a)')
    parser.add_argument('--examples', action='store_true',
                       help='显示常用正则表达式示例')
    parser.set_defaults(func=main)


def main(args):
    """regex-tester 工具的主函数"""
    try:
        if args.examples:
            examples = generate_regex_examples()
            lines = ["🔧 常用正则表达式示例:\n"]
            
            for name, pattern in examples.items():
                lines.append(f"{name}: {pattern}")
            
            return '\n'.join(lines)
        
        flags = get_regex_flags(args.flags) if args.flags else 0
        result = test_regex(args.pattern, args.text, flags)
        
        return format_test_result(result)
        
    except Exception as e:
        raise RuntimeError(f"正则表达式测试失败: {e}")


if __name__ == "__main__":
    # 测试代码
    test_pattern = r'\b\w+@\w+\.\w+\b'
    test_text = "联系邮箱: john@example.com 和 mary@test.org"
    
    print("正则表达式测试:")
    result = test_regex(test_pattern, test_text)
    print(format_test_result(result))
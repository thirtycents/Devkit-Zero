"""
文本差异对比工具
对比两段文本或文件的差异
"""

import argparse
import difflib
import os
from typing import List, Tuple, Optional


def compare_texts(text1: str, text2: str, context_lines: int = 3) -> List[str]:
    """
    对比两段文本的差异
    
    Args:
        text1: 第一段文本
        text2: 第二段文本
        context_lines: 上下文行数
        
    Returns:
        差异对比结果列表
    """
    lines1 = text1.splitlines(keepends=True)
    lines2 = text2.splitlines(keepends=True)
    
    # 生成统一差异格式
    diff = difflib.unified_diff(
        lines1, lines2,
        fromfile='文本1',
        tofile='文本2',
        n=context_lines
    )
    
    return list(diff)


def compare_files(file1_path: str, file2_path: str, context_lines: int = 3) -> List[str]:
    """
    对比两个文件的差异
    
    Args:
        file1_path: 第一个文件路径
        file2_path: 第二个文件路径
        context_lines: 上下文行数
        
    Returns:
        差异对比结果列表
    """
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"文件不存在: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"文件不存在: {file2_path}")
    
    with open(file1_path, 'r', encoding='utf-8') as f1:
        lines1 = f1.readlines()
    
    with open(file2_path, 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
    
    # 生成统一差异格式
    diff = difflib.unified_diff(
        lines1, lines2,
        fromfile=file1_path,
        tofile=file2_path,
        n=context_lines
    )
    
    return list(diff)


def get_similarity_ratio(text1: str, text2: str) -> float:
    """
    计算两段文本的相似度
    
    Args:
        text1: 第一段文本
        text2: 第二段文本
        
    Returns:
        相似度比例 (0.0 - 1.0)
    """
    return difflib.SequenceMatcher(None, text1, text2).ratio()


def get_side_by_side_diff(text1: str, text2: str, width: int = 80) -> List[str]:
    """
    生成并排对比格式的差异
    
    Args:
        text1: 第一段文本
        text2: 第二段文本
        width: 每列的宽度
        
    Returns:
        并排差异对比结果列表
    """
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    
    result = []
    max_len = max(len(lines1), len(lines2))
    
    # 添加标题行
    result.append(f"{'文本1':<{width}} | {'文本2':<{width}}")
    result.append("-" * (width * 2 + 3))
    
    for i in range(max_len):
        line1 = lines1[i] if i < len(lines1) else ""
        line2 = lines2[i] if i < len(lines2) else ""
        
        # 截断过长的行
        if len(line1) > width - 5:
            line1 = line1[:width - 8] + "..."
        if len(line2) > width - 5:
            line2 = line2[:width - 8] + "..."
        
        # 标记不同的行
        marker = "!=" if line1 != line2 else "  "
        result.append(f"{line1:<{width}} {marker} {line2:<{width}}")
    
    return result


def analyze_changes(text1: str, text2: str) -> dict:
    """
    分析文本变化统计
    
    Args:
        text1: 第一段文本
        text2: 第二段文本
        
    Returns:
        变化统计字典
    """
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    
    matcher = difflib.SequenceMatcher(None, lines1, lines2)
    
    additions = 0
    deletions = 0
    modifications = 0
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'insert':
            additions += j2 - j1
        elif tag == 'delete':
            deletions += i2 - i1
        elif tag == 'replace':
            modifications += max(i2 - i1, j2 - j1)
    
    total_lines1 = len(lines1)
    total_lines2 = len(lines2)
    similarity = matcher.ratio()
    
    return {
        'total_lines_1': total_lines1,
        'total_lines_2': total_lines2,
        'additions': additions,
        'deletions': deletions,
        'modifications': modifications,
        'similarity': similarity,
        'total_changes': additions + deletions + modifications
    }


def register_parser(subparsers):
    """注册 diff-tool 命令的参数解析器"""
    parser = subparsers.add_parser('diff', help='文本差异对比工具')
    
    # 输入选项
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--files', nargs=2, metavar=('FILE1', 'FILE2'),
                           help='对比两个文件')
    input_group.add_argument('--text1', help='第一段文本')
    
    parser.add_argument('--text2', help='第二段文本 (与 --text1 配合使用)')
    
    # 输出选项
    parser.add_argument('--format', choices=['unified', 'side-by-side', 'stats'],
                       default='unified', help='输出格式 (默认: unified)')
    parser.add_argument('--context', '-c', type=int, default=3,
                       help='上下文行数 (默认: 3)')
    parser.add_argument('--width', '-w', type=int, default=80,
                       help='并排模式的列宽 (默认: 80)')
    parser.add_argument('--output', '-o', help='输出文件路径')
    
    parser.set_defaults(func=main)


def main(args):
    """diff-tool 工具的主函数"""
    try:
        if args.files:
            # 对比文件
            file1, file2 = args.files
            
            if args.format == 'unified':
                result = compare_files(file1, file2, args.context)
            elif args.format == 'side-by-side':
                with open(file1, 'r', encoding='utf-8') as f1:
                    text1 = f1.read()
                with open(file2, 'r', encoding='utf-8') as f2:
                    text2 = f2.read()
                result = get_side_by_side_diff(text1, text2, args.width)
            elif args.format == 'stats':
                with open(file1, 'r', encoding='utf-8') as f1:
                    text1 = f1.read()
                with open(file2, 'r', encoding='utf-8') as f2:
                    text2 = f2.read()
                stats = analyze_changes(text1, text2)
                result = [
                    f"文件1行数: {stats['total_lines_1']}",
                    f"文件2行数: {stats['total_lines_2']}",
                    f"新增行数: {stats['additions']}",
                    f"删除行数: {stats['deletions']}",
                    f"修改行数: {stats['modifications']}",
                    f"相似度: {stats['similarity']:.2%}",
                    f"总变更数: {stats['total_changes']}"
                ]
                
        elif args.text1 and args.text2:
            # 对比文本
            if args.format == 'unified':
                result = compare_texts(args.text1, args.text2, args.context)
            elif args.format == 'side-by-side':
                result = get_side_by_side_diff(args.text1, args.text2, args.width)
            elif args.format == 'stats':
                stats = analyze_changes(args.text1, args.text2)
                result = [
                    f"文本1行数: {stats['total_lines_1']}",
                    f"文本2行数: {stats['total_lines_2']}",
                    f"新增行数: {stats['additions']}",
                    f"删除行数: {stats['deletions']}",
                    f"修改行数: {stats['modifications']}",
                    f"相似度: {stats['similarity']:.2%}",
                    f"总变更数: {stats['total_changes']}"
                ]
        else:
            raise ValueError("使用 --files 对比文件，或使用 --text1 和 --text2 对比文本")
        
        # 输出结果
        output_text = '\n'.join(result) if isinstance(result, list) else str(result)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"差异对比结果已保存到: {args.output}")
        else:
            return output_text
            
    except Exception as e:
        raise RuntimeError(f"差异对比失败: {e}")


if __name__ == "__main__":
    # 用于独立测试
    text1 = "Hello\nWorld\nTest"
    text2 = "Hello\nPython\nTest\nNew line"
    
    print("统一差异格式:")
    diff = compare_texts(text1, text2)
    print(''.join(diff))
    
    print("\n并排对比:")
    side_diff = get_side_by_side_diff(text1, text2)
    print('\n'.join(side_diff))
    
    print("\n变化统计:")
    stats = analyze_changes(text1, text2)
    print(stats)
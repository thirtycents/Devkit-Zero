"""
Markdown 预览工具
实时预览 Markdown 文件的渲染效果
"""

import argparse
import os
import re
from typing import Optional


def markdown_to_html(markdown_text: str) -> str:
    """
    将 Markdown 文本转换为 HTML
    简单实现，不依赖外部库
    
    Args:
        markdown_text: Markdown 文本
        
    Returns:
        转换后的 HTML 文本
    """
    html_lines = []
    lines = markdown_text.split('\n')
    in_code_block = False
    code_block_lang = ""
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 代码块处理
        if line.startswith('```'):
            if not in_code_block:
                # 开始代码块
                in_code_block = True
                code_block_lang = line[3:].strip()
                html_lines.append(f'<pre><code class="language-{code_block_lang}">')
            else:
                # 结束代码块
                in_code_block = False
                html_lines.append('</code></pre>')
            i += 1
            continue
        
        if in_code_block:
            # 在代码块中，直接添加内容
            html_lines.append(line)
            i += 1
            continue
        
        # 标题处理
        if line.startswith('#'):
            level = 0
            for char in line:
                if char == '#':
                    level += 1
                else:
                    break
            if level <= 6:
                title_text = line[level:].strip()
                html_lines.append(f'<h{level}>{title_text}</h{level}>')
                i += 1
                continue
        
        # 列表处理
        if line.strip().startswith(('- ', '* ', '+ ')):
            # 无序列表
            if i == 0 or not lines[i-1].strip().startswith(('- ', '* ', '+ ')):
                html_lines.append('<ul>')
            
            item_text = line.strip()[2:]
            html_lines.append(f'<li>{process_inline_formatting(item_text)}</li>')
            
            if i == len(lines) - 1 or not lines[i+1].strip().startswith(('- ', '* ', '+ ')):
                html_lines.append('</ul>')
            
            i += 1
            continue
        
        elif re.match(r'^\d+\.\s', line.strip()):
            # 有序列表
            if i == 0 or not re.match(r'^\d+\.\s', lines[i-1].strip()):
                html_lines.append('<ol>')
            
            item_text = re.sub(r'^\d+\.\s', '', line.strip())
            html_lines.append(f'<li>{process_inline_formatting(item_text)}</li>')
            
            if i == len(lines) - 1 or not re.match(r'^\d+\.\s', lines[i+1].strip()):
                html_lines.append('</ol>')
            
            i += 1
            continue
        
        # 引用处理
        if line.startswith('>'):
            quote_text = line[1:].strip()
            html_lines.append(f'<blockquote><p>{process_inline_formatting(quote_text)}</p></blockquote>')
            i += 1
            continue
        
        # 水平线
        if line.strip() in ['---', '***', '___']:
            html_lines.append('<hr>')
            i += 1
            continue
        
        # 普通段落
        if line.strip():
            html_lines.append(f'<p>{process_inline_formatting(line)}</p>')
        else:
            html_lines.append('<br>')
        
        i += 1
    
    return '\n'.join(html_lines)


def process_inline_formatting(text: str) -> str:
    """
    处理行内格式化
    
    Args:
        text: 文本
        
    Returns:
        处理后的 HTML 文本
    """
    # 粗体
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    
    # 斜体
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    
    # 行内代码
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    # 链接
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    
    # 图片
    text = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1">', text)
    
    return text


def generate_html_template(content: str, title: str = "Markdown Preview") -> str:
    """
    生成完整的 HTML 模板
    
    Args:
        content: HTML 内容
        title: 页面标题
        
    Returns:
        完整的 HTML 文档
    """
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 2em;
            margin-bottom: 1em;
        }}
        h1 {{ border-bottom: 2px solid #eee; padding-bottom: 0.3em; }}
        h2 {{ border-bottom: 1px solid #eee; padding-bottom: 0.3em; }}
        code {{
            background-color: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
        }}
        pre {{
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        blockquote {{
            border-left: 4px solid #dfe2e5;
            padding-left: 16px;
            margin-left: 0;
            color: #6a737d;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}
        th, td {{
            border: 1px solid #dfe2e5;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #f6f8fa;
            font-weight: 600;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
        hr {{
            border: none;
            height: 1px;
            background-color: #e1e4e8;
            margin: 2em 0;
        }}
        ul, ol {{
            padding-left: 2em;
        }}
        li {{
            margin-bottom: 0.5em;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""


def preview_file(file_path: str, output_path: Optional[str] = None) -> str:
    """
    预览 Markdown 文件
    
    Args:
        file_path: Markdown 文件路径
        output_path: 输出 HTML 文件路径
        
    Returns:
        HTML 内容或成功消息
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    html_content = markdown_to_html(markdown_content)
    title = os.path.splitext(os.path.basename(file_path))[0]
    full_html = generate_html_template(html_content, title)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        return f"HTML 预览已保存到: {output_path}"
    else:
        return full_html


def register_parser(subparsers):
    """注册 markdown-preview 命令的参数解析器"""
    parser = subparsers.add_parser('markdown', help='Markdown 预览工具')
    parser.add_argument('file', help='Markdown 文件路径')
    parser.add_argument('--output', '-o', help='输出 HTML 文件路径')
    parser.add_argument('--open', action='store_true', help='在浏览器中打开预览')
    parser.set_defaults(func=main)


def main(args):
    """markdown-preview 工具的主函数"""
    try:
        result = preview_file(args.file, args.output)
        
        if args.open and args.output:
            import webbrowser
            file_url = f"file://{os.path.abspath(args.output)}"
            webbrowser.open(file_url)
            return f"{result}\n浏览器已打开预览"
        
        return result
        
    except Exception as e:
        raise RuntimeError(f"Markdown 预览失败: {e}")


if __name__ == "__main__":
    # 测试代码
    test_markdown = """
# 测试标题

这是一个 **粗体** 和 *斜体* 的测试。

## 列表测试

- 项目 1
- 项目 2
- 项目 3

## 代码测试

`行内代码` 和代码块:

```python
def hello():
    print("Hello, World!")
```

> 这是一个引用块
"""
    
    print("Markdown 转换测试:")
    html_result = markdown_to_html(test_markdown)
    print(html_result)
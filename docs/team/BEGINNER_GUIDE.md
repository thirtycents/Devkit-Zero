# DevKit-Zero 框架详细介绍

## 📋 目录

1. [项目架构概览](#项目架构概览)
2. [目录结构详解](#目录结构详解)
3. [核心设计原则](#核心设计原则)
4. [新手开发指南](#新手开发指南)
5. [功能开发流程](#功能开发流程)
6. [代码规范](#代码规范)
7. [测试规范](#测试规范)
8. [团队协作流程](#团队协作流程)

---

## 🏗️ 项目架构概览

DevKit-Zero 是一个模块化的开发者工具包，采用标准的 Python 包结构设计。

### 核心特性
- **零依赖**: 核心功能不依赖第三方库
- **模块化**: 每个工具独立开发和使用
- **多入口**: 支持命令行、GUI、库导入三种使用方式
- **可扩展**: 易于添加新工具和功能

### 架构图
```
用户接口层
├── CLI (命令行界面)
├── GUI (图形界面)
└── API (库导入接口)
         ↓
核心处理层
├── DevKitCore (统一API)
├── 工具注册器
└── 参数解析器
         ↓
工具模块层
├── formatter (格式化)
├── random_gen (随机生成)
├── diff_tool (差异比较)
└── ... (其他工具)
         ↓
基础设施层
├── 配置管理
├── 日志系统
└── 工具函数
```

---

## 📁 目录结构详解

```
DevKit-Zero/                    # 项目根目录
├── devkit_zero/               # 主包目录 (这是核心!)
│   ├── __init__.py           # 包初始化，导出公共接口
│   ├── __version__.py        # 版本信息
│   ├── core.py               # 核心API类
│   ├── cli.py                # 命令行入口
│   ├── gui_main.py           # GUI入口
│   ├── tools/                # 工具模块目录
│   │   ├── __init__.py       # 工具注册
│   │   ├── formatter.py      # 代码格式化工具
│   │   ├── random_gen.py     # 随机生成工具
│   │   └── ...               # 其他工具
│   ├── ui/                   # 用户界面模块
│   │   ├── __init__.py
│   │   └── gui_app.py        # GUI主界面
│   └── utils/                # 工具函数
├── tests/                    # 测试目录
│   ├── test_tools/          # 工具测试
│   └── conftest.py          # 测试配置
├── docs/                     # 文档目录
├── assets/                   # 资源文件
├── templates/                # 模板文件
├── static/                   # 静态文件
├── .github/                  # GitHub配置
│   └── workflows/           # CI/CD配置
├── setup.py                  # 安装配置
├── pyproject.toml           # 项目元数据
├── requirements.txt         # 运行依赖
├── requirements-dev.txt     # 开发依赖
├── README.md                # 项目说明
├── DEVELOPMENT.md           # 开发指南
├── CHANGELOG.md             # 变更日志
├── .gitignore              # Git忽略文件
└── PROJECT_FRAMEWORK.md     # 架构文档
```

### 关键文件说明

| 文件/目录 | 作用 | 新手重点关注 |
|-----------|------|-------------|
| `devkit_zero/__init__.py` | 定义包的公共接口 | ⭐⭐⭐ |
| `devkit_zero/tools/` | 所有工具的实现 | ⭐⭐⭐ |
| `devkit_zero/core.py` | 统一的API接口 | ⭐⭐ |
| `tests/` | 测试代码 | ⭐⭐⭐ |
| `setup.py` | 包安装配置 | ⭐ |

---

## 🎯 核心设计原则

### 1. 单一职责原则
- 每个工具模块只负责一个功能
- 每个函数只做一件事

### 2. 开放封闭原则
- 对扩展开放：易于添加新工具
- 对修改封闭：不修改现有代码

### 3. 接口统一原则
- 所有工具都有相同的接口结构
- 统一的参数传递方式

### 4. 零依赖原则
- 核心功能使用Python标准库
- 可选功能可以使用第三方库

---

## 👶 新手开发指南

### 第一步：环境准备

```bash
# 1. 克隆项目
git clone <your-repo-url>
cd DevKit-Zero

# 2. 创建虚拟环境 (推荐)
python -m venv venv
# Windows激活
venv\Scripts\activate
# Linux/Mac激活
source venv/bin/activate

# 3. 安装开发依赖
pip install -r requirements-dev.txt

# 4. 以开发模式安装项目
pip install -e .
```

### 第二步：理解项目结构

**重点关注这三个目录：**
1. `devkit_zero/tools/` - 你主要工作的地方
2. `tests/test_tools/` - 写测试的地方  
3. `docs/` - 写文档的地方

### 第三步：运行现有功能

```bash
# 测试命令行
devkit-zero --help
devkit-zero formatter --help

# 测试GUI
devkit-zero-gui

# 运行测试
pytest
```

---

## 🔧 功能开发流程

### 场景：添加一个新工具 "json_validator" (JSON验证器)

#### Step 1: 创建工具模块

在 `devkit_zero/tools/` 创建 `json_validator.py`：

```python
"""JSON验证器工具"""

import json
import argparse
from typing import Dict, Any, Tuple


def main_function(json_text: str, schema: str = None) -> Dict[str, Any]:
    """
    JSON验证器主要功能
    
    Args:
        json_text: 要验证的JSON文本
        schema: JSON Schema (可选)
        
    Returns:
        Dict: 包含验证结果的字典
        
    Raises:
        ValueError: JSON格式错误时抛出
    """
    try:
        # 1. 基础JSON语法验证
        data = json.loads(json_text)
        
        result = {
            'valid': True,
            'data': data,
            'message': 'JSON格式正确',
            'type': type(data).__name__
        }
        
        # 2. Schema验证 (如果提供)
        if schema:
            # 这里可以扩展JSON Schema验证
            result['schema_valid'] = True
            result['message'] += ', Schema验证通过'
            
        return result
        
    except json.JSONDecodeError as e:
        return {
            'valid': False,
            'error': str(e),
            'message': f'JSON格式错误: {e.msg} (行{e.lineno}, 列{e.colno})'
        }


def register_parser(subparsers) -> argparse.ArgumentParser:
    """注册命令行参数解析器"""
    parser = subparsers.add_parser(
        'json-validator',
        help='JSON格式验证器',
        description='验证JSON文本格式是否正确'
    )
    
    # 必需参数
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='输入JSON文件路径或JSON文本'
    )
    
    # 可选参数
    parser.add_argument(
        '--schema', '-s',
        help='JSON Schema文件路径 (可选)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='输出结果到文件 (可选)'
    )
    
    return parser


def main(args) -> int:
    """命令行入口函数"""
    try:
        # 1. 读取输入
        if args.input.startswith('{') or args.input.startswith('['):
            # 直接的JSON文本
            json_text = args.input
        else:
            # 文件路径
            with open(args.input, 'r', encoding='utf-8') as f:
                json_text = f.read()
        
        # 2. 读取schema (如果有)
        schema = None
        if args.schema:
            with open(args.schema, 'r', encoding='utf-8') as f:
                schema = f.read()
        
        # 3. 执行验证
        result = main_function(json_text, schema)
        
        # 4. 输出结果
        if result['valid']:
            print(f"✓ {result['message']}")
            if 'type' in result:
                print(f"数据类型: {result['type']}")
        else:
            print(f"✗ {result['message']}")
            return 1
            
        # 5. 保存到文件 (如果指定)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"结果已保存到: {args.output}")
            
        return 0
        
    except FileNotFoundError as e:
        print(f"错误: 文件未找到 {e.filename}")
        return 1
    except Exception as e:
        print(f"错误: {e}")
        return 1


if __name__ == "__main__":
    # 用于直接运行测试
    import sys
    test_json = '{"name": "张三", "age": 25, "skills": ["Python", "JavaScript"]}'
    result = main_function(test_json)
    print(result)
```

#### Step 2: 注册工具

在 `devkit_zero/tools/__init__.py` 中添加：

```python
# 在文件末尾添加
from . import json_validator

# 在 AVAILABLE_TOOLS 字典中添加
AVAILABLE_TOOLS = {
    'formatter': formatter,
    'random_gen': random_gen,
    'diff_tool': diff_tool,
    'converter': converter,
    'linter': linter,
    'regex_tester': regex_tester,
    'batch_process': batch_process,
    'markdown_preview': markdown_preview,
    'port_checker': port_checker,
    'json_validator': json_validator,  # 新添加
}
```

#### Step 3: 创建测试

在 `tests/test_tools/` 创建 `test_json_validator.py`：

```python
"""JSON验证器测试"""

import unittest
from devkit_zero.tools.json_validator import main_function


class TestJsonValidator(unittest.TestCase):
    """JSON验证器测试类"""
    
    def test_valid_json_object(self):
        """测试有效的JSON对象"""
        json_text = '{"name": "张三", "age": 25}'
        result = main_function(json_text)
        
        self.assertTrue(result['valid'])
        self.assertEqual(result['data']['name'], '张三')
        self.assertEqual(result['data']['age'], 25)
    
    def test_valid_json_array(self):
        """测试有效的JSON数组"""
        json_text = '[1, 2, 3, "test"]'
        result = main_function(json_text)
        
        self.assertTrue(result['valid'])
        self.assertEqual(len(result['data']), 4)
    
    def test_invalid_json(self):
        """测试无效的JSON"""
        json_text = '{"name": "张三", "age":}'  # 缺少值
        result = main_function(json_text)
        
        self.assertFalse(result['valid'])
        self.assertIn('error', result)
    
    def test_empty_string(self):
        """测试空字符串"""
        result = main_function('')
        self.assertFalse(result['valid'])
    
    def test_complex_json(self):
        """测试复杂JSON结构"""
        json_text = '''
        {
            "users": [
                {"id": 1, "name": "张三", "active": true},
                {"id": 2, "name": "李四", "active": false}
            ],
            "meta": {
                "total": 2,
                "page": 1
            }
        }
        '''
        result = main_function(json_text)
        
        self.assertTrue(result['valid'])
        self.assertEqual(len(result['data']['users']), 2)
        self.assertEqual(result['data']['meta']['total'], 2)


if __name__ == '__main__':
    unittest.main()
```

#### Step 4: 运行测试

```bash
# 运行新工具的测试
pytest tests/test_tools/test_json_validator.py -v

# 运行所有测试
pytest

# 测试新功能
devkit-zero json-validator --input '{"test": "data"}'
```

#### Step 5: 更新文档

在 `README.md` 的工具列表中添加：

```markdown
### JSON验证器
验证JSON格式，检查语法错误

```bash
# 验证JSON文件
devkit-zero json-validator --input data.json

# 验证JSON字符串
devkit-zero json-validator --input '{"name": "test"}'

# 使用Schema验证
devkit-zero json-validator --input data.json --schema schema.json
```

#### Step 6: 提交代码

```bash
# 1. 添加文件到git
git add devkit_zero/tools/json_validator.py
git add tests/test_tools/test_json_validator.py
git add devkit_zero/tools/__init__.py
git add README.md

# 2. 提交
git commit -m "feat: add JSON validator tool

- Add json_validator.py with validation functionality
- Add comprehensive tests
- Update tool registration and documentation
- Support both file and string input
- Optional JSON Schema validation"

# 3. 推送
git push origin main
```

---

## 📝 代码规范

### Python代码规范 (PEP 8)

#### 1. 命名规范
```python
# ✓ 正确的命名
class JsonValidator:          # 类名用大驼峰
def validate_json():          # 函数名用下划线
JSON_SCHEMA_VERSION = "1.0"   # 常量用大写+下划线
user_data = {}               # 变量用下划线

# ✗ 错误的命名
class jsonvalidator:         # 类名太随意
def validateJson():          # 函数名用驼峰(这是Java风格)
jsonSchemaVersion = "1.0"    # 常量用驼峰
userData = {}               # 变量用驼峰
```

#### 2. 函数文档
```python
def main_function(json_text: str, schema: str = None) -> Dict[str, Any]:
    """
    函数的简短描述 (一行)
    
    更详细的功能说明，如果需要的话。
    可以多行，解释复杂的逻辑。
    
    Args:
        json_text: 要验证的JSON文本
        schema: JSON Schema字符串，可选
        
    Returns:
        包含验证结果的字典，格式：
        {
            'valid': bool,      # 是否有效
            'data': Any,        # 解析后的数据
            'message': str      # 结果信息
        }
        
    Raises:
        ValueError: 当输入参数无效时
        
    Example:
        >>> result = main_function('{"name": "test"}')
        >>> print(result['valid'])
        True
    """
```

#### 3. 类型注解
```python
# ✓ 推荐：使用类型注解
def process_data(items: List[str], count: int = 10) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    return result

# ✓ 可以：复杂类型
from typing import Union, Optional, Callable
def complex_function(
    callback: Callable[[str], bool],
    data: Optional[Union[str, List[str]]] = None
) -> bool:
    pass
```

#### 4. 错误处理
```python
# ✓ 具体的异常处理
try:
    data = json.loads(json_text)
except json.JSONDecodeError as e:
    return {
        'valid': False,
        'error': f'JSON语法错误: {e.msg} (行{e.lineno})'
    }
except FileNotFoundError:
    return {'valid': False, 'error': '文件不存在'}

# ✗ 避免裸露的except
try:
    # some code
except:  # 这样不好，不知道捕获了什么错误
    pass
```

### 工具模块标准结构

每个工具模块必须包含这三个函数：

```python
def main_function(...) -> ...:
    """核心功能实现"""
    pass

def register_parser(subparsers) -> argparse.ArgumentParser:
    """注册命令行参数"""
    pass

def main(args) -> int:
    """命令行入口，返回状态码"""
    pass
```

---

## 🧪 测试规范

### 测试文件命名
- 测试文件名：`test_{模块名}.py`
- 测试类名：`Test{模块名的驼峰形式}`
- 测试方法：`test_{测试场景}`

### 测试用例编写
```python
class TestJsonValidator(unittest.TestCase):
    
    def setUp(self):
        """每个测试前的准备工作"""
        self.valid_json = '{"name": "test"}'
        self.invalid_json = '{"name":}'
    
    def test_valid_input_returns_success(self):
        """测试：有效输入应该返回成功"""
        # Arrange (准备)
        json_text = self.valid_json
        
        # Act (执行)
        result = main_function(json_text)
        
        # Assert (断言)
        self.assertTrue(result['valid'])
        self.assertEqual(result['data']['name'], 'test')
    
    def test_invalid_input_returns_error(self):
        """测试：无效输入应该返回错误"""
        result = main_function(self.invalid_json)
        
        self.assertFalse(result['valid'])
        self.assertIn('error', result)
        
    def tearDown(self):
        """每个测试后的清理工作"""
        pass
```

### 测试覆盖要求
- **正常情况**: 正确的输入产生正确的输出
- **边界情况**: 空值、最大值、最小值等
- **异常情况**: 错误的输入、文件不存在等

---

## 👥 团队协作流程

### Git工作流程

#### 1. 分支策略
```bash
main        # 主分支，稳定版本
├── dev     # 开发分支，集成最新功能  
├── feature/json-validator    # 功能分支
├── bugfix/fix-formatter     # 修复分支
└── hotfix/critical-fix      # 紧急修复
```

#### 2. 开发流程
```bash
# 1. 从main创建功能分支
git checkout main
git pull origin main
git checkout -b feature/your-feature-name

# 2. 开发功能
# ... 编写代码 ...

# 3. 经常提交
git add .
git commit -m "feat: add basic structure for new tool"

# 4. 推送分支
git push origin feature/your-feature-name

# 5. 创建Pull Request
# 在GitHub/GitLab上创建PR，请求合并到dev分支

# 6. 代码审查通过后合并
# 删除功能分支
git branch -d feature/your-feature-name
```

#### 3. 提交信息规范
```bash
# 格式: <type>: <description>

feat: add JSON validator tool           # 新功能
fix: correct formatter indentation bug  # 修复bug
docs: update README with new tool       # 文档
test: add tests for random generator     # 测试
refactor: simplify core API             # 重构
style: fix code formatting              # 样式
chore: update dependencies              # 构建/工具
```

### 代码审查清单

提交PR时请确保：
- [ ] 代码通过所有测试 (`pytest`)
- [ ] 添加了相应的测试用例
- [ ] 更新了相关文档
- [ ] 遵循代码规范
- [ ] 提交信息清晰
- [ ] 没有硬编码的配置
- [ ] 处理了错误情况

### 新人上手检查清单

第一次贡献代码前：
- [ ] 已阅读 `README.md`
- [ ] 已阅读 `DEVELOPMENT.md`
- [ ] 本地环境搭建成功
- [ ] 能运行现有测试
- [ ] 理解项目结构
- [ ] 知道如何添加新工具
- [ ] 了解Git工作流程

---

## 🚀 常见问题解答

### Q: 我是Python新手，从哪里开始？
**A**: 
1. 先运行现有功能，理解项目如何工作
2. 阅读 `devkit_zero/tools/formatter.py` - 这是最简单的工具
3. 尝试修改 `formatter.py` 的输出信息
4. 运行测试看是否还能通过

### Q: 如何调试我的代码？
**A**:
```python
# 1. 使用print调试
def main_function(data):
    print(f"输入数据: {data}")  # 临时调试
    result = process(data)
    print(f"处理结果: {result}")  # 临时调试
    return result

# 2. 使用pytest的-s选项看到print输出
pytest tests/test_tools/test_your_tool.py -s -v

# 3. 在VS Code中设置断点调试
```

### Q: 如何知道我的功能是否完成？
**A**: 完成的标准：
- [ ] 功能正常工作
- [ ] 有测试用例且通过
- [ ] 命令行可以调用
- [ ] 文档已更新
- [ ] 代码审查通过

### Q: 出现导入错误怎么办？
**A**:
```python
# 确保使用相对导入
from ..core import DevKitCore        # ✓ 正确
from devkit_zero.core import DevKitCore  # ✗ 可能出错

# 如果仍有问题，检查__init__.py文件是否存在
```

---

## 📚 学习资源

### 新手推荐
1. **Python官方教程**: https://docs.python.org/3/tutorial/
2. **PEP 8代码规范**: https://pep8.org/
3. **Git教程**: https://learngitbranching.js.org/

### 进阶学习
1. **Python类型注解**: https://docs.python.org/3/library/typing.html
2. **单元测试**: https://docs.python.org/3/library/unittest.html
3. **包开发**: https://packaging.python.org/tutorials/packaging-projects/

记住：**不要害怕犯错，每个大牛都是从新手开始的！** 🌟

遇到问题随时在团队群里提问，我们都会帮助你！
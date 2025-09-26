# DevKit-Zero 项目框架说明

## 📊 项目概览

**DevKit-Zero** 现在已经完成了从简单脚本到专业 Python 包的完整转换。该项目既可以作为库被其他开发者导入使用，也可以作为独立的命令行工具或图形界面应用程序运行。

## 🏗️ 重构后的架构特点

### 1. 多入口支持

#### 作为库使用
```python
# 方式1：直接导入工具模块
from devkit_zero import formatter, random_gen
result = formatter.format_code("code", "python")

# 方式2：使用核心类（推荐）
from devkit_zero import DevKitCore
devkit = DevKitCore()
result = devkit.format_code("code", "python")

# 方式3：使用全局实例
from devkit_zero.core import devkit
result = devkit.generate_uuid()
```

#### 作为命令行工具
```bash
# 安装后可直接使用
devkit-zero format --input "code" --language python
devkit random uuid  # 简短别名
```

#### 作为图形界面应用
```bash
devkit-zero-gui  # 启动 GUI
```

### 2. 专业的包结构

```
DevKit-Zero/
├── devkit_zero/          # 主包（可导入）
│   ├── __init__.py      # 包入口，导出所有公共 API
│   ├── __version__.py   # 版本信息
│   ├── core.py         # 核心类，统一 API
│   ├── cli.py          # CLI 入口
│   ├── gui_main.py     # GUI 入口
│   ├── tools/          # 工具模块
│   └── ui/             # 界面模块
├── setup.py            # 安装配置
├── pyproject.toml      # 现代配置
├── README.md           # 项目说明
└── tests/              # 测试文件
```

### 3. 零依赖设计

- 核心功能仅使用 Python 标准库
- 可选依赖（GUI、Web）通过 `extras_require` 管理
- 保持轻量级特性

## 📦 安装和打包方式

### 开发安装
```bash
# 克隆项目
git clone <repository>
cd DevKit-Zero

# 安装为可编辑包
pip install -e .

# 安装开发依赖
pip install -e .[dev]
```

### 用户安装
```bash
# 从 PyPI 安装（发布后）
pip install devkit-zero

# 带可选依赖
pip install devkit-zero[gui,web]
```

### 打包为可执行文件
```bash
# 使用 PyInstaller
pip install pyinstaller

# CLI 版本
pyinstaller --onefile devkit_zero/cli.py

# GUI 版本  
pyinstaller --onefile --noconsole devkit_zero/gui_main.py
```

## 🔧 工具模块设计

每个工具都遵循统一的接口规范：

```python
# 工具模块结构
def main_function(args) -> result:
    """核心功能实现"""
    pass

def register_parser(subparsers):
    """注册CLI参数"""
    pass

def main(args):
    """CLI入口处理"""
    pass
```

现有工具：
- **formatter**: 代码格式化（Python/JavaScript）
- **random_gen**: 随机数据生成（UUID/密码/字符串等）
- **diff_tool**: 文本差异对比
- **converter**: 数据格式转换（JSON/CSV）
- **linter**: 代码静态检查
- **regex_tester**: 正则表达式测试
- **batch_process**: 批量文件处理
- **markdown_preview**: Markdown预览
- **port_checker**: 端口检查

## 🚀 使用场景

### 1. 个人开发者
```bash
# 快速格式化代码
devkit format --file script.py

# 生成测试数据
devkit random password --length 20

# 检查端口占用
devkit port check 8080
```

### 2. 团队项目集成
```python
# 在项目中集成使用
from devkit_zero import DevKitCore

devkit = DevKitCore()

# 代码质量检查
issues = devkit.lint_code(source_code)
if issues:
    print("发现代码问题:", issues)

# 生成项目ID
project_id = devkit.generate_uuid()
```

### 3. 自动化脚本
```python
#!/usr/bin/env python3
import devkit_zero as dk

# 批量处理文件
dk.batch_process.batch_rename(
    directory="./temp",
    pattern="*.tmp", 
    replacement="backup_*"
)

# 生成报告
diff_result = dk.diff_tool.compare_files("old.txt", "new.txt")
```

## 📝 开发和贡献

### 添加新工具的步骤

1. **创建工具模块**
   ```python
   # devkit_zero/tools/new_tool.py
   def my_function(input_data):
       """实现核心功能"""
       return processed_data
   
   def register_parser(subparsers):
       """注册CLI参数"""
       parser = subparsers.add_parser('newtool', help='新工具')
       # 添加参数...
       parser.set_defaults(func=main)
   ```

2. **更新包导入**
   ```python
   # devkit_zero/tools/__init__.py
   from . import new_tool
   ```

3. **注册CLI命令**
   ```python
   # devkit_zero/cli.py
   from .tools import new_tool
   new_tool.register_parser(subparsers)
   ```

4. **添加核心方法**（可选）
   ```python
   # devkit_zero/core.py
   def use_new_tool(self, input_data):
       return self._tools['new_tool'].my_function(input_data)
   ```

### 测试框架
```python
# tests/test_tools/test_new_tool.py
import unittest
from devkit_zero.tools import new_tool

class TestNewTool(unittest.TestCase):
    def test_basic_functionality(self):
        result = new_tool.my_function("test")
        self.assertEqual(result, "expected")
```

## 🔍 质量保证

### 代码规范
- 使用 **Black** 进行代码格式化
- 使用 **flake8** 进行静态检查
- 使用 **mypy** 进行类型检查

### 测试覆盖
- 单元测试覆盖所有工具模块
- CLI 测试验证命令行接口
- 集成测试确保整体功能

### 持续集成
- GitHub Actions 自动运行测试
- 多平台兼容性检查
- 自动化发布流程

## 📊 项目状态

### ✅ 已完成功能

1. **核心架构**
   - [x] 包结构重构
   - [x] 多入口支持（库/CLI/GUI）
   - [x] 统一API设计
   - [x] 零依赖实现

2. **工具模块**
   - [x] 代码格式化工具
   - [x] 随机数据生成工具
   - [x] 文本差异对比工具
   - [x] 其他6个工具模块

3. **用户界面**
   - [x] 命令行界面（CLI）
   - [x] 图形界面框架（GUI）
   - [x] 参数解析和错误处理

4. **开发工具**
   - [x] 测试框架搭建
   - [x] 打包配置
   - [x] 开发文档

### 🚧 待完善功能

1. **功能增强**
   - [ ] Web界面实现
   - [ ] 更多工具模块
   - [ ] 插件系统

2. **质量提升**
   - [ ] 完整的测试覆盖
   - [ ] 性能优化
   - [ ] 错误处理优化

3. **文档完善**
   - [ ] API文档生成
   - [ ] 使用教程视频
   - [ ] 示例项目

## 🎯 项目优势

1. **专业性**: 完整的包结构和开发规范
2. **灵活性**: 多种使用方式，适应不同场景
3. **可扩展性**: 模块化设计，易于添加新工具
4. **可维护性**: 清晰的代码结构和文档
5. **零依赖**: 轻量级，无外部依赖负担

这个重构后的项目现在具备了专业Python包的所有特征，可以满足从个人使用到企业级集成的各种需求。
# DevKit-Zero 项目开发规范

## 📋 目录

1. [项目架构](#项目架构)
2. [开发环境设置](#开发环境设置)
3. [代码规范](#代码规范)
4. [测试规范](#测试规范)
5. [文档规范](#文档规范)
6. [Git 工作流](#git-工作流)
7. [发布流程](#发布流程)
8. [打包指南](#打包指南)

## 🏗️ 项目架构

### 目录结构说明

```
DevKit-Zero/
├── devkit_zero/                 # 主包目录 (可导入的 Python 包)
│   ├── __init__.py             # 包入口，导出所有公共 API
│   ├── __version__.py          # 版本信息，单一数据源
│   ├── core.py                 # 核心类，统一的 API 接口
│   ├── cli.py                  # 命令行入口，处理所有 CLI 逻辑
│   ├── gui_main.py             # GUI 应用入口
│   ├── tools/                  # 工具模块目录
│   │   ├── __init__.py         # 导出所有工具
│   │   ├── formatter.py        # 代码格式化工具
│   │   ├── random_gen.py       # 随机数据生成工具
│   │   ├── diff_tool.py        # 文本差异对比工具
│   │   ├── converter.py        # 数据格式转换工具
│   │   ├── linter.py           # 代码静态检查工具
│   │   ├── regex_tester.py     # 正则表达式测试工具
│   │   ├── batch_process.py    # 批量文件处理工具
│   │   ├── markdown_preview.py # Markdown 预览工具
│   │   └── port_checker.py     # 端口检查工具
│   ├── ui/                     # 用户界面模块
│   │   ├── __init__.py
│   │   ├── gui_app.py          # Tkinter GUI 应用
│   │   └── web_app.py          # Flask Web 应用 (可选)
│   └── utils/                  # 通用工具函数
│       ├── __init__.py
│       └── helpers.py          # 辅助函数
├── tests/                      # 测试目录
│   ├── __init__.py
│   ├── test_tools/             # 工具测试
│   ├── test_cli.py             # CLI 测试
│   └── test_integration.py     # 集成测试
├── docs/                       # 文档目录
│   ├── api.md                  # API 文档
│   ├── cli.md                  # 命令行使用指南
│   └── development.md          # 开发指南
├── assets/                     # 资源文件
│   ├── icons/                  # 图标文件
│   └── templates/              # 模板文件
├── .github/                    # GitHub 配置
│   └── workflows/              # CI/CD 工作流
│       ├── test.yml            # 测试流程
│       └── publish.yml         # 发布流程
├── setup.py                    # 安装配置 (向后兼容)
├── pyproject.toml              # 现代 Python 项目配置
├── README.md                   # 项目说明
├── CHANGELOG.md                # 更新日志
├── LICENSE                     # 许可证
├── requirements.txt            # 运行时依赖 (空文件，保持零依赖)
├── requirements-dev.txt        # 开发依赖
└── .gitignore                  # Git 忽略文件
```

### 设计原则

1. **零依赖原则**: 核心功能仅使用 Python 标准库
2. **模块化设计**: 每个工具独立实现，可单独使用
3. **统一接口**: 通过 `DevKitCore` 类提供一致的 API
4. **多入口支持**: CLI、GUI、库导入三种使用方式
5. **向后兼容**: 同时支持 `setup.py` 和 `pyproject.toml`

## 🛠️ 开发环境设置

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/devkit-zero/devkit-zero.git
cd devkit-zero

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\\Scripts\\activate
# macOS/Linux
source venv/bin/activate

# 升级 pip
python -m pip install --upgrade pip

# 安装项目 (可编辑模式)
pip install -e .

# 安装开发依赖
pip install -r requirements-dev.txt
# 或者使用可选依赖
pip install -e .[dev]
```

### 2. 验证安装

```bash
# 测试 CLI
devkit-zero --version
devkit --help

# 测试 GUI (如果支持)
devkit-zero-gui

# 测试库导入
python -c "import devkit_zero; print(devkit_zero.get_version())"
```

## 📝 代码规范

### 1. Python 代码风格

#### 使用 Black 进行格式化
```bash
# 格式化所有文件
black devkit_zero/

# 检查格式化
black --check devkit_zero/
```

#### Black 配置 (pyproject.toml)
```toml
[tool.black]
line-length = 88
target-version = ['py37', 'py38', 'py39', 'py310', 'py311']
```

#### 使用 flake8 进行静态检查
```bash
# 运行检查
flake8 devkit_zero/
```

#### Flake8 配置
```toml
[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "W503"]
```

### 2. 类型注解

使用 mypy 进行类型检查：

```bash
# 运行类型检查
mypy devkit_zero/
```

#### 类型注解示例
```python
from typing import List, Dict, Optional, Union

def format_code(code: str, language: str) -> str:
    """格式化代码"""
    pass

def get_results() -> Optional[List[Dict[str, Union[str, int]]]]:
    """获取结果列表"""
    pass
```

### 3. 文档字符串规范

使用 Google 风格的文档字符串：

```python
def example_function(param1: str, param2: int = 10) -> bool:
    """
    函数功能简述
    
    更详细的功能描述...
    
    Args:
        param1: 第一个参数的描述
        param2: 第二个参数的描述，默认值为 10
        
    Returns:
        返回值的描述
        
    Raises:
        ValueError: 参数错误时抛出
        
    Example:
        >>> result = example_function("test", 20)
        >>> print(result)
        True
    """
    pass
```

### 4. 导入规范

```python
# 标准库导入
import os
import sys
from typing import List, Dict, Optional

# 第三方库导入 (尽量避免)
# import requests

# 本项目导入
from .tools import formatter
from ..utils import helpers
```

## 🧪 测试规范

### 1. 测试结构

```
tests/
├── __init__.py
├── conftest.py                 # pytest 配置
├── test_core.py               # 核心功能测试
├── test_cli.py                # CLI 测试
├── test_tools/                # 工具测试目录
│   ├── __init__.py
│   ├── test_formatter.py
│   ├── test_random_gen.py
│   └── test_*.py
└── test_integration.py        # 集成测试
```

### 2. 测试编写指南

#### 单元测试示例
```python
import pytest
from devkit_zero.tools import formatter

class TestFormatter:
    """代码格式化工具测试"""
    
    def test_format_python_code(self):
        """测试 Python 代码格式化"""
        input_code = "def hello():print('hi')"
        expected = "def hello():\n    print('hi')"
        
        result = formatter.format_python_code(input_code)
        assert result == expected
    
    def test_format_invalid_syntax(self):
        """测试无效语法处理"""
        invalid_code = "def hello( print('hi')"
        
        with pytest.raises(ValueError, match="语法错误"):
            formatter.format_python_code(invalid_code)
    
    @pytest.mark.parametrize("language,code", [
        ("python", "def test(): pass"),
        ("javascript", "function test() {}"),
    ])
    def test_format_different_languages(self, language, code):
        """测试不同语言格式化"""
        result = formatter.format_code(code, language)
        assert isinstance(result, str)
        assert len(result) > 0
```

#### CLI 测试示例
```python
import subprocess
from devkit_zero.cli import main

def test_cli_version():
    """测试版本显示"""
    result = main(["--version"])
    assert result == 0

def test_cli_help():
    """测试帮助信息"""
    result = main(["--help"])
    assert result == 0

def test_formatter_command():
    """测试格式化命令"""
    result = main([
        "format", 
        "--input", "def hello():print('hi')", 
        "--language", "python"
    ])
    assert result == 0
```

### 3. 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_formatter.py

# 运行特定测试方法
pytest tests/test_formatter.py::TestFormatter::test_format_python_code

# 显示覆盖率
pytest --cov=devkit_zero --cov-report=html

# 详细输出
pytest -v

# 失败时停止
pytest -x
```

## 📚 文档规范

### 1. README.md 结构

- 项目简介和特性
- 安装说明
- 快速开始示例
- 详细使用说明
- API 文档链接
- 贡献指南
- 许可证信息

### 2. API 文档

为每个公共函数和类编写详细的文档字符串，可以使用工具自动生成 API 文档：

```bash
# 生成文档 (使用 sphinx 等工具)
sphinx-build -b html docs/ docs/_build/
```

### 3. 更新日志 (CHANGELOG.md)

遵循 [Keep a Changelog](https://keepachangelog.com/) 规范：

```markdown
# Changelog

## [Unreleased]

### Added
- 新增功能描述

### Changed
- 更改的功能描述

### Fixed
- 修复的问题描述

## [1.0.0] - 2025-01-01

### Added
- 初始版本发布
```

## 🔄 Git 工作流

### 1. 分支策略

- `main`: 主分支，保持稳定
- `develop`: 开发分支，功能集成
- `feature/*`: 功能分支
- `hotfix/*`: 紧急修复分支
- `release/*`: 发布分支

### 2. 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

类型说明：
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建、工具等

示例：
```
feat(formatter): add javascript formatting support

Add basic JavaScript code formatting functionality
using internal AST parsing and indentation logic.

Closes #123
```

### 3. Pull Request 流程

1. 创建功能分支
2. 开发功能并编写测试
3. 确保所有测试通过
4. 代码格式化和静态检查
5. 提交 PR 到 `develop` 分支
6. 代码审查
7. 合并到 `develop`

## 🚀 发布流程

### 1. 版本号管理

使用 [Semantic Versioning](https://semver.org/) (SemVer)：

- `MAJOR.MINOR.PATCH`
- `1.0.0`: 初始版本
- `1.0.1`: 修复版本 
- `1.1.0`: 功能版本
- `2.0.0`: 破坏性更新

### 2. 发布检查清单

- [ ] 所有测试通过
- [ ] 代码覆盖率 ≥ 90%
- [ ] 更新版本号
- [ ] 更新 CHANGELOG.md
- [ ] 更新文档
- [ ] 标记 Git tag
- [ ] 构建和测试打包
- [ ] 发布到 PyPI

### 3. 自动化发布

使用 GitHub Actions：

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

## 📦 打包指南

### 1. PyPI 打包

```bash
# 清理旧文件
rm -rf build/ dist/ *.egg-info/

# 构建包
python -m build

# 检查包
twine check dist/*

# 上传到测试 PyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# 上传到正式 PyPI
twine upload dist/*
```

### 2. PyInstaller 打包

#### CLI 版本
```bash
pyinstaller --onefile \
    --name devkit-zero \
    --add-data "devkit_zero/assets;devkit_zero/assets" \
    devkit_zero/cli.py
```

#### GUI 版本
```bash
pyinstaller --onefile \
    --noconsole \
    --name devkit-zero-gui \
    --add-data "devkit_zero/assets;devkit_zero/assets" \
    --icon assets/app.ico \
    devkit_zero/gui_main.py
```

#### 打包配置文件 (devkit-zero.spec)
```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['devkit_zero/cli.py'],
    pathex=[],
    binaries=[],
    datas=[('devkit_zero/assets', 'devkit_zero/assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='devkit-zero',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

### 3. 跨平台构建

使用 GitHub Actions 进行多平台构建：

```yaml
name: Build Executables

on: [push, pull_request]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
        pip install pyinstaller
    
    - name: Build with PyInstaller
      run: |
        pyinstaller --onefile devkit_zero/cli.py
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v2
      with:
        name: devkit-zero-${{ matrix.os }}
        path: dist/
```

## 🔧 工具开发指南

### 1. 新工具模板

```python
"""
新工具模板
工具功能描述
"""

import argparse
from typing import Any, Dict, List, Optional


def main_function(param1: str, param2: int = 10) -> str:
    """
    主要功能函数
    
    Args:
        param1: 参数1描述
        param2: 参数2描述
        
    Returns:
        结果描述
        
    Raises:
        ValueError: 错误描述
    """
    # 实现主要逻辑
    return f"结果: {param1} - {param2}"


def register_parser(subparsers) -> None:
    """注册命令行参数解析器"""
    parser = subparsers.add_parser('newtool', help='新工具描述')
    
    # 添加参数
    parser.add_argument('param1', help='必需参数')
    parser.add_argument('--param2', '-p', type=int, default=10, help='可选参数')
    parser.add_argument('--output', '-o', help='输出文件路径')
    
    parser.set_defaults(func=main)


def main(args) -> str:
    """工具的主函数，处理命令行参数"""
    try:
        result = main_function(args.param1, args.param2)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            return f"结果已保存到: {args.output}"
        else:
            return result
            
    except Exception as e:
        raise RuntimeError(f"工具执行失败: {e}")


if __name__ == "__main__":
    # 独立测试代码
    print("测试新工具:")
    result = main_function("test", 20)
    print(result)
```

### 2. 添加新工具的步骤

1. **创建工具模块**: 在 `devkit_zero/tools/` 下创建新的 `.py` 文件
2. **实现核心功能**: 编写主要的功能函数
3. **添加CLI支持**: 实现 `register_parser()` 和 `main()` 函数
4. **更新包导入**: 在 `devkit_zero/tools/__init__.py` 中添加导入
5. **更新CLI注册**: 在 `devkit_zero/cli.py` 中注册新命令
6. **添加核心方法**: 在 `devkit_zero/core.py` 中添加便捷方法（可选）
7. **编写测试**: 在 `tests/test_tools/` 下创建测试文件
8. **更新文档**: 更新 README.md 和相关文档

### 3. 最佳实践

- 保持零依赖原则
- 提供清晰的错误信息
- 支持文件输入/输出
- 添加适当的日志记录
- 编写全面的测试
- 遵循统一的接口约定

---

遵循此开发规范，可以确保 DevKit-Zero 项目的代码质量、一致性和可维护性。
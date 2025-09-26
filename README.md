# DevKit-Zero

[![PyPI version](https://badge.fury.io/py/devkit-zero.svg)](https://badge.fury.io/py/devkit-zero)
[![Python Support](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**DevKit-Zero** 是一个轻量级、零依赖、功能强大的开发者工具箱，通过统一的命令行界面 (CLI) 和图形界面 (GUI)，解决开发者在代码处理、文本操作和环境辅助方面的高频需求。

> 🎯 **适合新手团队**: 本项目特别为编程新手和小团队设计，提供详细的开发指南和团队协作规范。详见 [📚文档中心](docs/README.md)。

## ✨ 特性

- 🚀 **零依赖**: 仅使用 Python 标准库，无需额外安装依赖
- 🛠️ **多工具集成**: 9+ 实用开发工具，一个包全搞定
- 💻 **双模式支持**: 命令行和图形界面双重体验
- 📦 **易于集成**: 既可作为库导入，也可独立运行
- 🎯 **开箱即用**: 一键安装，立即使用

## 🔧 包含工具

| 工具 | 功能描述 | 命令示例 |
|------|---------|-----------|
| **formatter** | 代码格式化 (Python/JS) | `devkit format --language python --input "code"` |
| **random_gen** | 随机数据生成 | `devkit random uuid` |
| **diff_tool** | 文本差异对比 | `devkit diff --text1 "a" --text2 "b"` |
| **converter** | 数据格式转换 | `devkit convert --from json --to csv` |
| **linter** | 代码静态检查 | `devkit lint --code "def test(): pass"` |
| **regex_tester** | 正则表达式测试 | `devkit regex "\\d+" "123abc"` |
| **batch_process** | 批量文件处理 | `devkit batch rename ./files "*.txt" "new_*"` |
| **markdown_preview** | Markdown 预览 | `devkit markdown README.md --output preview.html` |
| **port_checker** | 端口检查工具 | `devkit port check 80` |

## 📦 安装

### 从 PyPI 安装 (推荐)
```bash
pip install devkit-zero
```

### 开发版本安装
```bash
git clone https://github.com/devkit-zero/devkit-zero.git
cd devkit-zero
pip install -e .
```

### 安装可选依赖
```bash
# GUI 支持 (通常已包含在 Python 中)
pip install devkit-zero[gui]

# Web 界面支持
pip install devkit-zero[web]

# 开发依赖
pip install devkit-zero[dev]
```

## 🚀 快速开始

### 命令行使用

```bash
# 查看帮助
devkit-zero --help
devkit --help  # 简短别名

# 代码格式化
devkit format --input "def hello():print('hi')" --language python

# 生成 UUID
devkit random uuid

# 生成安全密码
devkit random password --length 16

# 文本对比
devkit diff --text1 "Hello World" --text2 "Hello Python"

# 代码检查
devkit lint --code "def badFunction(): pass"

# 正则测试
devkit regex "\\d+" "找到123个苹果"

# 端口检查
devkit port check 8080 --host localhost

# Markdown 预览
devkit markdown README.md --output preview.html --open
```

### 作为 Python 库使用

```python
import devkit_zero as dk

# 方式 1: 直接使用工具模块
from devkit_zero import formatter, random_gen, diff_tool

# 格式化代码
formatted = formatter.format_code("def hello():print('hi')", "python")
print(formatted)

# 生成随机数据
uuid = random_gen.generate_uuid()
password = random_gen.generate_secure_password(16)

# 文本对比
diff = diff_tool.compare_texts("text1", "text2")

# 方式 2: 使用核心类 (推荐)
from devkit_zero import DevKitCore

devkit = DevKitCore()

# 格式化代码
formatted = devkit.format_code("def hello():print('hi')", "python")

# 生成数据
uuid = devkit.generate_uuid()
password = devkit.generate_password(20)

# 检查代码
issues = devkit.lint_code("def badFunction(): pass")

# 测试正则
result = devkit.test_regex(r"\\d+", "123abc")

# 方式 3: 使用全局实例
from devkit_zero.core import devkit

formatted_code = devkit.format_code("code", "python")
```

### 图形界面使用

```bash
# 启动 GUI 应用
devkit-zero-gui

# 或者通过 Python 模块
python -m devkit_zero.gui_main
```

## 🏗️ 项目结构

```
DevKit-Zero/
├── devkit_zero/           # 🏠 主包目录
│   ├── __init__.py       #   包初始化，导出公共API
│   ├── __version__.py    #   版本信息 (v0.1.0)
│   ├── core.py           #   核心API类 (DevKitCore)
│   ├── cli.py            #   命令行入口 (devkit-zero)
│   ├── gui_main.py       #   GUI入口 (devkit-zero-gui)
│   ├── tools/            # 🛠️  工具模块目录
│   │   ├── __init__.py   #   工具注册和导出
│   │   ├── formatter.py  #   ⚡ 代码格式化器
│   │   ├── random_gen.py #   🎲 随机数据生成器
│   │   ├── diff_tool.py  #   📊 文件差异比较器
│   │   ├── converter.py  #   🔄 格式转换器
│   │   ├── linter.py     #   🔍 代码检查器
│   │   ├── regex_tester.py    #   📝 正则表达式测试器
│   │   ├── batch_process.py   #   📦 批量处理器
│   │   ├── markdown_preview.py #   📖 Markdown预览器
│   │   └── port_checker.py    #   🌐 端口检查器
│   ├── ui/               # 🖥️  用户界面模块
│   │   ├── __init__.py
│   │   └── gui_app.py    #   Tkinter GUI主界面
│   └── utils/            # 🔧 工具函数 (预留扩展)
├── tests/                # 🧪 测试目录
│   ├── test_tools/       #   工具模块测试
│   │   ├── test_formatter.py
│   │   └── test_random_gen.py
│   └── conftest.py       #   测试配置
├── docs/                 # 📚 文档目录 (预留)
├── assets/               # 🎨 资源文件 (预留)
├── templates/            # 📄 模板文件 (预留)
├── static/               # 📁 静态文件 (预留Web功能)
├── docs/                  # 📚 文档中心
│   ├── README.md         #   文档导航和使用指南
│   ├── team/             #   👥 团队协作文档
│   │   ├── BEGINNER_GUIDE.md      #   新手开发指南 ⭐
│   │   └── TEAM_GUIDELINES.md     #   团队协作规范 ⭐
│   ├── development/      #   🔧 开发技术文档
│   │   ├── DEVELOPMENT.md         #   开发者手册
│   │   ├── PROJECT_FRAMEWORK.md   #   项目架构设计
│   │   ├── PROJECT_SUMMARY.md     #   项目功能总结
│   │   └── FINAL_STATUS_REPORT.md #   项目完成状态
│   └── reference/        #   📖 参考资料
│       └── QUICK_REFERENCE.md     #   快速参考卡 ⭐
├── .github/              # ⚙️  GitHub配置
│   └── workflows/        #   CI/CD配置 (预留)
├── .gitignore            # Git忽略文件
├── setup.py              # 📦 安装配置 (pip install)
├── pyproject.toml        # 📋 项目元数据 (现代Python标准)
├── requirements.txt      # 📌 运行时依赖
├── requirements-dev.txt  # 🛠️  开发依赖
├── CHANGELOG.md          # 📈 版本变更记录
└── README.md             # 📖 项目说明 (本文件)
```

> 💡 **新手重点关注**: 标记了 ⭐ 的文档是团队新手必读文件
> 📚 **文档中心**: 所有详细文档都在 [docs/](docs/README.md) 目录，按类型分类整理

## 🔨 开发指南

### 环境设置

```bash
# 克隆项目
git clone https://github.com/devkit-zero/devkit-zero.git
cd devkit-zero

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# 安装开发依赖
pip install -e .[dev]
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_formatter.py

# 测试覆盖率
pytest --cov=devkit_zero --cov-report=html
```

### 代码规范

```bash
# 代码格式化
black devkit_zero/

# 静态检查
flake8 devkit_zero/
mypy devkit_zero/
```

### 添加新工具

1. 在 `devkit_zero/tools/` 下创建新模块
2. 实现核心功能和 `register_parser()` 函数
3. 在 `devkit_zero/tools/__init__.py` 中导入
4. 在 `devkit_zero/cli.py` 中注册命令
5. 在 `devkit_zero/core.py` 中添加快捷方法（可选）
6. 编写测试用例

## 📦 打包发布

### 使用 PyInstaller 打包

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包 CLI 版本
pyinstaller --onefile --name devkit-zero devkit_zero/cli.py

# 打包 GUI 版本
pyinstaller --onefile --noconsole --name devkit-zero-gui devkit_zero/gui_main.py

# 生成的可执行文件在 dist/ 目录
```

### 发布到 PyPI

```bash
# 构建包
python setup.py sdist bdist_wheel

# 上传到 PyPI
twine upload dist/*
```

## 👥 团队开发

### 📚 新手必读文档
- **[📖 文档中心](docs/README.md)** - 完整的文档导航和使用指南
- **[👶 新手开发指南](docs/team/BEGINNER_GUIDE.md)** - 从环境搭建到功能开发的完整教程
- **[👥 团队协作规范](docs/team/TEAM_GUIDELINES.md)** - Git工作流程和代码审查标准
- **[🚀 快速参考卡](docs/reference/QUICK_REFERENCE.md)** - 常用命令和开发模板速查

### 🚀 快速开始开发
```bash
# 1. 克隆项目
git clone <your-repo-url>
cd DevKit-Zero

# 2. 创建虚拟环境
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. 安装开发依赖
pip install -r requirements-dev.txt
pip install -e .

# 4. 运行测试确保环境正常
pytest

# 5. 运行现有功能
devkit-zero --help
devkit-zero-gui
```

### 🛠️ 添加新功能示例
想添加一个 `json-validator` 工具？跟着这个模板：

```python
# 在 devkit_zero/tools/json_validator.py 创建
def main_function(json_text: str) -> dict:
    """核心功能实现"""
    # 你的代码逻辑
    pass

def register_parser(subparsers) -> argparse.ArgumentParser:
    """注册命令行参数"""
    parser = subparsers.add_parser('json-validator', help='JSON验证器')
    parser.add_argument('--input', required=True, help='JSON输入')
    return parser

def main(args) -> int:
    """命令行入口"""
    result = main_function(args.input)
    print(result)
    return 0
```

详细开发流程请参考 [👶新手开发指南](docs/team/BEGINNER_GUIDE.md#功能开发流程)。

## 🤝 贡献

欢迎所有级别的开发者贡献！**特别欢迎编程新手**，我们有详细的指导文档。

### 💡 贡献方式
- 🐛 **报告Bug**: 通过 [Issues](../../issues) 提交bug报告
- ✨ **建议功能**: 提出新功能想法和建议
- 📝 **改进文档**: 帮助完善文档和示例
- 🔧 **贡献代码**: 修复bug或开发新功能
- 📞 **帮助他人**: 在讨论中帮助其他开发者

### 贡献步骤

1. **Fork** 项目到你的GitHub
2. **Clone** 到本地: `git clone <your-fork-url>`
3. **创建分支**: `git checkout -b feature/your-feature-name`
4. **开发功能**: 按照 [👶新手开发指南](docs/team/BEGINNER_GUIDE.md) 开发
5. **运行测试**: `pytest` 确保所有测试通过
6. **提交代码**: `git commit -am "feat: add your feature"`
7. **推送分支**: `git push origin feature/your-feature-name`
8. **创建PR**: 在GitHub上创建Pull Request

> 💡 **提示**: 提交前请阅读 [👥团队协作规范](docs/team/TEAM_GUIDELINES.md) 了解代码规范和提交格式。

## 📄 许可证

本项目采用 MIT 许可证。详情请看 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- 感谢所有贡献者
- 灵感来源于众多开发工具
- 特别感谢 Python 社区

## 📞 联系我们

- 项目主页: https://github.com/devkit-zero/devkit-zero
- 问题反馈: https://github.com/devkit-zero/devkit-zero/issues
- 邮箱: team@devkit-zero.com

---

**DevKit-Zero** - 让开发更简单 🚀
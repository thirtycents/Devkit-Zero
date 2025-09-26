# DevKit-Zero 快速参考卡 🚀

## 🏃‍♂️ 5分钟快速上手

### 环境准备
```bash
# 克隆项目
git clone <repo-url> && cd DevKit-Zero

# 虚拟环境
python -m venv venv && venv\Scripts\activate

# 安装依赖
pip install -r requirements-dev.txt && pip install -e .

# 验证安装
devkit-zero --help
```

---

## 🛠️ 工具快速使用

| 工具 | 命令 | 示例 |
|------|------|------|
| **格式化代码** | `devkit-zero formatter` | `devkit-zero formatter --input "def f():pass" --language python` |
| **生成UUID** | `devkit-zero random` | `devkit-zero random uuid` |
| **生成密码** | `devkit-zero random` | `devkit-zero random password --length 16` |
| **文本对比** | `devkit-zero diff` | `devkit-zero diff --text1 "hello" --text2 "world"` |
| **代码检查** | `devkit-zero linter` | `devkit-zero linter --code "def bad():pass"` |
| **正则测试** | `devkit-zero regex` | `devkit-zero regex "\\d+" "找到123个数字"` |
| **端口检查** | `devkit-zero port` | `devkit-zero port check 8080` |
| **MD预览** | `devkit-zero markdown` | `devkit-zero markdown README.md --output out.html` |

---

## 📁 重要目录结构

```
DevKit-Zero/
├── devkit_zero/tools/     # 👈 你主要工作的地方
├── tests/test_tools/      # 👈 写测试的地方
├── BEGINNER_GUIDE.md      # 👈 新手必读
├── TEAM_GUIDELINES.md     # 👈 团队规范
└── README.md              # 👈 项目说明
```

---

## 🔧 添加新工具模板

### 1. 创建工具文件
```python
# devkit_zero/tools/your_tool.py

def main_function(input_data: str) -> dict:
    """核心功能实现 - 这里写你的逻辑"""
    return {"result": f"处理了: {input_data}"}

def register_parser(subparsers):
    """注册命令行参数"""
    parser = subparsers.add_parser('your-tool', help='你的工具描述')
    parser.add_argument('--input', '-i', required=True, help='输入数据')
    return parser

def main(args) -> int:
    """命令行入口"""
    result = main_function(args.input)
    print(result)
    return 0
```

### 2. 注册工具
在 `devkit_zero/tools/__init__.py` 添加：
```python
from . import your_tool
AVAILABLE_TOOLS['your_tool'] = your_tool
```

### 3. 写测试
```python
# tests/test_tools/test_your_tool.py
import unittest
from devkit_zero.tools.your_tool import main_function

class TestYourTool(unittest.TestCase):
    def test_basic_function(self):
        result = main_function("test input")
        self.assertIn("result", result)
```

### 4. 测试运行
```bash
pytest tests/test_tools/test_your_tool.py -v
devkit-zero your-tool --input "test"
```

---

## 📝 Git工作流

### 开发新功能
```bash
# 1. 创建功能分支
git checkout main && git pull origin main
git checkout -b feature/your-feature-name

# 2. 开发 + 测试
# ... 写代码 ...
pytest

# 3. 提交
git add . && git commit -m "feat: add your feature"
git push origin feature/your-feature-name

# 4. 创建PR (在GitHub页面)
```

### 提交信息格式
```bash
feat: 新功能           # feat: add JSON validator
fix: 修复bug          # fix: correct formatter indentation
docs: 更新文档        # docs: update README
test: 添加测试        # test: add tests for random_gen
refactor: 重构代码    # refactor: simplify core API
```

---

## 🧪 测试命令

```bash
pytest                              # 运行所有测试
pytest tests/test_tools/ -v        # 运行工具测试，详细输出
pytest tests/test_tools/test_formatter.py  # 运行特定测试
pytest --cov=devkit_zero           # 测试覆盖率报告
```

---

## 🚨 常见问题

### Q: ImportError 导入错误？
```python
# ✓ 正确：使用相对导入
from ..core import DevKitCore

# ✗ 错误：绝对导入可能失败
from devkit_zero.core import DevKitCore
```

### Q: 测试失败？
```bash
# 确保在项目根目录
cd DevKit-Zero

# 重新安装项目
pip install -e .

# 清除Python缓存
find . -name "*.pyc" -delete
find . -name "__pycache__" -delete
```

### Q: GUI打不开？
```bash
# 检查tkinter是否安装 (通常内置)
python -c "import tkinter"

# 如果失败，安装GUI依赖
pip install tkinter  # 某些Linux发行版需要
```

---

## 📞 获取帮助

### 团队内部
- 💬 **微信群**: 日常问题快速讨论
- 📋 **GitHub Issues**: 正式bug报告和功能请求
- 📝 **Pull Request评论**: 代码相关讨论

### 自助资源
- 📖 [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md) - 完整开发指南
- 👥 [TEAM_GUIDELINES.md](TEAM_GUIDELINES.md) - 团队协作规范
- 🔧 [DEVELOPMENT.md](DEVELOPMENT.md) - 技术参考手册

### 提问模板
```markdown
**问题**: 简要描述问题
**环境**: Windows 10, Python 3.9
**重现步骤**: 
1. 执行了什么命令
2. 看到了什么错误

**尝试过的解决方法**: 
- 已经试过xxx
- 查看了xxx文档

**期望帮助**: 希望解决什么问题
```

---

## 💡 开发小贴士

### IDE设置 (VS Code)
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.linting.enabled": true,
    "editor.formatOnSave": true,
    "editor.rulers": [88]
}
```

### 调试技巧
```python
# 临时调试输出
def main_function(data):
    print(f"DEBUG: 输入数据 = {data}")  # 调试用
    result = process(data)
    print(f"DEBUG: 处理结果 = {result}")  # 调试用
    return result

# 运行单个工具进行测试
python -m devkit_zero.tools.your_tool
```

### 性能测试
```python
import time

def main_function(data):
    start = time.time()
    result = process(data)
    print(f"处理时间: {time.time() - start:.2f}秒")
    return result
```

---

**记住**: 不要害怕犯错，每个大神都是从新手开始的！有问题就问，团队一起成长！🌟
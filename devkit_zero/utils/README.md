# Utils 工具函数模块

这个模块包含项目中使用的通用工具函数和辅助类。

## 📁 模块规划

### 🔧 通用工具函数
```python
# 示例：文件操作工具
def safe_read_file(file_path: str, encoding: str = 'utf-8') -> str:
    """安全地读取文件内容"""
    pass

def ensure_directory(dir_path: str) -> None:
    """确保目录存在"""
    pass
```

### 🎨 字符串处理工具
```python
# 示例：文本处理函数
def clean_whitespace(text: str) -> str:
    """清理多余的空白字符"""
    pass

def truncate_text(text: str, max_length: int) -> str:
    """截断文本并添加省略号"""
    pass
```

### 🔍 验证工具
```python
# 示例：数据验证函数
def is_valid_email(email: str) -> bool:
    """验证邮箱格式"""
    pass

def is_valid_url(url: str) -> bool:
    """验证URL格式"""
    pass
```

### 📊 数据处理工具
```python
# 示例：数据转换函数
def flatten_dict(nested_dict: dict) -> dict:
    """扁平化嵌套字典"""
    pass

def merge_dicts(*dicts: dict) -> dict:
    """合并多个字典"""
    pass
```

## 💡 使用方式

### 导入工具函数
```python
# 导入特定函数
from devkit_zero.utils.file_utils import safe_read_file
from devkit_zero.utils.string_utils import clean_whitespace

# 或导入整个模块
from devkit_zero import utils

# 使用
content = utils.file_utils.safe_read_file('data.txt')
cleaned = utils.string_utils.clean_whitespace(content)
```

## 📋 添加新工具函数的步骤

### 1. 创建模块文件
```bash
# 在 devkit_zero/utils/ 目录下创建
touch devkit_zero/utils/new_utils.py
```

### 2. 实现工具函数
```python
# devkit_zero/utils/new_utils.py
def your_utility_function(param: str) -> str:
    """
    你的工具函数说明
    
    Args:
        param: 参数说明
        
    Returns:
        返回值说明
    """
    # 实现逻辑
    return processed_result
```

### 3. 在 __init__.py 中导出
```python
# devkit_zero/utils/__init__.py
from .new_utils import your_utility_function

__all__ = ['your_utility_function']
```

### 4. 编写测试
```python
# tests/test_utils/test_new_utils.py
import unittest
from devkit_zero.utils.new_utils import your_utility_function

class TestNewUtils(unittest.TestCase):
    def test_your_utility_function(self):
        result = your_utility_function("test")
        self.assertEqual(result, "expected")
```

## 🎯 工具函数设计原则

### 单一职责
- 每个函数只做一件事
- 函数名清楚表达功能

### 类型注解
- 使用类型注解提高代码可读性
- 便于IDE提供智能提示

### 错误处理
- 合理处理异常情况
- 提供有意义的错误信息

### 文档字符串
- 详细的函数说明
- 参数和返回值的描述
- 使用示例

## 🔄 重构建议

当工具模块中出现重复代码时，考虑将其提取到utils中：

```python
# 重构前：在多个工具中重复的代码
def format_file_size(size_bytes):
    # 在 formatter.py, batch_process.py 中都有类似代码
    pass

# 重构后：移动到 utils
# devkit_zero/utils/common.py
def format_file_size(size_bytes: int) -> str:
    """格式化文件大小显示"""
    pass

# 在工具模块中使用
from ..utils.common import format_file_size
```

> 📝 **注意**: 工具函数应该保持简单和通用，避免与特定业务逻辑耦合。
"""
测试代码格式化工具
"""

import unittest
from devkit_zero.tools import formatter


class TestFormatter(unittest.TestCase):
    """代码格式化工具测试类"""
    
    def setUp(self):
        """测试准备"""
        self.sample_python_code = """def hello():
print('Hello')
if True:
return 'done'
"""
        
        self.expected_python_code = """def hello():
    print('Hello')
    if True:
        return 'done'
"""

    def test_format_python_code_basic(self):
        """测试基础 Python 代码格式化"""
        result = formatter.format_python_code(self.sample_python_code)
        self.assertIsInstance(result, str)
        self.assertIn("def hello():", result)
        self.assertIn("    print('Hello')", result)

    def test_format_python_code_invalid_syntax(self):
        """测试无效语法处理"""
        invalid_code = "def hello( print('hi')"
        
        with self.assertRaises(ValueError):
            formatter.format_python_code(invalid_code)

    def test_format_javascript_code_basic(self):
        """测试基础 JavaScript 代码格式化"""
        js_code = """function hello(){
console.log('Hello');
if(true){
return 'done';
}
}"""
        
        result = formatter.format_javascript_code(js_code)
        self.assertIsInstance(result, str)
        self.assertIn("function hello(){", result)

    def test_format_code_with_language(self):
        """测试通过语言参数格式化代码"""
        # 测试 Python
        py_result = formatter.format_code(self.sample_python_code, "python")
        self.assertIsInstance(py_result, str)
        
        # 测试 JavaScript
        js_code = "function test(){console.log('test');}"
        js_result = formatter.format_code(js_code, "javascript")
        self.assertIsInstance(js_result, str)

    def test_unsupported_language(self):
        """测试不支持的语言"""
        with self.assertRaises(ValueError):
            formatter.format_code("code", "unsupported")

    def test_empty_code(self):
        """测试空代码"""
        result = formatter.format_python_code("")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
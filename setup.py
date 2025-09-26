#!/usr/bin/env python3
"""
DevKit-Zero 安装配置文件
"""

from setuptools import setup, find_packages
import os

# 读取 README 文件
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# 读取版本信息
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'devkit_zero', '__version__.py')
    version_dict = {}
    if os.path.exists(version_file):
        with open(version_file, 'r', encoding='utf-8') as f:
            exec(f.read(), version_dict)
    return version_dict.get('__version__', '1.0.0')

setup(
    name="devkit-zero",
    version=get_version(),
    author="DevKit-Zero Team",
    author_email="team@devkit-zero.com",
    description="零依赖开发者工具箱 - 轻量级、功能强大的开发者工具集",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/devkit-zero/devkit-zero",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Tools",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        # 保持零依赖，仅使用标准库
    ],
    extras_require={
        'gui': ['tkinter'],  # GUI 依赖（通常已包含在 Python 中）
        'web': ['flask'],    # Web 界面可选依赖
        'dev': [
            'pytest>=6.0',
            'black>=21.0',
            'flake8>=3.8',
            'mypy>=0.910',
        ],
    },
    entry_points={
        'console_scripts': [
            'devkit-zero=devkit_zero.cli:main',
            'devkit=devkit_zero.cli:main',  # 简短别名
        ],
        'gui_scripts': [
            'devkit-zero-gui=devkit_zero.gui_main:main',
        ],
    },
    include_package_data=True,
    package_data={
        'devkit_zero': ['assets/*', 'templates/*', 'static/*'],
    },
    zip_safe=False,
)
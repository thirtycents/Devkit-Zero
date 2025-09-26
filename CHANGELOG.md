# DevKit-Zero 更新日志

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 项目框架搭建完成
- 核心工具模块：格式化器、随机生成器、差异工具、转换器、代码检查器
- 正则表达式测试器
- 批量处理器
- Markdown 预览器
- 端口检查器
- 命令行界面（CLI）
- 图形用户界面（GUI）
- 统一的核心API接口
- 完整的包结构和配置文件
- 详细的文档和开发规范
- 单元测试框架
- 打包配置（PyInstaller, setuptools）

### Features
- 零依赖核心功能
- 模块化设计
- 插件式扩展
- 跨平台支持
- 多种安装和使用方式

## [0.1.0] - 2024-01-XX

### Added
- 初始版本发布
- 基础工具集合
- 命令行和GUI界面
- 基础文档

---

## 版本发布流程

1. 更新 `devkit_zero/__version__.py` 中的版本号
2. 更新此 CHANGELOG.md 文件
3. 提交更改：`git commit -am "Release vX.Y.Z"`
4. 创建标签：`git tag vX.Y.Z`
5. 推送到远程：`git push && git push --tags`
6. 发布到 PyPI：`python setup.py sdist bdist_wheel && twine upload dist/*`
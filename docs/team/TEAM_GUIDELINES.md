# DevKit-Zero 团队开发规范

## 📋 目录
1. [开发环境统一](#开发环境统一)
2. [代码提交规范](#代码提交规范)
3. [分支管理策略](#分支管理策略)
4. [代码审查流程](#代码审查流程)
5. [问题跟踪和解决](#问题跟踪和解决)
6. [团队沟通规范](#团队沟通规范)

---

## 💻 开发环境统一

### 必需工具清单
```bash
# 基础环境
Python 3.8+                 # 编程语言
Git 2.20+                  # 版本控制
VS Code / PyCharm          # 代码编辑器

# Python包管理
pip                        # 包安装工具
virtualenv 或 venv         # 虚拟环境

# 可选但推荐
GitHub Desktop             # Git图形界面 (新手友好)
Sourcetree                # 另一个Git图形界面
Postman                   # API测试 (如果开发Web功能)
```

### 开发环境配置

#### 1. 统一的VS Code设置
创建 `.vscode/settings.json`：
```json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=88"],
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true
}
```

#### 2. 统一的依赖管理
```bash
# 所有人使用相同的依赖版本
pip install -r requirements-dev.txt

# 新增依赖时，更新requirements文件
pip freeze > requirements.txt
```

---

## 📝 代码提交规范

### 提交信息格式
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Type类型说明
| Type | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: add JSON validator tool` |
| `fix` | 修复bug | `fix: correct formatter spacing issue` |
| `docs` | 文档更新 | `docs: update installation guide` |
| `test` | 测试相关 | `test: add unit tests for random_gen` |
| `refactor` | 重构代码 | `refactor: simplify core API interface` |
| `style` | 代码格式 | `style: fix indentation in cli.py` |
| `chore` | 构建/工具 | `chore: update gitignore file` |
| `perf` | 性能优化 | `perf: improve file reading speed` |

### 提交示例
```bash
# 好的提交信息 ✓
feat(tools): add JSON validator with schema support

- Implement basic JSON syntax validation
- Add optional JSON Schema validation
- Include comprehensive error messages
- Add CLI interface with file and string input

Closes #15

# 不好的提交信息 ✗
update stuff
fix bug
add new feature
```

### 提交频率建议
- **小步提交**: 每完成一个小功能就提交
- **功能完整**: 每次提交都应该是一个可运行的状态
- **描述清楚**: 其他人能理解这次改了什么

---

## 🌿 分支管理策略

### 分支类型和命名
```
main                        # 主分支，永远稳定
├── dev                    # 开发分支，集成测试
├── feature/tool-name      # 功能分支
├── bugfix/issue-123       # Bug修复分支
├── hotfix/critical-fix    # 紧急修复分支
└── release/v1.2.0         # 发布分支
```

### 分支工作流程

#### 新功能开发
```bash
# 1. 从main创建功能分支
git checkout main
git pull origin main
git checkout -b feature/json-validator

# 2. 开发过程中经常提交
git add .
git commit -m "feat: implement basic JSON parsing"
git push origin feature/json-validator

# 3. 功能完成后合并到dev
# (通过Pull Request)

# 4. 测试无问题后合并到main
```

#### Bug修复流程
```bash
# 1. 从main创建修复分支
git checkout main
git pull origin main
git checkout -b bugfix/formatter-indentation

# 2. 修复并测试
# ... fix code ...
git commit -m "fix: correct indentation logic in formatter"

# 3. 创建PR合并到main
```

### 分支保护规则
- `main` 分支需要通过PR才能合并
- 合并前必须通过所有测试
- 至少需要1人代码审查
- 禁止直接推送到 `main` 分支

---

## 🔍 代码审查流程

### 创建Pull Request

#### PR模板
```markdown
## 变更类型
- [ ] 新功能 (feature)
- [ ] Bug修复 (bugfix)
- [ ] 文档更新 (docs)
- [ ] 代码重构 (refactor)

## 变更描述
简要描述本次变更的内容...

## 测试情况
- [ ] 所有现有测试通过
- [ ] 添加了新的测试用例
- [ ] 手动测试通过

## 相关Issue
Closes #123

## 截图 (如果有UI变更)
[如果有的话，贴上截图]

## 额外说明
[任何需要审查者注意的事项]
```

### 代码审查清单

#### 审查者检查项
- [ ] 代码逻辑正确
- [ ] 符合代码规范
- [ ] 测试覆盖充分
- [ ] 文档更新及时
- [ ] 没有硬编码值
- [ ] 错误处理完善
- [ ] 性能无明显问题

#### 常见审查意见模板
```markdown
# 建议性意见 💡
建议将这个函数拆分成更小的函数，提高可读性。

# 必须修改 ⚠️
这里存在安全风险，需要添加输入验证。

# 赞扬 👍
这个解决方案很优雅，代码很清晰！

# 疑问 ❓
为什么选择这种方法而不是使用标准库的XXX？
```

### 处理审查意见
```bash
# 1. 根据意见修改代码
# ... make changes ...

# 2. 回复审查意见
# 在PR页面回复每个意见

# 3. 推送更新
git add .
git commit -m "refactor: address code review comments"
git push origin feature/your-branch

# 4. 请求重新审查
```

---

## 🐛 问题跟踪和解决

### Issue模板

#### Bug报告
```markdown
**Bug描述**
清楚简洁地描述bug是什么。

**重现步骤**
1. 执行 '...'
2. 点击 '...'
3. 看到错误

**期望行为**
描述你期望发生什么。

**实际行为**
描述实际发生了什么。

**环境信息**
- OS: [e.g. Windows 10]
- Python版本: [e.g. 3.9.1]
- 项目版本: [e.g. v1.2.0]

**其他信息**
任何其他有助于解决问题的信息。
```

#### 功能请求
```markdown
**功能描述**
清楚描述你想要的功能。

**使用场景**
描述什么情况下会用到这个功能。

**期望解决方案**
描述你希望如何实现这个功能。

**替代方案**
描述其他可能的实现方式。

**优先级**
- [ ] 高 (阻塞开发)
- [ ] 中 (重要但不紧急)  
- [ ] 低 (nice to have)
```

### 问题分类标签
- `bug`: 程序错误
- `enhancement`: 功能改进
- `documentation`: 文档相关
- `good-first-issue`: 新手友好
- `help-wanted`: 需要帮助
- `priority-high`: 高优先级

### 问题分配和跟踪
```markdown
# 问题状态流转
待分配 → 进行中 → 待审查 → 已完成

# 负责人分配原则
- Bug: 谁写的代码谁修复 (or 自愿认领)
- 新功能: 根据专长和工作量分配
- 文档: 大家轮流维护
```

---

## 💬 团队沟通规范

### 日常沟通渠道

#### 1. 微信群 - 日常沟通
- **用途**: 快速讨论、问题求助、进度同步
- **响应时间**: 工作时间1小时内，非工作时间尽力而为
- **使用规范**: 
  - 重要信息要@相关人员
  - 代码片段用代码格式发送
  - 截图时确保清晰可见

#### 2. GitHub Issues - 正式问题
- **用途**: Bug报告、功能请求、技术讨论
- **响应时间**: 48小时内
- **使用规范**: 
  - 使用标准模板
  - 提供充分的上下文信息
  - 及时更新状态

#### 3. Pull Request - 代码讨论
- **用途**: 代码审查、技术方案讨论
- **响应时间**: 24小时内审查
- **使用规范**: 
  - 详细的PR描述
  - 及时回复审查意见

### 会议规范

#### 每周站会 (15分钟)
- **时间**: 每周一上午10:00
- **内容**:
  - 上周完成了什么
  - 本周计划做什么
  - 遇到什么阻碍
- **记录**: 会议纪要发到群里

#### 月度回顾 (1小时)
- **内容**:
  - 项目进度回顾
  - 技术难点总结
  - 团队协作改进
- **输出**: 改进计划

### 求助规范

#### 提问的艺术 🤔
```markdown
# 好的提问方式 ✓
**问题**: 运行测试时出现ImportError
**环境**: Windows 10, Python 3.9, VS Code
**尝试过的方法**: 
1. 检查了__init__.py文件存在
2. 尝试了重新安装包
**错误信息**: [贴出完整的错误堆栈]
**期望帮助**: 如何解决这个导入问题？

# 不好的提问方式 ✗
"代码不能跑，求救！😭"
"有个bug，怎么办？"
```

#### 求助响应承诺
- **紧急问题** (阻塞工作): 1小时内响应
- **一般问题**: 当天回复
- **学习问题**: 有空时详细回答

### 知识分享

#### 技术分享会
- **频率**: 每两周一次
- **时长**: 30-45分钟
- **内容**: 
  - 新学到的技术
  - 踩过的坑
  - 开发经验

#### 文档维护
- **责任**: 谁写的功能谁负责文档
- **更新时机**: 代码变更时同步更新
- **审核**: PR时一并审查文档

---

## 🎯 团队发展规划

### 新人成长路径

#### Level 1: 入门 (1-2周)
- [ ] 熟悉项目结构
- [ ] 能够运行和测试项目
- [ ] 完成第一个小功能 (如修复拼写错误)
- [ ] 学会基本的Git操作

#### Level 2: 熟练 (1-2个月)
- [ ] 独立开发小工具模块
- [ ] 能够编写测试用例
- [ ] 参与代码审查
- [ ] 解决一般性bug

#### Level 3: 专家 (3-6个月)
- [ ] 设计复杂功能的架构
- [ ] 指导新人
- [ ] 负责关键模块维护
- [ ] 参与技术决策

### 技能发展计划
- **Python进阶**: 装饰器、生成器、异步编程
- **测试技能**: 单元测试、集成测试、性能测试
- **工程化**: CI/CD、代码质量、性能优化
- **领域知识**: 开发工具、用户体验、产品思维

---

## 🏆 团队激励机制

### 贡献积分制
- 完成Issue: 1-5分 (根据难度)
- 代码审查: 1分
- 文档贡献: 2分
- Bug修复: 3分
- 帮助队友: 1分

### 月度表彰
- **最佳贡献者**: 积分最高
- **最佳新人**: 新手中表现最好
- **最佳团队精神**: 帮助队友最多

### 成长激励
- **技术分享**: 分享学习心得
- **开源贡献**: 向其他项目贡献代码
- **参与决策**: 高级成员参与技术方案决策

---

记住我们的团队理念：

**"代码可以重写，但团队合作的经验是无价的！"** 🌟

**"没有愚蠢的问题，只有不问问题的愚蠢！"** 💡

**"今天的bug就是明天的经验！"** 🐛➡️✨
# Static Directory

这个目录用于存放Web界面的静态文件（如果开发Web功能）。

## 📁 用途说明
- **CSS样式**: Web界面样式文件
- **JavaScript**: 前端交互脚本
- **图片资源**: Web页面使用的图片
- **字体文件**: 自定义字体资源

## 📋 目录结构建议
```
static/
├── css/                # CSS样式文件
│   ├── main.css       # 主样式
│   ├── components/    # 组件样式
│   └── themes/        # 主题样式
├── js/                 # JavaScript文件
│   ├── app.js         # 主应用脚本
│   ├── utils/         # 工具函数
│   └── components/    # UI组件
├── images/             # 图片资源
│   ├── icons/         # 图标文件
│   ├── backgrounds/   # 背景图片
│   └── ui/            # UI相关图片
├── fonts/              # 字体文件
│   └── custom/        # 自定义字体
└── libs/               # 第三方库文件
    ├── bootstrap/     # CSS框架
    └── jquery/        # JavaScript库
```

## 💡 Web开发集成

### Flask应用集成
```python
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='../static')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)
```

### 样式文件引用
```html
<!-- 在HTML模板中引用 -->
<link rel="stylesheet" href="/static/css/main.css">
<script src="/static/js/app.js"></script>
```

## 🎨 样式开发规范

### CSS组织结构
- **main.css**: 全局样式和布局
- **components/**: 可复用组件样式
- **themes/**: 不同主题的样式变量

### JavaScript模块化
- **app.js**: 主应用逻辑
- **utils/**: 通用工具函数
- **components/**: UI组件的交互逻辑

## 🔧 开发工具支持

### 实时预览
```bash
# 如果使用Flask开发Web界面
python -m devkit_zero.web_app --debug
```

### 资源压缩
```bash
# CSS压缩
npm run build:css

# JS打包
npm run build:js
```

## 📱 响应式设计

建议使用移动优先的响应式设计：
```css
/* 移动端优先 */
.container {
    width: 100%;
    padding: 1rem;
}

/* 桌面端适配 */
@media (min-width: 768px) {
    .container {
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

> 📝 **注意**: 目前项目主要支持CLI和GUI，Web功能为可选扩展。如需开发Web界面，请参考项目架构文档。
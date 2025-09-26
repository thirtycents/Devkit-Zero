# Assets Directory

这个目录用于存放项目的资源文件，如：

## 📁 用途说明
- **图标文件**: 应用程序图标、工具图标
- **图片资源**: 文档中使用的图片、截图
- **配置文件**: 默认配置模板
- **样式文件**: CSS样式（如果有Web界面）

## 📋 文件组织建议
```
assets/
├── icons/          # 图标文件
│   ├── app.ico    # 应用程序图标
│   └── tools/     # 工具图标
├── images/         # 图片资源
│   ├── screenshots/  # 应用截图
│   └── docs/        # 文档图片
├── configs/        # 配置模板
│   └── default.json
└── styles/         # 样式文件
    └── app.css
```

## 💡 使用方式
在代码中引用资源文件：
```python
import os
from pathlib import Path

# 获取assets目录路径
assets_dir = Path(__file__).parent.parent / "assets"
icon_path = assets_dir / "icons" / "app.ico"
```

> 📝 **注意**: 添加新资源文件时，请保持目录结构清晰，并更新相关文档。
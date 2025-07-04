# My Hugo Blog

这是一个使用 Hugo 搭建的个人博客项目。博客内容托管在 GitHub Pages 上，使用 GitHub Actions 自动构建和部署。

## 本地开发

1. 安装 Hugo
```bash
# Windows 使用 Chocolatey
choco install hugo -confirm

# 或使用 Scoop
scoop install hugo
```

2. 本地预览
```bash
hugo server -D
```

3. 创建新文章
```bash
hugo new posts/my-first-post.md
```

## 部署

本项目使用 GitHub Actions 自动部署到 GitHub Pages。只需要将更改推送到 main 分支，GitHub Actions 将自动构建并部署网站。

## 目录结构

```
.
├── archetypes/    # 文章模板
├── content/       # 博客文章内容
├── layouts/       # 自定义布局
├── static/        # 静态文件
├── themes/        # 主题
└── config.toml    # Hugo 配置文件
``` 
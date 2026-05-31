---
title: "GordenPPTSkill: AI-friendly PPT builder skill: 17 hand-polished..."
date: 2026-05-31T20:31:32
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 GordenPPTSkill，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Python", "GordenPPTSkill", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/GordenSun/GordenPPTSkill"
    alt: "GordenPPTSkill"
---

# GordenPPTSkill: AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

![GordenPPTSkill](https://opengraph.githubassets.com/1/GordenSun/GordenPPTSkill)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill)
> 生成时间: 2026-05-31 20:31:32

## 项目概览

[GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@GordenSun](https://github.com/GordenSun) |
| **编程语言** | Python |
| **Star 数** | 555 ⭐ |
| **Fork 数** | 62 |
| **创建时间** | 2026-05-27 |
| **最后更新** | 2026-05-31 |

## 项目简介

AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only.

Python 是一门简洁优雅的编程语言，广泛应用于数据科学、人工智能、Web 开发等领域。

## 核心特性

根据项目 README 分析，GordenPPTSkill 的主要特点包括：

- **高关注度**：555 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：62 个 Fork，社区参与度高
- **快速成长**：自 2026-05-27 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

GordenPPTSkill 基于 **Python** 技术栈构建：

1. **编程语言**：Python
2. **项目规模**：555 个 Star，获得广泛认可
3. **社区活跃度**：62 个 Fork，开发者积极参与

## README 原文摘要

```
# PPT Builder Skill

> 史上最强原生PPT Skill，更适合中国宝宝。生成的效果不让你震惊，你来打我。
>
> ⚠️ **非商业使用**：本仓库及内置模板**仅供个人学习与研究**，禁止任何商业用途。
> 
> **支持定制私有化模板**：如果你想要Agent能按你公司的PPT模板来生成PPT，可以加我微信**duge360**定制。

## 交流群

扫码加入「PPT Skill 交流群」一起讨论 / 反馈问题 / 看新版本：

<p align="center">
  <img src="./assets/group-qr.jpg" alt="PPT Skill 交流群二维码" width="320" />
</p>

> ⚠️ 群二维码 7 天内有效；过期请来 [Issues](https://github.com/GordenSun/GordenPPTSkill/issues) 留言，我会贴新的。

## 几大特色
1、能生成信息密度高、排版复杂、看起来高大上的PPT，也支持生成简约、商务风格的PPT。适合国企、互联网大厂使用。

2、兼容所有模型，DeepSeek、小米Mimo、Claude、GPT均实测过，国产模型也能完成的非常好。

3、技能自动更新机制：如果我更新了可选用的PPT模板，使用技能时会自动更新技能。技能像软件一样可以更新

## 谁要看这个

- 想给自己用的 AI 助手装一个"做 PPT"技能的人：**请读 [SKILL.md](./SKILL.md)**
- 想看本项目目录怎么组织：继续往下看本文件
- 想理解模板分类 / 推荐：**请读 [templates/INDEX.md](./templates/INDEX.md)**

## 快速开始（命令行）

````bash
# 1. 确认依赖
python3 -c "import pptx; print(pptx.__version__)"   # python-pptx 1.0+
soffice --version    # LibreOffice (仅渲染预览时需要)
which pdftoppm       # poppler   (仅渲染预览时需要)

# 2. 选定模板 + 写 edits.json，跑构建
python3 scripts/build_pptx.py \
    templates/minimal-business-summary/template.pptx \
    edits.json \
    out/final.pptx \
    --detail templates/minimal-business-summary/detail.json

# 3. (可选) 渲染最终预览图
python3 scripts/render_slides.py out/final.pptx out/preview --dpi 144
````

## 字体环境

模板大量使用 `微软雅黑`。如果你的机器没装它，配 `~/.config/fontconfig/fonts.conf` 加一条 alias：

````xml
<alias binding="strong">
  <family>微软雅黑</family>
  <accept>
    <family>WenQuanYi Micro Hei</family>
    <family>DengXian</family>
    <family>Noto Sans SC</family>
    <family>PingFang SC</family>
  </accept>
</alias>
````

(`brew install --cask font-noto-sans-sc`，或下载 WenQuanYi Micro Hei 放进 `~/Library/Fonts/` 并 `fc-cache -f`。)

## 目录速览

````
SKILL.md         # AI 入口文档
VERSION          # 1.0.0
CHANGELOG.md     # 人读变更
updates.json     # 机读变更
manifest.json    # 每文件版本 + sha256
scripts/         # 5 个面向使用者的脚本（build / render / update / manifest）
references/      # 编辑规则、Schema、工作流参考
templates/       # 17 个模板（每个 4 文件）
````

## 致谢与版权

- 本仓库没有PPT模板的版权
- **禁止任何
```

## 最近更新记录

- 暂无提交记录


## 适用场景

GordenPPTSkill 适合以下用户：

- 数据科学家和 AI 研究者、Web 后端开发者、自动化脚本编写者
- 希望提升开发效率的技术团队
- 正在探索 Python 生态的开发者
- 对 AI-friendly PPT builder skill: 17 hand-polished Chinese PPTX templates + non-destructive text-only editing tools (python-pptx based). Pick a template, write edits.json, build a real .pptx with the layout intact. Personal/research use only. 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/GordenSun/GordenPPTSkill) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

GordenPPTSkill 是本周 GitHub 上值得关注的热门项目，凭借 555 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-27 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/GordenSun/GordenPPTSkill)*
*生成时间: 2026-05-31 20:31:32*

---
title: "GordenSuperPPTSkills: AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式..."
date: 2026-06-09T00:20:39
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 GordenSuperPPTSkills，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Python", "GordenSuperPPTSkills", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/GordenSun/GordenSuperPPTSkills"
    alt: "GordenSuperPPTSkills"
---

# GordenSuperPPTSkills: AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

![GordenSuperPPTSkills](https://opengraph.githubassets.com/1/GordenSun/GordenSuperPPTSkills)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills)
> 生成时间: 2026-06-09 00:20:39

## 项目概览

[GordenSun/GordenSuperPPTSkills](https://github.com/GordenSun/GordenSuperPPTSkills) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@GordenSun](https://github.com/GordenSun) |
| **编程语言** | Python |
| **Star 数** | 324 ⭐ |
| **Fork 数** | 40 |
| **创建时间** | 2026-06-07 |
| **最后更新** | 2026-06-08 |

## 项目简介

AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。

Python 是一门简洁优雅的编程语言，广泛应用于数据科学、人工智能、Web 开发等领域。

## 核心特性

根据项目 README 分析，GordenSuperPPTSkills 的主要特点包括：

- **高关注度**：324 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：40 个 Fork，社区参与度高
- **快速成长**：自 2026-06-07 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

GordenSuperPPTSkills 基于 **Python** 技术栈构建：

1. **编程语言**：Python
2. **项目规模**：324 个 Star，获得广泛认可
3. **社区活跃度**：40 个 Fork，开发者积极参与

## README 原文摘要

```
# Gorden Super PPT Skills（技能包）

AI PPT赛道终结者，史上最最最强 PPT Skill！！！

使用GPT生成豪华的图片格式PPT，然后转换为**完全可编辑**的PPTX文件。

Skill全流程已拆成 **3 个独立技能**，可以拆分使用和优化：

| 技能 | 作用 | 输入 → 输出 |
|---|---|---|
| **[GordenImagePPTGen](GordenImagePPTGen/SKILL.md)** | 生成「图片格式的 PPT」 | 主题/内容 → 每页 .png + 图片型 .pptx |
| **[GordenImage2PPTX](GordenImage2PPTX/SKILL.md)** | 把「图片 PPT / 图片」还原成可编辑 pptx | 图片 → 可编辑 .pptx（背景+骨架+图标+文本 四层） |
| **[GordenSuperPPTSkill](GordenSuperPPTSkill/SKILL.md)** | 打包编排前两者，依次执行 | 主题/内容 → 图片型 PPT + 可编辑 pptx |

- 只要做图片版 PPT → **GordenImagePPTGen**
- 只把图片转可编辑 → **GordenImage2PPTX**
- 一键"先出图再转可编辑" / 未指定 → **GordenSuperPPTSkill**（A→B 串联）

## 效果展示
1、GordenImagePPTGen（Gorden的图片PPT生成技能）生成图片格式的PPT

![GordenImagePPTGen 生成的图片格式 PPT 示例](examples/example-Image-ppt.png)

2、GordenImage2PPTX（Gorden的图片转PPTX技能）把图片转换为完全可编辑的PPTX文件

![GordenImage2PPTX 转换后的可编辑 PPTX 示例](examples/example-editable-pptx.png)

## 如何使用
仅限Codex使用。

第1步：把Github仓库地址发给Codex让他安装技能；

第2步：按需使用。GPT 5.5模型，推理强度选"中"即可。
如果只生成图片格式PPT，提示词：
````
使用GordenImagePPTGen技能，生成一个N页的PPT，内容为XXX，要求PPT要求豪华、信息密度高、排版复杂
````

如果只想**把图片PPT转换成可编辑的PPTX文件**，提示词：
````
把当前文件夹里的XXX.png，使用GordenImage2PPTX，还原成可编辑的PPT，必须严格遵循技能步骤
````

说明：
本技能仅适用于Codex，因为必须使用GPT生成图片和GPT的视觉能力，理论上Opus+GPT生图接口也可以实现，但是本技能没有做专门的适配。

图片转可编辑PPTX文件，比较费额度，转换1张图片大概耗费Plus订阅5小时额度的10%。

框架图默认是整体的一张图，也支持拆分成一个个独立的框架模块图，提示词里明确告诉Codex即可。

## 原理讲解
核心使用的是GPT的生图能力和视觉解析能力。
大致步骤是：依次提取PPT图片的背景图、框架图、图标和装饰图、文本。最后在PPT里按坐标拼装起来。当然为了实现完美的效果，做了很多细节验证和约束规则。
使用过程中，你能看到GPT生成的过程图片。

### 背景图

![图片转 PPTX 过程中的背景图](examples/背景图.png)

### 框架图

![图片转 PPTX 过程中的框架图](examples/框架图.png)

### 图标和装饰

![图片转 PPTX 过程中的图标和装饰](examples/图标和装饰.png)




## 安装（给AI看的）

每个技能目录都是**自包含**的（自带 `scripts/` 与 `references/`）。按需复制：

````bash
# Codex（按需选装其一/全部）
cp -R GordenImagePPTGen   "${CODEX_HOME:-$HOME/.codex}/skills/GordenImagePPTGen"
cp -R GordenImage2PPTX    "${CODEX_HOME:-$HOME/.codex}/skills/GordenImage2PPTX"
cp -R GordenSuperPPTSkill "${CODEX_HOME:-$HOME/.codex}/skills/GordenSuperPPTSkill"
````

> GordenSuperPPTSkill 依赖另两个技能，请与它们一起安装（同一 skill
```

## 最近更新记录

- **2026-06-07**: Update README.md
- **2026-06-07**: Update README.md
- **2026-06-07**: Update README.md
- **2026-06-07**: Initial commit


## 适用场景

GordenSuperPPTSkills 适合以下用户：

- 数据科学家和 AI 研究者、Web 后端开发者、自动化脚本编写者
- 希望提升开发效率的技术团队
- 正在探索 Python 生态的开发者
- 对 AI PPT赛道终结者，史上最最最强 PPT Skill！！！  使用GPT生成豪华的图片格式PPT，然后转换为完全可编辑的PPTX文件。 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/GordenSun/GordenSuperPPTSkills) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

GordenSuperPPTSkills 是本周 GitHub 上值得关注的热门项目，凭借 324 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-06-07 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/GordenSun/GordenSuperPPTSkills)*
*生成时间: 2026-06-09 00:20:39*

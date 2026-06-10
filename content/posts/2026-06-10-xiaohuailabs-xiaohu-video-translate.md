---
title: "xiaohu-video-translate: 对 AI 说一句话，把外语视频自动配上中文字幕 —— 下载/转写/翻译/润色/烧录一条龙，全程..."
date: 2026-06-10T14:31:45
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 xiaohu-video-translate，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Python", "xiaohu-video-translate", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/xiaohuailabs/xiaohu-video-translate"
    alt: "xiaohu-video-translate"
---

# xiaohu-video-translate: 对 AI 说一句话，把外语视频自动配上中文字幕 —— 下载/转写/翻译/润色/烧录一条龙，全程本地，转写零 API 费

![xiaohu-video-translate](https://opengraph.githubassets.com/1/xiaohuailabs/xiaohu-video-translate)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [xiaohuailabs/xiaohu-video-translate](https://github.com/xiaohuailabs/xiaohu-video-translate)
> 生成时间: 2026-06-10 14:31:45

## 项目概览

[xiaohuailabs/xiaohu-video-translate](https://github.com/xiaohuailabs/xiaohu-video-translate) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@xiaohuailabs](https://github.com/xiaohuailabs) |
| **编程语言** | Python |
| **Star 数** | 378 ⭐ |
| **Fork 数** | 56 |
| **创建时间** | 2026-06-08 |
| **最后更新** | 2026-06-10 |

## 项目简介

对 AI 说一句话，把外语视频自动配上中文字幕 —— 下载/转写/翻译/润色/烧录一条龙，全程本地，转写零 API 费

Python 是一门简洁优雅的编程语言，广泛应用于数据科学、人工智能、Web 开发等领域。

## 核心特性

根据项目 README 分析，xiaohu-video-translate 的主要特点包括：

- **高关注度**：378 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：56 个 Fork，社区参与度高
- **快速成长**：自 2026-06-08 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

xiaohu-video-translate 基于 **Python** 技术栈构建：

1. **编程语言**：Python
2. **项目规模**：378 个 Star，获得广泛认可
3. **社区活跃度**：56 个 Fork，开发者积极参与

## README 原文摘要

```
# xiaohu-video-translate

> 一句话把外语视频变成**带中文字幕的视频 + 中文文稿**。下载、转写、翻译、润色、烧录，一条龙跑完，全程本地，转写不花一分钱 API 费。
> One sentence turns a foreign-language video into a **Chinese-subtitled video + a clean transcript**. Download → transcribe → translate → polish → burn-in, end to end, all local, zero transcription API cost.

**语言 / Language:** [中文](#中文) ｜ [English](#english)

这是一套 AI 编程命令行工具用的**技能（Skills）**。它本质是「脚本 + 一份说明书」，**不绑死任何一家**：[Claude Code](https://claude.com/claude-code)、OpenClaw（小龙虾）、Gemini CLI、Codex 都能用。装好后你不用记任何命令，直接说一句「把这个链接翻译成中文字幕视频」，剩下的它全自动做完。

---

## 中文

### 一条龙工作流

它把原本要开四五个软件、来回折腾一两个小时的活，串成一条全自动流水线：

````
视频链接/本地文件
      │
      ▼
  ① 下载  ──►  ② 提取音频 + Whisper 转写  ──►  ③ 翻译  ──►  ④ 润色  ──►  ⑤ 烧录字幕
      │                  （词级时间戳）          （任意外语→中文）  （断句/去标点/对轴）      │
      │                                                                                ▼
      └──────────────────────────────────────────────►  带中文字幕的视频 + Markdown 文稿
````

你只管说一句话，五步它自己走完。中间任何一步要调整（双语、不要水印、快速模式），对它说就行。

### 支持多语种

不挑语言。**英语、日语、韩语、法语、西班牙语……只要 Whisper 听得懂的，都能转成中文字幕。** Whisper 自动识别原语种，翻译环节把任意外语翻成中文。中文视频则只做转写和文稿，不走翻译。

### 字幕两种选

- **纯中文**：画面干净
- **中英双语**：中文大、英文小，主次分明（用真正的 ASS 字幕做字号反差，SRT 做不到这个），适合顺便练听力

### 为什么用它

- **本地、免费、能离线**：转写用 [Whisper](https://github.com/openai/whisper)（苹果芯片走 MLX + Metal GPU 加速），在你电脑里完成，不上传、不收费。翻译复用你已经在用的 AI，不用再单独买翻译 API。
- **时间戳是真的准**：拿词级时间戳按「句子 + 停顿」切分，字幕不会跑在说话人前面，也不会半句甩到下一条。
- **字幕是给人看的**，不是机翻直出：自动纠正转写听错的专有名词（Claude 常被听成 cloud、MCP 被听成 NCP），按语义断句，术语保留英文。
- **烧字幕 + 水印一次编码完成**，不掉画质。

### 它其实是三个技能

| 技能 | 职责 |
|------|------|
| **xiaohu-video-md** | 总指挥。下载 / 提音频 / Whisper 转写 / 调用润色 / 烧字幕 / 出 Markdown |
| **xiaohu-subtitle-polish** | 字幕翻译与润色。纠错、翻译、断句、去标点、时间戳对齐、双语 ASS |
| **xiaohu-video-download** | 纯下载工具。下视频 / 下音频 / 下播放列表 / 给本地视频烧字幕 |

翻译管线由 `xiaohu-video-md` 总调度，翻译那一步它自己会去叫 `xiaohu-subtitle-polish`。三个技能各自独立，也可单独用。

### 演示案例

同一段 a16z 英文访谈，翻成中 / 日 / 韩 / 阿 / 法 5 种语言的双语字幕——各语种译文在上、英文原文在下，从右往左书写的阿拉伯语也排得整整齐齐：

![多语言双语字幕对比](assets/demo-multilang.jpg)

烧进画面后的中英双语字幕（中文大、
```

## 最近更新记录

- **2026-06-08**: docs: 补演示案例（5 语言双语字幕对比图 + 中英实拍）
- **2026-06-08**: 修复转写引擎默认路径、改名 xiaohu-video-translate、补全跨工具支持
- **2026-06-06**: bilingual_ass: 按文字脚本自动选字体，多语种双语开箱即用
- **2026-06-05**: README：突出一条龙工作流 + 多语种 + 多工具 + Windows/Linux 安装区别
- **2026-06-05**: 开源视频翻译技能套件：下载 + Whisper 转写 + 翻译润色 + 烧录字幕


## 适用场景

xiaohu-video-translate 适合以下用户：

- 数据科学家和 AI 研究者、Web 后端开发者、自动化脚本编写者
- 希望提升开发效率的技术团队
- 正在探索 Python 生态的开发者
- 对 对 AI 说一句话，把外语视频自动配上中文字幕 —— 下载/转写/翻译/润色/烧录一条龙，全程本地，转写零 API 费 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/xiaohuailabs/xiaohu-video-translate) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

xiaohu-video-translate 是本周 GitHub 上值得关注的热门项目，凭借 378 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-06-08 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/xiaohuailabs/xiaohu-video-translate)*
*生成时间: 2026-06-10 14:31:45*

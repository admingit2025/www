---
title: "nbd-vram: Use your NVIDIA GPU's VRAM as swap space on Lin..."
date: 2026-06-04T08:31:44
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 nbd-vram，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Shell", "nbd-vram", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/c0deJedi/nbd-vram"
    alt: "nbd-vram"
---

# nbd-vram: Use your NVIDIA GPU's VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you're getting swapped to SSD, this puts that VRAM to work

![nbd-vram](https://opengraph.githubassets.com/1/c0deJedi/nbd-vram)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [c0deJedi/nbd-vram](https://github.com/c0deJedi/nbd-vram)
> 生成时间: 2026-06-04 08:31:44

## 项目概览

[c0deJedi/nbd-vram](https://github.com/c0deJedi/nbd-vram) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@c0deJedi](https://github.com/c0deJedi) |
| **编程语言** | Shell |
| **Star 数** | 349 ⭐ |
| **Fork 数** | 10 |
| **创建时间** | 2026-05-30 |
| **最后更新** | 2026-06-03 |

## 项目简介

Use your NVIDIA GPU's VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you're getting swapped to SSD, this puts that VRAM to work

Shell 脚本是自动化运维和 DevOps 的利器，简单高效。

## 核心特性

根据项目 README 分析，nbd-vram 的主要特点包括：

- **高关注度**：349 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：10 个 Fork，社区参与度高
- **快速成长**：自 2026-05-30 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

nbd-vram 基于 **Shell** 技术栈构建：

1. **编程语言**：Shell
2. **项目规模**：349 个 Star，获得广泛认可
3. **社区活跃度**：10 个 Fork，开发者积极参与

## README 原文摘要

```
# nbd-vram

Use your NVIDIA GPU's VRAM as swap space on Linux.

Built for hybrid graphics laptops with soldered memory and no upgrade path. The display runs off the integrated AMD/ATI GPU. The NVIDIA card sits idle most of the time, its VRAM completely unused. This puts that VRAM to work as high-priority swap.

Tested on: AMD/ATI + RTX 3070 Laptop (GA104M, 16 GB RAM, 8 GB VRAM), driver 580.159.03, kernel 6.17, Pop!_OS. Allocated 7 GB for swap. End result including zram and SSD swap: ~46 GB total addressable memory, tripled from stock. Overflow order: RAM fills, then VRAM absorbs the spill (PCIe), then zram compresses the rest (CPU), then SSD only if everything else is exhausted.

![demo](demo.gif)

---

## How it works

A small daemon allocates VRAM via the CUDA driver API, then serves it as a block device using the NBD (Network Block Device) protocol over a Unix socket. The kernel's built-in `nbd` driver connects to it and exposes `/dev/nbdX`. From there it's a normal swap device.

Data path: kernel swap subsystem - /dev/nbdX - nbd kernel driver - Unix socket - nbd-vram daemon - cuMemcpyHtoD/DtoH - GPU VRAM.

No kernel module to write or maintain. No NVIDIA kernel symbols. Survives kernel and driver updates without rebuilding anything.

---

## Why not the NVIDIA P2P API?

The "obvious" approach is `nvidia_p2p_get_pages_persistent`, which pins VRAM pages in BAR1 so the CPU can access them directly via `ioremap_wc`. Every existing project that tried this route hits the same wall: the NVIDIA driver returns `EINVAL` on consumer GeForce GPUs. Both the persistent and non-persistent variants, both flag values. It's gated at the RM level for Quadro/datacenter SKUs only, regardless of driver version.

The other approach - directly `ioremap_wc` the BAR1 physical address without going through the P2P API - also doesn't work. The GPU's internal page tables only have ~16 MiB of BAR1 mapped (just the display framebuffer). Reads from the rest return zeros. `mkswap` appears to su
```

## 最近更新记录

- **2026-06-03**: Merge pull request #7 from c0deJedi/fix/readme-typo
- **2026-06-03**: fix: typo
- **2026-06-03**: Merge pull request #6 from c0deJedi/chore/issue-5-benchmark-suite
- **2026-06-03**: chore: add benchmark suite and performance results (closes #5)
- **2026-06-02**: Merge pull request #3 from c0deJedi/feat/issue-1-power-management


## 适用场景

nbd-vram 适合以下用户：

- 开源爱好者、技术探索者、相关领域开发者
- 希望提升开发效率的技术团队
- 正在探索 Shell 生态的开发者
- 对 Use your NVIDIA GPU's VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you're getting swapped to SSD, this puts that VRAM to work 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/c0deJedi/nbd-vram) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

nbd-vram 是本周 GitHub 上值得关注的热门项目，凭借 349 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-30 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/c0deJedi/nbd-vram)*
*生成时间: 2026-06-04 08:31:44*

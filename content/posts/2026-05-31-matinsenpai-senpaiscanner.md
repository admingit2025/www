---
title: "SenPaiScanner：轻量级 Cloudflare IP 扫描器，让代理连接不再掉线"
author: "GitHub Trending 深度解析"
date: 2026-05-31
draft: false
cover: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200"
tags: ["Go", "Cloudflare", "网络工具", "代理", "VLESS", "Trojan", "xray"]
categories: ["GitHub Trending"]
---

## 项目概览

| 信息 | 详情 |
|------|------|
| **项目** | SenPaiScanner |
| **作者** | MatinSenPai |
| **Stars** | 597 ⭐ |
| **Forks** | 41 |
| **语言** | Go |
| **许可证** | MIT |
| **最新版本** | v0.5.0 |
| **创建时间** | 2026-05-28 |

## 项目简介

SenPaiScanner 是一款用 Go 编写的轻量级 Cloudflare IP 扫描器，内置终端 UI（TUI），专为网络延迟不可预测、连接频繁掉线的场景设计。用户只需粘贴 VLESS 或 Trojan 配置，选择参数，即可自动寻找真正可用的 Cloudflare IP——无需记忆任何命令行参数。

## 下载资源

- **源码**：[GitHub 仓库](https://github.com/MatinSenPai/SenPaiScanner)
- **最新 Release**：[v0.5.0 下载](https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0)
- **支持平台**：Linux (x86_64/ARM64)、macOS (Intel/Apple Silicon)、Windows (x86_64)

## 核心功能分析

### 双阶段扫描架构

SenPaiScanner 的工作流程分为两个阶段：

**Phase 1 — 连通性扫描**
- 从 Cloudflare 官方 IP 段中随机选取候选 IP（或从自定义文件读取）
- 根据用户配置 URL 自动提取 SNI、Host、WebSocket Path、端口等参数
- 对每个候选 IP 执行 HTTP/TLS 探测，验证 trace 可达性
- 对 WebSocket 类型配置，额外检测 TLS 连接是否能抵御 DPI 干扰
- 支持 1,000 / 5,000 / 20,000 / 自定义数量 IP，50 / 100 / 200 / 自定义并发数

**Phase 2 — xray 端到端验证**
- 启动内嵌的 xray 实例
- 将 Phase 1 筛选出的最佳候选通过真实的 VLESS/Trojan 配置进行端到端测试
- 结果表格展示：端点地址、传输类型、下载速度、延迟（TTFB）、通过/失败状态
- 按 `c` 键一键复制可用 `IP:port` 到剪贴板，同时保存到 `ips.txt`

### 终端 UI（TUI）

整个操作通过终端界面完成，无需命令行参数：

- 方向键导航，Enter 确认
- 支持多端口选择（443, 8443, 2053, 2083, 2087, 2096）
- 实时扫描结果输出
- Vim 风格快捷键（h/j/k/l）
- Config URL 输入支持 Ctrl+A / Ctrl+E 跳转

### 邻居扫描

v0.5.0 新增功能：在 Phase 1 扫描中发现健康的 IP 后，自动搜索其邻近 IP 进行扩展验证，提高可用 IP 的发现率。

### 实时结果文件

每次扫描生成 `SenPaiScannerResult-YYYYMMDD-HHMMSS.txt` 文件，可在扫描运行期间用任何编辑器实时查看结果。

## 技术架构解读

### 技术栈

- **语言**：Go — 单二进制分发，无运行时依赖
- **UI 框架**：Bubble Tea（charmbracelet）— 现代 TUI 框架
- **代理核心**：内嵌 xray-core — 无需额外安装 xray
- **IP 来源**：Cloudflare 官方发布的 IPv4/IPv6 段列表（内嵌于二进制中）
- **构建系统**：Makefile + GitHub Actions CI

### 架构亮点

1. **零外部依赖**：xray 核心直接嵌入二进制，无需用户单独安装代理软件
2. **自适应探测**：根据配置 URL 自动选择探测策略（HTTP 探测 vs WebSocket 探测）
3. **多端口并行**：一个 IP 在多个 Cloudflare CDN 端口上同时测试，找到最佳 IP:port 组合
4. **内嵌 IP 段**：Cloudflare 官方 IP 段快照内嵌在二进制中，无需联网获取
5. **跨平台编译**：支持 Linux / macOS / Windows 多架构构建

### 为什么不用 Ping？

Cloudflare 在边缘 IP 上丢弃 ICMP 包，传统 ping 测试完全无效。SenPaiScanner 验证的是 HTTP/TLS 行为，并通过 xray 进行真实的代理流量测试——这比 ping 或裸 TCP 连接更接近 VLESS/Trojan 的实际使用场景。

## README 精选

> **Tips for restricted networks:**
> - Start with defaults — 5,000 random IPs, 50 workers, 5s timeout
> - Use "From File" after a partial run to re-validate your shortlist on more ports
> - Try multiple ports — Cloudflare CDN ports behave differently under DPI
> - 0% loss alone is not enough — non-zero download throughput is required

## 最近更新动态

| 日期 | 更新内容 |
|------|----------|
| 2026-05-30 | v0.5.0 — 新增邻居扫描功能，Phase 2 支持可选 Top N 配置，增强实时结果更新 |
| 2026-05-29 | v0.4.0 — 合并多菜单流程为单一工作流，优化 Phase 1 探测引擎 |
| 2026-05-28 | 项目创建，初始发布 |

## 应用场景

1. **网络受限环境**：在 DPI 干扰严重的网络中寻找可用的 Cloudflare IP
2. **代理稳定性优化**：找到延迟最低、速度最快的 IP:port 组合
3. **批量 IP 筛选**：快速从数千个 Cloudflare IP 中筛选出可用节点
4. **多端口探索**：在不同 CDN 端口上测试同一 IP，找到最佳端口
5. **配置验证**：验证 VLESS/Trojan 配置在特定 IP 上是否真正可用

## 快速开始指南

### 安装

**Linux / macOS（一键安装）：**
```bash
curl -fsSL https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh | bash
```

**Windows（PowerShell）：**
```powershell
$r = Invoke-RestMethod https://api.github.com/repos/matinsenpai/senpaiscanner/releases/latest
$url = ($r.assets | Where-Object name -like "*windows*x86_64*").browser_download_url
Invoke-WebRequest $url -OutFile senpaiscanner.zip
Expand-Archive senpaiscanner.zip .
```

**从源码构建：**
```bash
go install github.com/matinsenpai/senpaiscanner/cmd/senpaiscanner@latest
```

### 使用

1. 运行 `senpaiscanner` 打开 TUI
2. 选择 "Find Working IPs"
3. 粘贴 VLESS 或 Trojan 配置 URL
4. 调整扫描参数（IP 数量、并发数、超时、端口）
5. 按 Enter 开始扫描
6. Phase 2 完成后按 `c` 复制可用 IP:port

## 总结

SenPaiScanner 填补了一个真实的工具空白：在 Cloudflare CDN 上为代理配置找到真正可用的 IP。它不是又一个 ping 工具——而是通过真实的 TLS/HTTP/WebSocket 探测和 xray 端到端验证来确保找到的 IP 在实际代理场景中确实可用。Go 语言的单二进制特性加上内嵌的 xray 核心让用户无需任何额外安装即可上手，TUI 界面降低了使用门槛。对于需要稳定代理连接的用户来说，这是一款非常实用的开源工具。

---

*本文基于 SenPaiScanner v0.5.0 版本撰写，项目持续活跃开发中。*

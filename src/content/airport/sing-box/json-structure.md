---
title: "sing-box JSON 配置文件结构解析"
description: "从零读懂 sing-box 的配置代码，了解 inbounds, outbounds, route 的工作逻辑。"
order: 3
---

## 一、 核心骨架

sing-box 的配置文件是一个庞大的 JSON 对象。最核心的三个字段是：
1. `inbounds` (入站)：定义了设备如何把流量传给 sing-box（如 TUN 虚拟网卡、SOCKS 端口）。
2. `outbounds` (出站)：定义了 sing-box 把流量发往哪里（如机场的各个节点、直连 DIRECT）。
3. `route` (路由)：连接入站和出站的大脑，决定流量应该走哪条出站通道。

## 二、 JSON 语法的严谨性

不同于 Clash 的 YAML，JSON 对格式要求极其严格。少一个逗号或多一个括号都会导致核心启动失败。建议使用 VSCode 等专业编辑器进行修改。

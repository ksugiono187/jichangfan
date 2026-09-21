---
title: "Sing-box 极客配置与深度调优"
description: "包含 Hysteria2 协议支持、内存优化、TUN 模式故障排除等核心调优指南。"
order: 99
topics:
  - sing-box
---

本文将为您汇总该分类下的一系列高频问题与进阶技巧，帮助您全面提升使用体验。

## sing-box 与 Hysteria2 协议的完美结合

## 一、 暴力发包的魅力

基于 UDP 的 Hysteria2 协议不讲武德，它无视网络的拥塞控制，以固定的速度强行向客户端发送数据。在丢包率高达 20% 的晚高峰公网上，传统的 TCP 协议速度归零，而 Hysteria2 依然能跑满带宽。

## 二、 端口跳跃 (Port Hopping)

运营商经常会对异常的 UDP 大流量进行限速或封锁端口。sing-box 支持配置 Hysteria2 的端口跳跃功能，让连接在多个端口之间不断随机切换，有效躲避运营商的 QoS 审查。


---

## sing-box 在 iOS 端的完整使用评测

## 一、 免费的破局者

在 iOS 平台上，优秀的代理软件（如 Shadowrocket, Quantumult X, Surge）全部是收费的。而 sing-box 官方客户端作为开源项目，在美区 App Store 免费提供，这对小白用户是极大的福音。

## 二、 图形化界面的进步

早期的 sing-box iOS 端完全靠手搓代码。现在，它已经内置了完善的 Profile 管理面板，支持一键粘贴订阅链接、自动更新、可视化的节点选择和测速。

## 三、 后台保活表现

得益于 iOS 15+ 的 Network Extension 接口和自身的轻量内核，sing-box 在 iOS 后台挂机的耗电量甚至低于很多老牌软件，非常适合 24 小时常驻。


---

## sing-box JSON 配置文件结构解析

## 一、 核心骨架

sing-box 的配置文件是一个庞大的 JSON 对象。最核心的三个字段是：
1. `inbounds` (入站)：定义了设备如何把流量传给 sing-box（如 TUN 虚拟网卡、SOCKS 端口）。
2. `outbounds` (出站)：定义了 sing-box 把流量发往哪里（如机场的各个节点、直连 DIRECT）。
3. `route` (路由)：连接入站和出站的大脑，决定流量应该走哪条出站通道。

## 二、 JSON 语法的严谨性

不同于 Clash 的 YAML，JSON 对格式要求极其严格。少一个逗号或多一个括号都会导致核心启动失败。建议使用 VSCode 等专业编辑器进行修改。


---

## sing-box 内存占用极限优化技巧

## 一、 禁用不必要的模块

sing-box 包含了丰富的底层模块。如果您不需要，可以在配置文件中关闭 `clash_api`（这会禁用外部控制面板）和复杂的 `cache_file`（缓存文件），这能释放大量内存。

## 二、 精简规则集

不要在内存仅有 128MB 的老旧路由器上加载动辄几十兆的全球域名规则库。只保留必需的“国内直连”和“国外代理”基础规则，就能让 sing-box 运行得如丝般顺滑。


---

## sing-box 路由规则 (Route) 编写指南

## 一、 Rule 的基本写法

在 `route.rules` 数组中，每一项都是一个匹配条件。例如 `{"domain_suffix": [".cn"], "outbound": "direct"}`，意为所有国内域名直接发送到直连出站。

## 二、 Rule Set (规则集)

为了避免把上万个域名写在配置文件里，sing-box 引入了 Rule Set (SRS 格式文件)。这是经过二进制预编译的规则数据库，加载速度极快，内存占用极低，是 sing-box 性能强悍的秘诀之一。

## 三、 默认路由

如果所有规则都没有命中，流量将走向您配置的 `auto_detect_interface` 或排在出站列表第一位的 outbound。


---

## sing-box 服务端搭建初探

## 一、 一端两用

sing-box 最酷的地方在于，它的客户端和服务端用的是同一个二进制文件。只要您修改了配置文件，它就能瞬间从客户端变成一台提供代理服务的服务器。

## 二、 部署极简服务端

在 Linux VPS 上，您只需要编写一个 `inbounds` 为 vmess 或 trojan 的 JSON，配置好证书和监听端口，运行 `sing-box run`，您的专属节点就搭建完成了，完全不需要安装庞大的面板脚本。


---

## sing-box TUN 模式开启与排错

## 一、 权限问题

在 Windows 上开启 sing-box 的 TUN 模式，必须以管理员权限运行程序，否则无法加载 WinTun 虚拟网卡驱动，导致核心启动失败崩溃。

## 二、 DNS 劫持

TUN 模式下最常见的问题是 DNS 无法正确解析。在 `inbounds` 中配置 TUN 时，务必确保 `auto_route` 和 `strict_route` 参数开启，并将系统的 DNS 请求强行劫持到 sing-box 的 DNS 引擎中进行处理，防止产生 DNS 污染泄露。


---

## 如何在 sing-box 中配置 Vless Reality

## 一、 Reality 协议简介

Reality 取代了传统的 TLS 证书配置，不需要自己的域名，它通过模拟握手（Target 机制），向审查系统展示大厂（如微软或苹果）真实的公钥证书，从而隐藏代理的真实意图。

## 二、 配置关键参数

在 sing-box 的 outbound 中配置 Reality，您必须填对三个核心参数：
1. `server_name` (SNI)：您要伪装的目标域名（如 `www.microsoft.com`）。
2. `public_key`：服务端生成的公钥。
3. `short_id`：短 ID，用于验证连接身份。

只要填对这三个参数，您的节点将坚如磐石。


---


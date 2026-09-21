---
title: "sing-box 与 Hysteria2 协议的完美结合"
description: "拯救垃圾线路！利用 sing-box 驱动 Hysteria2 实现晚高峰满速狂飙。"
order: 7
---

## 一、 暴力发包的魅力

基于 UDP 的 Hysteria2 协议不讲武德，它无视网络的拥塞控制，以固定的速度强行向客户端发送数据。在丢包率高达 20% 的晚高峰公网上，传统的 TCP 协议速度归零，而 Hysteria2 依然能跑满带宽。

## 二、 端口跳跃 (Port Hopping)

运营商经常会对异常的 UDP 大流量进行限速或封锁端口。sing-box 支持配置 Hysteria2 的端口跳跃功能，让连接在多个端口之间不断随机切换，有效躲避运营商的 QoS 审查。

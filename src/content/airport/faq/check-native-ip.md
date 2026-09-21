---
title: "如何判断我的节点是不是原生 IP？"
description: "拒绝商家忽悠！教您三个实用的工具，一秒识别节点的真实归属地与纯净度。"
order: 4
---

## 方法一：IP 数据库查询

连上节点后，访问 `ipinfo.io` 或 `bgp.he.net`。查看页面上的 ASN 信息。如果显示的是大云厂商（如 Alibaba, Tencent, DigitalOcean），那大概率是机房广播 IP；如果显示的是当地的宽带运营商（如 HKT, Chunghwa Telecom），则有很大可能是原生 IP。

## 方法二：流媒体检测脚本

在节点连接状态下，使用开源的检测脚本（如 Github 上的 Netflix-Verify）。它会明确告诉你当前 IP 只能看 Netflix 自制剧，还是能看全部非自制版权剧（全解锁）。

## 方法三：欺诈分 (Fraud Score) 查询

访问 `scamalytics.com` 查 IP 欺诈分。分数越低（通常低于 15），说明这个 IP 越干净，越不容易在使用 ChatGPT 等服务时遇到频繁弹验证码或封号的问题。

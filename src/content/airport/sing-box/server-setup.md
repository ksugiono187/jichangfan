---
title: "sing-box 服务端搭建初探"
description: "不仅是客户端！教您如何在一台海外 VPS 上部署 sing-box 作为翻墙服务端。"
order: 10
---

## 一、 一端两用

sing-box 最酷的地方在于，它的客户端和服务端用的是同一个二进制文件。只要您修改了配置文件，它就能瞬间从客户端变成一台提供代理服务的服务器。

## 二、 部署极简服务端

在 Linux VPS 上，您只需要编写一个 `inbounds` 为 vmess 或 trojan 的 JSON，配置好证书和监听端口，运行 `sing-box run`，您的专属节点就搭建完成了，完全不需要安装庞大的面板脚本。

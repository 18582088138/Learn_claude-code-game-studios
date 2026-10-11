# Godot 官方教程学习索引

适用对象：有编程、AI 开发经验，第一次做游戏。目标：用 Godot + GDScript 做一款 2D 类《吸血鬼幸存者》单机游戏，先自玩，Windows 优先，尽早在手机测试。

整理日期：2026-10-10。

## 从哪里开始

1. 打开 [学习路线](01-learning-roadmap.md)：按功能学习，不用先学完全部文档。
2. 打开 [官方教程对照表](02-official-tutorials.md)：查中英文原文，区分必学、按需、后置内容。
3. 打开 [实践与验收清单](03-practice-checklist.md)：每完成一个阶段勾选并记录试玩结果。

**建议第一步：阅读“节点与场景”“创建实例”“第一个脚本”“玩家输入”，然后做出一个可移动的玩家。** 信号、碰撞、UI 在实现相应功能时学习。

## 使用方式

学习循环：阅读相关章节 → 自己解释概念 → 让 DSH 实现一个小功能 → 在 Godot 中运行 → 调整一个参数 → 记录结果。

让 AI 带你做项目时，要求它指出使用的节点、场景、信号与官方章节。不能把“AI 说已经完成”作为验收依据；移动、受伤、升级和重开都要实际操作。

这些 Markdown 文件可用 VS Code 的 Markdown 预览或其他支持 Markdown 的编辑器阅读。对照表中的本地链接不需要联网；官方原文链接需要联网。

## 版本约定

- 使用 Godot **4.x** 的稳定版并记录确切版本，教程、导出模板、插件与之匹配。
- `stable` 是官方的稳定版文档入口，会随版本发布变化，并不固定到本次整理日期的引擎。
- 安装引擎后，在官方文档版本选择器中选择对应版本；保存链接时可将 `stable` 换为实际存在的版本路径。
- 中文翻译可能落后于英文，遇到 API 或界面不一致时对照英文及安装版本的类参考。
- 本资料默认 GDScript、2D；不需要先学习 C#、GDExtension、3D 或联网。

## 手机范围

“手机”尚未区分 Android 或 iOS，因此指南同时列出两者。建议先完成 Windows 战斗循环，再在实际目标手机测试。

- Android：按安装版本的官方导出文档配置 JDK、Android SDK 和导出模板。
- iOS：官方流程需要 macOS 和 Xcode；Windows 上可以开发共用游戏逻辑，但不能直接完成该官方 iOS 构建流程。
- PC 与手机共用玩法逻辑，分别提供键盘和触屏输入；横屏只是本指南的起步建议，可以按个人设计调整。

具体要求见 [官方导出章节](02-official-tutorials.md#pc手机与后续功能)。

## 资料边界与来源

这是一份独立编写的学习索引与项目练习指南，**不是 Godot 官方教程的全文下载或官方翻译**。它把官方章节映射到你的项目需求，完整内容以链接中的官方文档为准。本地指南可以离线阅读。

- [Godot 官方中文文档](https://docs.godotengine.org/zh_CN/stable/)
- [Godot 官方英文文档](https://docs.godotengine.org/en/stable/)
- [官方 2D 游戏教程](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/index.html)
- [官方示例仓库](https://github.com/godotengine/godot-demo-projects)

`official-links.json` 保存本次中英文链接的核查状态和用于核查的短摘录。`check_official_links.py` 是可选的链接复查脚本，仅使用 Python 标准库；通常只需阅读上述三个文档。脚本中的 `checked_date` 是本次整理日期，今后复查时应更新该日期。

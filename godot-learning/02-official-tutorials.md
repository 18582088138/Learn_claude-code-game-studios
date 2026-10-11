# 官方教程对照表

[返回索引](README.md) · [学习路线](01-learning-roadmap.md) · [验收清单](03-practice-checklist.md)

链接来自 Godot 官方 `stable` 文档；中文与英文并列便于比较。下面的用途与练习是本指南编写的建议。标为“必学”也不要求一次性读完，在对应阶段学习即可。

## 基础流程

| 优先级 | 章节与中英文原文 | 对应你的游戏 | 学习后的检查 |
|---|---|---|---|
| 浏览 | [引擎简介：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/introduction/index.html) / [English](https://docs.godotengine.org/en/stable/getting_started/introduction/index.html) | 了解编辑器和基本工作方式 | 能找到场景树、检查器、文件系统和运行按钮 |
| 总入口 | [基础流程：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/step_by_step/index.html) / [English](https://docs.godotengine.org/en/stable/getting_started/step_by_step/index.html) | 核心概念学习目录 | 知道基础各章解决什么问题 |
| 必学 | [节点与场景：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/step_by_step/nodes_and_scenes.html) / [English](https://docs.godotengine.org/en/stable/getting_started/step_by_step/nodes_and_scenes.html) | 玩家、敌人、子弹的结构 | 能说明节点、场景、场景树的关系 |
| 必学 | [创建实例：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/step_by_step/instancing.html) / [English](https://docs.godotengine.org/en/stable/getting_started/step_by_step/instancing.html) | 重复生成敌人和子弹 | 能放入多个同一场景的实例 |
| 必学 | [第一个脚本：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/step_by_step/scripting_first_script.html) / [English](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_first_script.html) | 把行为连接到节点 | 知道脚本挂在哪个节点，如何查看错误 |
| 必学 | [玩家输入：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/step_by_step/scripting_player_input.html) / [English](https://docs.godotengine.org/en/stable/getting_started/step_by_step/scripting_player_input.html) | 键盘移动 | 能配置 Input Map 并改变按键 |
| 必学 | [信号：中文](https://docs.godotengine.org/zh_CN/stable/getting_started/step_by_step/signals.html) / [English](https://docs.godotengine.org/en/stable/getting_started/step_by_step/signals.html) | 死亡、拾取、升级、刷新 HUD | 能说明发出信号者与接收者 |
| 按需 | [GDScript 基础：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/scripting/gdscript/gdscript_basics.html) / [English](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html) | 看懂并修改 AI 生成的代码 | 能用类型、数组、字典、@export、函数；不用先通读 |

## 官方第一款 2D 游戏

这是 Dodge the Creeps 教程。完整项目入口：[GDScript 完成版](https://github.com/godotengine/godot-demo-projects/tree/master/2d/dodge_the_creeps)。示例仓库 `master` 对应开发分支，运行前按 [仓库版本说明](https://github.com/godotengine/godot-demo-projects#godot-versions)选择与引擎匹配的示例，不要默认最新分支能在任意 Godot 4.x 打开。

| 官方顺序 | 中英文原文 | 与类幸存者的对照 | 需要自己补充的内容 |
|---|---|---|---|
| 总览 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/index.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/index.html) | 理解一个完整小游戏的组成 | 自动攻击、升级等另行实现 |
| 1 项目设置 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/01.project_setup.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/01.project_setup.html) | 窗口与基础配置 | 你的分辨率、输入方案 |
| 2 玩家场景 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/02.player_scene.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/02.player_scene.html) | 玩家可视节点、碰撞 | 可按设计改用 CharacterBody2D；不能只换节点而保留不匹配代码 |
| 3 玩家代码 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/03.coding_the_player.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/03.coding_the_player.html) | 输入、运动、动画、被击中事件 | 血量、无敌时间、摄像机 |
| 4 创建敌人 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/04.creating_the_enemy.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/04.creating_the_enemy.html) | 复用敌人场景 | 教程敌人行为不是幸存者式追击，需要重新设计 |
| 5 主场景 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/05.the_main_game_scene.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/05.the_main_game_scene.html) | 生成、计时、开始与结束 | 波次、玩家周围生成、难度曲线 |
| 6 HUD | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/06.heads_up_display.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/06.heads_up_display.html) | 展示状态与开始按钮 | 血条、经验条、升级选择 |
| 7 收尾 | [中文](https://docs.godotengine.org/zh_CN/stable/getting_started/first_2d_game/07.finishing-up.html) / [English](https://docs.godotengine.org/en/stable/getting_started/first_2d_game/07.finishing-up.html) | 完善小游戏与音效 | 武器反馈、通关结算与多平台验证 |

## 类幸存者功能所需的专项章节

| 优先级 | 中英文官方原文 | 你的用途 | 建议练习 |
|---|---|---|---|
| 必学 | [物理简介：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/physics/physics_introduction.html) / [English](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html) | 碰撞对象、layer 与 mask | 写出玩家、敌人、子弹、经验的检测关系 |
| 必学 | [Area2D：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/physics/using_area_2d.html) / [English](https://docs.godotengine.org/en/stable/tutorials/physics/using_area_2d.html) | 受击、范围攻击、拾取 | 改变拾取范围且不影响受击范围 |
| 必学 | [CharacterBody2D：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/physics/using_character_body_2d.html) / [English](https://docs.godotengine.org/en/stable/tutorials/physics/using_character_body_2d.html) | 可控角色运动 | 比较移动方式；阅读 velocity 与 move_and_slide 的单位和调用约定 |
| 必学 | [Timer：中文](https://docs.godotengine.org/zh_CN/stable/classes/class_timer.html) / [English](https://docs.godotengine.org/en/stable/classes/class_timer.html) | 攻击、生成、倒计时 | 调整攻击间隔；核对暂停与重开行为 |
| 按需 | [Camera2D：中文](https://docs.godotengine.org/zh_CN/stable/classes/class_camera2d.html) / [English](https://docs.godotengine.org/en/stable/classes/class_camera2d.html) | 跟随玩家 | 调整平滑、缩放；检查视野 |
| 必学 | [资源：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/scripting/resources.html) / [English](https://docs.godotengine.org/en/stable/tutorials/scripting/resources.html) | 武器、敌人和升级配置 | 做两个不同武器配置；区分共享配置与每局状态 |
| 必学 | [GUI 尺寸与锚点：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/ui/size_and_anchors.html) / [English](https://docs.godotengine.org/en/stable/tutorials/ui/size_and_anchors.html) | 血量、经验、升级界面 | 改窗口尺寸后仍能正确显示 |
| 必学 | [GUI 容器：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/ui/gui_containers.html) / [English](https://docs.godotengine.org/en/stable/tutorials/ui/gui_containers.html) | 升级三选一布局 | 用容器排版三个升级按钮 |

## PC/手机与后续功能

| 优先级 | 中英文官方原文 | 用途与学习时机 |
|---|---|---|
| 初始选择 | [渲染器：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/rendering/renderers.html) / [English](https://docs.godotengine.org/en/stable/tutorials/rendering/renderers.html) | 简单 2D 第一版可从 Compatibility 开始；实际性能需要测试 |
| 尽早验证 | [多分辨率：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/rendering/multiple_resolutions.html) / [English](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html) | 窗口比例、缩放、手机画面；世界视野与 HUD 都要检查 |
| 手机阶段 | [ScreenTouch：中文](https://docs.godotengine.org/zh_CN/stable/classes/class_inputeventscreentouch.html) / [English](https://docs.godotengine.org/en/stable/classes/class_inputeventscreentouch.html) | 触点按下、抬起与触点 id |
| 手机阶段 | [ScreenDrag：中文](https://docs.godotengine.org/zh_CN/stable/classes/class_inputeventscreendrag.html) / [English](https://docs.godotengine.org/en/stable/classes/class_inputeventscreendrag.html) | 拖动方向，模拟摇杆；不是现成摇杆教程 |
| 手机阶段 | [TouchScreenButton：中文](https://docs.godotengine.org/zh_CN/stable/classes/class_touchscreenbutton.html) / [English](https://docs.godotengine.org/en/stable/classes/class_touchscreenbutton.html) | 游戏触屏按钮；不能直接当成模拟摇杆 |
| 尽早验证 | [导出项目：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/export/exporting_projects.html) / [English](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html) | 理解导出模板、预设和资源打包 |
| 第一版 | [Windows 导出：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/export/exporting_for_windows.html) / [English](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_windows.html) | 脱离编辑器运行自己的游戏 |
| Android 目标 | [Android 导出：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/export/exporting_for_android.html) / [English](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html) | 按安装版本文档准备 JDK、SDK、模板，在真机运行；商店发布后置 |
| iOS 目标 | [iOS 导出：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/export/exporting_for_ios.html) / [English](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_ios.html) | 官方导出需要 macOS 和 Xcode；提前确认设备与构建环境 |
| 战斗后 | [分析器：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/scripting/debug/the_profiler.html) / [English](https://docs.godotengine.org/en/stable/tutorials/scripting/debug/the_profiler.html) | 测量大量敌人与子弹时的耗时，不靠猜测优化 |
| 发现瓶颈后 | [优化概述：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/performance/general_optimization.html) / [English](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html) | 根据测量结果改进；不必第一天做复杂架构 |
| 完整闭环后 | [存档：中文](https://docs.godotengine.org/zh_CN/stable/tutorials/io/saving_games.html) / [English](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html) | 先保存最高分与设置，再考虑局外成长 |

## 暂时不用系统学习

3D 渲染、联网同步、编辑器插件、GDExtension、完整寻路系统、复杂 Shader、商店付费和广告接入。以后需求出现时再补对应章节。

## 如何比较中文与英文

1. 中文理解流程，英文确认方法名、参数与限制。
2. 两页使用相同的版本与相同的章节路径。
3. 教程讲组织方法，类参考确认具体 API；两者要配合。
4. AI 生成的代码若与示例不同，让它解释原因并提供对应版本出处。
5. 如链接失败或页面标题变化，回到官方文档首页搜索英文主题名；核查记录不代表未来永远可访问。

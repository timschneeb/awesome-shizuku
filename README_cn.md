# awesome-shizuku

### 语言
[English](/README.md) | 简体中文 | [繁體中文](/README_tw.md)

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允许普通应用程序在非root 设备上使用 ADB 直接使用权限提升的系统 API。本列表汇集了一些已知可利用 Shizuku 功能的应用程序。

更多详情：https://shizuku.rikka.app/

欢迎拉取请求。有关提示，请参阅 [贡献](CONTRIBUTING.md)。闭源应用列在另一个文件中。详情请参见[下文](#closed-source-apps)。


> [!NOTE]
> 如需获取本列表的最新动态，[你可以查看每日更新日志](https://github.com/timschneeb/changelog-awesome-shizuku)。

--------------------


## 目录

- [Apps](#apps)
  - [Shizuku implementations](#shizuku-implementations)
  - [AI agents](#ai-agents)
  - [Android Auto](#android-auto)
  - [Android TV](#android-tv)
  - [Audio](#audio)
  - [Automation](#automation)
  - [Communication](#communication)
  - [Customization](#customization)
  - [Development utilities](#development-utilities)
  - [Device Owner (DPM)](#device-owner-dpm)
  - [Display management](#display-management)
  - [Entertainment](#entertainment)
  - [File management](#file-management)
  - [Games](#games)
  - [Input methods](#input-methods)
  - [Installer & app stores](#installer--app-stores)
  - [Miscellaneous](#miscellaneous)
  - [Network](#network)
  - [Patching](#patching)
  - [Power management](#power-management)
  - [Privacy](#privacy)
  - [Productivity](#productivity)
  - [Quick settings](#quick-settings)
  - [Software management](#software-management)
  - [Task manager](#task-manager)
  - [Terminals](#terminals)
  - [Vendor-specific](#vendor-specific)
    - [Google Pixel](#google-pixel)
    - [Samsung OneUI](#samsung-oneui)
    - [MIUI](#miui)
    - [Other](#other)
  - [Closed-source apps](#closed-source-apps)
  - [Unlisted apps](#unlisted-apps)
- [Development libraries](#development-libraries)
  - [Core](#core)
  - [Filesystem](#filesystem)
  - [System](#system)
  - [Power](#power)
- [Miscellaneous content](#miscellaneous-content)
- [Rish shell](#rish-shell)
- [Annotations](#annotations)
- [License](#license)

--------------------

## Apps

### Shizuku implementations


* [Porter](https://github.com/d4rken-org/porter) - Minimal, maintained Shizuku fork that gives apps ADB access with optional root, plus a compatibility companion for Shizuku-only apps `Apache-2.0`
* [shevery](https://github.com/HmnDev-Tech/shevery) ✨ - Material 3 fork with autostart, TCP mode, Dhizuku, module support and a built-in terminal with AI integration
* [Shizako](https://github.com/xm1437/Shizako) - A catgirl-mascot edition of Shizuku, a drop-in replacement manager that official Shizuku-API apps connect to without modification (with similar features like shevery) `Apache-2.0`
* [Shizuku (thedjchi's fork)](https://github.com/thedjchi/Shizuku) - Fork of Shizuku with autostart, TCP mode and stealth mode (maintenance currently paused) `Apache-2.0`
* [ShizukuPlus](https://github.com/thejaustin/ShizukuPlus) - Shizuku fork with an extended API surface for developers, autostart, TCP mode, Dhizuku and more `Apache-2.0`
* [Stellar](https://github.com/roro2239/Stellar/blob/main/README_en.md) - Another Shizuku implementation with autostart, TCP mode and a simple terminal (can run commands automatically on startup) `MPL-2.0`

### AI agents

* [Aether](https://github.com/Zhou-Shilin/Aether) - Localized, extensible general-purpose AI agent for Android, iOS and macOS, with optional Shizuku and Termux integration for direct device control. `GPL-3.0`
* [AndroidHarness](https://github.com/Sanuu7/AndroidHarness) - On-device coding agent that routes privileged commands through a Shizuku shell UID, with a Termux-prefixed Linux toolchain as fallback. `MIT`
* [ClawGUI](https://github.com/ZJU-REAL/ClawGUI) - On-device GUI-agent runner deploying the full ClawGUI brain stack on one phone controlled via Shizuku. `Apache-2.0`
* [Hermes Agent](https://github.com/adybag14-cyber/hermes-agent) - Hermes Agent port for Android with a Shizuku privileged shell bridge for on-device actions. `MIT`
* [OmniBot](https://github.com/omnimind-ai/OmniBot) - On-device AI agent with terminal, web browsing, device control, and system integration `GPL-3.0`
* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - Automates actions on your device using the AutoGLM vision language model `GPL-3.0`
* [OpenCyvis](https://github.com/opencyvis/opencyvis-phone) - Open-source AI phone that sees your screen and operates apps from natural language tasks, works in the background `Apache-2.0`
* [OpenDroid](https://github.com/yashab-cyber/opendroid) - Open-source autonomous on-device AI agent that plans and executes multi-step tasks via screen automation `Apache-2.0`
* [OpenMinis](https://github.com/OpenMinis/OpenMinis) - AI-powered agent with Linux shell, browser automation, and system control via Shizuku `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - The most powerful AI agent and AI chat software on Android. Can run commands using Shizuku `LGPL-3.0`
* [rish-mcp](https://github.com/turin-dev/rish-mcp) - Exposes an Android device's Shizuku shell to AIs as an MCP `run_shell` tool over an outbound WebSocket relay — run shell commands from Claude or any MCP client with no VPN, ADB, or sshd `MIT`
* [roubao](https://github.com/Turbo1123/roubao/blob/main/README_EN.md) - Open-source on-device AI phone automation assistant based on vision-language models that performs tasks via Shizuku system permissions, no PC needed. `MIT` [(源代码)](https://github.com/Turbo1123/roubao)
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - Automation and Multitasking Framework using AutoGLM. Can create virtual screens that agents can run apps on and use multi-window `Apache 2.0`
* [Zafiro](https://github.com/niki914/zafiro) - Bring-your-own-key AI agent that reads the screen and controls the device through Shizuku, without root. `MIT`


### Android Auto

* [Flywheel](https://github.com/Benjamin-Wiegand/Flywheel) - Free and open source alternative to Android Auto aimed at de-googled phones, compatible with existing headunits; Shizuku is used for app embedding and call-audio capture. `GPL-3.0`

### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - An F-Droid client designed for Android TVs `GPL-3.0` [(源代码)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer designed for Android TVs `GPL-3.0` [(源代码)](https://github.com/mlm-games/fluffy)
* [RecentAppsTV](https://github.com/Qutaiba-Khader/RecentAppsTV) - Recent Apps overlay for Android TV `Propietary`

### Audio

* [allEQ](https://github.com/omixin/allEQ) - Rootless 10-band system equalizer that hooks the output mix audio session through Shizuku. `GPL-3.0`
* [android-realtime-voice-isolation](https://github.com/sk2andy/android-realtime-voice-isolation) - On-device real-time voice isolation using Shizuku, GTCRN, and ONNX Runtime `MIT`
* [Castix](https://github.com/elhizazi1/Castix) - Manages background playback restrictions and adds an AMOLED black-screen clock, with Shizuku, Dhizuku, root, LSPosed or accessibility backends. `GPL-3.0`
* [MicUp](https://github.com/papergray/MicUp) ✨ - Real-time microphone audio processing for Android `MIT`
* [Mixer (1)](https://github.com/farizanjum/mixer-1) - Per-app volume overlay intercepting hardware keys `Proprietary`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - 针对非 root Android 设备的系统级 JamesDSP 音频处理引擎的实现 `GPL-3.0` [(源代码)](https://github.com/timschneeb/RootlessJamesDSP)
* [Spotify Ad Skipper](https://github.com/sihooney/spotify-ad-skipper) - Watches Spotify notifications and auto-skips ads by restarting playback, using Shizuku to relaunch from background. `Proprietary`
* [Volume++](https://github.com/noel-digital-fan/volume_plus_plus) - Custom volume panel with per-app audio mixing via Shizuku or root `MIT`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - Control each app's volume independently `GPL-2.0`
* [wecho](https://github.com/qumolangmo/wecho) - An Android application for global audio effects processing `GPL-3.0`

### Automation

* [Argus](https://github.com/JackRushante/argus) - Tasker-class Android automation where an LLM compiles natural-language rules into a deterministic engine, with an optional Shizuku shell gateway. `GPL-3.0`
* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - JavaScript-based automation tool `MPL-2.0`
* [AutoSlide](https://github.com/tianxing-ovo/AutoSlide/blob/master/README.en.md) - Auto-slide tool that auto-plays short videos and flips reading pages, with floating controls `Apache-2.0` [(源代码)](https://github.com/tianxing-ovo/AutoSlide)
* [flowpilot](https://github.com/emi-ran/flowpilot) - Privacy-first offline automation engine running privileged system actions such as mobile data, airplane mode and dark theme through Shizuku. `GPL-3.0`
* [IMD](https://github.com/soul-99/SU_IMD) - Fork of Geto that hides developer options, ADB, accessibility services and Shizuku itself for restrictive apps like banking, then restores them `GPL-3.0`
* [NexaFlow](https://github.com/Alaa91H/NexaFlow) - Context-aware Android automation engine combining triggers, constraints and actions, with Shizuku execution for privileged device controls. `MIT`
* [Nothing_Modes](https://github.com/Dvorinka/Nothing_Modes) - Automation app for Nothing phones (modes, routines, Glyph) that also runs on other Android devices with optional Shizuku `GPL-3.0`
* [OpenTasker](https://github.com/SysAdminDoc/OpenTasker) - Local-first, open-source Tasker alternative with readable rules and honest permission gates; privileged actions run through a Shizuku AIDL user service. `MIT`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可针对特定生活环境自动或一键配置设备 `Apache-2.0`
* [Service-Keeper](https://github.com/shaunkleyn/Service-Keeper) - Watches background, accessibility and notification-listener services and auto-restarts ones the system kills. `GPL-3.0`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Helper app for Tasker `Propietary`
* [vFlow](https://github.com/ChaoMixian/vFlow/blob/master/README_EN.md) - Visual automation tool that combines tapping, recognition, branching, and system actions into approachable workflows `GPL-2.0`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord modding tool `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - A simple app for automatically launching Bluesky links in your preferred Bluesky client `MIT` [(源代码)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CallVault](https://github.com/madkongo/CallVault) - Non-root call recorder with on-device transcripts/summaries; self-contained over embedded ADB or via an optional Shizuku backend. `GPL-3.0`
* [cally](https://github.com/LyoSU/cally) - Call recorder for stock Pixel 6+ devices that captures both call directions via a Shizuku shell-UID audio service, without root or unlocked bootloader. `GPL-3.0`
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - Send and receive files over Bluetooth `MIT` [(源代码)](https://github.com/kmod-midori/CatShare)
* [ClipShare](https://clipshare.coclyun.top/) - Cross-platform clipboard sync for text, images, files and SMS; Shizuku keeps the Android clipboard listener running. `GPL-3.0` [(源代码)](https://github.com/aa2013/ClipShare/blob/master/README_EN.md)
* [GhostMode](https://github.com/Foxlape/GhostMode) - Makes the phone appear unavailable for incoming calls while keeping LTE/5G data active `Apache-2.0`
* [KDE Connect (Shizuku)](https://github.com/Batestinha/kdeconnect-android-shizuku) - KDE Connect build with Shizuku-powered automatic bidirectional clipboard sync between Android and PC. (Fork of KDE Connect with restored clipboard-send support via Shizuku.) `GPL-2.0`
* [KettuManager](https://github.com/C0C0B01/KettuManager) - Discord modding tool. Continuation of the abandoned BunnyManager project `OSL-3.0`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 这是一款简单的应用程序，可在您喜欢的 Lemmy 客户端中自动启动 lemmy 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 这是一个简单的应用程序，可在您喜欢的 Mastodon 客户端中自动启动 fediverse 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord modding tool. Another continuation of the abandoned Bunny-Manager project `OSL-3.0`
* [RivoPhoneApp](https://github.com/user-grinch/RivoPhoneApp) - Material 3 dialer and contacts app with Shizuku-powered call recording without root `GPL-3.0`
* [ShizuCallRecorder](https://github.com/kitsumed/ShizuCallRecorder) ✨ - ShizuCallRecorder empowers ADB through Shizuku to record phone calls on non-rooted device! `GPL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 让您通过短信浏览网页的应用程序 `GPL-3.0`

### Customization

* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - Smart dark mode based on ambient light `GPL-3.0` [(源代码)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 将 Now Playing 从 Pixels 移植到其他 Android 设备 `GPL-3.0`
* [android-perapp-language-selector](https://github.com/TakeruF/android-perapp-language-selector) - Force per-app language settings on Android 13+ without root, even for apps without built-in language options `Apache-2.0`
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - 使用指定应用程序时自动切换免打扰的简单工具 `AGPL-3.0` [(源代码)](https://github.com/im030/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - Manage automatic rotation of different screens on Android phones `GPL-3.0`
* [Capsulyric](https://github.com/FrancoGiudans/Capsulyric) - Displays now-playing lyrics on the status bar and lock screen via Android Live Update and Xiaomi Super Island `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一个非常简单的应用程序，用于更改未 root 的 Android 设备上的运营商名称 `GPL-3.0`
* [cebian](https://github.com/qpst4/cebian) - All-in-one gesture and one-hand navigation suite with edge panels, floating cursor, offline OCR ball, app freezer and freeform windows via Shizuku. `AGPL-3.0`
* [CleanBar](https://github.com/sachinmandawi/CleanBar) - 1-tap status bar and system icon hider to hide clock, battery, and icons, no root required `MIT`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - 修改设备 Material You 颜色的应用程序 `GPL-3.0`
* [Commander](https://github.com/astroboii47/Commander) - Keyboard-first command bar and notification hub; uses Shizuku for recent-app switching and privileged shell controls. `MIT`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - Customize animation speeds on a more fine-grained level `GPL-3.0` [(源代码)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ-Reborn](https://github.com/Arora-Sir/DarQ-Reborn) - Per-app selectable force dark option for Android 10 and above `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - Some Android app widgets and live wallpapers `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - Highly customizable, gestures based Android launcher focused on speed and efficiency `GPL-3.0` [(源代码)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - Tiling window manager, Samsung DEX replacement, popup app launcher `Proprietary`
* [DuoFold-Android](https://github.com/jcx396905-gif/DuoFold-Android) - System-wide iPhone Duo-style fold illusion that reprojects the whole screen from device motion with OpenGL ES, powered by Shizuku. `MIT`
* [essentials](https://github.com/sameerasw/essentials) ✨ - Essential tools, mods and workarounds for Pixels. Also compatible with other devices `MIT`
* [expressive-cutout](https://github.com/EvanKoe/expressive-cutout) - Offline Dynamic Island following Material Expressive design with notifications, live tiles, and Material You colors `GPL-3.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - 在智能手机的 Android 操作系统上添加类似桌面的多窗口支持。 `GPL-3.0`
* [FreeformShell](https://github.com/bravoyush/FreeformShell) - Experimental freeform window-manager helper adding title bars, resize borders and display scaling through Shizuku system APIs. `Apache-2.0`
* [gama](https://github.com/palincat/gama) - Can switch between OpenGL and Vulkan renderers by setting the `debug.hwui.renderer` system property `MIT`
* [HyperBridge](https://github.com/D4vidDf/HyperBridge) - Brings the native HyperIsland experience to HyperOS by bridging notifications into the camera cutout UI with themes and widgets `Apache-2.0`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - Launcher for dual-screen gaming devices. Uses Shizuku to map on of the touch screens to controller inputs `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允许用户选择单独的应用语言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - 使用 Material3 恢复 Android <12 Url-App 链接选择器 `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - Display widgets on the lockscreen. Shizuku is only required on Android 13 and later `MIT` [(源代码)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始设备制造商（小米）不允许您在设备的本地设置中添加额外的（或 "不支持的"）语言，那么这款简单的应用程序就能帮您实现这一功能。 `MIT`
* [O.status](https://github.com/CATCHINGL/O.status) - Minimal status-bar indicator for Wi-Fi, cellular and battery that uses optional Shizuku integration to match system icon colors. `Proprietary`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - A keyboard-first Android command palette that unifies app/device search, and system utilities into an overlay `GPL-3.0`
* [Renoir](https://github.com/exaclast/renoir) - Material You theme designer that applies custom overlays through a Shizuku shell command. `Proprietary`
* [SetEditPlus](https://github.com/kerneldroid/SetEditPlus) - Editor for Android System/Secure/Global settings tables with Shizuku/Root modes, change tracking and boot persistence. `Proprietary`
* [sharemove](https://github.com/thejaustin/sharemove) - Hides apps from Android's share, 'Open with' and APK-installer chooser sheets by suspending or disabling components via Shizuku or root. `GPL-3.0`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - Create launcher shortcuts for shell commands `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易于使用的工具，超越Android系统允许的控制级别 `GPL-3.0`
* [Smart Dock](https://f-droid.org/packages/cu.axel.smartdock/) - Transform your phone into a desktop environment with taskbar, recent apps, and start menu `GPL-3.0` [(源代码)](https://github.com/axel358/smartdock)
* [Smart Edge](https://f-droid.org/en/packages/com.imi.smartedge.sidebar.panel/) - A highly customizable Android side panel inspired by OriginOS `MIT` [(源代码)](https://github.com/Imtiaz-Official/Smart-Edge)
* [Smart Island](https://github.com/agupta07505/SmartIsland) - A lightweight Android overlay that turns notifications, calls, and media playback into a floating glanceable island `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 插件 `GPL-3.0`
* [SuperShade](https://github.com/thejaustin/SuperShade) - Notification shade replacement that drives brightness, status bar expansion and power actions through Shizuku shell commands. `Proprietary`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 查看和修改 Android 设备上的隐藏设置 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - 将设备背面的双击功能从 Android 12 移植到任何 Android 7.0+ 设备 `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - Clean up tracking from sharing links. Supports custom URL rewrite rules `GPL-3.0` [(源代码)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用开始菜单访问应用程序可以解锁其他功能 `Apache-2.0` [(源代码)](https://github.com/farmerbb/Taskbar)
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU and battery widgets `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - A full desktop experience layer for Android `GPL-3.0`
* [YoukiShell](https://github.com/mrYouki/YoukiShell-Android-Desktop) - Plugin-driven Android shell with a taskbar, floating windows and a built-in plugin store; some features need Root or Shizuku `GPL-3.0`

### Development utilities

* [80bee-app](https://github.com/Endda/80bee-app) - Root-free on-device ADB/Fastboot toolbox: boot modes, DPI, DNS, debloater and sideload bypass via Shizuku, plus USB-OTG host mode. `Apache-2.0`
* [ActivityLauncherShizukuPlugin](https://github.com/ActivityLauncher/ActivityLauncherShizukuPlugin) - A Shizuku-based plugin for [Activity Launcher](https://github.com/butzist/ActivityLauncher) that allows launching private (non-exported) activities. `GPL-3.0`
* [ActivityManager](https://github.com/sdex/ActivityManager) - Launch hidden and unexported activities directly without root `Apache-2.0`
* [ADB Captain](https://github.com/eatenlamp/adbcaptain) - ADB toolkit that runs shell commands, app management and log access through Shizuku, with no root required. `AGPL-3.0`
* [Android Code Studio](https://github.com/AndroidCSOfficial/android-code-studio) - On-device IDE for building Gradle-based Android projects; Shizuku enables silent installation of the built APK. `GPL-3.0`
* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 删除已为用户注册账户的应用程序的软件包名称. `Proprietary`
* [Cosmic-IDE](https://github.com/aload0/Cosmic-IDE) - IDE for JVM development. Uses Shizuku for an embedded shell - 用于 JVM 开发的 IDE。使用 Shizuku 作为嵌入式 shell `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - Backup/restore private app data of debuggable apps using Shizuku `GPL-3.0`
* [DEVTools](https://github.com/MetxStudio/DEVTools) - All-in-one Android dev toolkit: terminals, sensor monitor, app/file managers plus a Shizuku shell helper. `MIT`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一个简单的应用程序，旨在帮助用户通过 DSU 的 Android 功能轻松安装 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修复了 HostProfile 应用程序和 WorkProfile/DualApp/MultiApp 之间的 MediaStore 和文件 IO 兼容性问题。 `Proprietary`
* [FPS-Meter-Android](https://github.com/rdevz-ph/FPS-Meter-Android) - High-performance lightweight FPS monitoring overlay inspired by Samsung Perf Z for gaming and performance testing `MIT`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - FPS viewer overlay with graph `Proprietary`
* [FrameX-Android](https://github.com/MaheshSharan/FrameX-Android) - Real-time performance overlay for Android `MIT`
* [get_event](https://github.com/lalakii/get_event) - 读取/dev/input/event* `Proprietary`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用于查看设备上的应用程序中使用的库的应用程序。使用 Shizuku 确定其他应用程序的安装源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - 另一个适用于 Android 的 logcat 阅读器 `GPL-3.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - Utilizes Shizuku to call AppOps APIs for fine-grained app permission control `MIT`
* [panda-ide](https://github.com/ferelking242/panda-ide) - Mobile-first Flutter IDE with code editor, PTY terminal, Git and VS Code extensions; a Shizuku bridge provides ADB-level shell for on-device flutter run. `MIT`
* [roamer](https://github.com/eigenlux-ai/roamer) - Developer tool overriding SIM country ISO and carrier name via Shizuku, with optional per-app locale syncing. `MIT`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root. `GPL-3.0` [(源代码)](https://github.com/zacharee/RootActivityLauncher)
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - 用于切换无线调试的小部件和快速设置图块（与 KDE Con​​nect 集成） `GPL-3.0`

### Device owner (DPM)

* [Déchaîner](https://github.com/warleysr/dechainer) - Blocks adult content as Device Owner; Shizuku runs the dpm set-device-owner setup command. `Apache-2.0`
* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 启发的应用程序，允许将 DeviceOwner 权限共享给第三方应用程序 `GPL-3.0`
* [harbor](https://f-droid.org/packages/com.monstera.harbor/) - Work-profile manager with optional Shizuku tools for automation `Apache-2.0` [(源代码)](https://github.com/Stem0794/harbor)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用设备所有者权限管理您的设备 `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - Fork of OwnDroid with added features `GPL-3.0`

### Display management
* [Adaptive-Hz](https://github.com/mahmutaunal/Adaptive-Hz) - Automatically switches display refresh rate between 60Hz and 120Hz based on user interaction. Designed for Samsung devices without true adaptive refresh `MIT`
* [akiHz](https://github.com/anlaki-py/akihz) - Lightweight refresh rate switcher with Quick Settings tile, automatic rate detection, and floating FPS monitor `MIT`
* [android-display-extend](https://github.com/jqssun/android-display-extend) ✨ - Display manager for physical and virtual displays with a built-in virtual touchscreen. Great for use with `scrcpy --new-display` on a PC `GPL-3.0`
* [android-display-mirror](https://github.com/jqssun/android-display-mirror) ✨ - Screen mirroring hub with support for sharing screen content over AirPlay, Moonlight/Sunshine, and DisplayLink `GPL-3.0`
* [Castla](https://github.com/Suprhimp/castla) - Creates a virtual display, runs apps on it, and streams screen, touch, and audio into a remote browser over local Wi-Fi `Apache-2.0`
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - Turns your phone into a touchpad and keyboard for a single app running on a wired external display `GPL-3.0`
* [Dextop](https://github.com/NarYuki/Dextop) - Desktop environment using Samsung DeX or Shizuku with multitasking and custom resolution `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可折叠设备上的各种显示屏折叠状态之间切换 `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - Keep your phone mostly monochrome, but allow apps like camera to be in color `GPL-3.0`
* [magicdesk](https://github.com/mekhontsev/magicdesk) - Open-source Android 15+ workstation with native windows, external displays, desktops and Termux integration via Shizuku `GPL-3.0`
* [PortalPad](https://github.com/Smart-Home-User/PortalPad) - Turns your phone into a trackpad, air mouse, and remote for external displays like AR glasses, monitors, and TVs `MIT`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - 为 Android 设备提供更好的屏幕镜像 `Apache-2.0` [(源代码)](https://github.com/farmerbb/SecondScreen)
* [Tideo Auto Brightness](https://github.com/faded-penguin021/Tideo-Auto-Brightness) - Glass-box adaptive-brightness replacement with explainable decisions and circadian support. `MIT`

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork 具有动画支持和使用 Shizuku 的插件管理。 `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - Export videos downloaded from the Android version of Bilibili `GPL-3.0` [(源代码)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - Merge and export BiliBili cache files into MP4, supports mobile and computer client `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 进行插件管理的漫画阅读器。立读的独立继承者。 `Apache-2.0`
  * Mihon/Tachiyomi 还有其他几个活跃的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [Buge-Files](https://bugestudio.website/files/) - Material 3 Expressive file manager that installs APKs through Shizuku in addition to storage browsing and management. `GPL-3.0` [(源代码)](https://github.com/BugeStudioTeam/Buge-Files)
* [Butler](https://github.com/d4rken-org/butler) `IAP` 💰 - Fast, private file explorer for power users with tabs, trash bin, regex search, app manager, and root/Shizuku support `GPL-3.0`
* [FileExplorer](https://github.com/SysAdminDoc/FileExplorer) - File manager for local, root, archives, network shares, cloud, vaults and storage analysis `MIT`
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer designed for Android TVs `GPL-3.0` [(源代码)](https://github.com/mlm-games/fluffy)
* [immich-cloud-media](https://github.com/Dreaming-Codes/immich-cloud-media) - Cloud media provider that surfaces a self-hosted Immich library in Android's system photo picker, configured via Shizuku or ADB. `GPL-3.0`
* [MaterialFiles](https://github.com/zhanghai/MaterialFiles) - Material Design file manager for Android `GPL-3.0`
* [NFile](https://github.com/Senzme/NFile) - File manager with Android folder access using Shizuku `GPL-3.0`
* [plain-app](https://github.com/plainhub/plain-app) - Self-hosted web dashboard to manage files, media, contacts, SMS and calls from a browser, with Shizuku for privileged SMS deletion. `AGPL-3.0`
* [RippleFiles](https://github.com/GokulSB/RippleFiles-FileManager) - Expressive Material file manager with local and cloud storage plus Shizuku-gated Android/data access. `MIT`
* [ROSE](https://github.com/NarayanChetri/ROSE) - Modern file manager with Material 3 UI, archive support, recycle bin and Shizuku access to Android/data and Android/obb without root. `GPL-3.0`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE是Android最彻底的清理工具 `GPL-3.0` [(源代码)](https://github.com/d4rken-org/sdmaid-se)
* [sync-to-android-data](https://github.com/kamren-zirger/sync-to-android-data) - Syncs files in and out of restricted Android/data folders when target apps open or close `MIT`
* [twig](https://github.com/dev2ex/twig) - Size-first dual-pane file manager (~7MB) for local, archives, FTP/SFTP/SMB/WebDAV/S3/restic/Jellyfin `GPL-3.0`
* [UnscopeMyData](https://github.com/kepatotorica/UnscopeMyData) - Moves app data in and out of scoped storage folders using Shizuku for elevated file access. `GPL-3.0`
* [XArchiver](https://github.com/Xtra-Manager-Software/XArchiver) - File manager with built-in archive support `MIT`
* [XClean](https://github.com/utopiafar/XClean) - Rule-based cleaner with Normal, Shizuku and Root engines for clearing app junk. `Proprietary`
* [XFiles](https://github.com/Local1stDotApp/XFiles) - Offline file manager with root and Shizuku support for full filesystem access `GPL-3.0`
* [ZenFile](https://github.com/l930203811/ZenFile) - NFile fork with built-in remote file server support `GPL-3.0`
* [ZhuFiler](https://github.com/Artzhu86/ZhuFiler) - Open-source Material You file manager with archive, editor, media playback, APK handling and Shizuku-backed privileged access. `MIT`

> [!NOTE]
> [点击此处查看更多文件管理器（闭源）](pages/CLOSED_SOURCE_cn.md#file-management)

### Games

* [Ascent](https://github.com/4o3F/Ascent) - A tool for retrieving gacha history links from Mihoyo games  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - Browndust II Mod manager `Proprietary`
* [Cinderbox-Companion](https://github.com/ObfuscatedVoid/Cinderbox-Companion) - Companion app for Stardew Valley on Android with Steam Cloud save sync, game file download, and SMAPI mod management `MIT`
* [CloudSync-Mobile](https://github.com/StardewValleyMods/CloudSync-Mobile) - An app that allows you to sync your Stardew Valley saves across multiple devices `GPL-3.0`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - 管理“洛杉矶犯罪”游戏的地图、壁纸和屏幕截图 `GPL-3.0`
* [linkura-localify](https://github.com/ChocoLZS/linkura-localify) - Localization plugin for Link! Like! LoveLive! that translates game text via LLM `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 游戏“Last Origin”的 Mod 管理器 `Proprietary`
* [MAA-Meow](https://github.com/Aliothmoon/MAA-Meow/blob/main/README_EN.md) - Run MAA natively on Android for one-click Arknights daily tasks with foreground and background modes `AGPL-3.0`
* [mt-en-applier](https://github.com/Aikiooo/mt-en-applier) - One-tap installer for the unofficial English patch of the Mushoku Tensei mobile game, copying files via Shizuku with no root or PC. `Proprietary`
* [Nibnya](https://github.com/yinghuajimew/Nibnya) - An Android NBT editor for Minecraft Bedrock, powered by Shizuku for /data access `AGPL-3.0`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - Companion app for localizing the Android version of CHAOS;CHILD visual novel `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 轻松导入和共享 Polyfield 地图 `GPL-3.0`
* [pogoplusle](https://github.com/Mygod/pogoplusle) - Skip the pairing dialog when connecting a Pokémon GO Plus `Apache-2.0`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - Genshin Impact Auto-Conversation Clicker `MIT`
* [stalker](https://github.com/onerdna/stalker) - Save data viewer & editor for Shadow Fight 2 `GPL-3.0`
* [SwiftSense](https://github.com/itsmelissadev/SwiftSense) - Gaming tuner that uses Shizuku to freeze background apps, disable packages and raise sensor sampling rates. `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order游戏翻译项目 `MIT`

### Input methods

* [8bitdo-xbox-bridge](https://github.com/BoredNewCoder/8bitdo-xbox-bridge) - Makes the 8BitDo Ultimate Wired Controller for Xbox work as a real system-wide gamepad on Android TV via the reverse-engineered GIP protocol and Shizuku uinput injection. `MIT`
* [BiBi Keyboard](https://github.com/BryceWG/BiBi-Keyboard/blob/main/README_EN.md) - AI-powered voice input method keyboard; Shizuku or root keeps its floating-ball and volume-key background service alive. `Apache-2.0`
* [ButtonSilencer](https://github.com/EithonX/ButtonSilencer) - Blocks faulty headset and IEM remote buttons without disabling the phone's own buttons; Shizuku provides the privileged path for screen-off headset input protection. `MIT`
* [C9](https://github.com/austinauyeung/C9) - Efficient grid-based cursor provided alongside a traditional cursor. Shizuku is only required on Android 11. `Apache-2.0`
* [GameShift](https://github.com/tientien17/GameShift) - Auto-switches the default home launcher when a game controller connects and restores it on disconnect, using Shizuku without root. `Apache-2.0`
* [Joycon2Android](https://github.com/JoeGeC/joycon2android) - Connects Nintendo Switch 2 Joy-Con controllers over BLE and exposes them as system-wide virtual gamepads via a Shizuku UHID relay. `GPL-3.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - 一款 Android 应用程序，可改变您设备上按钮的功能！ `GPL-3.0` [(源代码)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - Play games using mouse and keyboard on Android device; keymapper for games `Apache-2.0`
* [OpenMapper](https://github.com/kinou-p/android-open-mapper) - Free open-source gamepad keymapper using Shizuku for touch injection with sub-millisecond latency; alternative to Mantis and Panda. `PolyForm-Noncommercial-1.0.0`
* [pastiera](https://github.com/palsoftware/pastiera) - Android keyboard specialized for Physical Keyboard Devices. Uses Shizuku for trackpad gestures `GPL-3.0`
* [Steam Controller for Android](https://github.com/SonicDX12/SteamController-Android) - Uses the Steam Controller 2026 as a real Android gamepad via Shizuku-backed Linux uinput; USB, dongle or BLE. `MIT`
* [TitanPad](https://github.com/sztupy/TitanPad) - Converts the Titan2's Physical Keyboard's capacitive input into mouse and scroll gestures. Uses Shizuku for reading the trackpad input and setting up virtual HID devices `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 适用于 Android x86 的键盘映射器 `GPL-3.0`


### Installer & app stores

* [APKUpdater](https://github.com/DmitryN71/apkupdater) - APKUpdater fork adding Shizuku-based silent installs next to its APKMirror, Aptoide, F-Droid and IzzyOnDroid sources. `GPL-3.0`
* [AuroraDroid](https://f-droid.org/packages/com.aurora.adroid/) - FOSS F-Droid client with silent installs via Shizuku/root and automatic updates `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/auroradroid)
* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - Google Play 商店的开源替代品，具有隐私性和现代设计 `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - 轻松下载、安装和共享模组 `Proprietary`
* [Discoverium](https://github.com/cygnusx-1-org/Discoverium) - Obtainium fork for discovering and installing apps from source, with Shizuku, Dhizuku and Sui install backends. `GPL-3.0`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：隐私友好浏览器的更新程序 `GPL-3.0` [(源代码)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F‑Droid Client `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - App store for GitHub releases with discovery function `Apache-2.0` [(源代码)](https://github.com/kurikomi-labs/komi-store)
* [instafel](https://github.com/mamiiblt/instafel) - Updater app for Instafel, an Instagram mod `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - 现代且实用的 Android 应用安装程序替代品 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 简单的应用程序使用 Shizuku 在设备上安装带有高级选项的 APK `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 存储库的非官方客户端 `GPL-3.0`
* [KingInstaller](https://github.com/fcaronte/KingInstaller) - APK installer that spoofs the Play Store installer identity to bypass app-visibility restrictions, installing via intents, Shizuku or root `GPL-3.0`
* [LocalAndroidStore](https://github.com/SysAdminDoc/LocalAndroidStore) - Private app catalog that installs signed GitHub and F-Droid releases, optionally through a Shizuku-owned install session. `MIT`
* [multistore](https://github.com/FedeFluork/multistore) - Aggregates third-party app stores into one catalogue to search, compare, download, and update APKs `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - An F-Droid client with modern UI and an arsenal of extra features `GPL-3.0` [(源代码)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接从源获取 Android 应用程序更新 `GPL-3.0`
  * [ObtainX](https://f-droid.org/packages/dev.bikram.obtainx/) - Obtainium fork with Material 3 UI redesign `GPL-3.0` [(源代码)](https://github.com/bikram-agarwal/ObtainX)
* [Omnify](https://github.com/Victor-root/Omnify) - F-Droid client fork that also installs apps from external sources, with a Shizuku installer and a Works with Shizuku discovery row. `GPL-3.0`
* [OpenLoader](https://github.com/thebytearray/OpenLoader) - APK installer built for the Android developer verification era, using Shizuku for the privileged install path. `GPL-3.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - App store for modded apps `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允许覆盖包请求者和执行者的包安装程序 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 拆分 APK 安装程序 `GPL-3.0` [(源代码)](https://github.com/Aefyr/SAI)
* [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch) - Shizuku-powered app manager with silent installs, updates, and batch operations `GPL-3.0`
* [ShizuStore](https://github.com/timschneeb/ShizuStore) ✨ - App store for Shizuku apps. Based on this awesome-shizuku list and installs APKs straight from their upstream sources `GPL-3.0`
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - A lightweight app installer replacement with split APK support `Apache-2.0`
* [universal-installer](https://github.com/pass-with-high-score/universal-installer) - Install and manage APK packages with split APK support, silent install via Shizuku, and VirusTotal malware scanning `GPL-3.0`
* [Vyxel Apps](https://github.com/NikhilKain/vyxel-apps) `IAP` 💰 - GitHub-backed app store with signature verification and silent installs through Shizuku. `AGPL-3.0`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - GUI for Android's builtin `dex2oat` utility, allowing DEX code of installed apps to be re-optimized `Apache-2.0`
* [CaptureCap](https://github.com/yepgoryo/CaptureCap) - Screen and audio recording and streaming app, no root required `MIT`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - Find the reason why the alarm icon is active in the status bar `Proprietary`
* [IrisShot](https://github.com/raging-flames/IrisShot) - Scrolling-screenshot tool for Android games that auto-scrolls and stitches long captures using MediaProjection or Shizuku-powered shell capture. `Proprietary`
* [kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) - Home Assistant kiosk: voice satellite, synchronized music and photo screensaver, with Shizuku used for privileged APK updates and device bridging. `Proprietary`
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [Mafza](https://github.com/yshalsager/Mafza) - Emergency actions runner with one configurable profile, external emergency triggers, and a safe Dry Run mode `Proprietary`
* [NekokoLPA2](https://github.com/iebb/NekokoLPA2) - Cross-platform eSIM/eUICC manager; on Android it asks Shizuku to open the shell-only QRTR socket for Telephony/TMAPI profile operations `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - Android utility to make notifications persistent/undismissable using Shizuku `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - Automatically close selected apps when you exit them to save power and memory `Apache-2.0`
* [overlay-translator](https://github.com/ciddwd/overlay-translator) - Real-time on-screen translator for games, visual novels, and manga with on-device/cloud OCR and floating overlay `Apache-2.0`
* [PhoneDiagnosticTool](https://github.com/ScoobyDouche/PhoneDiagnosticTool) - On-device phone diagnostics for CPU, GPU, battery, RAM, storage, sensors and display, with optional Shizuku/root elevated readings. `MIT`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - Exploits CVE-2024-31317 for Zygote injection, integrating remote terminal and file transfer capabilities `MIT`
* [Rainy Screenshot](https://github.com/CATMIAOZHI/RainyScreenShot/blob/main/README_EN.md) - Silent screenshots and screen recording through a Shizuku or Porter privileged shell instead of MediaProjection. `Proprietary`
* [Screen Recorder](https://github.com/muhammadhaseebiqbal-dev/Screen-Recorder) - Screen recorder with internal audio capture routed through Shizuku. `MIT`
* [silent-alarm](https://github.com/izumisagirii/silent-alarm) - Earphone-first alarm clock that keeps alarms alive on aggressive OEM ROMs with a Shizuku or root watchdog that restarts the app. `AGPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一个简单的应用程序，用于通过 WearOS 手表控制 Android 设备 `Apache-2.0` [(源代码)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - Remote control your device via Telegram messages `BSD 3-Clause`
* [VineOS](https://github.com/Hexadecinull/VineOS) - Android VM engine; Shizuku probes shell privileges for the no-root ADB and wireless debugging path. `GPL-3.0`

### Network

* [ADNS](https://github.com/eyalm2000/adns) - DNS-based ad blocker for Android `MIT`
* [Bluetooth Bouncer](https://github.com/harvzor/android-bluetooth-bouncer) - Per-device Bluetooth auto-connect control that stays paired; policy enforced via Shizuku user service. `GPL-3.0`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上读取手机信号塔信息 `MIT` [(源代码)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - App firewall without using an VPN; can also manage packages `MIT`
* [delta](https://github.com/supershadoe/delta) - 使用 Shizuku 的热点管理器 `BSD-3-Clause`
* [Dolphy-App](https://github.com/unvoiddd/Dolphy-App) - NFC, BLE, and IR multi-tool for wireless protocol research `GPL-3.0`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - An app that allows you to turn on your hotspot remotely via Bluetooth - think Apple Continuity, but for everyone `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Google FindMyDevice 服务的安全和开源替代方案 `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - Dual-mode firewall: blocks internet access using Shizuku or a standard local VPN interface or both. `MIT`
* [hikari-adblock](https://github.com/codegeasse1/hikari-adblock) - No-root ad/tracker/malware blocker with local VPN DNS filter plus Shizuku iptables/nftables firewall modes `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 预览和编辑/etc/hosts文件 `MIT`
* [MaybeEdgeScanner](https://github.com/maybeknott/MaybeEdgeScanner) - Route-pairing network scanner probing TCP/TLS/HTTP targets, with optional Shizuku-assisted radio diagnostics. `AGPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一个在 Android 上运行 Naiveproxy 的简单应用程序 `MIT`
* [NetManager](https://github.com/DottoXD/NetManager) - Material cell-network monitor for 4G/5G NR with tower map, drive tests and speed tests; a Shizuku shell bridge unlocks extra network data. `GPL-3.0`
* [NetSwitcher](https://github.com/nd4y/netswitcher) - Fast Wi-Fi, mobile-data and Ethernet switching via app, shortcut, widget or QS tile using Shizuku or root. `Proprietary`
* [NetToggle](https://github.com/Dhangofa/NetToggle) - A lightweight Android Quick Settings tile to force 5G Only, 4G Only and preferred network modes using Root or Shizuku `GPL-3.0`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - 用于 4G/5G 网络模式切换的 Android 应用 `GPL-3.0`
* [nobita](https://github.com/duhow/nobita) - Records Bluetooth HCI traffic into Wireshark-compatible PCAPNG files on-device using Shizuku. `Proprietary`
* [Quintz](https://github.com/corgilittlelegs/Quintz) - Rootless Wi-Fi band locker and BSSID steering tool that pins Android to 5/6 GHz via Shizuku, with AP telemetry and an RF direction finder. `MIT`
* [RKNHardering](https://github.com/xtclovver/RKNHardering) - Detects VPN/proxy circumvention tooling on-device using community-verified checks, with privileged probes via Shizuku or Root. `AGPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - Open-source app firewall that doesn't depend on VPNs or root `GPL-3.0`
* [Shizzi](https://github.com/carlelieser/shizzi) - Rootless Wi-Fi tethering bypass via Shizuku `Proprietary`
* [sing-box](https://f-droid.org/packages/io.nekohasekai.sfa/) - Universal proxy platform. Uses Shizuku for per-app proxying `GPL-3.0` [(源代码)](https://github.com/SagerNet/sing-box)
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - A persistent network speed tracker in your status bar `GPL-3.0` [(源代码)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - WireGuard 和 AmneziaWG 的 FOSS Android 客户端，支持自动隧道功能 `MIT`
* [WiFi Portal](https://github.com/lovitus/wifiportal) - Applies captive-portal probe settings via Shizuku UserService with backup, verify-before-write and regional presets. `Proprietary`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - Simple app using Shizuku to manage & view saved Wi-Fi passwords `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - 在 Android 11 及更高版本上查看您保存的 WiFi 密码，无需 root `Proprietary` [(源代码)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - 从 LSPod 扩展的非根 Xposed 框架 `GPL-3.0`
* [Morphe](https://morphe.software/) - User-friendly YouTube patcher based on Universal-ReVanced-Manager `GPL-3.0` [(源代码)](https://github.com/MorpheApp/morphe-manager)
* [NPatch](https://github.com/7723mod/NPatch) - Rootless LSPosed-based Xposed framework that injects the Xposed API into target APKs `GPL-3.0`
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - ReVanced patcher that has extra features the official manager doesn't have `GPL-3.0`

### Power management

* [Amply](https://github.com/d4rken-org/amply) - Easy control of charging limits. Temporarily allows one full charge, then automatically restores your protective charge limit `GPL-3.0`
* [BatStats](https://github.com/mlm-games/BatStats) - Battery monitor with stats via Shizuku `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - 一个简单的应用程序，可在 Android 14 及更高版本上显示电池状态信息。 `GPL-3.0`
* [Battery](https://github.com/zhyang18/Battery/blob/main/README_EN.md) - Battery health and hardware analysis; Shizuku provides the elevated shell for deep battery parameter reads. `MIT`
* [Battery Mode Checker](https://github.com/mrdarksidetm/Android-Battery-Unrestricted-Checker) - Audit, manage, and toggle Android battery optimization states (Unrestricted, Optimized, Restricted) with Shizuku `Apache-2.0`
* [Battery-Monitor](https://github.com/tswistak/Battery-Monitor) - Track and log battery capacity and parameters over time using Shizuku `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - Open source app to visually change battery data via Shizuku `GPL-3.0`
* [DozeTap](https://github.com/dhruvanbhalara/DozeTap) - Screen timeout presets that grant WRITE_SECURE_SETTINGS in one tap through Shizuku. `Apache-2.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - Enable Doze mode immediately after screen off and turn off motion sensing to get best battery life `GPL-3.0` [(源代码)](https://github.com/Akylas/EnforceDoze)
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - A fire-and-forget program to stop Android apps from running in the background `GPL-3.0` [(源代码)](https://github.com/adil192/no_more_background)
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - Advanced reboot menu with Shizuku support `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 关闭 Android 屏幕而不进入待机/睡眠模式 `Proprietary`
* [sleep-timer](https://github.com/Xitee1/sleep-timer) - Sleep timer that can pause media, and turn off WIFI/Bluetooth/Display `GPL-3.0`
* [USB PD Bypass](https://github.com/ONDER1E/usbpdbs) - Toggles USB PD battery-bypass mode at charge thresholds via Shizuku with self-healing recovery. `Proprietary`
* [volt](https://github.com/lebiggg/volt) - Greenify successor: scored app hibernation with UnifiedPush wake-on-push via Shizuku `GPL-3.0`
* [wakelogs](https://github.com/dernikiausd/wakelogs) - Analyzes display wakeups, CPU activity, alarms and device rest with Shizuku-based system diagnostics. `GPL-3.0`
* [zukulock](https://github.com/tiendnm/zukulock) - Very lightweight app that locks the screen when launched. Helps reduce wear on the power button `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一键隐藏您的私人文件和 Android 应用程序。 `Apache-2.0` [(源代码)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - An application designed to silently protect user data from powerful adversaries `GPL-3.0`
* [anubis](https://github.com/sogonov/anubis) - App manager that freezes/unfreezes app groups based on VPN state via Shizuku pm disable, so frozen apps cannot detect or bypass the VPN. `MIT`
* [AppLock](https://github.com/aload0/AppLock) ✨ - MIUI 12+ 防止应用被侧滑或一键清理杀死 `MIT`
* [AppOpsNext](https://github.com/1zumiii/AppOpsNext) - Android 15+ AppOps manager with permission templates, batch changes, install history and diagnostics via Shizuku `Proprietary`
* [AvarionX-Android-Antivirus](https://github.com/phsycologicalFudge/AvarionX-Android-Antivirus) - On-device antivirus with local malware/APK scanning, download monitoring and DNS filtering; Shizuku powers ransomware-style behaviour monitoring `MPL-2.0`
* [Monica](https://github.com/Monica-Pass/Monica) - Local-first Bitwarden/KeePass password vault with TOTP; Shizuku keeps autofill protection running in the background. `GPL-3.0`
* [Privacify](https://github.com/robinsrk/privacify) - Privacy control center: permission scanner, sensor-usage timeline and privacy score, with Root/Shizuku advanced hardware controls. `Apache-2.0`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - Manage your device privacy based on lock/unlock state `MIT` [(源代码)](https://github.com/dorumrr/privacyflip)

### Productivity

* [Blink](https://github.com/character-flat/Blink) - A persistent, highly customizable 20-20-20 rule eye-care timer that uses Shizuku to whitelist itself from Android's battery optimizations `GPL-3.0`
* [Cresto](https://github.com/Nevodev/Cresto) - To-do app with AI capture, calendar sync and reminders; its Quick Settings current-screen extraction captures the screen through Shizuku shell access. `Apache-2.0`
* [Curbox](https://f-droid.org/packages/neth.iecal.curbox/) ✨ - Tool to reduce screen addiction and view usage analytics `GPL-3.0` [(源代码)](https://github.com/curbox-app/curbox-android)
* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - Digital Detoxing: Use your phone rather than letting your phone use you `GPL-3.0`
* [HyperCopy](https://github.com/1812z/HyperCopy) - Clipboard-to-app jump tool watching copied links and opening them directly in the right app via Shizuku or LSPosed monitoring. `Proprietary`
* [input-leaf](https://github.com/anasvhora284/input-leaf) - Android client for Input Leap/Deskflow: control your phone with your PC mouse and keyboard over LAN using Shizuku input injection, no root. `Apache-2.0`
* [quickdash](https://github.com/Balajitechlabs/quickdash) - Floating productivity dashboard with UPI/PayPal collection and chat shortcuts; a Shizuku bridge unlocks privileged system capabilities. `Proprietary`
* [Sefirah](https://github.com/shrimqy/Sefirah-Android) - Windows-Android integration for clipboard, notification, file, SMS and call sync; Shizuku enables clipboard on Android 10+. `GPL-3.0`

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一个用于切换“息屏显示（Always on Display）”的 Android 快捷设置 `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本上带回独立的 Wi-Fi 和移动数据磁贴，并提供更好的统一网络磁贴 `GPL-3.0` [(源代码)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DataSimTile](https://github.com/Mygod/DataSimTile) - Tile to switch the default mobile data SIM `Apache-2.0`
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - Provides quick settings tile and shortcuts to turn off the display without locking the screen or stopping foreground running apps `MIT` [(源代码)](https://github.com/UlyssesZh/DisplayToggle)
* [DNS Toggle](https://f-droid.org/packages/com.ericlowry.dnstoggle/) - Quick Settings tile for Private DNS toggling and configuration, with optional advanced automation. `MIT` [(源代码)](https://github.com/ELowry/DNSToggle)
* [ManualRotate](https://github.com/Verisonder/ManualRotate) - Quick-settings tile switching portrait/landscape without rotating the phone; optional Shizuku override for apps that lock orientation. `GPL-3.0`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - 用于开启或关闭私有 DNS 设置的快捷磁贴 `GPL-3.0` [(源代码)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 用于切换当前私有 DNS 服务器的快捷设置磁贴 `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - 提供用于切换 USB 调试和切换私有 DNS 主机的快捷磁贴 `GPL-3.0` [(源代码)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 通过快捷设置启用/禁用设备传感器 `Apache-2.0`
* [Tooler](https://github.com/jehan593/tooler) - Quick Settings tiles for lock screen, private DNS, grayscale and charging, executed through Shizuku. `MIT`

### Software management

* [AppControlX](https://github.com/risunCode/AppControl-X) - Freeze, force stop, uninstall apps, change background optimization and more `GPL-3.0`
* [AppDualZuku](https://github.com/nathanatgit/AppDualZuku) - Manages multiple app instances in isolated or shared workspaces (managed profiles) using Shizuku, with an optional root backend. `Proprietary`
* [AppManagerNG](https://github.com/SysAdminDoc/AppManagerNG) - Fork of [AppManager](https://github.com/muntashirakon/appmanager) to inspect, debloat, back up, freeze and control Android apps; works with Shizuku, ADB, Dhizuku or root. `GPL-3.0`
* [Appslim](https://github.com/Horizen5/Appslim/blob/master/docs/README_en.md) - Android runtime analyzer profiling launch behavior, CPU/memory and Dex calls, then slimming apps through hooks, rules and Shizuku or root actions. `Proprietary`
* [AppVaultX](https://github.com/sunilpaulmathew/AppVaultX) - High-performance app manager powered by Shizuku `GPL-3.0`
* [Blocker](https://github.com/lihenggui/blocker) - 启用/禁用 Android 组件，例如活动、服务、接收器和提供者 `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - An app manager focusing on permission management `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - 无需root即可卸载任何应用程序 `LGPL-3.0` [(源代码)](https://github.com/samolego/Canta)
* [CloneCat](https://github.com/AhmetCanArslan/CloneCat) - Clone and manage apps across work profile, private space, dual apps, and secondary users with home screen shortcuts `Proprietary`
* [Dexor](https://github.com/DeveshTone/Dexor) - Ahead-of-time (AOT) bytecode compilation and dexopt runtime manager for Android applications `MIT`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 应用程序可禁用未使用的应用程序，同时仍允许方便地访问它们 `MIT`
* [DroidUtility](https://github.com/DroidUtility/DroidUtility) - Non-root utility suite for debloating, system tweaks and privileged shell execution through Shizuku, aimed at mobile-only developers. `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 通过手动或半自动冻结蹩脚软件来提高设备的速度和电池寿命 `Apache-2.0` [(源代码)](https://github.com/FreezeYou/FreezeYou)
* [Guest-Manager](https://github.com/dlawoals2713/Guest-Manager) - Enables hidden Guest and multi-user modes on devices where the maker disabled them, via Shizuku shell without root. `Proprietary`
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - 冻结、隐藏或禁用任何应用程序。创建并组织可一键冻结的应用程序组。 `GPL-3.0` [(源代码)](https://github.com/aistra0528/Hail)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Island 完整的 FLOSS 分叉 `Apache-2.0` [(源代码)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - 适用于 root 和非 root 设备的 Android 应用程序管理器 `GPL-3.0` [(源代码)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔离和克隆应用程序以保护隐私和并行运行 `Apache-2.0` [(源代码)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [Minimal Kernel Manager](https://github.com/abhay-byte/mkm) - Kernel manager and system monitor with battery stats, apply-on-boot and hidden-app support via Shizuku or root. `GPL-3.0`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - 管理您的 Magisk 模块存储库 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能强大的应用程序，可管理系统和用户应用程序 `GPL-3.0` [(源代码)](https://github.com/SmartPack/PackageManager)
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - App manager with freeze and install capabilities. `GPL-3.0` [(源代码)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 检查 Android 应用程序、Magisk 模块等的更新！ `GPL-3.0` [(源代码)](https://github.com/DUpdateSystem/UpgradeAll)

### Task manager

* [KillMyApps](https://github.com/dedeadend/KillMyApps) - Background process killer to improve battery life and performance via Shizuku or root `GPL-3.0`
* [memhogs](https://github.com/cicerothoma/memhogs-android) - Which apps are eating your phone's memory. Per-app breakdown via Shizuku, helpers grouped under the app that owns them `MIT`
* [MemorySnapshot](https://github.com/RyensX/MemorySnapshot/blob/master/docs/README_EN.md) - On-device Android memory observer: per-app/process PSS tracking, snapshot save and compare, with data gathered via Shizuku or root. `Proprietary`
* [Pensum](https://github.com/troikoss/Pensum) ✨ - Windows-style Task Manager for Android `GPL-3.0`
* [ProcessLens](https://github.com/Dreamucxe/ProcessLens) - Process observatory using Shizuku for ADB-level CPU, memory, thread, wake lock and per-app battery readings. `MIT`
* [ReAppzuku](https://github.com/gree1d/ReAppzuku) - Control and manage background applications. Fork of shappky `GPL-3.0`
* [Recents](https://github.com/tymwitko/Recents) - Launcher-agnostic replacement for the system Recents menu, with app-kill support via Shizuku `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - Monitor running services on your Android device `MIT` [(源代码)](https://github.com/biplobsd/running_services_monitor)
* [RvSystem Monitor](https://github.com/Rve27/RvSystem-Monitor) - High-performance system monitor (Compose + Rust) with Shizuku-fed CPU and hardware insights `GPL-3.0`
* [shappky](https://github.com/YasserNull/shappky) ✨ - A simple app to boost performance by stopping background apps. `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - A Task Manager for Android. Killing processes requires root access. `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 适用于 Shizuku 支持的 Android 设备的本地 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新设计了 aShell 应用程序。 `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - Terminal, SSH, VNC, RDP, SFTP & cloud storage client for Android `AGPL-3.0` [(源代码)](https://github.com/GlassHaven/Haven)

> [!NOTE]
> Using [rish](pages/RISH_cn.md), 您可以使用任何终端模拟器（例如 Termux）创建本地 ADB shell。

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一个用于切换“息屏显示（Always on Display）”的 Android 快捷设置 `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [carrier-ims-for-pixel](https://github.com/ryfineZ/carrier-ims-for-pixel) - Maintained Pixel IMS toolkit: tune VoLTE/VoWiFi/VoNR, 5G display and carrier config via Shizuku `Apache-2.0`
* [hilight-studio](https://github.com/DhananjayBhosale/hilight-studio) - Pixel 11 HiLight LED controller for custom notification and status light effects `MIT`
* [Pixel-IMS-5G](https://github.com/barrylk/Pixel-IMS-5G) - Enable 5G standalone (5G SA) and VoNR on Google Pixel devices `GPL-3.0`
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 通过 LG U+ 在 Pixel 6 和 7 上启用 VoLTE `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - Enable VoLTE for carriers in unsupported regions on Pixel devices `GPL-3.0`
* [Root-My-Pixel](https://github.com/alex193a/Root-My-Pixel) - Root automation for Pixel devices via CVE-2026-43499 exploit `Proprietary`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定制的小部件，可以使用 Shizuku 升级 Pixel 设备上内置的“概览”小部件 `GPL-3.0`
* [TensorIMS](https://github.com/Pixel-Tailor-CN/TensorIMS) - IMS configuration tool for Tensor Pixel devices; Shizuku applies VoLTE, VoWiFi, VT and VoNR toggles. `Apache-2.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - Enhanced IMS Configuration Tool for Google Pixel devices `Apache-2.0`
* [Video Boost AO](https://github.com/AgusRomeroL/video-boost-ao) - Keeps Video Boost enabled on Pixel Pro cameras, re-enabling it every time the camera opens. Shizuku grants WRITE_SECURE_SETTINGS for the on-demand mode `MIT`

#### Samsung OneUI

* [4Zones](https://github.com/mr-biz-apps/4zones) - Restores four-zone window tiling on Samsung DeX and Android desktop mode with tap-to-snap and keyboard shortcuts `Apache-2.0`
* [android-battery-health](https://github.com/willbilec/android-battery-health) - Samsung battery health and cycle-count viewer with screen-reader-friendly layout via Shizuku. `Proprietary`
* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 rootless font installer `GPL-3.0` [(源代码)](https://codeberg.org/dryerlint/fontsmanager)
* [Root-My-Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy) - KSU installer for supported Samsung Galaxy firmware with CVE-2026-43499 `Apache-2.0`
* [pearity](https://github.com/thejaustin/pearity) - Matches Samsung One UI system settings to iOS defaults one toggle at a time (three-state Android/Custom/iOS), writing secure settings via Shizuku or root. `Proprietary`
* [SamsungRegionOverride](https://github.com/Ritel-T/SamsungRegionOverride) - Temporarily change the SIM region seen by Galaxy Store and other region-locked apps, no root, one-tap restore `MIT`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - Enable or disable fast charging mode on Samsung devices when the battery temperature reaches a certain point  `Proprietary`
* [ScamsungFonts](https://github.com/KhunHtetzNaing/ScamsungFonts) - Font manager for Samsung Galaxy (OneUI) via System shell or Root `No license`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - Disable the forced camera shutter sounds on Samsung devices that have their CSC set to certain countries with this restriction `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 权限提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 运行 OneUI 5 的非 root 设备上的系统用户访问 (UID 1000)。使用 Shizuku 实现自动化 `LGPL-2.1`
* [ZFold-Multi-DPI](https://github.com/balamurugan15/ZFold-Multi-DPI) - Applies separate screen zoom and DPI presets for the cover and inner displays of Samsung Galaxy Z Fold devices `Proprietary`

#### MIUI

* [Aura](https://github.com/tgvdufuture/Aura) - Custom RGB notification LED app for POCO X8 Pro with per-app, per-contact, and per-group colors and animations `MIT`
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) `Paid` 💰 - HyperOS/MIUI 5G快捷开关 `GPL-3.0` [(源代码)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本关闭 MIUI 广告 `Apache-2.0`
* [HyperOS FCM Fix](https://github.com/dingwen07/hyperos-fcm-fix) - Keeps Google Play services unrestricted on HyperOS so FCM push notifications arrive on time `GPL-3.0`
* [HyperOS-MTZ-Studio](https://github.com/GloriousApps/HyperOS-MTZ-Studio/blob/main/readme_en.md) - MTZ theme workspace for Xiaomi HyperOS; imports, composes, translates and applies themes, using Shizuku or Shevery for rootless theme application. `Proprietary`
* [HyperOS3ScrollSetter](https://github.com/BlizzardAn225/HyperOS3ScrollSetter) - Restores scrolling wallpapers and disables forced darkening on HyperOS 3/4, applying secure settings and restarts through Shizuku.newProcess or a root module. `GPL-3.0`
* [HyperOSUnfcker](https://github.com/Enki013/hyperosunfcker) - Unlocks hidden performance, display, memory, battery, and visual settings on HyperOS/MIUI devices `LGPL-3.0`
* [IslandRecorder](https://github.com/wxxsfxyzm/IslandRecorder) - Xiaomi-focused screen recorder with Super Island controls `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - One-click configuration for Mix Flip's outer screen: Use any apps and restore system apps to default style `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 节奏游戏中启用 3 键导航  `Proprietary`

#### Other

* [buttonoo](https://github.com/bractstudio/buttonoo) - Remaps the Nothing Essential Key to any press pattern; Shizuku enables the privileged input route. `GPL-3.0`
* [Calibrate-SoC](https://github.com/mayusi/Calibrate-SoC) - SoC tuner, monitor and benchmark suite for Android gaming handhelds with goal-seeking governor and live HUD. `Apache-2.0`
* [Evolve_Launcher_v2](https://github.com/JarJarBlinkz/Evolve_Launcher_v2) - Customizable home launcher for Meta Quest headsets with app organization, playtime tracking and Shizuku-powered clear data/cache actions. `Proprietary`
* [flipx](https://github.com/jlgrimes/flipx) - Routes the home button to different launchers based on Anbernic RG Rotate hinge state `Proprietary`
* [GlyphBarty](https://github.com/Link2011-Act2/GlyphBarty) - Customizable Glyph visualizer for Nothing Phone with music sync, Quick Settings toggle, and charging status display `MIT`
* [Heimdall-AYN-Thor-Assistant](https://github.com/mastercook777/Heimdall-AYN-Thor-Assistant) - Lower-screen game assistant for the AYN Thor with profiles, macros, touch controls, maps and Shizuku-powered touch injection. `Apache-2.0`
* [MindControl](https://github.com/Dinico414/MindControl) - Hardware button remapper and AOD toolkit for the iKKO MindOne that monitors physical keys through Shizuku getevent, with a root fallback. `Proprietary`
* [panel-assistant](https://github.com/panel-assistant/android) - Home Assistant wall-panel dashboard with entity filtering, MQTT device controls and Shizuku/root-powered provisioning and verified installs. `Apache-2.0`
* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control gives precise control over the Nothing Phone (3)'s recording light `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - System-wide shoulder triggers for Nubia Red Magic phones `MIT`
* [Thor SidePad](https://github.com/bentolanh/thor-sidepad) - Turns the AYN Thor bottom screen into a virtual gamepad; Shizuku injects its presses as native controller input. `MIT`
* [thor-wayfinder](https://github.com/Thor-Wayfinder/thor-wayfinder) - Moves apps between the two AYN Thor screens with back-button gestures `CC-BY-NC-ND-4.0`
* [Thors-Lightning](https://github.com/HughesTechNZ/Thors-Lightning) - Controller-driven dual-screen brightness control for the AYN Thor, with optional Shizuku-privileged input recording. `MIT`
* [ThorVolumeLink](https://github.com/pth2000/ThorVolumeLink) - Synchronized volume control for the dual displays of the AYN Thor `MIT`

### Closed-source apps

闭源应用已移至一个单独的子列表中。[您可以在此处查看它们。](pages/CLOSED_SOURCE_cn.md) 


> [!NOTE]
> **为什么闭源应用会被单独列出？**
> Shizuku 会向应用授予高级 ADB 访问权限。出于安全考虑，本主目录仅收录开源及提供源代码的应用，因为任何人都可以检查其代码以确保它们没有进行任何可疑操作，并且可以在自己的机器上自行编译。
>
> 完全闭源的应用需要用户盲目信任，因此它们被单独列出。

### Unlisted apps
为了保持主列表干净，所有不满足特定要求的应用程序都存储在单独的页面上： [ARCHIVED.md](pages/ARCHIVED.md)

> [!NOTE]
> 我还使用自动爬虫来搜索新项目，并在 GitHub 和多个 F-Droid 存储库中使用 Shizuku。您可以在此处查看当前自动生成的爬网报告：[TODO.md](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Porter API](https://github.com/d4rken-org/porter-api) - Android SDK for Porter, a maintained Shizuku fork, offering compatible Shizuku APIs with direct Porter support `MIT`
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的开发人员文档，包括示例 `Apache-2.0`
* [Shizuku-API-Flutter-Plugin](https://github.com/runoob-coder/shizuku-api-flutter-plugin) - 一个用于对接 Shizuku API 的 Flutter 插件。 `MIT`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - Shizuku API bindings for Flutter apps `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android Coroutines-friendly Kotlin-first Package Installer extensions with Shizuku support `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常规文件系统后端的文件操作库 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`


### System

* [droid-mcp](https://github.com/stixez/droid-mcp) - Android SDK giving local LLM/AI apps structured on-device access to phone data, plus shell-level control via Shizuku `Apache-2.0`
* [libterm](https://github.com/niki914/libterm) - Kotlin-first Android terminal session library with User, Root, Shizuku, and SSH backends behind one API `Proprietary`
* [Priv Kit](https://github.com/priv-kit/priv-kit) - Lightweight privileged-runtime library for Root, ADB, or Shizuku-backed Binder access in your own app `Proprietary`

--------------------

## Miscellaneous content

### Command-line utilities

* [AndroSH](https://github.com/ahmed-alnassif/AndroSH) - Professional Multi-Distribution Linux Environments for Android. Run Archlinux, Fedora, Alpine, Debian, Ubuntu, Kali, Void, Manjaro & Chimera with full Android system integration `GPL-3.0`

### Flows for [Automate](https://llamalab.com/automate/)

* [Better Shizuku Starter](https://llamalab.com/automate/community/flows/50863) - Check and automatically start Shizuku **13.6** on key events via wireless debugging with the *free* version of Automate. `MIT`
* [Shizuku Keeper](https://llamalab.com/automate/community/flows/51118) - Continuously run Shizuku **13.6** or **ADB** uninterrupted without root, Wi-Fi, or cables via USB debugging with Automate *Premium.* `MIT`
  * [Shizuku Keeper Lite](https://llamalab.com/automate/community/flows/51012) - Check Shizuku **13.6** at regular intervals and automatically restart it via wireless debugging with the *free* version of Automate. `MIT`
--------------------

## Annotations
- ✨ - 我的个人推荐：深度利用了 Shizuku，或者是独具特色/鲜为人知的宝藏应用。
- `Paid` 💰 - 付费应用程序
- `IAP` 💰 - 包含应用内购买
- `Ads` - 包含广告
- `Proprietary` - 缺少许可证或闭源软件
- `n-day trial` - `n`天后需要付款
- `Root` - 需要在Root模式下运行Shizuku

--------------------

## License

本列表采用[Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 许可协议。

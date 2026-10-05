# awesome-shizuku

### 语言
[English](/README.md) | 简体中文 | [繁體中文](/README_tw.md)

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允许普通应用程序在非root 设备上使用 ADB 直接使用权限提升的系统 API。本列表汇集了一些已知可利用 Shizuku 功能的应用程序。

更多详情：https://shizuku.rikka.app/

欢迎拉取请求。有关提示，请参阅 [贡献](CONTRIBUTING.md)。闭源应用列在另一个文件中。详情请参见[下文](#closed-source-apps)。


> [!NOTE]
> 如需获取本列表的最新动态，[你可以查看每日更新日志](https://github.com/timschneeb/changelog-awesome-shizuku)。

<table>
  <tr>
    <td>
      <h2>Shizuku 应用商店</h2>   
      <p>
      本列表现已作为一个名为 ShizuStore 的开源 Android 应用商店提供。<br/>
        <a href="https://github.com/timschneeb/ShizuStore">下载和源代码可在 GitHub 上获取。</a>
      </p>
      你可以按分类浏览所有 Shizuku 应用，按最近添加、GitHub 星标数、下载量或更新日期排序，并通过 Shizuku 静默安装或更新 APK。
      APK 直接从官方开发者处通过 GitHub、GitLab、F-Droid 及其他来源下载。
      <br><br>
      <a href="https://github.com/timschneeb/ShizuStore"><img src="https://raw.githubusercontent.com/Kunzisoft/Github-badge/main/get-it-on-github.png" width="240" alt="在 GitHub 上获取"></a>
    </td>
    <td align="right">
      <img src="https://raw.githubusercontent.com/timschneeb/ShizuStore/master/fastlane/metadata/android/en-US/images/phoneScreenshots/2.png" width="800" alt="按分类浏览 Shizuku 应用">
    </td>
  </tr>
</table>

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


* [Porter](https://github.com/d4rken-org/porter) - 精简且持续维护的 Shizuku 分支，为应用提供 ADB 访问权限并可选支持 root，还为仅支持 Shizuku 的应用提供兼容配套组件 `Apache-2.0`
* [shevery](https://github.com/HmnDev-Tech/shevery) ✨ - Material 3 分支，支持自启动、TCP 模式、Dhizuku、模块，以及内置集成 AI 的终端
* [Shizako](https://github.com/cr1437/Shizako) - 猫娘形象版 Shizuku，可无缝替代官方管理器，官方 Shizuku-API 应用无需修改即可连接（功能与 shevery 类似） `Apache-2.0`
* [Shizuku (thedjchi's fork)](https://github.com/thedjchi/Shizuku) - Shizuku 分支，支持自启动、TCP 模式和隐身模式（目前暂停维护） `Apache-2.0`
* [Shizuku Next](https://github.com/rushiranpise/Shizuku-Next) - Maintained continuation of thedjchi's fork: automated pairing without typing, start method selection, watchdog, in-app shell terminal, app-ops/firewall manager and a Material 3 UI `Apache-2.0`
* [ShizukuPlus](https://github.com/thejaustin/ShizukuPlus) - Shizuku 分支，为开发者提供扩展 API，并支持自启动、TCP 模式、Dhizuku 等 `Apache-2.0`
* [Stellar](https://github.com/roro2239/Stellar/blob/main/README_en.md) - 另一个 Shizuku 实现，支持自启动、TCP 模式和简易终端（可在启动时自动执行命令） `MPL-2.0`
* [Xhizuku](https://github.com/xeonleonreal/Xhizuku) - Maintained Shizuku fork with Material 3 Expressive UI, ADB module runner, onboarding wizard, server monitor and built-in diagnostics `Apache-2.0`

### AI agents

* [Aether](https://github.com/Zhou-Shilin/Aether) - 本地化、可扩展的通用 AI 智能体，适用于 Android、iOS 和 macOS，可选集成 Shizuku 和 Termux 以直接控制设备。 `GPL-3.0`
* [AndroidHarness](https://github.com/Sanuu7/AndroidHarness) - 设备端编程智能体，通过 Shizuku shell UID 转发特权命令，并以带 Termux 前缀的 Linux 工具链作为回退方案。 `MIT`
* [AutoXiao'er](https://github.com/Joy-word/AutoXiaoer) - 在安卓机器上 7*24h 的伙伴，像人一样基于视觉操作手机。同时支持 Shizuku 和 无障碍操作 模式。 `MIT`
* [ClawGUI](https://github.com/ZJU-REAL/ClawGUI) - 设备端 GUI 智能体运行器，可在单部手机上部署完整的 ClawGUI 大脑栈，并通过 Shizuku 控制。 `Apache-2.0`
* [Hermes Agent](https://github.com/adybag14-cyber/hermes-agent) - Hermes Agent 的 Android 移植版，通过 Shizuku 特权 shell 桥接在设备上执行操作。 `MIT`
* [OmniBot](https://github.com/omnimind-ai/OmniBot) - 设备端 AI 智能体，具备终端、网页浏览、设备控制和系统集成能力 `GPL-3.0`
* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - 使用 AutoGLM 视觉语言模型在设备上自动执行操作 `GPL-3.0`
* [OpenCyvis](https://github.com/opencyvis/opencyvis-phone) - 开源 AI 手机助手，能识别屏幕并根据自然语言任务操作应用，可在后台运行 `Apache-2.0`
* [OpenDroid](https://github.com/yashab-cyber/opendroid) - 开源自主式设备端 AI 智能体，通过屏幕自动化规划并执行多步骤任务 `Apache-2.0`
* [OpenMinis](https://github.com/OpenMinis/OpenMinis) - AI 智能体，具备 Linux shell、浏览器自动化，并通过 Shizuku 控制系统 `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - Android 上最强大的 AI 智能体与 AI 聊天软件。可使用 Shizuku 运行命令 `LGPL-3.0`
* [rish-mcp](https://github.com/turin-dev/rish-mcp) - 通过出站 WebSocket 中继，将 Android 设备的 Shizuku shell 作为 MCP `run_shell` 工具提供给 AI——无需 VPN、ADB 或 sshd，即可从 Claude 或任意 MCP 客户端运行 shell 命令 `MIT`
* [roubao](https://github.com/Turbo1123/roubao/blob/main/README_EN.md) - 基于视觉语言模型的开源设备端 AI 手机自动化助手，通过 Shizuku 系统权限执行任务，无需电脑。 `MIT` [(源代码)](https://github.com/Turbo1123/roubao)
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - 基于 AutoGLM 的自动化与多任务框架。可创建虚拟屏幕供智能体运行应用，并使用多窗口 `Apache 2.0`
* [talon](https://github.com/thefalconry/talon) - Multi-platform agentic AI harness for Telegram/Discord/Teams/terminal with a Flutter companion app; Shizuku enables silent self-updates and elevated access. `Apache-2.0`
* [Zafiro](https://github.com/niki914/zafiro) - 自带 API Key 的 AI 智能体，通过 Shizuku 读取屏幕并控制设备，无需 root。 `MIT`

### Android Auto

* [Flywheel](https://github.com/Benjamin-Wiegand/Flywheel) - 面向去 Google 化手机的自由开源 Android Auto 替代方案，兼容现有车机；Shizuku 用于应用嵌入和通话音频捕获。 `GPL-3.0`

### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - 专为 Android TV 设计的 F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - 专为 Android TV 设计的文件管理器和压缩包查看器 `GPL-3.0` [(源代码)](https://github.com/mlm-games/fluffy)
* [RecentAppsTV](https://github.com/Qutaiba-Khader/RecentAppsTV) - Android TV 的最近任务悬浮界面 `Propietary`
* [TVPilot](https://github.com/mahmutaunal/TVPilot) - 面向 Android TV / Google TV 的遥控优先系统控制与应用管理工具，可选通过 Shizuku 执行高级操作 `Apache-2.0`

### Audio

* [allEQ](https://github.com/omixin/allEQ) - 无需 root 的 10 段系统均衡器，通过 Shizuku 挂接输出混音音频会话。 `GPL-3.0`
* [android-realtime-voice-isolation](https://github.com/sk2andy/android-realtime-voice-isolation) - 使用 Shizuku、GTCRN 和 ONNX Runtime 的设备端实时语音隔离 `MIT`
* [Castix](https://github.com/elhizazi1/Castix) - 管理后台播放限制，并添加 AMOLED 纯黑息屏时钟，支持 Shizuku、Dhizuku、root、LSPosed 或无障碍等多种后端。 `GPL-3.0`
* [centuryplay](https://github.com/g8row/centuryplay) - Streams Android system audio to AirPlay 1/2 speakers; optional Shizuku mode provides silent-phone capture via AudioPolicy loopback and removes capture prompts. `AGPL-3.0`
* [finevolume](https://github.com/broknhrt2562/finevolume) - Pixel-style volume panel with 120-step precision plus per-app and per-stream volume control, using a Shizuku high-precision audio proxy. `Apache-2.0`
* [MicUp](https://github.com/papergray/MicUp) ✨ - 适用于 Android 的实时麦克风音频处理 `MIT`
* [Mixer (1)](https://github.com/farizanjum/mixer-1) - 拦截硬件按键的分应用音量悬浮窗 `Proprietary`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - 针对非 root Android 设备的系统级 JamesDSP 音频处理引擎的实现 `GPL-3.0` [(源代码)](https://github.com/timschneeb/RootlessJamesDSP)
* [Spotify Ad Skipper](https://github.com/sihooney/spotify-ad-skipper) - 监控 Spotify 通知，通过重新开始播放自动跳过广告，并使用 Shizuku 从后台重新拉起 `Proprietary`
* [Volume++](https://github.com/noel-digital-fan/volume_plus_plus) - 自定义音量面板，可通过 Shizuku 或 root 进行分应用音频混合 `MIT`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - 独立控制每个应用的音量 `GPL-2.0`
* [wecho](https://github.com/qumolangmo/wecho) - 用于全局音频效果处理的 Android 应用 `GPL-3.0`

### Automation

* [Argus](https://github.com/JackRushante/argus) - Tasker 级别的 Android 自动化工具，由 LLM 将自然语言规则编译为确定性引擎，可选配 Shizuku shell 网关。 `GPL-3.0`
* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - 基于 JavaScript 的自动化工具 `MPL-2.0`
* [AutoSlide](https://github.com/tianxing-ovo/AutoSlide/blob/master/README.en.md) - 自动滑动工具，可自动播放短视频和自动翻页阅读，并带有悬浮控制 `Apache-2.0` [(源代码)](https://github.com/tianxing-ovo/AutoSlide)
* [flowpilot](https://github.com/emi-ran/flowpilot) - 隐私优先的离线自动化引擎，通过 Shizuku 执行移动数据、飞行模式和深色主题等特权系统操作。 `GPL-3.0`
* [IMD](https://github.com/soul-99/SU_IMD) - Geto 的分支，可针对银行等限制严格的应用隐藏开发者选项、ADB、无障碍服务和 Shizuku 本身，之后还可恢复 `GPL-3.0`
* [NexaFlow](https://github.com/Alaa91H/NexaFlow) - 情境感知的 Android 自动化引擎，结合触发器、约束和动作，并通过 Shizuku 执行特权设备控制。 `MIT`
* [Nothing_Modes](https://github.com/Dvorinka/Nothing_Modes) - 适用于 Nothing 手机的自动化应用（模式、例程、Glyph），也可在其他 Android 设备上运行，可选支持 Shizuku `GPL-3.0`
* [OpenTasker](https://github.com/SysAdminDoc/OpenTasker) - 本地优先的开源 Tasker 替代品，规则易读、权限提示透明；特权操作通过 Shizuku AIDL 用户服务执行。 `MIT`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可针对特定生活环境自动或一键配置设备 `Apache-2.0`
* [Service-Keeper](https://github.com/shaunkleyn/Service-Keeper) - 监控后台、无障碍和通知监听服务，并在被系统杀死后自动重启它们。 `GPL-3.0`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Tasker 的辅助应用 `Propietary`
* [vFlow](https://github.com/ChaoMixian/vFlow/blob/master/README_EN.md) - 可视化自动化工具，将点击、识别、分支和系统操作组合为易于上手的工作流 `GPL-2.0`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord 修改工具 `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - 一款简单的应用，可在你偏好的 Bluesky 客户端中自动打开 Bluesky 链接 `MIT` [(源代码)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CallVault](https://github.com/madkongo/CallVault) - 无需 root 的通话录音器，支持设备端转录/摘要；可通过内置 ADB 独立运行，或选用 Shizuku 后端。 `GPL-3.0`
* [cally](https://github.com/LyoSU/cally) - 适用于搭载原生系统的 Pixel 6 及更新机型的通话录音器，通过 Shizuku shell UID 音频服务录制双向通话，无需 root 或解锁 bootloader。 `GPL-3.0`
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - 通过蓝牙发送和接收文件 `MIT` [(源代码)](https://github.com/kmod-midori/CatShare)
* [ClipShare](https://clipshare.coclyun.top/) - 跨平台剪贴板同步，支持文本、图片、文件和短信；Shizuku 可保持 Android 剪贴板监听器持续运行。 `GPL-3.0` [(源代码)](https://github.com/aa2013/ClipShare/blob/master/README_EN.md)
* [GhostMode](https://github.com/Foxlape/GhostMode) - 让手机在来电时表现为无法接通，同时保持 LTE/5G 数据连接 `Apache-2.0`
* [KDE Connect (Shizuku)](https://github.com/Batestinha/kdeconnect-android-shizuku) - 由 Shizuku 实现 Android 与 PC 之间自动双向剪贴板同步的 KDE Connect 版本。（KDE Connect 的分支，通过 Shizuku 恢复了剪贴板发送支持。） `GPL-2.0`
* [KettuManager](https://github.com/C0C0B01/KettuManager) - Discord 修改工具。已废弃的 BunnyManager 项目的延续 `OSL-3.0`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 这是一款简单的应用程序，可在您喜欢的 Lemmy 客户端中自动启动 lemmy 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 这是一个简单的应用程序，可在您喜欢的 Mastodon 客户端中自动启动 fediverse 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord 修改工具。已废弃的 Bunny-Manager 项目的另一延续 `OSL-3.0`
* [RivoPhoneApp](https://github.com/user-grinch/RivoPhoneApp) - Material 3 拨号与联系人应用，通过 Shizuku 实现无需 root 的通话录音 `GPL-3.0`
* [ShizuCallRecorder](https://github.com/kitsumed/ShizuCallRecorder) ✨ - ShizuCallRecorder 借助 Shizuku 提供的 ADB 权限，在未 root 的设备上录制通话！ `GPL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 让您通过短信浏览网页的应用程序 `GPL-3.0`

### Customization

* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - 基于环境光的智能深色模式 `GPL-3.0` [(源代码)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 将 Now Playing 从 Pixels 移植到其他 Android 设备 `GPL-3.0`
* [android-perapp-language-selector](https://github.com/TakeruF/android-perapp-language-selector) - 在 Android 13+ 上无需 root 强制设置分应用语言，即使应用本身没有内置语言选项 `Apache-2.0`
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - 使用指定应用程序时自动切换免打扰的简单工具 `AGPL-3.0` [(源代码)](https://github.com/im030/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - 管理 Android 手机各屏幕的自动旋转 `GPL-3.0`
* [Capsulyric](https://github.com/FrancoGiudans/Capsulyric) - 通过 Android 实时更新和小米超级岛在状态栏和锁屏上显示当前播放歌词 `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一个非常简单的应用程序，用于更改未 root 的 Android 设备上的运营商名称 `GPL-3.0`
* [cebian](https://github.com/qpst4/cebian) - 一体化的手势与单手导航套件，包含边缘面板、悬浮光标、离线 OCR 悬浮球、应用冻结，以及通过 Shizuku 实现的自由窗口。 `AGPL-3.0`
* [CleanBar](https://github.com/sachinmandawi/CleanBar) - 一键隐藏状态栏和系统图标（时钟、电池等），无需 root `MIT`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - 修改设备 Material You 颜色的应用程序 `GPL-3.0`
* [Commander](https://github.com/astroboii47/Commander) - 键盘优先的命令栏和通知中心；使用 Shizuku 切换最近应用并执行特权 shell 控制。 `MIT`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - 更精细地自定义动画速度 `GPL-3.0` [(源代码)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ-Reborn](https://github.com/Arora-Sir/DarQ-Reborn) - 适用于 Android 10 及以上、可按应用选择的强制深色模式选项 `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - 一些 Android 应用小部件和动态壁纸 `GPL-3.0`
* [DevBay-Launcher](https://github.com/Zoder-Studio/DevBay-Launcher) - Developer-focused launcher with debug app sections, folders, gestures and Quick toggle chips for developer options, animations, fonts and wireless ADB via Shizuku. `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - 高度可定制、基于手势的 Android 启动器，注重速度与效率 `GPL-3.0` [(源代码)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - 平铺窗口管理器、三星 DeX 替代品、弹出式应用启动器 `Proprietary`
* [duo-open](https://github.com/marcoazeem/duo-open) - System-wide iPhone-Duo frosted-glass fold effect for book-style foldables, driven by the real hinge angle as an accessibility overlay or live wallpaper, with optional Shizuku. `MIT`
* [DuoFold-Android](https://github.com/jcx396905-gif/DuoFold-Android) - 全局 iPhone Duo 风格折叠错觉效果，利用 OpenGL ES 根据设备运动重新投影整个屏幕，由 Shizuku 驱动。 `MIT`
* [EdgeGesture](https://github.com/Evilgodxu/EdgeGesture) - Edge-gesture app built on accessibility plus Shizuku: edge swipes, back-tap, floating music and task panels, freeform and app-kill actions. `AGPL-3.0`
* [essentials](https://github.com/sameerasw/essentials) ✨ - 适用于 Pixel 的必备工具、修改和变通方案，也兼容其他设备 `MIT`
* [expressive-cutout](https://github.com/EvanKoe/expressive-cutout) - 遵循 Material Expressive 设计的离线灵动岛，支持通知、实时磁贴和 Material You 颜色 `GPL-3.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - 在智能手机的 Android 操作系统上添加类似桌面的多窗口支持。 `GPL-3.0`
* [FreeformShell](https://github.com/bravoyush/FreeformShell) - 实验性自由窗口管理器辅助工具，通过 Shizuku 系统 API 添加标题栏、调整边框和显示缩放。 `Apache-2.0`
* [gama](https://github.com/palincat/gama) - 可通过设置 `debug.hwui.renderer` 系统属性在 OpenGL 和 Vulkan 渲染器之间切换 `MIT`
* [Google-Shortcuts-Launcher](https://github.com/WSTxda/Google-Shortcuts-Launcher) - Launcher app-drawer shortcut hub for Google app features; Shizuku launches otherwise inaccessible Google components. `GPL-3.0`
* [GSplit](https://github.com/Salat39/GSplit) - Split-screen and freeform multi-window presets with scheduling, boot autostart and overlays; an optional Shizuku ADB shell configures splits. `Proprietary`
* [HyperBridge](https://github.com/D4vidDf/HyperBridge) - 通过将通知桥接到摄像头挖孔 UI，为 HyperOS 带来原生 HyperIsland 体验，支持主题和小部件 `Apache-2.0`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - 双屏游戏设备启动器。使用 Shizuku 将其中一个触摸屏映射为手柄输入 `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允许用户选择单独的应用语言（Android 13+） `Apache-2.0`
* [Lightspeed](https://github.com/SBFlabs/Lightspeed) `IAP` 💰 - Offline gesture-driven workstation and control layer over OEM setups, using Shizuku for elevated navigation and seamless app switching. `Proprietary`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - 使用 Material3 恢复 Android <12 Url-App 链接选择器 `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - 在锁屏上显示小部件。仅在 Android 13 及更高版本需要 Shizuku `MIT` [(源代码)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始设备制造商（小米）不允许您在设备的本地设置中添加额外的（或 "不支持的"）语言，那么这款简单的应用程序就能帮您实现这一功能。 `MIT`
* [O.status](https://github.com/CATCHINGL/O.status) - 简洁的状态栏指示器，用于 Wi-Fi、蜂窝网络和电池，可选集成 Shizuku 以匹配系统图标颜色。 `Proprietary`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - 键盘优先的 Android 命令面板，将应用/设备搜索和系统工具统一到悬浮界面中 `GPL-3.0`
* [Renoir](https://github.com/exaclast/renoir) - Material You 主题设计器，通过 Shizuku shell 命令应用自定义覆盖层。 `Proprietary`
* [SetEditPlus](https://github.com/kerneldroid/SetEditPlus) - Android System/Secure/Global 设置表编辑器，支持 Shizuku/Root 模式、更改跟踪和开机持久化。 `Proprietary`
* [sharemove](https://github.com/thejaustin/sharemove) - 通过 Shizuku 或 root 暂停或禁用组件，将应用从 Android 的分享、“打开方式”和 APK 安装器选择列表中隐藏。 `GPL-3.0`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - 为 shell 命令创建启动器快捷方式 `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易于使用的工具，超越Android系统允许的控制级别 `GPL-3.0`
* [Smart Dock](https://f-droid.org/packages/cu.axel.smartdock/) - 将手机变为桌面环境，提供任务栏、最近应用和开始菜单 `GPL-3.0` [(源代码)](https://github.com/axel358/smartdock)
* [Smart Edge](https://f-droid.org/en/packages/com.imi.smartedge.sidebar.panel/) - 受 OriginOS 启发的高度可定制 Android 侧边面板 `MIT` [(源代码)](https://github.com/Imtiaz-Official/Smart-Edge)
* [Smart Island](https://github.com/agupta07505/SmartIsland) - 轻量级 Android 悬浮界面，将通知、通话和媒体播放汇集为可快速浏览的悬浮岛 `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 插件 `GPL-3.0`
* [SuperShade](https://github.com/thejaustin/SuperShade) - 通知栏替代品，通过 Shizuku shell 命令控制亮度、状态下拉和电源操作。 `Proprietary`
* [SysReadout-Launcher](https://github.com/AndSni/SysReadout-Launcher) - Terminal-style launcher that turns the home screen into a live system monitor with pinned status rows, process/connection/DNS tables and an event log, reading system data through Shizuku. `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 查看和修改 Android 设备上的隐藏设置 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - 将设备背面的双击功能从 Android 12 移植到任何 Android 7.0+ 设备 `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - 清除分享链接中的跟踪参数，支持自定义 URL 重写规则 `GPL-3.0` [(源代码)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用开始菜单访问应用程序可以解锁其他功能 `Apache-2.0` [(源代码)](https://github.com/farmerbb/Taskbar)
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU 和电池小部件 `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - 适用于 Android 的完整桌面体验层 `GPL-3.0`

### Development utilities

* [80bee-app](https://github.com/Endda/80bee-app) - 无需 root 的设备端 ADB/Fastboot 工具箱：通过 Shizuku 实现启动模式、DPI、DNS、应用精简和绕过 sideload 安装限制，还支持 USB-OTG 主机模式。 `Apache-2.0`
* [ActivityLauncherShizukuPlugin](https://github.com/ActivityLauncher/ActivityLauncherShizukuPlugin) - 基于 Shizuku 的 [Activity Launcher](https://github.com/butzist/ActivityLauncher) 插件，可启动私有（未导出）Activity。 `GPL-3.0`
* [ActivityManager](https://github.com/sdex/ActivityManager) - 无需 root 直接启动隐藏和未导出的 Activity `Apache-2.0`
* [ADB Captain](https://github.com/eatenlamp/adbcaptain) - 通过 Shizuku 运行 shell 命令、应用管理和日志访问的 ADB 工具箱，无需 root。 `AGPL-3.0`
* [Android Code Studio](https://github.com/AndroidCSOfficial/android-code-studio) - 用于构建基于 Gradle 的 Android 项目的设备端 IDE；Shizuku 可实现构建后 APK 的静默安装。 `GPL-3.0`
* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 删除已为用户注册账户的应用程序的软件包名称. `Proprietary`
* [Cosmic-IDE](https://github.com/aload0/Cosmic-IDE) - 用于 JVM 开发的 IDE。使用 Shizuku 作为嵌入式 shell `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - 使用 Shizuku 备份/恢复可调试应用的私有数据 `GPL-3.0`
* [DEVTools](https://github.com/MetxStudio/DEVTools) - 一体化 Android 开发工具箱：终端、传感器监视器、应用/文件管理器，以及 Shizuku shell 助手。 `MIT`
* [DroidPerf](https://github.com/fortifying/DroidPerf) - Real-time FPS and hardware telemetry overlay that measures true frame delivery from SurfaceFlinger; Shizuku is required for target FPS, frame times and shell-level app detection. `Proprietary`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一个简单的应用程序，旨在帮助用户通过 DSU 的 Android 功能轻松安装 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修复了 HostProfile 应用程序和 WorkProfile/DualApp/MultiApp 之间的 MediaStore 和文件 IO 兼容性问题。 `Proprietary`
* [FPS-Meter-Android](https://github.com/rdevz-ph/FPS-Meter-Android) - 受三星 Perf Z 启发的高性能轻量 FPS 监控悬浮窗，适用于游戏和性能测试 `MIT`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - 带图表的 FPS 查看悬浮窗 `Proprietary`
* [FrameX-Android](https://github.com/MaheshSharan/FrameX-Android) - 适用于 Android 的实时性能悬浮窗 `MIT`
* [get_event](https://github.com/lalakii/get_event) - 读取/dev/input/event* `Proprietary`
* [IntentX](https://github.com/wxxsfxyzm/IntentX) - Explores installed apps and activities and crafts, tests and launches intents with normal, root or Shizuku access; saves intents as shortcuts. `GPL-3.0`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用于查看设备上的应用程序中使用的库的应用程序。使用 Shizuku 确定其他应用程序的安装源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - 另一个适用于 Android 的 logcat 阅读器 `GPL-3.0`
* [LogSleuth](https://github.com/shiaho777/LogSleuth) - Powerful root-free logcat viewer and embeddable logging SDK with live streaming, search, filters, crash/ANR detection and session replay. `Apache-2.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - 利用 Shizuku 调用 AppOps API，实现精细的应用权限控制 `MIT`
* [panda-ide](https://github.com/ferelking242/panda-ide) - 移动优先的 Flutter IDE，包含代码编辑器、PTY 终端、Git 和 VS Code 扩展；Shizuku 桥接提供 ADB 级 shell，用于在设备上运行 flutter run。 `MIT`
* [roamer](https://github.com/eigenlux-ai/roamer) - 开发者工具，可通过 Shizuku 覆盖 SIM 的 ISO 国家代码和运营商名称，并可选择同步分应用语言区域。 `MIT`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root. `GPL-3.0` [(源代码)](https://github.com/zacharee/RootActivityLauncher)
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - 用于切换无线调试的小部件和快速设置图块（与 KDE Con​​nect 集成） `GPL-3.0`

### Device owner (DPM)

* [Déchaîner](https://github.com/warleysr/dechainer) - 以设备所有者身份屏蔽成人内容；Shizuku 运行 dpm set-device-owner 设置命令。 `Apache-2.0`
* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 启发的应用程序，允许将 DeviceOwner 权限共享给第三方应用程序 `GPL-3.0`
* [harbor](https://f-droid.org/packages/com.monstera.harbor/) - 工作资料管理器，可选配 Shizuku 工具实现自动化 `Apache-2.0` [(源代码)](https://github.com/Stem0794/harbor)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用设备所有者权限管理您的设备 `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - OwnDroid 的分支，增加了额外功能 `GPL-3.0`

### Display management
* [Adaptive-Hz](https://github.com/mahmutaunal/Adaptive-Hz) - 根据用户交互在 60Hz 和 120Hz 之间自动切换显示刷新率。专为不支持真正自适应刷新率的三星设备设计 `MIT`
* [akiHz](https://github.com/anlaki-py/akihz) - 轻量级刷新率切换器，具备快捷设置磁贴、自动刷新率检测和悬浮 FPS 监视器 `MIT`
* [android-display-extend](https://github.com/jqssun/android-display-extend) ✨ - 适用于物理和虚拟显示器的显示管理器，内置虚拟触摸屏。非常适合在 PC 上配合 `scrcpy --new-display` 使用 `GPL-3.0`
* [android-display-mirror](https://github.com/jqssun/android-display-mirror) ✨ - 屏幕镜像中心，支持通过 AirPlay、Moonlight/Sunshine 和 DisplayLink 共享屏幕内容 `GPL-3.0`
* [BetterNightLight](https://github.com/paulsnuff/BetterNightLight) - Grants advanced control over Android's native Night Light: scheduling, boost phases and precise colour temperature through Shizuku or root secure-settings access. `GPL-3.0`
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - 将手机变为触控板和键盘，用于控制在外接有线显示器上运行的单个应用 `GPL-3.0`
* [Dextop](https://github.com/NarYuki/Dextop) - 使用三星 DeX 或 Shizuku 的桌面环境，支持多任务和自定义分辨率 `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可折叠设备上的各种显示屏折叠状态之间切换 `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - 让手机大部分时间保持单色，但允许相机等应用显示彩色 `GPL-3.0`
* [magicdesk](https://github.com/mekhontsev/magicdesk) - 开源 Android 15+ 工作站，通过 Shizuku 提供原生窗口、外接显示器、桌面和 Termux 集成 `GPL-3.0`
* [PortalPad](https://github.com/Smart-Home-User/PortalPad) - 将手机变为触控板、空中鼠标和遥控器，用于 AR 眼镜、显示器和电视等外接显示设备 `MIT`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - 为 Android 设备提供更好的屏幕镜像 `Apache-2.0` [(源代码)](https://github.com/farmerbb/SecondScreen)
* [Tideo Auto Brightness](https://github.com/faded-penguin021/Tideo-Auto-Brightness) - 可解释的自适应亮度替代方案，决策透明并支持昼夜节律。 `MIT`

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi 的分支，支持动画和通过 Shizuku 进行插件管理。 `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - 导出从 Android 版哔哩哔哩下载的视频 `GPL-3.0` [(源代码)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - 将哔哩哔哩缓存文件合并并导出为 MP4，支持手机和电脑客户端 `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 进行插件管理的漫画阅读器。Tachiyomi 的独立后继者。 `Apache-2.0`
  * Mihon/Tachiyomi 还有其他几个活跃的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [Buge-Files](https://bugestudio.website/files/) - Material 3 Expressive 文件管理器，除存储浏览和管理外，还可通过 Shizuku 安装 APK。 `GPL-3.0` [(源代码)](https://github.com/BugeStudioTeam/Buge-Files)
* [Butler](https://github.com/d4rken-org/butler) `IAP` 💰 - 面向高级用户的快速、私密文件浏览器，具备标签页、回收站、正则搜索、应用管理以及 root/Shizuku 支持 `GPL-3.0`
* [Continuum Explorer (Memories)](https://github.com/johakovi/Continuum-Explorer-Memories) - Desktop-class multimedia file manager for DeX, tablets and phones with media/PDF viewers, archives, network storage and game saves, using Shizuku for privileged file access. `GPL-3.0`
* [FileExplorer](https://github.com/SysAdminDoc/FileExplorer) - 支持本地、root、压缩包、网络共享、云、保险库和存储分析的文件管理器 `MIT`
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - 专为 Android TV 设计的文件管理器和压缩包查看器 `GPL-3.0` [(源代码)](https://github.com/mlm-games/fluffy)
* [immich-cloud-media](https://github.com/Dreaming-Codes/immich-cloud-media) - 云媒体提供程序，在 Android 系统照片选择器中显示自托管的 Immich 媒体库，可通过 Shizuku 或 ADB 配置。 `GPL-3.0`
* [KArchiver](https://github.com/sysrv64/KArchiver) - 以归档为核心的 Android 文件管理器：浏览存储，无需解压即可打开并原地编辑 ZIP/TAR/7Z，可在文件和归档内搜索，并可选 Shizuku 或 root 引擎访问受限路径 `GPL-3.0`
* [MaterialFiles](https://github.com/zhanghai/MaterialFiles) - 适用于 Android 的 Material Design 文件管理器 `GPL-3.0`
* [MP-Manager](https://github.com/AbdurazaaqMohammed/MP-Manager) - Dual-pane Material file manager focused on APKs as an open-source MT Manager alternative, with root and Shizuku privileged file management. `GPL-3.0`
* [NFile](https://github.com/Senzme/NFile) - 使用 Shizuku 访问 Android 文件夹的文件管理器 `GPL-3.0`
* [plain-app](https://github.com/plainhub/plain-app) - 自托管 Web 控制面板，可从浏览器管理文件、媒体、联系人、短信和通话，并通过 Shizuku 执行特权短信删除。 `AGPL-3.0`
* [RippleFiles](https://github.com/GokulSB/RippleFiles-FileManager) - Expressive Material 文件管理器，支持本地和云存储，并通过 Shizuku 访问 Android/data。 `MIT`
* [ROSE](https://github.com/NarayanChetri/ROSE) - 现代化文件管理器，采用 Material 3 UI，支持压缩包、回收站，并可通过 Shizuku 无需 root 访问 Android/data 和 Android/obb。 `GPL-3.0`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE是Android最彻底的清理工具 `GPL-3.0` [(源代码)](https://github.com/d4rken-org/sdmaid-se)
* [sync-to-android-data](https://github.com/kamren-zirger/sync-to-android-data) - 在目标应用打开或关闭时，同步 Android/data 受限文件夹中的文件（导入/导出） `MIT`
* [twig](https://github.com/dev2ex/twig) - 体积优先的双栏文件管理器（约 7MB），支持本地、压缩包、FTP/SFTP/SMB/WebDAV/S3/restic/Jellyfin `GPL-3.0`
* [UnscopeMyData](https://github.com/kepatotorica/UnscopeMyData) - 使用 Shizuku 提升文件访问权限，将应用数据移入/移出分区存储文件夹。 `GPL-3.0`
* [XArchiver](https://github.com/Xtra-Manager-Software/XArchiver) - 内置压缩包支持的文件管理器 `MIT`
* [XClean](https://github.com/utopiafar/XClean) - 基于规则的清理工具，具备普通、Shizuku 和 Root 三种引擎，用于清除应用垃圾。 `Proprietary`
* [XFiles](https://github.com/Local1stDotApp/XFiles) - 离线文件管理器，支持 root 和 Shizuku，可完整访问文件系统 `GPL-3.0`
* [ZenFile](https://github.com/l930203811/ZenFile) - NFile 的分支，内置远程文件服务器支持 `GPL-3.0`
* [ZhuFiler](https://github.com/Artzhu86/ZhuFiler) - 开源 Material You 文件管理器，具备压缩包、编辑器、媒体播放、APK 处理以及由 Shizuku 支持的特权访问。 `MIT`

> [!NOTE]
> [点击此处查看更多文件管理器（闭源）](pages/CLOSED_SOURCE_cn.md#file-management)

### Games

* [ADOFAI-Key-Viewer-Mobile](https://github.com/QuyetGD-15/ADOFAI-Key-Viewer-Mobile) - Overlay key visualizer for ADOFAI and rhythm games; reads hardware input events through Shizuku getevent for ultra-low-latency touch visualization, KPS tracking and click counting. `Proprietary`
* [AimBuddy](https://github.com/1337Xcode/AimBuddy) - On-device aim assistant for Android games: real-time screen capture, object detection and target-tracking overlays; optional assisted input through Shizuku injectInputEvent. `Proprietary`
* [Ascent](https://github.com/4o3F/Ascent) - 用于获取米哈游游戏抽卡历史链接的工具  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - 《BrownDust II》Mod 管理器 `Proprietary`
* [Cinderbox-Companion](https://github.com/ObfuscatedVoid/Cinderbox-Companion) - 《星露谷物语》Android 版配套应用，支持 Steam 云存档同步、游戏文件下载和 SMAPI Mod 管理 `MIT`
* [CloudSync-Mobile](https://github.com/StardewValleyMods/CloudSync-Mobile) - 可在多台设备间同步《星露谷物语》存档的应用 `GPL-3.0`
* [ex-astris-save-editor](https://github.com/Ncorror/ex-astris-save-editor) - Unofficial Ex Astris save editor: inventory editing, verified backups and Arknights skin switching, with automatic save discovery through Root or Shizuku. `GPL-3.0`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - 管理“洛杉矶犯罪”游戏的地图、壁纸和屏幕截图 `GPL-3.0`
* [linkura-localify](https://github.com/ChocoLZS/linkura-localify) - 《Link！Like！LoveLive！》的本地化插件，通过 LLM 翻译游戏文本 `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 游戏“Last Origin”的 Mod 管理器 `Proprietary`
* [MAA-Meow](https://github.com/Aliothmoon/MAA-Meow/blob/main/README_EN.md) - 在 Android 上原生运行 MAA，一键完成《明日方舟》日常任务，支持前台和后台模式 `AGPL-3.0`
* [mt-en-applier](https://github.com/Aikiooo/mt-en-applier) - 《无职转生》手游非官方英文补丁的一键安装器，通过 Shizuku 复制文件，无需 root 或电脑。 `Proprietary`
* [Nibnya](https://github.com/yinghuajimew/Nibnya) - 适用于 Minecraft 基岩版的 Android NBT 编辑器，由 Shizuku 提供 /data 访问权限 `AGPL-3.0`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - 用于本地化 Android 版《CHAOS;CHILD》视觉小说的配套应用 `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 轻松导入和共享 Polyfield 地图 `GPL-3.0`
* [pogoplusle](https://github.com/Mygod/pogoplusle) - 连接 Pokémon GO Plus 时跳过配对对话框 `Apache-2.0`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - 《原神》自动对话点击器 `MIT`
* [stalker](https://github.com/onerdna/stalker) - 《暗影格斗 2》存档查看与编辑器 `GPL-3.0`
* [SwiftSense](https://github.com/itsmelissadev/SwiftSense) - 游戏调优工具，使用 Shizuku 冻结后台应用、禁用软件包并提高传感器采样率。 `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order游戏翻译项目 `MIT`

### Input methods

* [8bitdo-xbox-bridge](https://github.com/BoredNewCoder/8bitdo-xbox-bridge) - 通过逆向工程的 GIP 协议和 Shizuku uinput 注入，让 8BitDo Ultimate Xbox 有线控制器在 Android TV 上作为真正的全局手柄使用。 `MIT`
* [BiBi Keyboard](https://github.com/BryceWG/BiBi-Keyboard/blob/main/README_EN.md) - AI 语音输入法键盘；Shizuku 或 root 可保持其悬浮球和音量键后台服务存活。 `Apache-2.0`
* [ButtonSilencer](https://github.com/EithonX/ButtonSilencer) - 屏蔽故障耳机及入耳式耳机（IEM）的线控按钮，同时不影响手机自身按键；Shizuku 为息屏耳机输入保护提供特权通道。 `MIT`
* [C9](https://github.com/austinauyeung/C9) - 在传统光标之外提供高效的网格光标。仅在 Android 11 上需要 Shizuku。 `Apache-2.0`
* [GameShift](https://github.com/tientien17/GameShift) - 游戏手柄连接时自动切换默认桌面启动器，断开时恢复；使用 Shizuku，无需 root。 `Apache-2.0`
* [Joycon2Android](https://github.com/JoeGeC/joycon2android) - 通过 BLE 连接 Nintendo Switch 2 Joy-Con 控制器，并通过 Shizuku UHID 中继将其用作全局虚拟手柄。 `GPL-3.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - 一款 Android 应用程序，可改变您设备上按钮的功能！ `GPL-3.0` [(源代码)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - 在 Android 设备上使用鼠标和键盘玩游戏；游戏按键映射工具 `Apache-2.0`
* [OpenMapper](https://github.com/kinou-p/android-open-mapper) - 免费开源的游戏手柄按键映射工具，使用 Shizuku 进行亚毫秒级延迟的触摸注入；Mantis 和 Panda 的替代品。 `PolyForm-Noncommercial-1.0.0`
* [pastiera](https://github.com/palsoftware/pastiera) - 专为物理键盘设备设计的 Android 键盘。使用 Shizuku 实现触控板手势 `GPL-3.0`
* [Steam Controller for Android](https://github.com/SonicDX12/SteamController-Android) - 通过由 Shizuku 支持的 Linux uinput，将 Steam Controller 2026 用作真正的 Android 手柄；支持 USB、接收器或 BLE。 `MIT`
* [TitanPad](https://github.com/sztupy/TitanPad) - 将 Titan2 物理键盘的电容输入转换为鼠标和滚动手势。使用 Shizuku 读取触控板输入并设置虚拟 HID 设备 `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 适用于 Android x86 的键盘映射器 `GPL-3.0`


### Installer & app stores

* [APKUpdater](https://github.com/DmitryN71/apkupdater) - APKUpdater 分支，在其 APKMirror、Aptoide、F-Droid 和 IzzyOnDroid 来源之外，新增基于 Shizuku 的静默安装。 `GPL-3.0`
* [AuroraDroid](https://f-droid.org/packages/com.aurora.adroid/) - 自由开源的 F-Droid 客户端，支持通过 Shizuku/root 静默安装和自动更新 `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/auroradroid)
* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - Google Play 商店的开源替代品，具有隐私性和现代设计 `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - 轻松下载、安装和共享模组 `Proprietary`
* [Discoverium](https://github.com/cygnusx-1-org/Discoverium) - Obtainium 分支，用于从源头发现和安装应用，支持 Shizuku、Dhizuku 和 Sui 安装后端。 `GPL-3.0`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：隐私友好浏览器的更新程序 `GPL-3.0` [(源代码)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F-Droid 客户端 `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - 用于 GitHub Release 的应用商店，具备发现功能 `Apache-2.0` [(源代码)](https://github.com/kurikomi-labs/komi-store)
* [instafel](https://github.com/mamiiblt/instafel) - Instafel（Instagram Mod）的更新应用 `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - 现代且实用的 Android 应用安装程序替代品 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 简单的应用程序使用 Shizuku 在设备上安装带有高级选项的 APK `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 存储库的非官方客户端 `GPL-3.0`
* [KingInstaller](https://github.com/fcaronte/KingInstaller) - APK 安装器，可伪装成 Play 商店安装器身份以绕过应用可见性限制，支持通过 intent、Shizuku 或 root 安装 `GPL-3.0`
* [LocalAndroidStore](https://github.com/SysAdminDoc/LocalAndroidStore) - 私有应用目录，可安装经过签名的 GitHub 和 F-Droid 版本，可选通过 Shizuku 持有的安装会话进行安装。 `MIT`
* [multistore](https://github.com/FedeFluork/multistore) - 将第三方应用商店聚合为一个目录，用于搜索、比较、下载和更新 APK `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - 具有现代 UI 和大量额外功能的 F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接从源获取 Android 应用程序更新 `GPL-3.0`
  * [ObtainX](https://f-droid.org/packages/dev.bikram.obtainx/) - Obtainium 分支，重新设计了 Material 3 UI `GPL-3.0` [(源代码)](https://github.com/bikram-agarwal/ObtainX)
* [Omnify](https://github.com/Victor-root/Omnify) - F-Droid 客户端分支，还可安装来自外部来源的应用，具备 Shizuku 安装器和“支持 Shizuku”发现栏目。 `GPL-3.0`
* [OpenLoader](https://github.com/thebytearray/OpenLoader) - 为 Android 开发者验证时代打造的 APK 安装器，使用 Shizuku 执行特权安装。 `GPL-3.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - Mod 应用商店 `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允许覆盖包请求者和执行者的包安装程序 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 拆分 APK 安装程序 `GPL-3.0` [(源代码)](https://github.com/Aefyr/SAI)
* [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch) - 由 Shizuku 驱动的应用管理器，支持静默安装、更新和批量操作 `GPL-3.0`
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - 轻量级应用安装器替代品，支持拆分 APK `Apache-2.0`
* [ShizuStore](https://github.com/timschneeb/ShizuStore) ✨ - Shizuku 应用商店。基于这份 awesome-shizuku 列表，直接从上游来源安装 APK `GPL-3.0`
* [tern](https://github.com/munzzyy/tern) - Obtainium-style updater that verifies package name, signing certificate and publisher checksums before installing via Shizuku, Dhizuku, root or the system installer on phones, tablets and TV. `GPL-3.0`
* [universal-installer](https://github.com/pass-with-high-score/universal-installer) - 安装和管理 APK 软件包，支持拆分 APK、通过 Shizuku 静默安装以及 VirusTotal 恶意软件扫描 `GPL-3.0`
* [Vyxel Apps](https://github.com/NikhilKain/vyxel-apps) `IAP` 💰 - 由 GitHub 支持的应用商店，具备签名验证和通过 Shizuku 的静默安装。 `AGPL-3.0`
* [yuki](https://github.com/carlelieser/yuki) - Catalog and storefront for open-source Shizuku apps, crawled from GitHub `MIT`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - Android 内置 `dex2oat` 工具的图形界面，可重新优化已安装应用的 DEX 代码 `Apache-2.0`
* [CaptureCap](https://github.com/yepgoryo/CaptureCap) - 屏幕和音频录制及串流应用，无需 root `MIT`
* [Device Watch](https://github.com/jrs8205/Device-Watch) - Offline device monitor with widgets, per-app usage insights and a charging screensaver; optional Shizuku access reveals battery statistics, real CPU/GPU load and temperatures. `GPL-3.0`
* [Fern](https://github.com/wized2/Fern) - Material 3 live system monitor for CPU, RAM, storage, battery, thermal and network, with an optional Shizuku shell for elevated readings. `Proprietary`
* [ghostlock-app](https://github.com/YuKongA/ghostlock-app) - One-tap CVE-2026-43499 privilege-escalation app granting temporary uid 0 across many stock devices; Shizuku-required kernel profiles run through a shell Shizuku. `Apache-2.0`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - 找出状态栏闹钟图标处于活动状态的原因 `Proprietary`
* [IrisShot](https://github.com/raging-flames/IrisShot) - 适用于 Android 游戏的长截图工具，使用 MediaProjection 或由 Shizuku 驱动的 shell 截图自动滚动并拼接长截图。 `Proprietary`
* [KeiOS](https://github.com/hosizoraru/KeiOS) - 系统工具控制台，内置本地 MCP 服务、GitHub 发布跟踪，可通过 Shizuku 或 root 执行特权安装，并提供 Blue Archive 辅助工具 `Apache-2.0`
* [kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) - Home Assistant 展示屏：语音卫星、同步音乐和照片屏保，并使用 Shizuku 执行特权 APK 更新和设备桥接。 `Proprietary`
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [Mafza](https://github.com/yshalsager/Mafza) - 紧急操作运行器，支持单个可配置方案、外部紧急触发器以及安全的试运行模式 `Proprietary`
* [NekokoLPA2](https://github.com/iebb/NekokoLPA2) - 跨平台 eSIM/eUICC 管理器；在 Android 上通过 Shizuku 打开仅 shell 可用的 QRTR 套接字，以执行 Telephony/TMAPI 配置文件操作 `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - 使用 Shizuku 让通知保持常驻/无法清除的 Android 工具 `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - 退出选定应用时自动关闭它们，以节省电量和内存 `Apache-2.0`
* [overlay-translator](https://github.com/ciddwd/overlay-translator) - 适用于游戏、视觉小说和漫画的实时屏幕翻译器，支持设备端/云端 OCR 和悬浮窗 `Apache-2.0`
* [PhoneDiagnosticTool](https://github.com/ScoobyDouche/PhoneDiagnosticTool) - 设备端手机诊断工具，涵盖 CPU、GPU、电池、RAM、存储、传感器和显示屏，可选通过 Shizuku/root 提权读取。 `MIT`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - 利用 CVE-2024-31317 进行 Zygote 注入，集成远程终端和文件传输功能 `MIT`
* [Rainy Screenshot](https://github.com/CATMIAOZHI/RainyScreenShot/blob/main/README_EN.md) - 通过 Shizuku 或 Porter 特权 shell 而非 MediaProjection 进行静默截图和录屏。 `Proprietary`
* [Screen Recorder](https://github.com/muhammadhaseebiqbal-dev/Screen-Recorder) - 屏幕录制器，通过 Shizuku 捕获内部音频。 `MIT`
* [silent-alarm](https://github.com/izumisagirii/silent-alarm) - 耳机优先的闹钟，在后台管控严格的 OEM ROM 上通过 Shizuku 或 root 看门狗重启应用来保持闹钟存活。 `AGPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一个简单的应用程序，用于通过 WearOS 手表控制 Android 设备 `Apache-2.0` [(源代码)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - 通过 Telegram 消息远程控制设备 `BSD 3-Clause`
* [VineOS](https://github.com/Hexadecinull/VineOS) - Android 虚拟机引擎；Shizuku 探测 shell 权限，以支持无需 root 的 ADB 和无线调试路径。 `GPL-3.0`

### Network

* [ADNS](https://github.com/eyalm2000/adns) - 适用于 Android 的基于 DNS 的广告拦截器 `MIT`
* [Bluetooth Bouncer](https://github.com/harvzor/android-bluetooth-bouncer) - 针对各个已配对设备控制蓝牙自动连接并保持配对；策略通过 Shizuku 用户服务强制执行。 `GPL-3.0`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上读取手机信号塔信息 `MIT` [(源代码)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - 无需 VPN 的应用防火墙；还可管理软件包 `MIT`
* [delta](https://github.com/supershadoe/delta) - 使用 Shizuku 的热点管理器 `BSD-3-Clause`
* [Dolphy-App](https://github.com/unvoiddd/Dolphy-App) - 用于无线协议研究的 NFC、BLE 和红外多功能工具 `GPL-3.0`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - 可通过蓝牙远程开启热点的应用——类似 Apple 连续互通，但面向所有人 `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Google FindMyDevice 服务的安全和开源替代方案 `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - 双模式防火墙：可使用 Shizuku、标准本地 VPN 接口或两者同时阻止互联网访问。 `MIT`
* [hikari-adblock](https://github.com/codegeasse1/hikari-adblock) - 无需 root 的广告/跟踪器/恶意软件拦截器，具备本地 VPN DNS 过滤以及 Shizuku iptables/nftables 防火墙模式 `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 预览和编辑/etc/hosts文件 `MIT`
* [hotspot_channel_setter](https://github.com/Lorax121/hotspot_channel_setter) - Lists and applies the Wi-Fi hotspot SoftAP 2.4/5 GHz channel via Shizuku or root and persists the choice across reboots. `Proprietary`
* [MaybeEdgeScanner](https://github.com/maybeknott/MaybeEdgeScanner) - 路由配对网络扫描器，探测 TCP/TLS/HTTP 目标，可选 Shizuku 辅助的射频诊断。 `AGPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一个在 Android 上运行 Naiveproxy 的简单应用程序 `MIT`
* [NetManager](https://github.com/DottoXD/NetManager) - Material 风格的 4G/5G NR 蜂窝网络监视器，具备基站地图、路测和速度测试；Shizuku shell 桥接可解锁额外网络数据。 `GPL-3.0`
* [NetSwitcher](https://github.com/nd4y/netswitcher) - 通过应用、快捷方式、小部件或快捷设置磁贴，使用 Shizuku 或 root 快速切换 Wi-Fi、移动数据和以太网。 `Proprietary`
* [NetToggle](https://github.com/Dhangofa/NetToggle) - 轻量级 Android 快捷设置磁贴，使用 Root 或 Shizuku 强制仅 5G、仅 4G 和首选网络模式 `GPL-3.0`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - 用于 4G/5G 网络模式切换的 Android 应用 `GPL-3.0`
* [nobita](https://github.com/duhow/nobita) - 使用 Shizuku 在设备上将蓝牙 HCI 流量记录为 Wireshark 兼容的 PCAPNG 文件。 `Proprietary`
* [Quintz](https://github.com/corgilittlelegs/Quintz) - 无需 root 的 Wi-Fi 频段锁定和 BSSID 引导工具，通过 Shizuku 将 Android 固定在 5/6 GHz，具备 AP 遥测和射频测向功能。 `MIT`
* [RKNHardering](https://github.com/xtclovver/RKNHardering) - 使用社区验证的检查在设备上检测 VPN/代理规避工具，并通过 Shizuku 或 Root 执行特权探测。 `AGPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - 不依赖 VPN 或 root 的开源应用防火墙 `GPL-3.0`
* [Shizzi](https://github.com/carlelieser/shizzi) - 通过 Shizuku 无需 root 绕过 Wi-Fi 网络共享限制 `Proprietary`
* [sing-box](https://f-droid.org/packages/io.nekohasekai.sfa/) - 通用代理平台。使用 Shizuku 实现分应用代理 `GPL-3.0` [(源代码)](https://github.com/SagerNet/sing-box)
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - 状态栏中的常驻网速跟踪器 `GPL-3.0` [(源代码)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - WireGuard 和 AmneziaWG 的 FOSS Android 客户端，支持自动隧道功能 `MIT`
* [WiFi Portal](https://github.com/lovitus/wifiportal) - 通过 Shizuku UserService 应用强制门户探测设置，支持备份、写入前验证和地区预设。 `Proprietary`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - 使用 Shizuku 管理和查看已保存 Wi-Fi 密码的简单应用 `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - 在 Android 11 及更高版本上查看您保存的 WiFi 密码，无需 root `Proprietary` [(源代码)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - 基于 LSPosed 扩展的免 root Xposed 框架 `GPL-3.0`
* [Morphe](https://morphe.software/) - 基于 Universal-ReVanced-Manager 的易用 YouTube 补丁工具 `GPL-3.0` [(源代码)](https://github.com/MorpheApp/morphe-manager)
* [NPatch](https://github.com/7723mod/NPatch) - 基于 LSPosed 的免 root Xposed 框架，可将 Xposed API 注入目标 APK `GPL-3.0`
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - 具备官方管理器所没有的额外功能的 ReVanced 补丁工具 `GPL-3.0`

### Power management

* [Amply](https://github.com/d4rken-org/amply) - 轻松控制充电上限。可临时允许一次完整充电，然后自动恢复你的保护性充电上限 `GPL-3.0`
* [BatStats](https://github.com/mlm-games/BatStats) - 通过 Shizuku 提供统计信息的电池监视器 `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - 一个简单的应用程序，可在 Android 14 及更高版本上显示电池状态信息。 `GPL-3.0`
* [Battery](https://github.com/zhyang18/Battery/blob/main/README_EN.md) - 电池健康和硬件分析；Shizuku 提供提权 shell 以深入读取电池参数。 `MIT`
* [Battery Health Tracker](https://github.com/FrancescoMin/batteryhealthtracker) - 适用于 Oppo、OnePlus 和 Realme 设备的电池健康诊断和真实化学容量跟踪，通过 Shizuku 实现。 `Apache-2.0`
* [Battery-Monitor](https://github.com/tswistak/Battery-Monitor) - 使用 Shizuku 长期跟踪并记录电池容量和参数 `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - 通过 Shizuku 直观修改电池数据的开源应用 `GPL-3.0`
* [DozeTap](https://github.com/dhruvanbhalara/DozeTap) - 屏幕超时预设，通过 Shizuku 一键授予 WRITE_SECURE_SETTINGS 权限。 `Apache-2.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - 息屏后立即启用 Doze 模式并关闭运动感应，以获得最佳电池续航 `GPL-3.0` [(源代码)](https://github.com/Akylas/EnforceDoze)
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - 设置后无需打理的程序，用于阻止 Android 应用在后台运行 `GPL-3.0` [(源代码)](https://github.com/adil192/no_more_background)
* [PULSE // BATTERY](https://github.com/kreza6173-pixel/pulse-battery) - Overnight per-app alarm-wakeup report with verified one-tap standby restrict and revert, plus wake lock and alarm diagnostics, Doze controls and APK backup `MIT`
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - 支持 Shizuku 的高级重启菜单 `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 关闭 Android 屏幕而不进入待机/睡眠模式 `Proprietary`
* [sleep-timer](https://github.com/Xitee1/sleep-timer) - 睡眠定时器，可暂停媒体并关闭 WIFI/蓝牙/显示屏 `GPL-3.0`
* [USB PD Bypass](https://github.com/ONDER1E/usbpdbs) - 通过 Shizuku 在充电阈值时切换 USB PD 电池旁路模式，具备自愈恢复功能。 `Proprietary`
* [volt](https://github.com/lebiggg/volt) - Greenify 的继任者：通过 Shizuku 实现评分式应用休眠和 UnifiedPush 推送唤醒 `GPL-3.0`
* [wakelogs](https://github.com/dernikiausd/wakelogs) - 通过基于 Shizuku 的系统诊断分析屏幕唤醒、CPU 活动、闹钟和设备休眠。 `GPL-3.0`
* [zukulock](https://github.com/tiendnm/zukulock) - 非常轻量的应用，启动时锁定屏幕，有助于减少电源键磨损 `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一键隐藏您的私人文件和 Android 应用程序。 `Apache-2.0` [(源代码)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - 旨在静默保护用户数据免受强大对手侵害的应用 `GPL-3.0`
* [anubis](https://github.com/sogonov/anubis) - 应用管理器，通过 Shizuku pm disable 根据 VPN 状态冻结/解冻应用组，使被冻结的应用无法检测或绕过 VPN。 `MIT`
* [AppLock](https://github.com/aload0/AppLock) ✨ - MIUI 12+ 防止应用被侧滑或一键清理杀死 `MIT`
* [AppOpsNext](https://github.com/1zumiii/AppOpsNext) - 适用于 Android 15+ 的 AppOps 管理器，具备权限模板、批量更改、安装历史和通过 Shizuku 的诊断 `Proprietary`
* [AvarionX-Android-Antivirus](https://github.com/phsycologicalFudge/AvarionX-Android-Antivirus) - 设备端杀毒软件，具备本地恶意软件/APK 扫描、下载监控和 DNS 过滤；Shizuku 支持勒索软件式行为监控 `MPL-2.0`
* [Monica](https://github.com/Monica-Pass/Monica) - 本地优先的 Bitwarden/KeePass 密码保险库，支持 TOTP；Shizuku 可保持自动填充保护在后台运行。 `GPL-3.0`
* [Privacify](https://github.com/robinsrk/privacify) - 隐私控制中心：权限扫描器、传感器使用时间线和隐私评分，并可通过 Root/Shizuku 进行高级硬件控制。 `Apache-2.0`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - 根据锁定/解锁状态管理设备隐私 `MIT` [(源代码)](https://github.com/dorumrr/privacyflip)

### Productivity

* [Blink](https://github.com/character-flat/Blink) - 常驻且高度可定制的 20-20-20 护眼定时器，使用 Shizuku 将自身加入 Android 电池优化白名单 `GPL-3.0`
* [Cresto](https://github.com/Nevodev/Cresto) - 待办应用，具备 AI 捕获、日历同步和提醒；其快捷设置当前屏幕提取功能通过 Shizuku shell 访问来抓取屏幕。 `Apache-2.0`
* [Curbox](https://f-droid.org/packages/neth.iecal.curbox/) ✨ - 减少屏幕成瘾并查看使用分析的工具 `GPL-3.0` [(源代码)](https://github.com/curbox-app/curbox-android)
* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - 数字排毒：让你使用手机，而不是让手机使用你 `GPL-3.0`
* [HyperCopy](https://github.com/1812z/HyperCopy) - 剪贴板直达应用工具：监控复制的链接，并通过 Shizuku 或 LSPosed 直接在对应应用中打开。 `Proprietary`
* [input-leaf](https://github.com/anasvhora284/input-leaf) - Input Leap/Deskflow 的 Android 客户端：通过局域网使用 PC 鼠标和键盘控制手机，使用 Shizuku 输入注入，无需 root。 `Apache-2.0`
* [quickdash](https://github.com/Balajitechlabs/quickdash) - 悬浮生产力面板，具备 UPI/PayPal 收款和聊天快捷方式；Shizuku 桥接可解锁特权系统功能。 `Proprietary`
* [Sefirah](https://github.com/shrimqy/Sefirah-Android) - Windows-Android 集成工具，实现剪贴板、通知、文件、短信和通话同步；Shizuku 可在 Android 10+ 上启用剪贴板。 `GPL-3.0`

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一个用于切换“息屏显示（Always on Display）”的 Android 快捷设置 `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本上带回独立的 Wi-Fi 和移动数据磁贴，并提供更好的统一网络磁贴 `GPL-3.0` [(源代码)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DataSimTile](https://github.com/Mygod/DataSimTile) - 用于切换默认移动数据 SIM 卡的磁贴 `Apache-2.0`
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - 提供快捷设置磁贴和快捷方式，可在不锁定屏幕或停止前台运行应用的情况下关闭显示屏 `MIT` [(源代码)](https://github.com/UlyssesZh/DisplayToggle)
* [DNS Toggle](https://f-droid.org/packages/com.ericlowry.dnstoggle/) - 用于切换和配置私有 DNS 的快捷设置磁贴，可选高级自动化。 `MIT` [(源代码)](https://github.com/ELowry/DNSToggle)
* [ManualRotate](https://github.com/Verisonder/ManualRotate) - 无需旋转手机即可切换竖屏/横屏的快捷设置磁贴；可选通过 Shizuku 覆盖应用的方向锁定。 `GPL-3.0`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - 用于开启或关闭私有 DNS 设置的快捷磁贴 `GPL-3.0` [(源代码)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 用于切换当前私有 DNS 服务器的快捷设置磁贴 `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - 提供用于切换 USB 调试和切换私有 DNS 主机的快捷磁贴 `GPL-3.0` [(源代码)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 通过快捷设置启用/禁用设备传感器 `Apache-2.0`
* [Tooler](https://github.com/jehan593/tooler) - 用于锁屏、私有 DNS、灰度和充电的快捷设置磁贴，通过 Shizuku 执行。 `MIT`

### Software management

* [ADB Application Manager Pro](https://github.com/Bingblop/ADB-Application-Manager) - All-in-one app and device manager for debloating, freezing, installing, backing up and tweaking hidden settings through Shizuku or ADB. `Proprietary`
* [AppControlX](https://github.com/risunCode/AppControl-X) - 冻结、强制停止、卸载应用，更改后台优化等 `GPL-3.0`
* [AppDualZuku](https://github.com/nathanatgit/AppDualZuku) - 使用 Shizuku 在隔离或共享工作区（托管配置文件）中管理多个应用实例，可选 root 后端。 `Proprietary`
* [AppManagerNG](https://github.com/SysAdminDoc/AppManagerNG) - [AppManager](https://github.com/muntashirakon/appmanager) 的分支，用于检查、精简、备份、冻结和控制 Android 应用；支持 Shizuku、ADB、Dhizuku 或 root。 `GPL-3.0`
* [Appslim](https://github.com/Horizen5/Appslim/blob/master/docs/README_en.md) - Android 运行时分析器，分析启动行为、CPU/内存和 Dex 调用，然后通过钩子、规则以及 Shizuku 或 root 操作精简应用。 `Proprietary`
* [AppVaultX](https://github.com/sunilpaulmathew/AppVaultX) - 由 Shizuku 驱动的高性能应用管理器 `GPL-3.0`
* [Blocker](https://github.com/lihenggui/blocker) - 启用/禁用 Android 组件，例如活动、服务、接收器和提供者 `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - 专注于权限管理的应用管理器 `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - 无需root即可卸载任何应用程序 `LGPL-3.0` [(源代码)](https://github.com/samolego/Canta)
* [CloneCat](https://github.com/AhmetCanArslan/CloneCat) - 跨工作资料、私密空间、双应用和次要用户克隆和管理应用，并提供主屏幕快捷方式 `Proprietary`
* [CloneSpace](https://github.com/udmodz0/adb-cloner) - App cloner and isolated multi-user workspace powered by Shizuku that runs extra copies of apps in separate profiles without duplicating APKs or needing a PC. `Apache-2.0`
* [Dexor](https://github.com/DeveshTone/Dexor) - 面向 Android 应用的提前（AOT）字节码编译和 dexopt 运行时管理器 `MIT`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 应用程序可禁用未使用的应用程序，同时仍允许方便地访问它们 `MIT`
* [DroidUtility](https://github.com/DroidUtility/DroidUtility) - 无需 root 的工具套件，通过 Shizuku 进行应用精简、系统调整和特权 shell 执行，面向仅使用手机的开发者。 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 通过手动或半自动冻结蹩脚软件来提高设备的速度和电池寿命 `Apache-2.0` [(源代码)](https://github.com/FreezeYou/FreezeYou)
* [Guest-Manager](https://github.com/dlawoals2713/Guest-Manager) - 在厂商已禁用访客和多用户模式的设备上，通过 Shizuku shell 无需 root 启用这些隐藏模式。 `Proprietary`
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - 冻结、隐藏或禁用任何应用程序。创建并组织可一键冻结的应用程序组。 `GPL-3.0` [(源代码)](https://github.com/aistra0528/Hail)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Island 完整的 FLOSS 分叉 `Apache-2.0` [(源代码)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - 适用于 root 和非 root 设备的 Android 应用程序管理器 `GPL-3.0` [(源代码)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔离和克隆应用程序以保护隐私和并行运行 `Apache-2.0` [(源代码)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [Minimal Kernel Manager](https://github.com/abhay-byte/mkm) - 内核管理器和系统监视器，具备电池统计、开机自动应用以及通过 Shizuku 或 root 支持隐藏应用。 `GPL-3.0`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - 管理您的 Magisk 模块存储库 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能强大的应用程序，可管理系统和用户应用程序 `GPL-3.0` [(源代码)](https://github.com/SmartPack/PackageManager)
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - 具备冻结和安装功能的应用管理器。 `GPL-3.0` [(源代码)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 检查 Android 应用程序、Magisk 模块等的更新！ `GPL-3.0` [(源代码)](https://github.com/DUpdateSystem/UpgradeAll)
* [VOID // APPS](https://github.com/kreza6173-pixel/void-apps) - Shizuku app manager: suspend, disable, debloat presets, permissions and AppOps, autostart, per-app network block, APK/XAPK installer and cleaner. Every change is read back from Android `MIT`
* [Youki Users](https://github.com/mrYouki/Youki-Users) ✨ - Standalone Android multi-user manager to create, switch and delete user profiles with custom photos. `GPL-3.0`

### Task manager

* [Android Monitor (Preview)](https://github.com/TerminalDev-1/AndroidMonitor-Preview) - Task-Manager-style system monitor with live CPU, GPU, RAM, network and thermal graphs; Shizuku unlocks real CPU usage, the process list and End task. `MIT`
* [KillMyApps](https://github.com/dedeadend/KillMyApps) - 通过 Shizuku 或 root 结束后台进程，以改善电池续航和性能 `GPL-3.0`
* [memhogs](https://github.com/cicerothoma/memhogs-android) - 查看哪些应用在消耗手机内存。通过 Shizuku 提供分应用明细，辅助进程归组到所属应用下 `MIT`
* [MemorySnapshot](https://github.com/RyensX/MemorySnapshot/blob/master/docs/README_EN.md) - 设备端 Android 内存观察器：按应用/进程跟踪 PSS、保存和比较快照，通过 Shizuku 或 root 收集数据。 `Proprietary`
* [Pensum](https://github.com/troikoss/Pensum) ✨ - Android 版 Windows 风格任务管理器 `GPL-3.0`
* [ProcessLens](https://github.com/Dreamucxe/ProcessLens) - 使用 Shizuku 获取 ADB 级 CPU、内存、线程、唤醒锁和分应用电池读数的进程观察器。 `MIT`
* [ReAppzuku](https://github.com/gree1d/ReAppzuku) - 控制和管理后台应用。shappky 的分支 `GPL-3.0`
* [Recents](https://github.com/tymwitko/Recents) - 不依赖启动器的系统最近任务菜单替代品，通过 Shizuku 支持结束应用 `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - 监控 Android 设备上运行的服务 `MIT` [(源代码)](https://github.com/biplobsd/running_services_monitor)
* [RvSystem Monitor](https://github.com/Rve27/RvSystem-Monitor) - 高性能系统监视器（Compose + Rust），通过 Shizuku 提供 CPU 和硬件洞察 `GPL-3.0`
* [shappky](https://github.com/YasserNull/shappky) ✨ - 通过停止后台应用来提升性能的简单应用。 `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - 适用于 Android 的任务管理器。结束进程需要 root 权限。 `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 适用于 Shizuku 支持的 Android 设备的本地 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新设计了 aShell 应用程序。 `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - 适用于 Android 的终端、SSH、VNC、RDP、SFTP 和云存储客户端 `AGPL-3.0` [(源代码)](https://github.com/GlassHaven/Haven)

> [!NOTE]
> Using [rish](pages/RISH_cn.md), 您可以使用任何终端模拟器（例如 Termux）创建本地 ADB shell。

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一个用于切换“息屏显示（Always on Display）”的 Android 快捷设置 `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [carrier-ims-for-pixel](https://github.com/ryfineZ/carrier-ims-for-pixel) - 持续维护的 Pixel IMS 工具包：通过 Shizuku 调整 VoLTE/VoWiFi/VoNR、5G 图标显示和运营商配置 `Apache-2.0`
* [hilight-studio](https://github.com/DhananjayBhosale/hilight-studio) - Pixel 11 HiLight LED 控制器，可自定义通知和状态灯效果 `MIT`
* [Pixel-IMS-5G](https://github.com/barrylk/Pixel-IMS-5G) - 在 Google Pixel 设备上启用 5G 独立组网（5G SA）和 VoNR `GPL-3.0`
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 通过 LG U+ 在 Pixel 6 和 7 上启用 VoLTE `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - 在 Pixel 设备上为不受支持地区的运营商启用 VoLTE `GPL-3.0`
* [Root-My-Pixel](https://github.com/alex193a/Root-My-Pixel) - 利用 CVE-2026-43499 漏洞为 Pixel 设备自动获取 root `Proprietary`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定制的小部件，可以使用 Shizuku 升级 Pixel 设备上内置的“概览”小部件 `GPL-3.0`
* [TensorIMS](https://github.com/Pixel-Tailor-CN/TensorIMS) - 适用于 Tensor Pixel 设备的 IMS 配置工具；Shizuku 可应用 VoLTE、VoWiFi、VT 和 VoNR 开关。 `Apache-2.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - 适用于 Google Pixel 设备的增强 IMS 配置工具 `Apache-2.0`
* [Video Boost AO](https://github.com/AgusRomeroL/video-boost-ao) - 在 Pixel Pro 相机上保持 Video Boost 启用，每次相机打开时重新启用。Shizuku 为按需模式授予 WRITE_SECURE_SETTINGS 权限 `MIT`

#### Samsung OneUI

* [4Zones](https://github.com/mr-biz-apps/4zones) - 在三星 DeX 和 Android 桌面模式下恢复四区域窗口平铺，支持点击吸附和键盘快捷键 `Apache-2.0`
* [android-battery-health](https://github.com/willbilec/android-battery-health) - 三星电池健康和循环次数查看器，通过 Shizuku 提供对屏幕阅读器友好的布局。 `Proprietary`
* [duo-fold-live](https://github.com/joeconsorti/duo-fold-live) - Live hinge-driven iPhone-Duo fold animation for Galaxy Z Fold 8 with windowed glass, live cover previews and smooth display handoff, reading the true hinge angle via Shizuku. `MIT`
* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 免 root 字体安装器 `GPL-3.0` [(源代码)](https://codeberg.org/dryerlint/fontsmanager)
* [galaxy-auto-brightness-offset](https://github.com/fullmetalsonic/galaxy-auto-brightness-offset) - Samsung Galaxy adaptive-brightness offset for screens that feel too dark or too bright, including under privacy films: applies a fixed correction to the auto-brightness curve via Shizuku. `Proprietary`
* [pearity](https://github.com/thejaustin/pearity) - 逐项将三星 One UI 系统设置匹配为 iOS 默认值（Android/自定义/iOS 三种状态），并通过 Shizuku 或 root 写入安全设置。 `Proprietary`
* [Root-My-Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy) - 使用 CVE-2026-43499 为受支持的三星 Galaxy 固件安装 KSU `Apache-2.0`
* [SamsungRegionOverride](https://github.com/Ritel-T/SamsungRegionOverride) - 临时更改 Galaxy Store 及其他区域锁定应用所见的 SIM 地区，无需 root，一键恢复 `MIT`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - 在三星设备电池温度达到特定值时启用或禁用快速充电模式  `Proprietary`
* [ScamsungFonts](https://github.com/KhunHtetzNaing/ScamsungFonts) - 通过系统 shell 或 Root 为三星 Galaxy（OneUI）管理字体 `No license`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - 在 CSC 设置为强制快门声的特定国家/地区的三星设备上禁用相机快门声 `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 权限提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 运行 OneUI 5 的非 root 设备上的系统用户访问 (UID 1000)。使用 Shizuku 实现自动化 `LGPL-2.1`
* [ZFold-Multi-DPI](https://github.com/balamurugan15/ZFold-Multi-DPI) - 为三星 Galaxy Z Fold 设备的外屏和内屏应用独立的屏幕缩放和 DPI 预设 `Proprietary`

#### MIUI

* [Aura](https://github.com/tgvdufuture/Aura) - 适用于 POCO X8 Pro 的自定义 RGB 通知 LED 应用，支持按应用、联系人和群组设置颜色和动画 `MIT`
* [CodecTweaker](https://github.com/Halo0sama/CodecTweaker) - Bluetooth codec fix for Xiaomi HyperOS: restores each earphone's chosen codec and bitrate after A2DP reconnects using Shizuku plus accessibility UI automation. `GPL-3.0`
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) `Paid` 💰 - HyperOS/MIUI 5G快捷开关 `GPL-3.0` [(源代码)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本关闭 MIUI 广告 `Apache-2.0`
* [HyperOS FCM Fix](https://github.com/dingwen07/hyperos-fcm-fix) - 在 HyperOS 上保持 Google Play 服务不受限制，确保 FCM 推送通知准时送达 `GPL-3.0`
* [HyperOS-MTZ-Studio](https://github.com/GloriousApps/HyperOS-MTZ-Studio/blob/main/readme_en.md) - 面向小米 HyperOS 的 MTZ 主题工作区；可导入、组合、翻译和应用主题，使用 Shizuku 或 Shevery 以免 root 方式应用主题。 `Proprietary`
* [HyperOS3ScrollSetter](https://github.com/BlizzardAn225/HyperOS3ScrollSetter) - 在 HyperOS 3/4 上恢复滚动壁纸并禁用强制变暗，通过 Shizuku.newProcess 或 root 模块应用安全设置并重启相关进程。 `GPL-3.0`
* [HyperOSUnfcker](https://github.com/Enki013/hyperosunfcker) - 解锁 HyperOS/MIUI 设备上隐藏的性能、显示、内存、电池和视觉设置 `LGPL-3.0`
* [IslandRecorder](https://github.com/wxxsfxyzm/IslandRecorder) - 面向小米设备的屏幕录制器，支持超级岛控制 `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - Mix Flip 外屏一键配置：使用任意应用并将系统应用恢复为默认样式 `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 节奏游戏中启用 3 键导航  `Proprietary`

#### Other

* [BooxUltimatum](https://github.com/huuunleashed/BooxUltimatum) - Open-source suite for BOOX E Ink tablets: high-contrast home, sleep screens, instant pen ink, battery log and reversible tweaks, using Shizuku for privileged tweak tiers. `GPL-3.0`
* [buttonoo](https://github.com/bractstudio/buttonoo) - 将 Nothing 的 Essential 键重新映射为任意按压模式；Shizuku 启用特权输入通道。 `GPL-3.0`
* [Calibrate-SoC](https://github.com/mayusi/Calibrate-SoC) - 面向 Android 游戏掌机的 SoC 调优、监控和基准测试套件，具备目标寻优型频率策略和实时 HUD。 `Apache-2.0`
* [DiAuto](https://github.com/shihabal3amri/DiAuto) - Wireless and USB Android Auto receiver for BYD DiLink head units; runs entirely on the car display and uses Shizuku or root for privileged setup. No phone companion app or dongle. `AGPL-3.0`
* [Evolve_Launcher_v2](https://github.com/JarJarBlinkz/Evolve_Launcher_v2) - 适用于 Meta Quest 头显的可定制桌面启动器，具备应用整理、游戏时长跟踪和由 Shizuku 支持的清除数据/缓存操作。 `Proprietary`
* [flipx](https://github.com/jlgrimes/flipx) - 根据 Anbernic RG Rotate 的转轴状态将主页键路由到不同的启动器 `Proprietary`
* [GlyphBarty](https://github.com/Link2011-Act2/GlyphBarty) - 适用于 Nothing Phone 的可定制 Glyph 可视化工具，支持音乐同步、快捷设置开关和充电状态显示 `MIT`
* [Heimdall-AYN-Thor-Assistant](https://github.com/mastercook777/Heimdall-AYN-Thor-Assistant) - 适用于 AYN Thor 的下屏游戏助手，具备配置档案、宏、触控、地图和由 Shizuku 驱动的触摸注入。 `Apache-2.0`
* [MindControl](https://github.com/Dinico414/MindControl) - 适用于 iKKO MindOne 的硬件按键重映射和息屏显示工具包，通过 Shizuku getevent 监控物理按键，并支持 root 回退。 `Proprietary`
* [panel-assistant](https://github.com/panel-assistant/android) - Home Assistant 墙面板仪表板，具备实体过滤、MQTT 设备控制，以及由 Shizuku/root 支持的配置和经校验的安装流程。 `Apache-2.0`
* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control 可精确控制 Nothing Phone (3) 的录制指示灯 `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - 适用于 Nubia Red Magic 手机的全局肩键 `MIT`
* [Thor SidePad](https://github.com/bentolanh/thor-sidepad) - 将 AYN Thor 下屏变为虚拟手柄；Shizuku 将其按压注入为原生手柄输入。 `MIT`
* [thor-pathfinder](https://github.com/KaitonGxx/thor-pathfinder) - AYN Thor dual-screen companion: swaps running apps between screens and maps button/combo shortcuts per game profile, using Shizuku to move windows to the other display. `GPL-3.0`
* [thor-wayfinder](https://github.com/Thor-Wayfinder/thor-wayfinder) - 通过返回键手势在 AYN Thor 的两块屏幕之间移动应用 `CC-BY-NC-ND-4.0`
* [Thors-Lightning](https://github.com/HughesTechNZ/Thors-Lightning) - 适用于 AYN Thor 的手柄驱动双屏亮度控制，可选 Shizuku 特权级输入（宏）录制。 `MIT`
* [ThorVolumeLink](https://github.com/pth2000/ThorVolumeLink) - AYN Thor 双屏的同步音量控制 `MIT`

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

* [Porter API](https://github.com/d4rken-org/porter-api) - Porter（持续维护的 Shizuku 分支）的 Android SDK，提供兼容的 Shizuku API 和直接的 Porter 支持 `MIT`
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的开发人员文档，包括示例 `Apache-2.0`
* [Shizuku-API-Flutter-Plugin](https://github.com/runoob-coder/shizuku-api-flutter-plugin) - 一个用于对接 Shizuku API 的 Flutter 插件。 `MIT`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - 适用于 Flutter 应用的 Shizuku API 绑定 `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android 上对协程友好、Kotlin 优先的软件包安装器扩展，支持 Shizuku `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常规文件系统后端的文件操作库 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - 兼容 Shizuku 的 Xamarin android/data 访问 - AIDL 库 `MIT`


### System

* [droid-mcp](https://github.com/stixez/droid-mcp) - Android SDK，为本地 LLM/AI 应用提供设备上手机数据的结构化访问，并通过 Shizuku 实现 shell 级控制 `Apache-2.0`
* [libterm](https://github.com/niki914/libterm) - Kotlin 优先的 Android 终端会话库，在单一 API 后提供 User、Root、Shizuku 和 SSH 后端 `Proprietary`
* [Priv Kit](https://github.com/priv-kit/priv-kit) - 轻量级特权运行时库，可在自己的应用中实现 Root、ADB 或 Shizuku 支持的 Binder 访问 `Proprietary`

--------------------

## Miscellaneous content

### Command-line utilities

* [AndroSH](https://github.com/ahmed-alnassif/AndroSH) - 适用于 Android 的专业多发行版 Linux 环境。可运行 Archlinux、Fedora、Alpine、Debian、Ubuntu、Kali、Void、Manjaro 和 Chimera，并与 Android 系统完全集成 `GPL-3.0`

### Flows for [Automate](https://llamalab.com/automate/)

* [Better Shizuku Starter](https://llamalab.com/automate/community/flows/50863) - 使用 *免费* 版 Automate，在关键事件发生时通过无线调试检查并自动启动 Shizuku **13.6**。 `MIT`
* [Shizuku Keeper](https://llamalab.com/automate/community/flows/51118) - 使用 Automate *Premium*，通过 USB 调试让 Shizuku **13.6** 或 **ADB** 无需 root、Wi-Fi 或线缆即可不间断运行。 `MIT`
  * [Shizuku Keeper Lite](https://llamalab.com/automate/community/flows/51012) - 使用 *免费* 版 Automate，定期检查 Shizuku **13.6** 并在需要时通过无线调试自动重启它。 `MIT`
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

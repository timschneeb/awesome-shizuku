# awesome-shizuku

### 语言
[English](/README.md) | 简体中文 | [繁體中文](/README_tw.md)

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允许普通应用程序在非root 设备上使用 ADB 直接使用权限提升的系统 API。本列表汇集了一些已知可利用 Shizuku 功能的应用程序。

更多详情：https://shizuku.rikka.app/

欢迎拉取请求。有关提示，请参阅 [贡献](CONTRIBUTING.md)。

> [!NOTE]
> 如需获取本列表的最新动态，[你可以查看每日更新日志](https://github.com/timschneeb/changelog-awesome-shizuku)。

--------------------


## 目录

- [Apps](#apps)
  - [AI agents](#ai-agents)
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

### AI agents

* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - Automates actions on your device using the AutoGLM vision language model `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - The most powerful AI agent and AI chat software on Android. Can run commands using Shizuku `LGPL-3.0`
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - Automation and Multitasking Framework using AutoGLM. Can create virtual screens that agents can run apps on and use multi-window `Apache 2.0`


### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - An F-Droid client designed for Android TVs `GPL-3.0` [(源代码)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer designed for Android TVs `GPL-3.0` [(源代码)](https://github.com/mlm-games/fluffy)


### Audio

* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - 针对非 root Android 设备的系统级 JamesDSP 音频处理引擎的实现 `GPL-3.0` [(源代码)](https://github.com/timschneeb/RootlessJamesDSP)
* [MicUp](https://github.com/papergray/MicUp) ✨ - Real-time microphone audio processing for Android `MIT`
* [PrecisEQ](https://play.google.com/store/apps/details?id=com.yokodev.preciseqpro) `IAP` `15-minute trial` 💰 - 在系统全局使用空间音频、耳机校准和参数均衡器。 `Proprietary`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - Control each app's volume independently `GPL-2.0`

### Automation

* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - JavaScript-based automation tool `MPL-2.0`
* [Geto](https://github.com/JackEblan/Geto) - Automatically change device settings when a specific app is launched. `GPL-3.0`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可针对特定生活环境自动或一键配置设备 `Apache-2.0`
* [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) `Ads` `IAP` 💰 - 适用于 Android 设备的自动化应用程序。版本 5.46 及更高版本引入了 Shizuku 支持。 `Proprietary`
* [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) `Paid` 💰 - Automation app for Android devices. Version 6.6 and later introduce Shizuku support. `Proprietary`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Helper app for Tasker `Propietary`
* [UbikiTouch](https://play.google.com/store/apps/details?id=eu.toneiv.ubktouch) `IAP` 💰 - 为您喜爱的应用程序添加功能，只需一个手势即可访问。轻扫屏幕的一侧边缘，即可显示一个可定制的菜单，其中显示了您最喜欢的操作。 `Proprietary`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord modding tool `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - A simple app for automatically launching Bluesky links in your preferred Bluesky client `MIT` [(源代码)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - Send and receive files over Bluetooth `MIT` [(源代码)](https://github.com/kmod-midori/CatShare)
* [Kettu](https://github.com/C0C0B01/Kettu) - Discord modding tool. Continuation of the abandoned Bunny-Manager project `BSD-3-Clause`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 这是一款简单的应用程序，可在您喜欢的 Lemmy 客户端中自动启动 lemmy 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 这是一个简单的应用程序，可在您喜欢的 Mastodon 客户端中自动启动 fediverse 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord modding tool. Another continuation of the abandoned Bunny-Manager project `OSL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 让您通过短信浏览网页的应用程序 `GPL-3.0`

### Customization

* [AAAD](https://github.com/shmykelsa/AAAD) `IAP` 💰 - 下载流行的 Android Auto 第三方应用程序并安装到 Android Auto 上 `Proprietary`
* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - Smart dark mode based on ambient light `GPL-3.0` [(源代码)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 将 Now Playing 从 Pixels 移植到其他 Android 设备 `GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) - 一款小巧的 Android 应用程序，可让你安排暗模式的开启/关闭时间 `MIT` [(源代码)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - 使用指定应用程序时自动切换免打扰的简单工具 `AGPL-3.0` [(源代码)](https://github.com/dic1911/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - Manage automatic rotation of different screens on Android phones `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一个非常简单的应用程序，用于更改未 root 的 Android 设备上的运营商名称 `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - 修改设备 Material You 颜色的应用程序 `GPL-3.0`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - Customize animation speeds on a more fine-grained level `GPL-3.0` [(源代码)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ](https://github.com/KieronQuinn/DarQ) ✨ - DarQ 为 Android 10 及更高版本提供了每个应用程序可选择的强制黑暗选项 `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - Some Android app widgets and live wallpapers `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - Highly customizable, gestures based Android launcher focused on speed and efficiency `GPL-3.0` [(源代码)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - Tiling window manager, Samsung DEX replacement, popup app launcher `Proprietary`
* [essentials](https://github.com/sameerasw/essentials) ✨ - Essential tools, mods and workarounds for Pixels. Also compatible with other devices `MIT`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - 在智能手机的 Android 操作系统上添加类似桌面的多窗口支持。 `GPL-3.0`
* [gama](https://github.com/palincat/gama) - Can switch between OpenGL and Vulkan renderers by setting the `debug.hwui.renderer` system property `MIT`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - Launcher for dual-screen gaming devices. Uses Shizuku to map on of the touch screens to controller inputs `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允许用户选择单独的应用语言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - 使用 Material3 恢复 Android <12 Url-App 链接选择器  `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - Display widgets on the lockscreen. Shizuku is only required on Android 13 and later `MIT` [(源代码)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始设备制造商（小米）不允许您在设备的本地设置中添加额外的（或 "不支持的"）语言，那么这款简单的应用程序就能帮您实现这一功能。  `MIT`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - A keyboard-first Android command palette that unifies app/device search, and system utilities into an overlay `GPL-3.0`
* [SetEdit: Settings Editor](https://play.google.com/store/apps/details?id=com.netvor.settings.database.editor) - View and edit settings from the system, global, and secure tables `Proprietary`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - Create launcher shortcuts for shell commands `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易于使用的工具，超越Android系统允许的控制级别 `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 插件 `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 查看和修改 Android 设备上的隐藏设置 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - 将设备背面的双击功能从 Android 12 移植到任何 Android 7.0+ 设备 `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - Clean up tracking from sharing links. Supports custom URL rewrite rules `GPL-3.0` [(源代码)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用开始菜单访问应用程序可以解锁其他功能 `Apache-2.0` [(源代码)](https://github.com/farmerbb/Taskbar)
* [UbikiTouch](https://play.google.com/store/apps/details?id=eu.toneiv.ubktouch) `IAP` 💰 - 为您喜爱的应用程序添加功能，只需一个手势即可访问。轻扫屏幕的一侧边缘，即可显示一个可定制的菜单，其中显示了您最喜欢的操作。 `Propietary`
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU and battery widgets `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - A full desktop experience layer for Android `GPL-3.0`
* [zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2) `Ads` `IAP` 💰 - 表情符号和字体更换器 `Proprietary`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 删除已为用户注册账户的应用程序的软件包名称. `Proprietary`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - 检测 Treble、GSI、Mainline、APEX、system-as-root(SAR)、A/B 等。 `Apache-2.0` [(源代码)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) IDE for JVM development. Uses Shizuku for an embedded shell - 用于 JVM 开发的 IDE。使用 Shizuku 作为嵌入式 shell`GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity) - 电流活动监视器 `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - Backup/restore private app data of debuggable apps using Shizuku `GPL-3.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一个简单的应用程序，旨在帮助用户通过 DSU 的 Android 功能轻松安装 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修复了 HostProfile 应用程序和 WorkProfile/DualApp/MultiApp 之间的 MediaStore 和文件 IO 兼容性问题。 `Proprietary`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - FPS viewer overlay with graph `Proprietary`
* [get_event](https://github.com/lalakii/get_event) - 读取/dev/input/event*  `Proprietary`
* [KeyAttestation](https://github.com/vvb2060/KeyAttestation) - Supports generating, saving, loading, parsing and verifying Android key and ID attestation data. `Proprietary`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用于查看设备上的应用程序中使用的库的应用程序。使用 Shizuku 确定其他应用程序的安装源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - 另一个适用于 Android 的 logcat 阅读器  `GPL-3.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - Utilizes Shizuku to call AppOps APIs for fine-grained app permission control `MIT`
* [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) `Ads` `IAP` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root。 `Proprietary`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root. `GPL-3.0` [(源代码)](https://github.com/zacharee/RootActivityLauncher)
* [TakoStats](https://play.google.com/store/apps/details?id=rikka.fpsmonitor) `IAP` 💰 - FPS 和性能叠加，提供详细的实时系统信息 `Proprietary`
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - 用于切换无线调试的小部件和快速设置图块（与 KDE Con​​nect 集成） `GPL-3.0`

### Device owner (DPM)

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 启发的应用程序，允许将 DeviceOwner 权限共享给第三方应用程序 `GPL-3.0`
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用设备所有者权限管理您的设备 `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - Fork of OwnDroid with added features `GPL-3.0`

### Display management
* [AG Displays](https://play.google.com/store/apps/details?id=com.htl.agdisplays) `Ads` - Launch other apps on external displays (TV/Monitor) or desktop mode on virtual displays while the phone screen can be used for other purposes or turned off `Proprietary`
* [ConnectScreen](https://connect-screen.com/) - Launch single apps to display in fullscreen on external displays, supporting both USB 2.0 (via DisplayLink dock) and USB 3.0 mobile phones. Can control the external display with a touch screen, USB devices or Bluetooth controller (even if you are USB 2.0 and using a DisplayLink dock). Can use the primary screen of the mobile as a virtual touchpad to control external display. Can rotate the screen for applications like TikTok `GPL-3.0` [(源代码)](https://gitee.com/connect-screen/connect-screen)
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - Turns your phone into a touchpad and keyboard for a single app running on a wired external display `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可折叠设备上的各种显示屏折叠状态之间切换 `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - Keep your phone mostly monochrome, but allow apps like camera to be in color `GPL-3.0`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - 为 Android 设备提供更好的屏幕镜像 `Apache-2.0` [(源代码)](https://github.com/farmerbb/SecondScreen)

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork 具有动画支持和使用 Shizuku 的插件管理。 `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - Export videos downloaded from the Android version of Bilibili `GPL-3.0` [(源代码)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - Merge and export BiliBili cache files into MP4, supports mobile and computer client  `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 进行插件管理的漫画阅读器。立读的独立继承者。 `Apache-2.0`
  * Mihon/Tachiyomi 还有其他几个活跃的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [AirData UAV](https://play.google.com/store/apps/details?id=com.airdata.uav.app) - 无人机飞行分析和机队管理平台 [access to /Android/Data](https://app.airdata.com/wiki/Help/Granting+Permissions+in+Android+13+and+14) `Proprietary`
* [File Manager Plus](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager)  `Ads` `IAP` 💰 - Can manage your files and folders, whether on local device, NAS storage (via sftp, ftp, webdav or smb) or in the cloud (e.g. Google Drive). Supports Shizuku for Android/data, Android/obb and partly /. `Proprietary`
* [FV File Manager](https://play.google.com/store/apps/details?id=com.folderv.file) - 文件管理器 [access Android/data and Android/obb](https://folderv.com/2023/11/24/access-Android-data-and-Android-obb-on-Android-14/) `Proprietary`
* [MiXplorer](https://xdaforums.com/t/app-2-2-mixplorer-v6-x-released-fully-featured-file-manager.1523691/#post-23109280) - 文件管理器，可以批量安装 APK 并使用 Shizuku 访问 Android/数据和 obb `Proprietary`
  * [MiXplorer Silver](https://play.google.com/store/apps/details?id=com.mixplorer.silver) - MiXplorer 付费 Google Play 版本 `Proprietary`
* [MT Manager](https://mt2.cn) - 分屏文件管理器。可以使用 Shizuku 安装 APK 并访问 Android/data 和 Android/obb `Proprietary`
* [NMM File Manager / Text Edit](https://play.google.com/store/apps/details?id=in.mfile) - 文件管理器和内置文本编辑器 `Proprietary`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE是Android最彻底的清理工具 `GPL-3.0` [(源代码)](https://github.com/d4rken-org/sdmaid-se)
* [Solid Explorer](https://play.google.com/store/apps/details?id=pl.solidexplorer2) `Ads` `IAP` 💰 - File explorer `Proprietary`
* [SwiftBackup](https://play.google.com/store/apps/details?id=org.swiftapps.swiftbackup) `IAP` 💰 - Swift Backup 可在几分钟内备份重要数据 `Proprietary`
* [Total Commander](https://play.google.com/store/apps/details?id=com.ghisler.android.TotalCommander) - Android port of the desktop Total Commander app (Version 3.60 beta or later) `Proprietary`
* [X-Plore](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore) `Ads` `IAP` 💰 - 可使用 Shizuku 访问 Android/数据和 obb 的文件管理器 `Proprietary`
* [ZArchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) - 归档管理程序。支持使用 Root/Shizuku 编辑文件。 `Proprietary`

### Games

* [Ascent](https://github.com/4o3F/Ascent) - A tool for retrieving gacha history links from Mihoyo games  `AGPL-3.0`
* [blocktopograph](https://github.com/Blocktopograph/Blocktopograph) - Blocktopograph 是 MCBE 的应用程序服务器，它包括一个用于本地世界的世界、NBT 编辑器 `Apache-2.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - Browndust II Mod manager `Proprietary`
* [CloudSync-Mobile](https://github.com/FawazTakahji/CloudSync-Mobile) - An app that allows you to sync your Stardew Valley saves across multiple devices `GPL-3.0`
* [HandheldExp](https://github.com/Teppichseite/HandheldExp) - Android 上 EmulationStation (ES-DE) 的游戏菜单中  `MIT`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - 管理“洛杉矶犯罪”游戏的地图、壁纸和屏幕截图 `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 游戏“Last Origin”的 Mod 管理器 `Proprietary`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - Genshin Impact Auto-Conversation Clicker `MIT`
* [stalker](https://github.com/onerdna/stalker) - Save data viewer & editor for Shadow Fight 2 `GPL-3.0`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - Companion app for localizing the Android version of CHAOS;CHILD visual novel `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 轻松导入和共享 Polyfield 地图 `GPL-3.0`
* [PGT: GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool.free) `Ads` - PUBG 的其他设置 `Proprietary`
  * [PGT+: Pro GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool) `Paid` 💰 - PUBG 的其他设置 `Proprietary`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order游戏翻译项目 `MIT`

### Input methods

* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - 触摸时显示自定义的点击 `GPL-3.0`
* [Auto Cursor](https://play.google.com/store/apps/details?id=eu.toneiv.cursor) `IAP` 💰 - 通过屏幕边缘的指针，单手即可轻松使用大型智能手机。 `Proprietary`
* [C9](https://github.com/austinauyeung/C9) - Efficient grid-based cursor provided alongside a traditional cursor. Shizuku is only required on Android 11. `Apache-2.0`
* [andRemote2](https://github.com/c0dev0id/andRemote2) - Emulates the DMD Remote 2 for map apps `Properietary`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - 一款 Android 应用程序，可改变您设备上按钮的功能！ `GPL-3.0` [(源代码)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - Play games using mouse and keyboard on Android device; keymapper for games `Apache-2.0`
* [Panda Gamepad Pro](https://play.google.com/store/apps/details?id=com.panda.gamepad) `Paid` `IAP` 💰 - 游戏键盘映射器 `Proprietary`
* [pastiera](https://github.com/palsoftware/pastiera) - Android keyboard specialized for Physical Keyboard Devices. Uses Shizuku for trackpad gestures `GPL-3.0`
* [RealMouse](https://play.google.com/store/apps/details?id=com.redlee90.realmouse) - 使用虚拟触摸板控制鼠标。专为辅助显示器而设计。 `Proprietary`
* [TitanPad](https://github.com/sztupy/TitanPad) - Converts the Titan2's Physical Keyboard's capacitive input into mouse and scroll gestures. Uses Shizuku for reading the trackpad input and setting up virtual HID devices `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 适用于 Android x86 的键盘映射器  `GPL-3.0`


### Installer & app stores

* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - Google Play 商店的开源替代品，具有隐私性和现代设计 `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - 轻松下载、安装和共享模组 `Proprietary`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：隐私友好浏览器的更新程序 `GPL-3.0` [(源代码)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F‑Droid Client `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - App store for GitHub releases with discovery function `Apache-2.0` [(源代码)](https://github.com/OpenHub-Store/GitHub-Store)
* [instafel](https://github.com/mamiiblt/instafel) - Updater app for Instafel, an Instagram mod `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - 现代且实用的 Android 应用安装程序替代品 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 简单的应用程序使用 Shizuku 在设备上安装带有高级选项的 APK `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 存储库的非官方客户端 `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - An F-Droid client with modern UI and an arsenal of extra features `GPL-3.0` [(源代码)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接从源获取 Android 应用程序更新 `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允许覆盖包请求者和执行者的包安装程序 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 拆分 APK 安装程序 `GPL-3.0` [(源代码)](https://github.com/Aefyr/SAI)
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - A lightweight app installer replacement with split APK support `Apache-2.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - App store for modded apps `GPL-3.0`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - GUI for Android's builtin `dex2oat` utility, allowing DEX code of installed apps to be re-optimized `Apache-2.0`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - Find the reason why the alarm icon is active in the status bar `Properietary`
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - Android utility to make notifications persistent/undismissable using Shizuku `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - Automatically close selected apps when you exit them to save power and memory `Apache-2.0`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - Exploits CVE-2024-31317 for Zygote injection, integrating remote terminal and file transfer capabilities `MIT`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一个简单的应用程序，用于通过 WearOS 手表控制 Android 设备 `Apache-2.0` [(源代码)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - Remote control your device via Telegram messages `BSD 3-Clause`


### Network

* [ADNS](https://github.com/eyalm2000/adns) - DNS-based ad blocker for Android `MIT`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上读取手机信号塔信息 `MIT` [(源代码)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - App firewall without using an VPN; can also manage packages `MIT`
* [delta](https://github.com/supershadoe/delta) - 使用 Shizuku 的热点管理器 `BSD-3-Clause`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - An app that allows you to turn on your hotspot remotely via Bluetooth - think Apple Continuity, but for everyone `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Google FindMyDevice 服务的安全和开源替代方案 `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - Dual-mode firewall: blocks internet access using Shizuku or a standard local VPN interface or both. `MIT`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 预览和编辑/etc/hosts文件 `MIT`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一个在 Android 上运行 Naiveproxy 的简单应用程序 `MIT`
* [NetWall](https://play.google.com/store/apps/details?id=com.ysy.app.firewall) `IAP` 💰 - 不依赖本地 VPN 或 root 的应用防火墙 `Proprietary`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - 用于 4G/5G 网络模式切换的 Android 应用 `GPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - Open-source app firewall that doesn't depend on VPNs or root `GPL-3.0`
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - A persistent network speed tracker in your status bar `GPL-3.0` [(源代码)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - WireGuard 和 AmneziaWG 的 FOSS Android 客户端，支持自动隧道功能 `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - 在 Android 11 及更高版本上查看您保存的 WiFi 密码，无需 root `Proprietary` [(源代码)](https://github.com/zacharee/WiFiList)
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - Simple app using Shizuku to manage & view saved Wi-Fi passwords  `MIT`

### Patching

* [Morphe](https://morphe.software/) - User-friendly YouTube patcher based on Universal-ReVanced-Manager `GPL-3.0` [(源代码)](https://github.com/MorpheApp/morphe-manager)
* [LSPatch](https://github.com/JingMatrix/LSPatch) - 从 LSPod 扩展的非根 Xposed 框架 `GPL-3.0`
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - ReVanced patcher that has extra features the official manager doesn't have  `GPL-3.0`

### Power management

* [BatStats](https://github.com/mlm-games/BatStats) - Battery monitor with stats via Shizuku `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - 一个简单的应用程序，可在 Android 14 及更高版本上显示电池状态信息。 `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - Open source app to visually change battery data via Shizuku `GPL-3.0`
* [FDE.AI](https://github.com/feravolt/FDE.AI-docs/releases) `IAP` 💰 - All-in-One optimizer for Android `Proprietary`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - Enable Doze mode immediately after screen off and turn off motion sensing to get best battery life `GPL-3.0` [(源代码)](https://github.com/farfromrefug/EnforceDoze)
* [Extinguish](https://play.google.com/store/apps/details?id=own.moderpach.extinguish) - 熄灭关闭屏幕，但保持设备唤醒状态 `Proprietary`
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - A fire-and-forget program to stop Android apps from running in the background `GPL-3.0` [(源代码)](https://github.com/adil192/no_more_background)
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - Advanced reboot menu with Shizuku support `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 关闭 Android 屏幕而不进入待机/睡眠模式 `Proprietary`
* [zukulock](https://github.com/tiendnm/zukulock) - Very lightweight app that locks the screen when launched. Helps reduce wear on the power button `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一键隐藏您的私人文件和 Android 应用程序。 `Apache-2.0` [(源代码)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - An application designed to silently protect user data from powerful adversaries `GPL-3.0`
* [AppLock](https://github.com/aload0/AppLock) ✨ - MIUI 12+ 防止应用被侧滑或一键清理杀死 `MIT`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - Manage your device privacy based on lock/unlock state `MIT` [(源代码)](https://github.com/dorumrr/privacyflip)

### Productivity

* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - Digital Detoxing: Use your phone rather than letting your phone use you `GPL-3.0`
* [digipaws](https://f-droid.org/packages/nethical.digipaws/) ✨ - Tool to reduce screen addiction by regulating app usage through a gamified experience `GPL-3.0` [(源代码)](https://github.com/nethical6/digipaws)

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一个用于切换“息屏显示（Always on Display）”的 Android 快捷设置 `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本上带回独立的 Wi-Fi 和移动数据磁贴，并提供更好的统一网络磁贴 `GPL-3.0` [(源代码)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - Provides quick settings tile and shortcuts to turn off the display without locking the screen or stopping foreground running apps `MIT` [(源代码)](https://github.com/UlyssesZh/DisplayToggle)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 通过快捷设置启用/禁用设备传感器 `Apache-2.0`
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 用于切换当前私有 DNS 服务器的快捷设置磁贴  `MIT`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - 用于开启或关闭私有 DNS 设置的快捷磁贴  `GPL-3.0` [(源代码)](https://github.com/flashsphere/private-dns-qs)
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - 提供用于切换 USB 调试和切换私有 DNS 主机的快捷磁贴 `GPL-3.0` [(源代码)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [Ultimate Settings](https://play.google.com/store/apps/details?id=com.precisebytes.androidtoggles.free.release) `Ads` - 可从小部件/应用/通知/锁屏通知直接切换 Wi-Fi、蓝牙、移动网络、飞行模式、GPS、NFC、Wi-Fi/蓝牙/USB 网络共享热点、屏幕亮度、屏幕自动旋转、LED 灯、铃声模式。 `Proprietary`
* [Ultimate Settings PRO](https://play.google.com/store/apps/details?id=com.precisebytes.androidtoggles.pro.release) `Paid` 💰 - 可从小部件/应用/通知/锁屏通知直接切换 Wi-Fi、蓝牙、移动网络、飞行模式、GPS、NFC、Wi-Fi/蓝牙/USB 网络共享热点、屏幕亮度、屏幕自动旋转、LED 灯、铃声模式。 `Proprietary`

### Software management

* [AppControlX](https://github.com/risunCode/AppControl-X) - Freeze, force stop, uninstall apps, change background optimization and more `GPL-3.0`
* [AppDash](https://play.google.com/store/apps/details?id=flar2.appdashboard) `7-day trial` `Paid` 💰 - 一个应用程序管理器，可以轻松管理设备上安装的 APK 和应用程序 `Proprietary`
* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 - 无需root即可管理应用程序权限 `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - 启用/禁用 Android 组件，例如活动、服务、接收器和提供者 `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - An app manager focusing on permission management `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - 无需root即可卸载任何应用程序 `LGPL-3.0` [(源代码)](https://github.com/samolego/Canta)
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 应用程序可禁用未使用的应用程序，同时仍允许方便地访问它们 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 通过手动或半自动冻结蹩脚软件来提高设备的速度和电池寿命 `Apache-2.0` [(源代码)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - 冻结、隐藏或禁用任何应用程序。创建并组织可一键冻结的应用程序组。 `GPL-3.0` [(源代码)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - 使用 Shizuku 冻结或隐藏应用程序 `Proprietary`
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - 适用于 root 和非 root 设备的 Android 应用程序管理器 `GPL-3.0` [(源代码)](https://github.com/Hamza417/Inure)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Island 完整的 FLOSS 分叉 `Apache-2.0` [(源代码)](https://gitlab.com/secure-system/Insular)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔离和克隆应用程序以保护隐私和并行运行 `Apache-2.0` [(源代码)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - 管理您的 Magisk 模块存储库 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能强大的应用程序，可管理系统和用户应用程序 `GPL-3.0` [(源代码)](https://github.com/SmartPack/PackageManager)
* [Package Name Scripter](https://play.google.com/store/apps/details?id=in.ms.packagenamesscripter) - Manage installed apps using Shizuku or create ADB scripts to enable, disable, uninstall, reinstall, or run other app-related ADB commands. `Proprietary`
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - App manager with freeze and install capabilities. `GPL-3.0`  [(源代码)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 检查 Android 应用程序、Magisk 模块等的更新！ `GPL-3.0` [(源代码)](https://github.com/DUpdateSystem/UpgradeAll)

### Task manager

* [Pensum](https://github.com/troikoss/Pensum) ✨ - Windows-style Task Manager for Android `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - Monitor running services on your Android device `MIT` [(源代码)](https://github.com/biplobsd/running_services_monitor)
* [shappky](https://github.com/YasserNull/shappky) ✨ - A simple app to boost performance by stopping background apps. `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - A Task Manager for Android. Killing processes requires root access. `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 适用于 Shizuku 支持的 Android 设备的本地 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新设计了 aShell 应用程序。 `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - Terminal, SSH, VNC, RDP, SFTP & cloud storage client for Android `AGPL-3.0`
* [ReTerminal](https://github.com/RohitKushvaha01/ReTerminal) ✨ - Sleek, Material 3-inspired terminal emulator based on Termux's robust TerminalView `MIT`
* [ShizuShell](https://play.google.com/store/apps/details?id=com.noxinfinity.shell) - 使用 Shizuku 的 ADB shell `Proprietary`


> [!NOTE]
> Using [rish](pages/RISH_cn.md), 您可以使用任何终端模拟器（例如 Termux）创建本地 ADB shell。

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一个用于切换“息屏显示（Always on Display）”的 Android 快捷设置 `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 通过 LG U+ 在 Pixel 6 和 7 上启用 VoLTE `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定制的小部件，可以使用 Shizuku 升级 Pixel 设备上内置的“概览”小部件 `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - Enable VoLTE for carriers in unsupported regions on Pixel devices `GPL-3.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - Enhanced IMS Configuration Tool for Google Pixel devices `Apache-2.0`

#### Samsung OneUI

* [Galaxy MaxHz](https://github.com/tribalfs/GalaxyMaxHzPub) `IAP` 💰 - Refresh Rate Mods, Screen-off Mods, QS Tiles, Tasker Support and More  `Proprietary`
* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 rootless font installer `GPL-3.0` [(源代码)](https://codeberg.org/dryerlint/fontsmanager)
* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - 适用于 Samsung OneUI 设备的自定义系统范围主题引擎 `Proprietary`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - Enable or disable fast charging mode on Samsung devices when the battery temperature reaches a certain point  `Proprietary`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - Disable the forced camera shutter sounds on Samsung devices that have their CSC set to certain countries with this restriction `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 权限提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 运行 OneUI 5 的非 root 设备上的系统用户访问 (UID 1000)。使用 Shizuku 实现自动化 `LGPL-2.1`

#### MIUI

* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - HyperOS/MIUI 5G快捷开关 `GPL-3.0` [(源代码)](https://github.com/ysy950803/FiveGSwitcher)
* [FpsSwitcher](https://play.google.com/store/apps/details?id=com.ysy.fpsswitcher) `Paid` 💰 - HyperOS/MIUI 刷新率快捷开关 `Proprietary`
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本关闭 MIUI 广告 `Apache-2.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - One-click configuration for Mix Flip's outer screen: Use any apps and restore system apps to default style `GPL-3.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - 在 MIUI 上以自由格式显示大多数应用程序 `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 节奏游戏中启用 3 键导航  `Proprietary`

#### Other

* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control gives precise control over the Nothing Phone (3)'s recording light `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - System-wide shoulder triggers for Nubia Red Magic phones `MIT`

### Unlisted apps
为了保持主列表干净，所有不满足特定要求的应用程序都存储在单独的页面上： [ARCHIVED.md](pages/ARCHIVED.md)

我还使用自动爬虫来搜索新项目，并在 GitHub 和多个 F-Droid 存储库中使用 Shizuku。您可以在此处查看当前自动生成的爬网报告：[TODO.md](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的开发人员文档，包括示例 `Apache-2.0`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - Shizuku API bindings for Flutter apps `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android Coroutines-friendly Kotlin-first Package Installer extensions with Shizuku support `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常规文件系统后端的文件操作库 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - 使用 Shizuku API 安装 Android APK 的 Flutter 插件 `MIT`

### System
* [ServiceManagerCompat](https://github.com/SanmerApps/ServiceManagerCompat) - ServiceManager bindings `MIT`

--------------------

## Miscellaneous content

### Command-line utilities

* [AndroSH](https://github.com/ahmed-alnassif/AndroSH) - Professional Multi-Distribution Linux Environments for Android. Run Archlinux, Fedora, Alpine, Debian, Ubuntu, Kali, Void, Manjaro & Chimera with full Android system integration `GPL-3.0`

### Flows for [Automate](https://llamalab.com/automate/)

* [Better Shizuku Starter](https://llamalab.com/automate/community/flows/50863) - Check and automatically start Shizuku **13.6** on key events via wireless debugging with the *free* version of Automate.
* [Shizuku Keeper](https://llamalab.com/automate/community/flows/51118) - Continuously run Shizuku **13.6** or **ADB** uninterrupted without root, Wi-Fi, or cables via USB debugging with Automate *Premium.*
  * [Shizuku Keeper Lite](https://llamalab.com/automate/community/flows/51012) - Check Shizuku **13.6** at regular intervals and automatically restart it via wireless debugging with the *free* version of Automate.
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

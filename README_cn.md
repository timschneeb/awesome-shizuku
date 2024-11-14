# awesome-shizuku

> [!IMPORTANT]
> 由于一些原因(不方便透露)，我不得不停止为该项目提供简体中文翻译的工作 除他人接手继续提供翻译
> 
> 中文文档可能落后于英文文档，如果有问题请先查看英文文档。


### 语言
[English](/README.md) | 简体中文

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允许普通应用程序在非root 设备上使用 ADB 直接使用权限提升的系统 API。本列表汇集了一些已知可利用 Shizuku 功能的应用程序。

更多详情：https://shizuku.rikka.app/

欢迎拉取请求。有关提示，请参阅 [贡献](CONTRIBUTING.md)。

--------------------


## 目录

- [Apps](#apps)
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
  - [Power management](#power-management)
  - [Software management](#software-management)
  - [Terminals](#terminals)
  - [Vendor-specific](#vendor-specific)
    - [Google Pixel](#google-pixel)
    - [Samsung OneUI](#samsung-oneui)
    - [MIUI](#miui)
  - [Unlisted apps](#unlisted-apps)
- [Development libraries](#development-libraries)
  - [Core](#core)
  - [Filesystem](#filesystem)
  - [Power](#power)
- [Rish shell](#rish-shell)
- [Annotations](#annotations)
- [License](#license)

--------------------

## Apps


### Audio

* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - 针对非 root Android 设备的系统级 JamesDSP 音频处理引擎的实现 `GPL-3.0` [(源代码)](https://github.com/ThePBone/RootlessJamesDSP)

### Automation

* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可针对特定生活环境自动或一键配置设备 `Apache-2.0`
* [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) `Ads` `IAP` 💰 - 适用于 Android 设备的自动化应用程序。版本 5.46 及更高版本引入了 Shizuku 支持。`Proprietary`
* [UbikiTouch](https://play.google.com/store/apps/details?id=eu.toneiv.ubktouch) `IAP` 💰 - 为您喜爱的应用程序添加功能，只需一个手势即可访问。轻扫屏幕的一侧边缘，即可显示一个可定制的菜单，其中显示了您最喜欢的操作。 `Proprietary`

### Communication

* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 这是一款简单的应用程序，可在您喜欢的 Lemmy 客户端中自动启动 lemmy 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 这是一个简单的应用程序，可在您喜欢的 Mastodon 客户端中自动启动 fediverse 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 让您通过短信浏览网页的应用程序 `GPL-3.0`
* [Bunny-Manager](https://github.com/pyoncord/BunnyManager) - Discord Bunny Mod 的补丁管理器 `OSL-3.0`


### Customization

* [AAAD](https://github.com/shmykelsa/AAAD) `IAP` 💰 - 下载流行的 Android Auto 第三方应用程序并安装到 Android Auto 上 `Proprietary`
* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - Android 快速设置可切换“始终显示” `MIT` [(源代码)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 将 Now Playing 从 Pixels 移植到其他 Android 设备 `GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) - 一款小巧的 Android 应用程序，可让你安排暗模式的开启/关闭时间`。MIT` [(源代码)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) -使用指定应用程序时自动切换免打扰的简单工具 `AGPL-3.0` [(源代码)](https://github.com/dic1911/android_AutoDND)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本中恢复 Wi-Fi 和移动数据磁贴，以及更统一的互联网磁贴 `GPL-3.0` [(源代码)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
  * [Better Internet Tiles Libre](https://github.com/D3SOX/Better-Network-Tiles-Libre) - Better Internet Tiles 的 Libre 分支，无需专有库 `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一个非常简单的应用程序，用于更改未 root 的 Android 设备上的运营商名称 `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr)- 修改设备 Material You 颜色的应用程序 `GPL-3.0`
* [DarQ](https://github.com/KieronQuinn/DarQ) - DarQ 为 Android 10 及更高版本提供了每个应用程序可选择的强制黑暗选项 `Apache-2.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid)- 在智能手机的 Android 操作系统上添加类似桌面的多窗口支持。`No license`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允许用户选择单独的应用语言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/1fexd/LinkSheet) - 使用 Material3 恢复 Android <12 Url-App 链接选择器  `Modified MPL-2.0`
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始设备制造商（小米）不允许您在设备的本地设置中添加额外的（或 "不支持的"）语言，那么这款简单的应用程序就能帮您实现这一功能。  `MIT`
* [NoPopping](https://play.google.com/store/apps/details?id=rikka.nopeeking) `IAP` 💰 - 自动免打扰模式 `Proprietary`
* [Repainter](https://play.google.com/store/apps/details?id=dev.kdrag0n.dyntheme) `IAP` 💰 - 在设备上安装自定义 Material You 设计 `Proprietary`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易于使用的工具，超越Android系统允许的控制级别`No license`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 插件 `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 查看和修改 Android 设备上的隐藏设置 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) - 将设备背面的双击功能从 Android 12 移植到任何 Android 7.0+ 设备 `GPL-3.0`
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用开始菜单访问应用程序可以解锁其他功能 `Apache-2.0` [(源代码)](https://github.com/farmerbb/Taskbar)
* [zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2) `Ads` `IAP` 💰 - 表情符号和字体更换器 `Proprietary`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 删除已为用户注册账户的应用程序的软件包名称. `No license`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - 检测 Treble、GSI、Mainline、APEX、system-as-root(SAR)、A/B 等。 `Apache-2.0` [(源代码)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) 用于 JVM 开发的 IDE。使用 Shizuku 作为嵌入式 shell - `GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity) - 电流活动监视器 `GPL-3.0`
* [get_event](https://github.com/lalakii/get_event)- 读取/dev/input/event*  `No license`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用于查看设备上的应用程序中使用的库的应用程序。使用 Shizuku 确定其他应用程序的安装源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) - 另一个适用于 Android 的 logcat 阅读器  `GPL-3.0`
* [Logra](https://github.com/wingio/Logra) - 适用于 Android 的 Material You logcat 查看器 `GPL-2.0` 
* [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) `Ads` `IAP` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root。 `Proprietary`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher&hl=en&gl=US) `Paid` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root. `Proprietary` [(源代码)](https://github.com/zacharee/RootActivityLauncher)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 通过快速设置启用/禁用设备传感器 `Apache-2.0`
* [TakoStats](https://play.google.com/store/apps/details?id=rikka.fpsmonitor) `IAP` 💰 - FPS 和性能叠加，提供详细的实时系统信息 `Proprietary`
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) 用于切换无线调试的小部件和快速设置图块（与 KDE Con​​nect 集成） - `GPL-3.0`

### Device owner (DPM)

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 启发的应用程序，允许将 DeviceOwner 权限共享给第三方应用程序 `GPL-3.0`
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用设备所有者权限管理您的设备 `GPL-3.0`

### Display management
* [Android-Screener](https://github.com/jiesou/Android-Screener) - 轻松调整屏幕分辨率和帧频的工具 `MIT`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可折叠设备上的各种显示屏折叠状态之间切换 `Apache-2.0`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) -为 Android 设备提供更好的屏幕镜像 `Apache-2.0` [(源代码)](https://github.com/farmerbb/SecondScreen)

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi)- Tachiyomi fork 具有动画支持和使用 Shizuku 的插件管理。 `Apache-2.0`
* [BilibiliCacheVideoMerge](https://github.com/molihuan/BilibiliCacheVideoMerge) - 将BiliBili视频缓存文件导出为MP4 `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 进行插件管理的漫画阅读器。立读的独立继承者。 `Apache-2.0`
  * Mihon/Tachiyomi 还有其他几个活跃的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [AirData UAV](https://play.google.com/store/apps/details?id=com.airdata.uav.app) - 无人机飞行分析和机队管理平台 [access to /Android/Data](https://app.airdata.com/wiki/Help/Granting+Permissions+in+Android+13+and+14) `Proprietary`
* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一键隐藏您的私人文件和 Android 应用程序。`Apache-2.0` [(源代码)](https://github.com/deltazefiro/Amarok-Hider)
* [EDS Full - Encrypted Data Store Full](https://sovworks.com/eds/index.php) `Paid` 💰 - 适用于 Android 的虚拟磁盘加密软件，允许您将文件存储在加密容器中。适用于 root 和非 root 的广泛而丰富的功能，此处无法列出（请参阅站点）。通过 Android 意图进行 Shizuku 控制（请参阅常见问题解答）。 `Proprietary`
  * [EDS Lite - Encrypted Data Store Lite](https://sovworks.com/eds/index.php) - EDS 完整版的免费版本。功能有限但仍然强大。非 root 和 root 功能。仅适用于非安装模式（有关说明，请参阅站点）。 `GPL-2.0` [(源代码)](https://github.com/sovworks/edslite)
* [FV File Manager](https://play.google.com/store/apps/details?id=com.folderv.file) - 文件管理器 [access Android/data and Android/obb](https://folderv.com/2023/11/24/access-Android-data-and-Android-obb-on-Android-14/) `Proprietary`
* [MiXplorer](https://xdaforums.com/t/app-2-2-mixplorer-v6-x-released-fully-featured-file-manager.1523691/#post-23109280) - 文件管理器，可以批量安装 APK 并使用 Shizuku 访问 Android/数据和 obb`Proprietary`
  * [MiXplorer Silver](https://play.google.com/store/apps/details?id=com.mixplorer.silver) - MiXplorer 付费 Google Play 版本 `Proprietary`
* [MT Manager](https://mt2.cn) - 分屏文件管理器。可以使用 Shizuku 安装 APK 并访问 Android/data 和 Android/obb `Proprietary`
* [NMM File Manager / Text Edit](https://play.google.com/store/apps/details?id=in.mfile) - 文件管理器和内置文本编辑器 `Proprietary`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) - SD Maid 2/SE是Android最彻底的清理工具 `GPL-3.0` [(源代码)](https://github.com/d4rken-org/sdmaid-se)
* [SwiftBackup](https://play.google.com/store/apps/details?id=org.swiftapps.swiftbackup) `IAP` 💰 - Swift Backup 可在几分钟内备份重要数据 `Proprietary`
* [X-Plore](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore) `Paid` 💰- 可使用 Shizuku 访问 Android/数据和 obb 的文件管理器 `Proprietary`
* [ZArchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) - 归档管理程序。支持使用 Root/Shizuku 编辑文件。 `Proprietary`

### Games

* [90 FPS + 120 FPS & IPAD VIEW](https://play.google.com/store/apps/details?id=tq.tech.Fps) `Ads` -在 PUBG 中实现高 FPS `Proprietary`
* [blocktopograph](https://github.com/NguyenDuck/blocktopograph) - Blocktopograph 是 MCBE 的应用程序服务器，它包括一个用于本地世界的世界、NBT 编辑器`AGPL-3.0`
* [HandheldExp](https://github.com/Teppichseite/HandheldExp) - Android 上 EmulationStation (ES-DE) 的游戏菜单中 `MIT`
* [lac-tool](https://github.com/aliernfrog/lac-tool)- 管理“洛杉矶犯罪”游戏的地图、壁纸和屏幕截图 `MIT`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 游戏“Last Origin”的 Mod 管理器 `No license`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 轻松导入和共享 Polyfield 地图 `MIT`
* [PGT: GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool.free) `Ads` - PUBG 的其他设置 `Proprietary`
  * [PGT+: Pro GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool) `Paid` 💰 - PUBG 的其他设置 `Proprietary`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order游戏翻译项目 `CC BY-NC-SA 4.0`

### Input methods

* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - 触摸时显示自定义的点击 `GPL-3.0`
* [Auto Cursor](https://play.google.com/store/apps/details?id=eu.toneiv.cursor) `IAP` 💰 - 通过屏幕边缘的指针，单手即可轻松使用大型智能手机。`Proprietary`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)- 一款 Android 应用程序，可改变您设备上按钮的功能！ `GPL-3.0` [(源代码)](https://github.com/keymapperorg/KeyMapper)
* [Panda Gamepad Pro](https://play.google.com/store/apps/details?id=com.panda.gamepad) `Paid` `IAP` 💰 - 游戏键盘映射器 `Proprietary`
* [RealMouse](https://play.google.com/store/apps/details?id=com.redlee90.realmouse) - 使用虚拟触摸板控制鼠标。专为辅助显示器而设计。 `Proprietary`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 适用于 Android x86 的键盘映射器  `GPL-3.0`


### Installer & app stores

* [AuroraStore](https://f-droid.org/en/packages/com.aurora.store/) - Google Play 商店的开源替代品，具有隐私性和现代设计 `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub)- 轻松下载、安装和共享模组 `No license`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/Droid-ify/client)
* [fdroid_shizuku_privileged_extension](https://depau.github.io/fdroid_shizuku_privileged_extension/fdroid/repo/) - 与 Shizuku 协同工作的 F-Droid 权限扩展`Apache-2.0` [(源代码)](https://github.com/depau/fdroid_shizuku_privileged_extension)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：隐私友好浏览器的更新程序 `GPL-3.0` [(源代码)](https://github.com/Tobi823/ffupdater)
* [glassdown](https://github.com/Sinneida/glassdown) - APKMirror 客户端 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 简单的应用程序使用 Shizuku 在设备上安装带有高级选项的 APK `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 存储库的非官方客户端`GPL-3.0`
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接从源获取 Android 应用程序更新 `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允许覆盖包请求者和执行者的包安装程序 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 拆分 APK 安装程序 `GPL-3.0` [(源代码)](https://github.com/Aefyr/SAI)
* [skydroid](https://github.com/redsolver/skydroid) - 适用于 Android 的分散式基于域的应用程序商店 `GPL-3.0`

### Miscellaneous

* [Anywhere](https://github.com/zhaobozhen/Anywhere-/) - 活动和 shell 快捷方式文件夹 `Apache-2.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一个简单的应用程序，旨在帮助用户通过 DSU 的 Android 功能轻松安装 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修复了 HostProfile 应用程序和 WorkProfile/DualApp/MultiApp 之间的 MediaStore 和文件 IO 兼容性问题。 `No license`
* [LSPatch](https://github.com/LSPosed/LSPatch)- 从 LSPod 扩展的非根 Xposed 框架`GPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一个简单的应用程序，用于通过 WearOS 手表控制 Android 设备 `Apache-2.0` [(源代码)](https://github.com/SimpleAppProjects/SimpleWear)

### Network

* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上读取手机信号塔信息`MIT` [(源代码)](https://github.com/zacharee/CellReader)
* [FindMyDevice](https://gitlab.com/Nulide/findmydevice) - Google FindMyDevice 服务的安全和开源替代方案。 `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 预览和编辑/etc/hosts文件 `MIT`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一个在 Android 上运行 Naiveproxy 的简单应用程序`MIT`
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 快速设置图块可切换活动的私有 DNS 服务器 `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰- 在 Android 11 及更高版本上查看您保存的 WiFi 密码，无需 root `Proprietary` [(源代码)](https://github.com/zacharee/WiFiList)
* [WiFiList (FOSS)](https://github.com/jaredcat/WiFiList) - 'WiFiList' 的 FOSS 分叉  `Missing license`

### Power management

* [Batt](https://gitlab.com/narektor/batt) - 一个简单的应用程序，可在 Android 14 及更高版本上显示电池状态信息。 `GPL-3.0`
* [Extinguish](https://play.google.com/store/apps/details?id=own.moderpach.extinguish) - 熄灭关闭屏幕，但保持设备唤醒状态 `Proprietary`
* [rebootmenu](https://github.com/ryuunoakaihitomi/rebootmenu)- 使用快捷方式锁定屏幕或打开电源菜单。如果您的电源按钮坏了，这很有用。 `MIT`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 关闭 Android 屏幕而不进入待机/睡眠模式 `Proprietary`

### Software management

* [AppDash](https://play.google.com/store/apps/details?id=flar2.appdashboard) `IAP` 💰 - 一个应用程序管理器，可以轻松管理设备上安装的 APK 和应用程序 `Proprietary`
* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 - 无需root即可管理应用程序权限 `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - 启用/禁用 Android 组件，例如活动、服务、接收器和提供者 `Apache-2.0`
* [Canta](https://github.com/samolego/Canta)- 无需root即可卸载任何应用程序 `LGPL-3.0`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 应用程序可禁用未使用的应用程序，同时仍允许方便地访问它们 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 通过手动或半自动冻结蹩脚软件来提高设备的速度和电池寿命`Apache-2.0` [(源代码)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) 冻结、隐藏或禁用任何应用程序。创建并组织可一键冻结的应用程序组。 - `GPL-3.0` [(源代码)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - 使用 Shizuku 冻结或隐藏应用程序 `Proprietary`
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `Paid` 💰 - 适用于 root 和非 root 设备的 Android 应用程序管理器 `GPL-3.0` [(源代码)](https://github.com/Hamza417/Inure)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/)- Island 完整的 FLOSS 分叉 `Apache-2.0` [(源代码)](https://gitlab.com/secure-system/Insular)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔离和克隆应用程序以保护隐私和并行运行 `Apache-2.0` [(源代码)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一应用程序和工作流程启动器 `MIT`
* [MMRL](https://github.com/DerGoogler/MMRL) `Root` - 管理您的 Magisk 模块存储库 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能强大的应用程序，可管理系统和用户应用程序 `GPL-3.0` [(源代码)](https://github.com/SmartPack/PackageManager)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 检查 Android 应用程序、Magisk 模块等的更新！ `GPL-3.0` [(源代码)](https://github.com/DUpdateSystem/UpgradeAll)

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 适用于 Shizuku 支持的 Android 设备的本地 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新设计了 aShell 应用程序。 `GPL-3.0`
* [ShizuShell](https://play.google.com/store/apps/details?id=com.noxinfinity.shell) - 使用 Shizuku 的 ADB shell `Proprietary`


> [!NOTE]
> Using [rish](#rish-shell), 您可以使用任何终端模拟器（例如 Termux）创建本地 ADB shell。

### Vendor-specific

#### Google Pixel
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 通过 LG U+ 在 Pixel 6 和 7 上启用 VoLTE `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定制的小部件，可以使用 Shizuku 升级 Pixel 设备上内置的“概览”小部件`GPL-3.0`

#### Samsung OneUI

* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - 适用于 Samsung OneUI 设备的自定义系统范围主题引擎 `Proprietary` 
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 权限提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 运行 OneUI 5 的非 root 设备上的系统用户访问 (UID 1000)。使用 Shizuku 实现自动化`LGPL-2.1`

#### MIUI

* [AppLock](https://github.com/Mufanc/AppLock) - MIUI 12+ 防止应用被侧滑或一键清理杀死 `GPL-3.0` 
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - MIUI 5G快捷开关 `GPL-3.0` - [(源代码)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本关闭 MIUI 广告 `Apache-2.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - 在 MIUI 上以自由格式显示大多数应用程序 `GPL-3.0`
  * [Flyme-FreeForm](https://github.com/Live-Block/Flyme-FreeForm)- Mi-FreeForm 的分叉 `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 节奏游戏中启用 3 键导航  `No license`

### Unlisted apps
为了保持主列表干净，所有不满足特定要求的应用程序都存储在单独的页面上： [UNLISTED.md](pages/UNLISTED.md)

我还使用自动爬虫来搜索新项目，并在 GitHub 和多个 F-Droid 存储库中使用 Shizuku。您可以在此处查看当前自动生成的爬网报告：[TODO.md](pages/TODO.md).


--------------------

## Development libraries

### Core

* [Shizuku](https://github.com/RikkaApps/Shizuku) - Shizuku系统服务器、API和应用程序 `Apache-2.0` 
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的开发人员文档，包括示例 `Apache-2.0` 

### Filesystem
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常规文件系统后端的文件操作库 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - 使用 Shizuku API 安装 Android APK 的 Flutter 插件 `MIT`

### Power

* [PowerAct](https://github.com/ryuunoakaihitomi/PowerAct) - 一个 Android 库，只需几行代码即可操纵与电源相关的操作`Apache-2.0`


--------------------

## Rish shell

`rish` 是一个 Android 可执行文件（不是应用程序），用于与在高权限守护进程上运行的 shell 进行交互。
例如，如果 Shizuku 是使用 ADB 权限启动的，那么 `rish` 还将提供一个维护 ADB 权限的 shell。

要设置 `rish`，请打开 Shizuku，导航到 "在终端应用程序中使用 Shizuku"，然后按照设置说明进行操作。请注意，您需要对 shell、终端和基本命令有基本的了解，才能有效地使用它。

设置好 `rish` 后，您可以在任何支持调用任何 shell 脚本或可执行文件的应用程序中使用它，即使应用程序本身不支持 Shizuku。

> [!NOTE] 
> 由于 `rish` 的位置不在 `$PATH` 中，因此可能需要指定可执行文件的路径才能手动启动它。如果它位于当前工作目录中，则使用 `./rish` 启动它。

**Syntax:**

* `rish`: 启动默认的交互式 shell（使用 /system/bin/sh）
* `rish exec /path/to/custom/shell`: 启动自定义/替代交互式 shell
* `rish -c 'whoami'`: 执行shell命令，完成后退出
* `echo 'whoami' | rish`: 从 stdin 读取 shell 命令，执行它，完成后退出

> [!NOTE]
> `whoami` 用作示例命令，并将返回当前 shell 用户的名称。

**Usage examples:**

* 直接在设备上使用 **Termux** 等终端模拟器打开交互式 ADB shell
* 使用 **Tasker** 等自动化应用程序在后台自动触发高权限 ADB shell 命令
  * 示例：命令 `rish -c 'reboot'` 将通过 shell 使用 Shizuku 重新启动设备

官方的 rish 文档可以在这里找到：https://github.com/RikkaApps/Shizuku-API/blob/master/rish/README.md

--------------------

## Annotations

- `Paid` 💰  - 付费应用程序
- `IAP` 💰 - 包含应用内购买
- `Ads`  - 包含广告
- `Proprietary`  - 缺少许可证或闭源软件
- `n-day trial` - - `n`天后需要付款
- `Root` - 需要在Root模式下运行Shizuku

--------------------

## License

本列表采用[Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 许可协议。

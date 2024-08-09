
# awesome-shizuku

> [!IMPORTANT]
> 中文文档可能落后于英文文档，如果有问题请先查看英文文档。

### 语言
[English](/README.md) | 简体中文

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允许普通应用程序在非root 设备上使用 ADB 直接使用权限提升的系统 API。本列表汇集了一些已知可利用 Shizuku 功能的应用程序。

更多详情：https://shizuku.rikka.app/

欢迎拉取请求。有关提示，请参阅 [贡献](CONTRIBUTING.md)。

--------------------


## Table of contents

- [Apps](#apps)
  - [Audio](#audio)
  - [Automation](#automation)
  - [Communication](#communication)
  - [Customization](#customization)
  - [Development utilities](#development-utilities)
  - [Entertainment](#entertainment)
  - [File management](#file-management)
  - [Installer & app stores](#installer--app-stores)
  - [Miscellaneous](#miscellaneous)
  - [Network](#network)
  - [Software management](#software-management)
  - [Vendor-specific](#vendor-specific)
    - [Google Pixel](#google-pixel)
    - [Samsung OneUI](#samsung-oneui)
    - [MIUI](#miui)
  - [Unlisted apps](#unlisted-apps)
- [Development libraries](#development-libraries)
  - [Core](#core)
  - [Filesystem](#filesystem)
  - [Power](#power)
- [Similar projects](#similar-projects)
- [Rish shell](#rish-shell)
- [Annotations](#annotations)
- [License](#license)

--------------------

## Apps


### Audio

* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - 适用于非 root Android 设备的全系统 JamesDSP 音频处理引擎的实现 `GPL-3.0` [(源代码)](https://github.com/ThePBone/RootlessJamesDSP)

### Automation

* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 允许对特定生活环境自动或一键配置设备 `Apache-2.0`
* [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) `Ads` `IAP` 💰 - 适用于Android设备的自动化应用程序。5.46 版及更高版本引入了 Shizuku 支持。 `Proprietary`

### Communication

* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 这是一款简单的应用程序，可在您喜欢的 Lemmy 客户端中自动启动 lemmy 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 这是一个简单的应用程序，可在您喜欢的 Mastodon 客户端中自动启动 fediverse 链接。 `MIT` [(源代码)](https://github.com/zacharee/MastodonRedirect)
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 让您通过短信浏览网页的应用程序`GPL-3.0`
* [Bunny-Manager](https://github.com/pyoncord/BunnyManager) - Discord Bunny Mod 的补丁管理器 `OSL-3.0`


### Customization

* [AAAD](https://github.com/shmykelsa/AAAD) `IAP` 💰 - 下载流行的 Android Auto 第 3 方应用程序并安装在 Android Auto 上 `Proprietary`
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 将 Now Playing 从 Pixels 移植到其他 Android 设备`GPL-3.0`
* [Android-Screener](https://github.com/jiesou/Android-Screener) - 轻松调整屏幕分辨率和帧频的工具`MIT`
* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - 触摸时显示定制的轻触`GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) -一款小巧的Android应用程序，让你安排暗光模式的开启/关闭`MIT` [(源代码)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - 使用指定应用程序时自动切换免打扰的简单工具`AGPL-3.0` [(源代码)](https://github.com/dic1911/android_AutoDND)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本中恢复 Wi-Fi 和移动数据磁贴，以及更统一的互联网磁贴 `GPL-3.0` [(源代码)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
  * [Better Internet Tiles Libre](https://github.com/D3SOX/Better-Network-Tiles-Libre) - Better Internet Tiles 的 Libre 分支，无需专有库 `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName)- Carrier Vanity Name 是一个非常简单的应用程序，用于更改未 root 的 Android 设备上的运营商名称 `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - 修改设备 Material You 颜色的应用程序 `GPL-3.0`
* [DarQ](https://github.com/KieronQuinn/DarQ) - DarQ 为 Android 10 及以上版本提供可按应用程序选择的强制变暗选项`Apache-2.0`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允许用户选择单独的应用程序语言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/1fexd/LinkSheet) - 使用 Material3 恢复 Android <12 Url-App-Link-Chooser `Modified MPL-2.0`
* [NoPopping](https://play.google.com/store/apps/details?id=rikka.nopeeking) `IAP` 💰- 自动免打扰模式 `Proprietary`
* [Repainter](https://play.google.com/store/apps/details?id=dev.kdrag0n.dyntheme) `IAP` 💰- 在设备上安装自定义 Material You 设计 `Proprietary`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易于使用的工具，可超越 Android 系统允许的控制水平 `No license`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) -Smartspacer 插件`GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 查看和修改 Android 设备上的隐藏设置 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap)- 将双击设备背面功能从 Android 12 移植到任何 Android 7.0+ 设备上 `GPL-3.0`
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/)- 使用开始菜单访问应用程序小雯可以解锁其他功能 `Apache-2.0` [(源代码)](https://github.com/farmerbb/Taskbar)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用设备所有者权限管理设备`GPL-3.0`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 删除已为用户注册账户的应用程序的软件包名称。 `No license`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - 检测 Treble、GSI、Mainline、APEX、system-as-root(SAR)、A/B 等。`Apache-2.0` [(源代码)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) 用于 JVM 开发的集成开发环境。使用 Shizuku 作为嵌入式外壳 - `GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity)- 当前活动监视器`GPL-3.0`
* [get_event](https://github.com/lalakii/get_event) - 读取/dev/input/event* `No license`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 一款用于查看设备上应用程序所使用库的应用程序。使用 Shizuku 来确定其他应用程序的安装源。`Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) -另一个适用于 Android 的 logcat 阅读器 `GPL-3.0`
* [Logra](https://github.com/wingio/Logra) - 适用于 Android 的 Material You logcat 查看器 `GPL-2.0` 
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher&hl=en&gl=US) `Paid` 💰 - 启动/交互（未）导出的活动、服务和接收器。支持 Shizuku 和 root。 `Proprietary` [(源代码)](https://github.com/zacharee/RootActivityLauncher)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 通过快速设置启用/禁用设备传感器 `Apache-2.0`
* [TakoStats](https://play.google.com/store/apps/details?id=rikka.fpsmonitor) `IAP` 💰- FPS 和性能叠加，提供详细的实时系统信息`Proprietary`
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch)用于切换无线调试的小部件和快速设置图块（与 KDE Con​​nect 集成）- `GPL-3.0`

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork 具有动画支持和使用 Shizuku 的插件管理。 `Apache-2.0`
* [BilibiliCacheVideoMerge](https://github.com/molihuan/BilibiliCacheVideoMerge) - 将 BiliBili 视频缓存文件导出为 MP4 `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 进行插件管理的漫画阅读器。Tachiyomi 的独立继承者. `Apache-2.0`
  * Mihon/Tachiyomi 还有其他几个活跃的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和[TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)
* [lac-tool](https://github.com/aliernfrog/lac-tool) - 管理游戏'Los Angeles Crimes'的地图、壁纸和截图  `MIT`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 游戏“Last Origin”的 Mod 管理器 'Last Origin' `No license`
* [Panda Gamepad Pro](https://play.google.com/store/apps/details?id=com.panda.gamepad) `Paid` `IAP` 💰 - 游戏键盘映射器`Proprietary`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 轻松导入和共享 Polyfield 地图 `MIT`
* [translatefgo](https://github.com/rayshift/translatefgo)- Fate/Grand Order游戏翻译项目 `CC BY-NC-SA 4.0`

### File management
* [AirData UAV](https://play.google.com/store/apps/details?id=com.airdata.uav.app) - 无人机飞行分析和机队管理平台，包括 [access to /Android/Data](https://app.airdata.com/wiki/Help/Granting+Permissions+in+Android+13+and+14) `Proprietary`
* [FV File Manager](https://play.google.com/store/apps/details?id=com.folderv.file) -文件管理器 [access Android/data and Android/obb](https://folderv.com/2023/11/24/access-Android-data-and-Android-obb-on-Android-14/) `Proprietary`
* [MiXplorer](https://xdaforums.com/t/app-2-2-mixplorer-v6-x-released-fully-featured-file-manager.1523691/#post-23109280) - 可批量安装 APK 并使用 Shizuku 访问 Android/data 和 obb 的文件管理器 `Proprietary`
* [MT Manager](https://mt2.cn) - 分屏文件管理器。可使用 Shizuku 安装 APK 并访问 Android/data和 Android/OB。 `Proprietary`
* [X-Plore](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore)- 可以使用 Shizuku 访问 Android/data 和 obb 的文件管理器 `Proprietary`
* [ZArchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) - 归档管理程序。支持使用 Root/Shizuku 编辑文件。`Proprietary`

### Installer & app stores

* [AuroraStore](https://f-droid.org/en/packages/com.aurora.store/)- Google Play 应用商店的开源替代品，具有隐私保护功能和现代化设计 `GPL-3.0` [(源代码)](https://gitlab.com/AuroraOSS/AuroraStore)
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客户端 `GPL-3.0` [(源代码)](https://github.com/Droid-ify/client)
* [fdroid_shizuku_privileged_extension](https://depau.github.io/fdroid_shizuku_privileged_extension/fdroid/repo/) - 与 Shizuku 协同工作的 F-Droid 权限扩展 `Apache-2.0` [(源代码)](https://github.com/depau/fdroid_shizuku_privileged_extension)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/)- FFUpdater：隐私友好浏览器的更新程序 `GPL-3.0` [(源代码)](https://github.com/Tobi823/ffupdater)
* [glassdown](https://github.com/Sinneida/glassdown) - APKMirror 客户端`GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 使用 Shizuku 在设备上安装带有高级选项的 APK 的简单应用程序 `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 资源库的非官方客户端 `GPL-3.0`
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接从源获取 Android 应用程序更新`GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允许覆盖软件包请求器和执行器的软件包安装程序 `MIT`
* [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) - Android 拆分 APK 安装程序 `GPL-3.0` [(源代码)](https://github.com/Aefyr/SAI)
* [skydroid](https://github.com/redsolver/skydroid) - 适用于 Android 的分散式基于域的 应用商店 `GPL-3.0`

### Miscellaneous

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一键隐藏您的私人文件和 Android 应用程序。 `Apache-2.0` [(源代码)](https://github.com/deltazefiro/Amarok-Hider)
* [Anywhere](https://github.com/zhaobozhen/Anywhere-/) - Activity 和 shell 快捷方式文件夹 `Apache-2.0`
* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 适用于搭载 Shizuku 系统的安卓设备的本地 ADB shell`GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新设计 aShell 应用程序。 `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - 这是一款简单的应用程序，可在 Android 14 及更高版本上显示电池状态信息。 `GPL-3.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 这是一个简单的应用程序，可帮助用户通过 DSU 的安卓功能轻松安装 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修复了 HostProfile 应用程序和 WorkProfile/DualApp/MultiApp 之间的 MediaStore 和文件 IO 兼容性问题。 `No license`
* [EDS Full - Encrypted Data Store Full](https://sovworks.com/eds/index.php) `Paid` 💰- 适用于 Android 的虚拟磁盘加密软件，允许您将文件存储在加密容器中。适用于 root 和非 root 的广泛而丰富的功能，此处无法列出（请参阅站点）。通过 Android 意图进行 Shizuku 控制（请参阅常见问题解答）。`Proprietary`
  * [EDS Lite - Encrypted Data Store Lite](https://sovworks.com/eds/index.php) -EDS 完整版的免费版本。功能有限但仍然强大。非 root 和 root 功能。仅适用于非安装模式（有关说明，请参阅站点）。 `GPL-2.0` [(源代码)](https://github.com/sovworks/edslite)
* [Extinguish](https://play.google.com/store/apps/details?id=own.moderpach.extinguish) - 熄灭关闭屏幕，但保持设备唤醒状态 `Proprietary`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - 一款 Android 应用程序，可改变您设备上按钮的功能！`GPL-3.0` [(源代码)](https://github.com/keymapperorg/KeyMapper)
* [LSPatch](https://github.com/LSPosed/LSPatch) - 从 LSPosed 延伸而来的非 root Xposed 框架 `GPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 在 Android 上运行 Naiveproxy 的简单应用程序`MIT`
* [RealMouse](https://play.google.com/store/apps/details?id=com.redlee90.realmouse) - 使用虚拟触摸板控制鼠标。专为辅助显示器而设计。`Proprietary`
* [rebootmenu](https://github.com/ryuunoakaihitomi/rebootmenu) - 使用快捷方式锁定屏幕或打开电源菜单。如果你的电源按钮坏了，这个功能很有用。 `MIT`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 关闭 Android 屏幕而不进入待机/睡眠模式 `Proprietary`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse)- SD Maid 2/SE是Android最彻底的清理工具`GPL-3.0` [(源代码)](https://github.com/d4rken-org/sdmaid-se)
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free)- 更好的 Android 设备屏幕镜像`Apache-2.0` [(源代码)](https://github.com/farmerbb/SecondScreen)
* [Show taps](https://play.google.com/store/apps/details?id=show.taps) `Ads` - 显示屏幕上触摸事件的位置 `Proprietary`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一个简单的应用程序，用于通过 WearOS 手表控制 Android 设备 `Apache-2.0` [(源代码)](https://github.com/SimpleAppProjects/SimpleWear)
* [SwiftBackup](https://play.google.com/store/apps/details?id=org.swiftapps.swiftbackup) `IAP` 💰 - Swift Backup 可在几分钟内备份重要数据 `Proprietary`
* [XtMapper](https://github.com/Xtr126/XtMapper)- 适用于 Android x86 的键盘映射器  `GPL-3.0`

### Network

* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上读取手机信号塔信息`MIT` [(源代码)](https://github.com/zacharee/CellReader)
* [FindMyDevice](https://gitlab.com/Nulide/findmydevice) - Google FindMyDevice 服务的安全和开源替代方案。`GPL-3.0`
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 快速设置可切换活动的私有 DNS 服务器 `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰- 无需 root 即可在 Android 11 及更高版本上查看已保存的 WiFi 密码 `Proprietary` [(源代码)](https://github.com/zacharee/WiFiList)
* [WiFiList (FOSS)](https://github.com/jaredcat/WiFiList) -WiFiList' 的 FOSS 分支 `Missing license`

### Software management

* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 -  无需 root 即可管理应用程序权限 `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - 启用/禁用 Android 组件，例如活动、服务、接收器和提供者 `Apache-2.0`
* [Canta](https://github.com/samolego/Canta) - 无需 root 即可卸载任何应用程序 `LGPL-3.0`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 应用程序可禁用未使用的应用程序，同时仍允许方便地访问它们 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 通过手动或半自动冻结软件来提高设备的速度和电池寿命 `Apache-2.0` [(源代码)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/)  -  冻结、隐藏或禁用任何应用程序。创建和组织可一键冻结的应用程序组。  - `GPL-3.0` [(源代码)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - 使用 Shizuku 冻结或隐藏应用程序`Proprietary`
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `Paid` 💰 - 适用于 root 和非 root 设备的 Android 应用程序管理器 `GPL-3.0` [(源代码)](https://github.com/Hamza417/Inure)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Island 完整的 FLOSS 分叉 `Apache-2.0` [(源代码)](https://gitlab.com/secure-system/Insular)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) -隔离和克隆应用程序，以保护隐私并实现并行运行 `Apache-2.0` [(源代码)](https://github.com/oasisfeng/island)
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能强大的应用程序，可同时管理系统和用户应用程序`GPL-3.0` [(源代码)](https://github.com/SmartPack/PackageManager)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 检查 Android 应用程序、Magisk 模块等的更新！ `GPL-3.0` [(源代码)](https://github.com/DUpdateSystem/UpgradeAll)

### Vendor-specific

#### Google Pixel
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 通过 LG U+ 在 Pixel 6 和 7 上启用 VoLTE `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定制的小部件，可以使用 Shizuku 升级 Pixel 设备上内置的“概览”小部件 `GPL-3.0`

#### Samsung OneUI

* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - 为三星 OneUI 设备定制全系统主题引擎 `Proprietary` 
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 权限升级漏洞 [(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 在运行至 OneUI 5 的非root 设备上实现系统用户访问（UID 1000）。 使用 Shizuku 实现自动化 `LGPL-2.1`

#### MIUI

* [AppLock](https://github.com/Mufanc/AppLock) - 在 MIUI 12+ 上防止通过侧滑或一键清理杀死应用程序  `GPL-3.0` 
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - MIUI 的 5G 快捷开关`GPL-3.0` - [(源代码)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最小的成本关闭MIUI广告`Apache-2.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - 在 MIUI 上以自由形式显示大多数应用程序 `GPL-3.0`
  * [Flyme-FreeForm](https://github.com/Live-Block/Flyme-FreeForm) - Mi-FreeForm 的分叉 `GPL-3.0`


### Unlisted apps
为了保持主列表干净，所有不满足特定要求的应用程序都存储在单独的页面上： [UNLISTED.md](pages/UNLISTED.md)

我还使用自动爬虫来搜索新项目，并在 GitHub 和多个 F-Droid 存储库中使用 Shizuku。您可以在此处查看当前自动生成的爬网报告： [TODO.md](pages/TODO.md).


--------------------

## Development libraries

### Core

* [Shizuku](https://github.com/RikkaApps/Shizuku) - Shizuku 系统服务器、API 和应用程序 `Apache-2.0` 
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的开发人员文档，包括示例 `Apache-2.0` 

### Filesystem
* [LintFile](https://github.com/lumkit/LintFile) - 带有 Shizuku、root 和常规文件系统后端的文件操作库 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - 从 Xamarin 访问与 Shizuku 兼容的 Android/数据 - AIDL 库`MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - 使用 Shizuku API 安装 Android APK 的 Flutter 插件 `MIT`

### Power

* [PowerAct](https://github.com/ryuunoakaihitomi/PowerAct) - 一个 Android 库，只需几行代码即可操纵与电源相关的操作 `Apache-2.0`

--------------------

## Similar projects

* [Dhizuku](https://github.com/iamr0s/Dhizuku)- 受 Shizuku 启发的应用程序，可与第三方应用程序共享 DeviceOwner 权限 `GPL-3.0`

--------------------

## Rish shell

`rish` 是一个 Android 可执行文件（不是应用程序），用于与运行在高权限守护进程上的 `shell` 进行交互。例如，如果 Shizuku 是使用 ADB 权限启动的，那么 rish 也将提供一个保持 ADB 权限的 shell。

要设置 `rish`，请打开 Shizuku，导航到 "在终端应用程序中使用 Shizuku"，然后按照设置说明进行操作。请注意，您需要对 shell、终端和基本命令有基本的了解，才能有效地使用它。

设置好 `rish` 后，您可以将它与任何支持调用任何 shell 脚本或可执行文件的应用程序一起使用，即使应用程序本身不支持 Shizuku。

> [!NOTE] 
> 由于 `rish` 的位置不在 `$PATH` 中，因此您可能需要指定可执行文件的路径才能手动启动它。如果它位于您当前的工作目录中，请使用“./rish”启动它。

**Syntax:**

* `rish`：启动默认的交互式 shell（使用 /system/bin/sh）
* `rish exec /path/to/custom/shell`：启动自定义/替代交互式 shell
* `rish -c 'whoami'`：执行 shell 命令，完成后退出
* `echo 'whoami' | rish`：从 stdin 读取 shell 命令，执行并在完成后退出

> [!NOTE] 
> 以 `whoami` 为例，它将返回当前 shell 用户的名称。

**Usage examples:**

* 使用终端模拟器（如**Termux**）直接在设备上打开交互式 ADB shell
* 使用自动化应用程序（如**Tasker**）在后台自动触发高权限 ADB shell 命令
  * 示例：命令 `rish -c 'reboot'` 将通过 shell 使用 Shizuku 重启设备

这里有 rish 的官方文档： https://github.com/RikkaApps/Shizuku-API/blob/master/rish/README.md

--------------------

## Annotations

- `Paid` 💰 - 付费申请
- `IAP` 💰 - 包含应用内购买
- `Ads` - 包含广告
- `Proprietary` - 许可证缺失或闭源软件
- `n-day trial` - 要求在 `n` 天后付款

--------------------

## License

此列表遵循 [Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 许可证。

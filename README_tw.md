# awesome-shizuku

### 語言
[English](/README.md) | [简体中文](/README_cn.md) | 繁體中文

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允許普通應用程式在非root 裝置上使用 ADB 直接使用許可權提升的系統 API。本列表彙集了一些已知可利用 Shizuku 功能的應用程式。

更多詳情：https://shizuku.rikka.app/

歡迎拉取請求。有關提示，請參閱 [貢獻](CONTRIBUTING.md)。

> [!NOTE]
> 若要掌握此列表的最新動態，[你可以查看每日更新日誌](https://github.com/timschneeb/changelog-awesome-shizuku)。

--------------------


## 目錄

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

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - An F-Droid client designed for Android TVs `GPL-3.0` [(原始碼)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer designed for Android TVs `GPL-3.0` [(原始碼)](https://github.com/mlm-games/fluffy)


### Audio

* [MicUp](https://github.com/papergray/MicUp) ✨ - Real-time microphone audio processing for Android `MIT`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - 針對非 root Android 裝置的系統級 JamesDSP 音訊處理引擎的實現 `GPL-3.0` [(原始碼)](https://github.com/timschneeb/RootlessJamesDSP)
* [PrecisEQ](https://play.google.com/store/apps/details?id=com.yokodev.preciseqpro) `IAP` `15-minute trial` 💰 - 在系統全域使用空間音訊、耳機校準與參數均衡器。 `Proprietary`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - Control each app's volume independently `GPL-2.0`

### Automation

* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - JavaScript-based automation tool `MPL-2.0`
* [Geto](https://github.com/JackEblan/Geto) - Automatically change device settings when a specific app is launched. `GPL-3.0`
* [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) `Ads` `IAP` 💰 - 適用於 Android 裝置的自動化應用程式。版本 5.46 及更高版本引入了 Shizuku 支援。 `Proprietary`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可針對特定生活環境自動或一鍵配置裝置 `Apache-2.0`
* [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) `Paid` 💰 - Automation app for Android devices. Version 6.6 and later introduce Shizuku support. `Proprietary`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Helper app for Tasker `Propietary`
* [UbikiTouch](https://play.google.com/store/apps/details?id=eu.toneiv.ubktouch) `IAP` 💰 - 為您喜愛的應用程式新增功能，只需一個手勢即可訪問。輕掃螢幕的一側邊緣，即可顯示一個可定製的選單，其中顯示了您最喜歡的操作。 `Proprietary`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord modding tool `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - A simple app for automatically launching Bluesky links in your preferred Bluesky client `MIT` [(原始碼)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - Send and receive files over Bluetooth `MIT` [(原始碼)](https://github.com/kmod-midori/CatShare)
* [Kettu](https://github.com/C0C0B01/Kettu) - Discord modding tool. Continuation of the abandoned Bunny-Manager project `BSD-3-Clause`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 這是一款簡單的應用程式，可在您喜歡的 Lemmy 客戶端中自動啟動 lemmy 連結。 `MIT` [(原始碼)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 這是一個簡單的應用程式，可在您喜歡的 Mastodon 客戶端中自動啟動 fediverse 連結。 `MIT` [(原始碼)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord modding tool. Another continuation of the abandoned Bunny-Manager project `OSL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 讓您透過簡訊瀏覽網頁的應用程式 `GPL-3.0`

### Customization

* [AAAD](https://github.com/shmykelsa/AAAD) `IAP` 💰 - 下載流行的 Android Auto 第三方應用程式並安裝到 Android Auto 上 `Proprietary`
* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - Smart dark mode based on ambient light `GPL-3.0` [(原始碼)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 將 Now Playing 從 Pixels 移植到其他 Android 裝置 `GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) - 一款小巧的 Android 應用程式，可讓你安排暗模式的開啟/關閉時間 `MIT` [(原始碼)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - 使用指定應用程式時自動切換免打擾的簡單工具 `AGPL-3.0` [(原始碼)](https://github.com/dic1911/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - Manage automatic rotation of different screens on Android phones `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一個非常簡單的應用程式，用於更改未 root 的 Android 裝置上的電信公司名稱 `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - 修改裝置 Material You 顏色的應用程式 `GPL-3.0`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - Customize animation speeds on a more fine-grained level `GPL-3.0` [(原始碼)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ](https://github.com/KieronQuinn/DarQ) ✨ - DarQ 為 Android 10 及更高版本提供了每個應用程式可選擇的強制黑暗選項 `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - Some Android app widgets and live wallpapers `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - Highly customizable, gestures based Android launcher focused on speed and efficiency `GPL-3.0` [(原始碼)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - Tiling window manager, Samsung DEX replacement, popup app launcher `Proprietary`
* [essentials](https://github.com/sameerasw/essentials) ✨ - Essential tools, mods and workarounds for Pixels. Also compatible with other devices `MIT`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - 在智慧手機的 Android 作業系統上新增類似桌面的多視窗支援。 `GPL-3.0`
* [gama](https://github.com/palincat/gama) - Can switch between OpenGL and Vulkan renderers by setting the `debug.hwui.renderer` system property `MIT`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - Launcher for dual-screen gaming devices. Uses Shizuku to map on of the touch screens to controller inputs `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允許使用者選擇單獨的應用語言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - 使用 Material3 恢復 Android <12 Url-App 連結選擇器  `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - Display widgets on the lockscreen. Shizuku is only required on Android 13 and later `MIT` [(原始碼)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始裝置製造商（小米）不允許您在裝置的本地設定中新增額外的（或 "不支援的"）語言，那麼這款簡單的應用程式就能幫您實現這一功能。  `MIT`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - A keyboard-first Android command palette that unifies app/device search, and system utilities into an overlay `GPL-3.0`
* [SetEdit: Settings Editor](https://play.google.com/store/apps/details?id=com.netvor.settings.database.editor) - View and edit settings from the system, global, and secure tables `Proprietary`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - Create launcher shortcuts for shell commands `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易於使用的工具，超越Android系統允許的控制級別 `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 外掛 `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 檢視和修改 Android 裝置上的隱藏設定 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - 將裝置背面的雙擊功能從 Android 12 移植到任何 Android 7.0+ 裝置 `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - Clean up tracking from sharing links. Supports custom URL rewrite rules `GPL-3.0` [(原始碼)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用開始選單訪問應用程式可以解鎖其他功能 `Apache-2.0` [(原始碼)](https://github.com/farmerbb/Taskbar)
* [UbikiTouch](https://play.google.com/store/apps/details?id=eu.toneiv.ubktouch) `IAP` 💰 - 為您喜愛的應用程式新增功能，只需一個手勢即可訪問。輕掃螢幕的一側邊緣，即可顯示一個可定製的選單，其中顯示了您最喜歡的操作。 `Propietary`
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU and battery widgets `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - A full desktop experience layer for Android `GPL-3.0`
* [zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2) `Ads` `IAP` 💰 - 表情符號和字型更換器 `Proprietary`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 刪除已為使用者註冊帳號的應用程式的軟體包名稱. `Proprietary`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - 檢測 Treble、GSI、Mainline、APEX、system-as-root(SAR)、A/B 等。 `Apache-2.0` [(原始碼)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) - IDE for JVM development. Uses Shizuku for an embedded shell - 用於 JVM 開發的 IDE。使用 Shizuku 作為嵌入式 shell `GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity) - 電流活動監視器 `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - Backup/restore private app data of debuggable apps using Shizuku `GPL-3.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一個簡單的應用程式，旨在幫助使用者透過 DSU 的 Android 功能輕鬆安裝 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修復了 HostProfile 應用程式和 WorkProfile/DualApp/MultiApp 之間的 MediaStore 和檔案 IO 相容性問題。 `Proprietary`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - FPS viewer overlay with graph `Proprietary`
* [get_event](https://github.com/lalakii/get_event) - 讀取/dev/input/event*  `Proprietary`
* [KeyAttestation](https://github.com/vvb2060/KeyAttestation) - Supports generating, saving, loading, parsing and verifying Android key and ID attestation data. `Proprietary`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用於檢視裝置上的應用程式中使用的庫的應用程式。使用 Shizuku 確定其他應用程式的安裝源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - 另一個適用於 Android 的 logcat 閱讀器  `GPL-3.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - Utilizes Shizuku to call AppOps APIs for fine-grained app permission control `MIT`
* [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) `Ads` `IAP` 💰 - 啟動/互動（未）匯出的活動、服務和接收器。支援 Shizuku 和 root。 `Proprietary`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - 啟動/互動（未）匯出的活動、服務和接收器。支援 Shizuku 和 root. `GPL-3.0` [(原始碼)](https://github.com/zacharee/RootActivityLauncher)
* [TakoStats](https://play.google.com/store/apps/details?id=rikka.fpsmonitor) `IAP` 💰 - FPS 和效能疊加，提供詳細的即時系統資訊 `Proprietary`
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - 用於切換無線除錯的小部件和快速設定圖塊（與 KDE Con​​nect 整合） `GPL-3.0`

### Device owner (DPM)

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 啟發的應用程式，允許將 DeviceOwner 許可權共享給第三方應用程式 `GPL-3.0`
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用裝置所有者許可權管理您的裝置 `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - Fork of OwnDroid with added features `GPL-3.0`

### Display management
* [AG Displays](https://play.google.com/store/apps/details?id=com.htl.agdisplays) `Ads` - Launch other apps on external displays (TV/Monitor) or desktop mode on virtual displays while the phone screen can be used for other purposes or turned off `Proprietary`
* [ConnectScreen](https://connect-screen.com/) - Launch single apps to display in fullscreen on external displays, supporting both USB 2.0 (via DisplayLink dock) and USB 3.0 mobile phones. Can control the external display with a touch screen, USB devices or Bluetooth controller (even if you are USB 2.0 and using a DisplayLink dock). Can use the primary screen of the mobile as a virtual touchpad to control external display. Can rotate the screen for applications like TikTok `GPL-3.0` [(原始碼)](https://gitee.com/connect-screen/connect-screen)
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - Turns your phone into a touchpad and keyboard for a single app running on a wired external display `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可摺疊裝置上的各種螢幕摺疊狀態之間切換 `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - Keep your phone mostly monochrome, but allow apps like camera to be in color `GPL-3.0`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - 為 Android 裝置提供更好的螢幕映象 `Apache-2.0` [(原始碼)](https://github.com/farmerbb/SecondScreen)

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork 具有動畫支援和使用 Shizuku 的外掛管理。 `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - Export videos downloaded from the Android version of Bilibili `GPL-3.0` [(原始碼)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - Merge and export BiliBili cache files into MP4, supports mobile and computer client  `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 進行外掛管理的漫畫閱讀器。立讀的獨立繼承者。 `Apache-2.0`
  * Mihon/Tachiyomi 還有其他幾個活躍的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [AirData UAV](https://play.google.com/store/apps/details?id=com.airdata.uav.app) - 無人機飛行分析和機隊管理平臺 [access to /Android/Data](https://app.airdata.com/wiki/Help/Granting+Permissions+in+Android+13+and+14) `Proprietary`
* [File Manager Plus](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager)  `Ads` `IAP` 💰 - Can manage your files and folders, whether on local device, NAS storage (via sftp, ftp, webdav or smb) or in the cloud (e.g. Google Drive). Supports Shizuku for Android/data, Android/obb and partly /. `Proprietary`
* [FV File Manager](https://play.google.com/store/apps/details?id=com.folderv.file) - 檔案管理器 [access Android/data and Android/obb](https://folderv.com/2023/11/24/access-Android-data-and-Android-obb-on-Android-14/) `Proprietary`
* [MiXplorer](https://xdaforums.com/t/app-2-2-mixplorer-v6-x-released-fully-featured-file-manager.1523691/#post-23109280) - 檔案管理器，可以批次安裝 APK 並使用 Shizuku 訪問 Android/資料和 obb `Proprietary`
  * [MiXplorer Silver](https://play.google.com/store/apps/details?id=com.mixplorer.silver) - MiXplorer 付費 Google Play 版本 `Proprietary`
* [MT Manager](https://mt2.cn) - 分屏檔案管理器。可以使用 Shizuku 安裝 APK 並訪問 Android/data 和 Android/obb `Proprietary`
* [NMM File Manager / Text Edit](https://play.google.com/store/apps/details?id=in.mfile) - 檔案管理器和內建文字編輯器 `Proprietary`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE是Android最徹底的清理工具 `GPL-3.0` [(原始碼)](https://github.com/d4rken-org/sdmaid-se)
* [Solid Explorer](https://play.google.com/store/apps/details?id=pl.solidexplorer2) `Ads` `IAP` 💰 - File explorer `Proprietary`
* [SwiftBackup](https://play.google.com/store/apps/details?id=org.swiftapps.swiftbackup) `IAP` 💰 - Swift Backup 可在幾分鐘內備份重要資料 `Proprietary`
* [Total Commander](https://play.google.com/store/apps/details?id=com.ghisler.android.TotalCommander) - Android port of the desktop Total Commander app (Version 3.60 beta or later) `Proprietary`
* [X-Plore](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore) `Ads` `IAP` 💰 - 可使用 Shizuku 訪問 Android/資料和 obb 的檔案管理器 `Proprietary`
* [ZArchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) - 歸檔管理程式。支援使用 Root/Shizuku 編輯檔案。 `Proprietary`

### Games

* [Ascent](https://github.com/4o3F/Ascent) - A tool for retrieving gacha history links from Mihoyo games  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - Browndust II Mod manager `Proprietary`
* [blocktopograph](https://github.com/Blocktopograph/Blocktopograph) - Blocktopograph 是 MCBE 的應用程式伺服器，它包括一個用於本地世界的世界、NBT 編輯器 `Apache-2.0`
* [CloudSync-Mobile](https://github.com/FawazTakahji/CloudSync-Mobile) - An app that allows you to sync your Stardew Valley saves across multiple devices `GPL-3.0`
* [HandheldExp](https://github.com/Teppichseite/HandheldExp) - Android 上 EmulationStation (ES-DE) 的遊戲選單中  `MIT`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - 管理「洛杉磯犯罪」遊戲的地圖、桌布和螢幕截圖 `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 遊戲「Last Origin」的 Mod 管理器 `Proprietary`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - Companion app for localizing the Android version of CHAOS;CHILD visual novel `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 輕鬆匯入和共享 Polyfield 地圖 `GPL-3.0`
* [PGT: GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool.free) `Ads` - PUBG 的其他設定 `Proprietary`
  * [PGT+: Pro GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool) `Paid` 💰 - PUBG 的其他設定 `Proprietary`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - Genshin Impact Auto-Conversation Clicker `MIT`
* [stalker](https://github.com/onerdna/stalker) - Save data viewer & editor for Shadow Fight 2 `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order遊戲翻譯專案 `MIT`

### Input methods

* [andRemote2](https://github.com/c0dev0id/andRemote2) - Emulates the DMD Remote 2 for map apps `Proprietary`
* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - 觸控時顯示自訂的點選 `GPL-3.0`
* [Auto Cursor](https://play.google.com/store/apps/details?id=eu.toneiv.cursor) `IAP` 💰 - 透過螢幕邊緣的指標，單手即可輕鬆使用大型智慧手機。 `Proprietary`
* [C9](https://github.com/austinauyeung/C9) - Efficient grid-based cursor provided alongside a traditional cursor. Shizuku is only required on Android 11. `Apache-2.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - 一款 Android 應用程式，可改變您裝置上按鈕的功能！ `GPL-3.0` [(原始碼)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - Play games using mouse and keyboard on Android device; keymapper for games `Apache-2.0`
* [Panda Gamepad Pro](https://play.google.com/store/apps/details?id=com.panda.gamepad) `Paid` `IAP` 💰 - 遊戲鍵盤對映器 `Proprietary`
* [pastiera](https://github.com/palsoftware/pastiera) - Android keyboard specialized for Physical Keyboard Devices. Uses Shizuku for trackpad gestures `GPL-3.0`
* [RealMouse](https://play.google.com/store/apps/details?id=com.redlee90.realmouse) - 使用虛擬觸控板控制滑鼠。專為輔助顯示器而設計。 `Proprietary`
* [TitanPad](https://github.com/sztupy/TitanPad) - Converts the Titan2's Physical Keyboard's capacitive input into mouse and scroll gestures. Uses Shizuku for reading the trackpad input and setting up virtual HID devices `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 適用於 Android x86 的鍵盤對映器  `GPL-3.0`


### Installer & app stores

* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - Google Play 商店的開源替代品，具有隱私性和現代設計 `GPL-3.0` [(原始碼)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - 輕鬆下載、安裝和共享模組 `Proprietary`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客戶端 `GPL-3.0` [(原始碼)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：隱私友好瀏覽器的更新程式 `GPL-3.0` [(原始碼)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F‑Droid Client `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - App store for GitHub releases with discovery function `Apache-2.0` [(原始碼)](https://github.com/OpenHub-Store/GitHub-Store)
* [instafel](https://github.com/mamiiblt/instafel) - Updater app for Instafel, an Instagram mod `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - 現代且實用的 Android 應用安裝程式替代品 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 簡單的應用程式使用 Shizuku 在裝置上安裝帶有高階選項的 APK `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 儲存庫的非官方客戶端 `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - An F-Droid client with modern UI and an arsenal of extra features `GPL-3.0` [(原始碼)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接從源獲取 Android 應用程式更新 `GPL-3.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - App store for modded apps `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允許覆蓋包請求者和執行者的包安裝程式 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 拆分 APK 安裝程式 `GPL-3.0` [(原始碼)](https://github.com/Aefyr/SAI)
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - A lightweight app installer replacement with split APK support `Apache-2.0`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - GUI for Android's builtin `dex2oat` utility, allowing DEX code of installed apps to be re-optimized `Apache-2.0`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - Find the reason why the alarm icon is active in the status bar `Proprietary`
* [krude](https://github.com/KusStar/krude) - 多合一應用程式和工作流程啟動器 `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - Android utility to make notifications persistent/undismissable using Shizuku `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - Automatically close selected apps when you exit them to save power and memory `Apache-2.0`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - Exploits CVE-2024-31317 for Zygote injection, integrating remote terminal and file transfer capabilities `MIT`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一個簡單的應用程式，用於透過 WearOS 手錶控制 Android 裝置 `Apache-2.0` [(原始碼)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - Remote control your device via Telegram messages `BSD 3-Clause`


### Network

* [ADNS](https://github.com/eyalm2000/adns) - DNS-based ad blocker for Android `MIT`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上讀取手機訊號塔資訊 `MIT` [(原始碼)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - App firewall without using an VPN; can also manage packages `MIT`
* [delta](https://github.com/supershadoe/delta) - 使用 Shizuku 的熱點管理器 `BSD-3-Clause`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - An app that allows you to turn on your hotspot remotely via Bluetooth - think Apple Continuity, but for everyone `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Google FindMyDevice 服務的安全和開源替代方案 `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - Dual-mode firewall: blocks internet access using Shizuku or a standard local VPN interface or both. `MIT`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 預覽和編輯/etc/hosts檔案 `MIT`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一個在 Android 上執行 Naiveproxy 的簡單應用程式 `MIT`
* [NetWall](https://play.google.com/store/apps/details?id=com.ysy.app.firewall) `IAP` 💰 - 不依賴本地 VPN 或 root 的應用防火牆 `Proprietary`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - 用於 4G/5G 網路模式切換的 Android 應用 `GPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - Open-source app firewall that doesn't depend on VPNs or root `GPL-3.0`
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - A persistent network speed tracker in your status bar `GPL-3.0` [(原始碼)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - WireGuard 和 AmneziaWG 的 FOSS Android 客戶端，支援自動隧道功能 `MIT`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - Simple app using Shizuku to manage & view saved Wi-Fi passwords  `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - 在 Android 11 及更高版本上檢視您儲存的 WiFi 密碼，無需 root `Proprietary` [(原始碼)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - 從 LSPod 擴充套件的非根 Xposed 框架 `GPL-3.0`
* [Morphe](https://morphe.software/) - User-friendly YouTube patcher based on Universal-ReVanced-Manager `GPL-3.0` [(原始碼)](https://github.com/MorpheApp/morphe-manager)
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - ReVanced patcher that has extra features the official manager doesn't have  `GPL-3.0`

### Power management

* [BatStats](https://github.com/mlm-games/BatStats) - Battery monitor with stats via Shizuku `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - 一個簡單的應用程式，可在 Android 14 及更高版本上顯示電池狀態資訊。 `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - Open source app to visually change battery data via Shizuku `GPL-3.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - Enable Doze mode immediately after screen off and turn off motion sensing to get best battery life `GPL-3.0` [(原始碼)](https://github.com/farfromrefug/EnforceDoze)
* [Extinguish](https://play.google.com/store/apps/details?id=own.moderpach.extinguish) - 熄滅關閉螢幕，但保持裝置喚醒狀態 `Proprietary`
* [FDE.AI](https://github.com/feravolt/FDE.AI-docs/releases) `IAP` 💰 - All-in-One optimizer for Android `Proprietary`
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - A fire-and-forget program to stop Android apps from running in the background `GPL-3.0` [(原始碼)](https://github.com/adil192/no_more_background)
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - Advanced reboot menu with Shizuku support `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 關閉 Android 螢幕而不進入待機/睡眠模式 `Proprietary`
* [zukulock](https://github.com/tiendnm/zukulock) - Very lightweight app that locks the screen when launched. Helps reduce wear on the power button `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一鍵隱藏您的私人檔案和 Android 應用程式。 `Apache-2.0` [(原始碼)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - An application designed to silently protect user data from powerful adversaries `GPL-3.0`
* [AppLock](https://github.com/aload0/AppLock) ✨ - MIUI 12+ 防止應用被側滑或一鍵清理殺死 `MIT`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - Manage your device privacy based on lock/unlock state `MIT` [(原始碼)](https://github.com/dorumrr/privacyflip)

### Productivity

* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - Digital Detoxing: Use your phone rather than letting your phone use you `GPL-3.0`
* [digipaws](https://f-droid.org/packages/nethical.digipaws/) ✨ - Tool to reduce screen addiction by regulating app usage through a gamified experience `GPL-3.0` [(原始碼)](https://github.com/nethical6/digipaws)

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一個用於切換「息屏顯示（Always on Display）」的 Android 快捷設定 `MIT` [(原始碼)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本上帶回獨立的 Wi-Fi 和移動資料磁貼，並提供更好的統一網路磁貼 `GPL-3.0` [(原始碼)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - Provides quick settings tile and shortcuts to turn off the display without locking the screen or stopping foreground running apps `MIT` [(原始碼)](https://github.com/UlyssesZh/DisplayToggle)
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - 用於開啟或關閉私有 DNS 設定的快捷磁貼  `GPL-3.0` [(原始碼)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 用於切換當前私有 DNS 伺服器的快捷設定磁貼  `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - 提供用於切換 USB 除錯和切換私有 DNS 主機的快捷磁貼 `GPL-3.0` [(原始碼)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 透過快捷設定啟用/停用裝置感測器 `Apache-2.0`
* [Ultimate Settings](https://play.google.com/store/apps/details?id=com.precisebytes.androidtoggles.free.release) `Ads` - 可從小部件/應用/通知/鎖屏通知直接切換 Wi-Fi、藍牙、行動網路、飛航模式、GPS、NFC、Wi-Fi/藍牙/USB 網路共享熱點、螢幕亮度、螢幕自動旋轉、LED 燈、鈴聲模式。 `Proprietary`
* [Ultimate Settings PRO](https://play.google.com/store/apps/details?id=com.precisebytes.androidtoggles.pro.release) `Paid` 💰 - 可從小部件/應用/通知/鎖屏通知直接切換 Wi-Fi、藍牙、行動網路、飛航模式、GPS、NFC、Wi-Fi/藍牙/USB 網路共享熱點、螢幕亮度、螢幕自動旋轉、LED 燈、鈴聲模式。 `Proprietary`

### Software management

* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 - 無需root即可管理應用程式許可權 `Proprietary`
* [AppControlX](https://github.com/risunCode/AppControl-X) - Freeze, force stop, uninstall apps, change background optimization and more `GPL-3.0`
* [AppDash](https://play.google.com/store/apps/details?id=flar2.appdashboard) `7-day trial` `Paid` 💰 - 一個應用程式管理器，可以輕鬆管理裝置上安裝的 APK 和應用程式 `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - 啟用/停用 Android 元件，例如活動、服務、接收器和提供者 `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - An app manager focusing on permission management `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - 無需root即可解除安裝任何應用程式 `LGPL-3.0` [(原始碼)](https://github.com/samolego/Canta)
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 應用程式可停用未使用的應用程式，同時仍允許方便地訪問它們 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 透過手動或半自動凍結蹩腳軟體來提高裝置的速度和電池壽命 `Apache-2.0` [(原始碼)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - 凍結、隱藏或停用任何應用程式。建立並組織可一鍵凍結的應用程式組。 `GPL-3.0` [(原始碼)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - 使用 Shizuku 凍結或隱藏應用程式 `Proprietary`
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Island 完整的 FLOSS 分叉 `Apache-2.0` [(原始碼)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - 適用於 root 和非 root 裝置的 Android 應用程式管理器 `GPL-3.0` [(原始碼)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔離和複製應用程式以保護隱私和並行執行 `Apache-2.0` [(原始碼)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一應用程式和工作流程啟動器 `MIT`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - 管理您的 Magisk 模組儲存庫 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能強大的應用程式，可管理系統和使用者應用程式 `GPL-3.0` [(原始碼)](https://github.com/SmartPack/PackageManager)
* [Package Name Scripter](https://play.google.com/store/apps/details?id=in.ms.packagenamesscripter) - Manage installed apps using Shizuku or create ADB scripts to enable, disable, uninstall, reinstall, or run other app-related ADB commands. `Proprietary`
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - App manager with freeze and install capabilities. `GPL-3.0`  [(原始碼)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 檢查 Android 應用程式、Magisk 模組等的更新！ `GPL-3.0` [(原始碼)](https://github.com/DUpdateSystem/UpgradeAll)

### Task manager

* [Pensum](https://github.com/troikoss/Pensum) ✨ - Windows-style Task Manager for Android `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - Monitor running services on your Android device `MIT` [(原始碼)](https://github.com/biplobsd/running_services_monitor)
* [shappky](https://github.com/YasserNull/shappky) ✨ - A simple app to boost performance by stopping background apps. `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - A Task Manager for Android. Killing processes requires root access. `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 適用於 Shizuku 支援的 Android 裝置的本地 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新設計了 aShell 應用程式。 `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - Terminal, SSH, VNC, RDP, SFTP & cloud storage client for Android `AGPL-3.0`
* [ReTerminal](https://github.com/RohitKushvaha01/ReTerminal) ✨ - Sleek, Material 3-inspired terminal emulator based on Termux's robust TerminalView `MIT`
* [ShizuShell](https://play.google.com/store/apps/details?id=com.noxinfinity.shell) - 使用 Shizuku 的 ADB shell `Proprietary`


> [!NOTE]
> Using [rish](pages/RISH_tw.md), 您可以使用任何終端模擬器（例如 Termux）建立本地 ADB shell。

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一個用於切換「息屏顯示（Always on Display）」的 Android 快捷設定 `MIT` [(原始碼)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 透過 LG U+ 在 Pixel 6 和 7 上啟用 VoLTE `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - Enable VoLTE for carriers in unsupported regions on Pixel devices `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定製的小部件，可以使用 Shizuku 升級 Pixel 裝置上內建的「概覽」小部件 `GPL-3.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - Enhanced IMS Configuration Tool for Google Pixel devices `Apache-2.0`

#### Samsung OneUI

* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 rootless font installer `GPL-3.0` [(原始碼)](https://codeberg.org/dryerlint/fontsmanager)
* [Galaxy MaxHz](https://github.com/tribalfs/GalaxyMaxHzPub) `IAP` 💰 - Refresh Rate Mods, Screen-off Mods, QS Tiles, Tasker Support and More  `Proprietary`
* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - 適用於 Samsung OneUI 裝置的自訂系統範圍主題引擎 `Proprietary`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - Enable or disable fast charging mode on Samsung devices when the battery temperature reaches a certain point  `Proprietary`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - Disable the forced camera shutter sounds on Samsung devices that have their CSC set to certain countries with this restriction `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 許可權提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 執行 OneUI 5 的非 root 裝置上的系統使用者訪問 (UID 1000)。使用 Shizuku 實現自動化 `LGPL-2.1`

#### MIUI

* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - HyperOS/MIUI 5G快捷開關 `GPL-3.0` [(原始碼)](https://github.com/ysy950803/FiveGSwitcher)
* [FpsSwitcher](https://play.google.com/store/apps/details?id=com.ysy.fpsswitcher) `Paid` 💰 - HyperOS/MIUI 重新整理率快捷開關 `Proprietary`
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本關閉 MIUI 廣告 `Apache-2.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - 在 MIUI 上以自由格式顯示大多數應用程式 `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - One-click configuration for Mix Flip's outer screen: Use any apps and restore system apps to default style `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 節奏遊戲中啟用 3 鍵導航  `Proprietary`

#### Other

* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control gives precise control over the Nothing Phone (3)'s recording light `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - System-wide shoulder triggers for Nubia Red Magic phones `MIT`

### Unlisted apps
為了保持主列表乾淨，所有不滿足特定要求的應用程式都儲存在單獨的頁面上： [ARCHIVED.md](pages/ARCHIVED.md)

我還使用自動爬蟲來搜尋新專案，並在 GitHub 和多個 F-Droid 儲存庫中使用 Shizuku。您可以在此處檢視當前自動生成的爬網報告：[TODO.md](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的開發人員檔案，包括示例 `Apache-2.0`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - Shizuku API bindings for Flutter apps `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android Coroutines-friendly Kotlin-first Package Installer extensions with Shizuku support `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常規檔案系統後端的檔案操作庫 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - 使用 Shizuku API 安裝 Android APK 的 Flutter 外掛 `MIT`

### System
* [ServiceManagerCompat](https://github.com/SanmerApps/ServiceManagerCompat) - ServiceManager bindings `MIT`

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
- ✨ - 我的個人推薦：大量運用 Shizuku，或是獨特 / 隱藏版的寶藏 App。
- `Paid` 💰 - 付費應用程式
- `IAP` 💰 - 包含應用內購買
- `Ads` - 包含廣告
- `Proprietary` - 缺少許可證或閉源軟體
- `n-day trial` - `n`天后需要付款
- `Root` - 需要在Root模式下執行Shizuku

--------------------

## License

本列表採用[Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 許可協議。

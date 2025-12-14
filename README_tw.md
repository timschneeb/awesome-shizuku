# awesome-shizuku

> [!IMPORTANT]
> 由於一些原因(不方便透露)，我不得不停止為該專案提供簡體中文翻譯的工作 除他人接手繼續提供翻譯
> 此也會影響到繁體中文
> 中文件案可能落後於英文件案，如果有問題請先檢視英文件案。


### 語言
[English](/README.md) | [简体中文](/README_cn.md) | 繁體中文

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允許普通應用程式在非root 裝置上使用 ADB 直接使用許可權提升的系統 API。本列表彙集了一些已知可利用 Shizuku 功能的應用程式。

更多詳情：https://shizuku.rikka.app/

歡迎拉取請求。有關提示，請參閱 [貢獻](CONTRIBUTING.md)。

--------------------


## 目錄

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
  - [Quick Settings](#quick-settings)
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

* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - 針對非 root Android 裝置的系統級 JamesDSP 音訊處理引擎的實現 `GPL-3.0` [(原始碼)](https://github.com/ThePBone/RootlessJamesDSP)

### Automation

* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可針對特定生活環境自動或一鍵配置裝置 `Apache-2.0`
* [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) `Ads` `IAP` 💰 - 適用於 Android 裝置的自動化應用程式。版本 5.46 及更高版本引入了 Shizuku 支援。`Proprietary`
* [UbikiTouch](https://play.google.com/store/apps/details?id=eu.toneiv.ubktouch) `IAP` 💰 - 為您喜愛的應用程式新增功能，只需一個手勢即可訪問。輕掃螢幕的一側邊緣，即可顯示一個可定製的選單，其中顯示了您最喜歡的操作。 `Proprietary`

### Communication

* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 這是一款簡單的應用程式，可在您喜歡的 Lemmy 客戶端中自動啟動 lemmy 連結。 `MIT` [(原始碼)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 這是一個簡單的應用程式，可在您喜歡的 Mastodon 客戶端中自動啟動 fediverse 連結。 `MIT` [(原始碼)](https://github.com/zacharee/MastodonRedirect)
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 讓您透過簡訊瀏覽網頁的應用程式 `GPL-3.0`
* [Bunny-Manager](https://github.com/pyoncord/BunnyManager) - Discord Bunny Mod 的補丁管理器 `OSL-3.0`


### Customization

* [AAAD](https://github.com/shmykelsa/AAAD) `IAP` 💰 - 下載流行的 Android Auto 第三方應用程式並安裝到 Android Auto 上 `Proprietary`
* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - Android 快速設定可切換「始終顯示」 `MIT` [(原始碼)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 將 Now Playing 從 Pixels 移植到其他 Android 裝置 `GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) - 一款小巧的 Android 應用程式，可讓你安排暗模式的開啟/關閉時間`。MIT` [(原始碼)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) -使用指定應用程式時自動切換免打擾的簡單工具 `AGPL-3.0` [(原始碼)](https://github.com/dic1911/android_AutoDND)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本中恢復 Wi-Fi 和移動資料磁貼，以及更統一的網際網路磁貼 `GPL-3.0` [(原始碼)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
  * [Better Internet Tiles Libre](https://github.com/D3SOX/Better-Network-Tiles-Libre) - Better Internet Tiles 的 Libre 分支，無需專有庫 `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一個非常簡單的應用程式，用於更改未 root 的 Android 裝置上的電信公司名稱 `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr)- 修改裝置 Material You 顏色的應用程式 `GPL-3.0`
* [DarQ](https://github.com/KieronQuinn/DarQ) - DarQ 為 Android 10 及更高版本提供了每個應用程式可選擇的強制黑暗選項 `Apache-2.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid)- 在智慧手機的 Android 作業系統上新增類似桌面的多視窗支援。`No license`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允許使用者選擇單獨的應用語言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/1fexd/LinkSheet) - 使用 Material3 恢復 Android <12 Url-App 連結選擇器  `Modified MPL-2.0`
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始裝置製造商（小米）不允許您在裝置的本地設定中新增額外的（或 "不支援的"）語言，那麼這款簡單的應用程式就能幫您實現這一功能。  `MIT`
* [NoPopping](https://play.google.com/store/apps/details?id=rikka.nopeeking) `IAP` 💰 - 自動免打擾模式 `Proprietary`
* [Repainter](https://play.google.com/store/apps/details?id=dev.kdrag0n.dyntheme) `IAP` 💰 - 在裝置上安裝自訂 Material You 設計 `Proprietary`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易於使用的工具，超越Android系統允許的控制級別`No license`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 外掛 `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 檢視和修改 Android 裝置上的隱藏設定 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) - 將裝置背面的雙擊功能從 Android 12 移植到任何 Android 7.0+ 裝置 `GPL-3.0`
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用開始選單訪問應用程式可以解鎖其他功能 `Apache-2.0` [(原始碼)](https://github.com/farmerbb/Taskbar)
* [zFont 3](https://play.google.com/store/apps/details?id=com.htetznaing.zfont2) `Ads` `IAP` 💰 - 表情符號和字型更換器 `Proprietary`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 刪除已為使用者註冊帳號的應用程式的軟體包名稱. `No license`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - 檢測 Treble、GSI、Mainline、APEX、system-as-root(SAR)、A/B 等。 `Apache-2.0` [(原始碼)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) 用於 JVM 開發的 IDE。使用 Shizuku 作為嵌入式 shell - `GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity) - 電流活動監視器 `GPL-3.0`
* [get_event](https://github.com/lalakii/get_event)- 讀取/dev/input/event*  `No license`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用於檢視裝置上的應用程式中使用的庫的應用程式。使用 Shizuku 確定其他應用程式的安裝源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) - 另一個適用於 Android 的 logcat 閱讀器  `GPL-3.0`
* [Logra](https://github.com/wingio/Logra) - 適用於 Android 的 Material You logcat 檢視器 `GPL-2.0`
* [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) `Ads` `IAP` 💰 - 啟動/互動（未）匯出的活動、服務和接收器。支援 Shizuku 和 root。 `Proprietary`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher&hl=en&gl=US) `Paid` 💰 - 啟動/互動（未）匯出的活動、服務和接收器。支援 Shizuku 和 root. `Proprietary` [(原始碼)](https://github.com/zacharee/RootActivityLauncher)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 透過快速設定啟用/停用裝置感測器 `Apache-2.0`
* [TakoStats](https://play.google.com/store/apps/details?id=rikka.fpsmonitor) `IAP` 💰 - FPS 和效能疊加，提供詳細的即時系統資訊 `Proprietary`
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) 用於切換無線除錯的小部件和快速設定圖塊（與 KDE Con​​nect 整合） - `GPL-3.0`

### Device owner (DPM)

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 啟發的應用程式，允許將 DeviceOwner 許可權共享給第三方應用程式 `GPL-3.0`
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用裝置所有者許可權管理您的裝置 `GPL-3.0`

### Display management
* [Android-Screener](https://github.com/jiesou/Android-Screener) - 輕鬆調整螢幕解析度和幀頻的工具 `MIT`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可摺疊裝置上的各種螢幕摺疊狀態之間切換 `Apache-2.0`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) -為 Android 裝置提供更好的螢幕映象 `Apache-2.0` [(原始碼)](https://github.com/farmerbb/SecondScreen)

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi)- Tachiyomi fork 具有動畫支援和使用 Shizuku 的外掛管理。 `Apache-2.0`
* [BilibiliCacheVideoMerge](https://github.com/molihuan/BilibiliCacheVideoMerge) - 將BiliBili影片快取檔案匯出為MP4 `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 進行外掛管理的漫畫閱讀器。立讀的獨立繼承者。 `Apache-2.0`
  * Mihon/Tachiyomi 還有其他幾個活躍的分叉，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [AirData UAV](https://play.google.com/store/apps/details?id=com.airdata.uav.app) - 無人機飛行分析和機隊管理平臺 [access to /Android/Data](https://app.airdata.com/wiki/Help/Granting+Permissions+in+Android+13+and+14) `Proprietary`
* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一鍵隱藏您的私人檔案和 Android 應用程式。`Apache-2.0` [(原始碼)](https://github.com/deltazefiro/Amarok-Hider)
* [EDS Full - Encrypted Data Store Full](https://sovworks.com/eds/index.php) `Paid` 💰 - 適用於 Android 的虛擬磁碟加密軟體，允許您將檔案儲存在加密容器中。適用於 root 和非 root 的廣泛而豐富的功能，此處無法列出（請參閱站點）。透過 Android 意圖進行 Shizuku 控制（請參閱常見問題解答）。 `Proprietary`
  * [EDS Lite - Encrypted Data Store Lite](https://sovworks.com/eds/index.php) - EDS 完整版的免費版本。功能有限但仍然強大。非 root 和 root 功能。僅適用於非安裝模式（有關說明，請參閱站點）。 `GPL-2.0` [(原始碼)](https://github.com/sovworks/edslite)
* [FV File Manager](https://play.google.com/store/apps/details?id=com.folderv.file) - 檔案管理器 [access Android/data and Android/obb](https://folderv.com/2023/11/24/access-Android-data-and-Android-obb-on-Android-14/) `Proprietary`
* [MiXplorer](https://xdaforums.com/t/app-2-2-mixplorer-v6-x-released-fully-featured-file-manager.1523691/#post-23109280) - 檔案管理器，可以批次安裝 APK 並使用 Shizuku 訪問 Android/資料和 obb`Proprietary`
  * [MiXplorer Silver](https://play.google.com/store/apps/details?id=com.mixplorer.silver) - MiXplorer 付費 Google Play 版本 `Proprietary`
* [MT Manager](https://mt2.cn) - 分屏檔案管理器。可以使用 Shizuku 安裝 APK 並訪問 Android/data 和 Android/obb `Proprietary`
* [NMM File Manager / Text Edit](https://play.google.com/store/apps/details?id=in.mfile) - 檔案管理器和內建文字編輯器 `Proprietary`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) - SD Maid 2/SE是Android最徹底的清理工具 `GPL-3.0` [(原始碼)](https://github.com/d4rken-org/sdmaid-se)
* [SwiftBackup](https://play.google.com/store/apps/details?id=org.swiftapps.swiftbackup) `IAP` 💰 - Swift Backup 可在幾分鐘內備份重要資料 `Proprietary`
* [X-Plore](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore) `Paid` 💰- 可使用 Shizuku 訪問 Android/資料和 obb 的檔案管理器 `Proprietary`
* [ZArchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) - 歸檔管理程式。支援使用 Root/Shizuku 編輯檔案。 `Proprietary`

### Games

* [90 FPS + 120 FPS & IPAD VIEW](https://play.google.com/store/apps/details?id=tq.tech.Fps) `Ads` -在 PUBG 中實現高 FPS `Proprietary`
* [blocktopograph](https://github.com/NguyenDuck/blocktopograph) - Blocktopograph 是 MCBE 的應用程式伺服器，它包括一個用於本地世界的世界、NBT 編輯器`AGPL-3.0`
* [HandheldExp](https://github.com/Teppichseite/HandheldExp) - Android 上 EmulationStation (ES-DE) 的遊戲選單中 `MIT`
* [lac-tool](https://github.com/aliernfrog/lac-tool)- 管理「洛杉磯犯罪」遊戲的地圖、桌布和螢幕截圖 `MIT`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 遊戲「Last Origin」的 Mod 管理器 `No license`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 輕鬆匯入和共享 Polyfield 地圖 `MIT`
* [PGT: GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool.free) `Ads` - PUBG 的其他設定 `Proprietary`
  * [PGT+: Pro GFX, Launcher & Optimizer](https://play.google.com/store/apps/details?id=inc.trilokia.pubgfxtool) `Paid` 💰 - PUBG 的其他設定 `Proprietary`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order遊戲翻譯專案 `CC BY-NC-SA 4.0`

### Input methods

* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - 觸控時顯示自訂的點選 `GPL-3.0`
* [Auto Cursor](https://play.google.com/store/apps/details?id=eu.toneiv.cursor) `IAP` 💰 - 透過螢幕邊緣的指標，單手即可輕鬆使用大型智慧手機。`Proprietary`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)- 一款 Android 應用程式，可改變您裝置上按鈕的功能！ `GPL-3.0` [(原始碼)](https://github.com/keymapperorg/KeyMapper)
* [Panda Gamepad Pro](https://play.google.com/store/apps/details?id=com.panda.gamepad) `Paid` `IAP` 💰 - 遊戲鍵盤對映器 `Proprietary`
* [RealMouse](https://play.google.com/store/apps/details?id=com.redlee90.realmouse) - 使用虛擬觸控板控制滑鼠。專為輔助顯示器而設計。 `Proprietary`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 適用於 Android x86 的鍵盤對映器  `GPL-3.0`


### Installer & app stores

* [AuroraStore](https://f-droid.org/en/packages/com.aurora.store/) - Google Play 商店的開源替代品，具有隱私性和現代設計 `GPL-3.0` [(原始碼)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub)- 輕鬆下載、安裝和共享模組 `No license`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 客戶端 `GPL-3.0` [(原始碼)](https://github.com/Droid-ify/client)
* [fdroid_shizuku_privileged_extension](https://depau.github.io/fdroid_shizuku_privileged_extension/fdroid/repo/) - 與 Shizuku 協同工作的 F-Droid 許可權擴充套件`Apache-2.0` [(原始碼)](https://github.com/depau/fdroid_shizuku_privileged_extension)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：隱私友好瀏覽器的更新程式 `GPL-3.0` [(原始碼)](https://github.com/Tobi823/ffupdater)
* [glassdown](https://github.com/Sinneida/glassdown) - APKMirror 客戶端 `GPL-3.0`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - 現代且實用的 Android 應用安裝程式替代品 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 簡單的應用程式使用 Shizuku 在裝置上安裝帶有高階選項的 APK `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 儲存庫的非官方客戶端`GPL-3.0`
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接從源獲取 Android 應用程式更新 `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允許覆蓋包請求者和執行者的包安裝程式 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 拆分 APK 安裝程式 `GPL-3.0` [(原始碼)](https://github.com/Aefyr/SAI)
* [skydroid](https://github.com/redsolver/skydroid) - 適用於 Android 的分散式基於域的應用程式商店 `GPL-3.0`

### Miscellaneous

* [Anywhere](https://github.com/zhaobozhen/Anywhere-/) - 活動和 shell 快捷方式資料夾 `Apache-2.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一個簡單的應用程式，旨在幫助使用者透過 DSU 的 Android 功能輕鬆安裝 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修復了 HostProfile 應用程式和 WorkProfile/DualApp/MultiApp 之間的 MediaStore 和檔案 IO 相容性問題。 `No license`
* [LSPatch](https://github.com/LSPosed/LSPatch)- 從 LSPod 擴充套件的非根 Xposed 框架`GPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一個簡單的應用程式，用於透過 WearOS 手錶控制 Android 裝置 `Apache-2.0` [(原始碼)](https://github.com/SimpleAppProjects/SimpleWear)

### Network

* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可以在Android上讀取手機訊號塔資訊`MIT` [(原始碼)](https://github.com/zacharee/CellReader)
* [delta](https://github.com/supershadoe/delta) - 使用 Shizuku 的熱點管理器 `BSD-3-Clause`
* [FindMyDevice](https://gitlab.com/Nulide/findmydevice) - Google FindMyDevice 服務的安全和開源替代方案 `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 預覽和編輯/etc/hosts檔案 `MIT`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一個在 Android 上執行 Naiveproxy 的簡單應用程式 `MIT`
* [NetWall](https://play.google.com/store/apps/details?id=com.ysy.app.firewall) `IAP` 💰 - 不依賴本地 VPN 或 root 的應用防火牆 `Proprietary`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - 用於 4G/5G 網路模式切換的 Android 應用 `GPL-3.0`
* [WG Tunnel](https://github.com/wgtunnel/wgtunnel) - WireGuard 和 AmneziaWG 的 FOSS Android 客戶端，支援自動隧道功能 `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - 在 Android 11 及更高版本上檢視您儲存的 WiFi 密碼，無需 root `Proprietary` [(原始碼)](https://github.com/zacharee/WiFiList)
  * [WiFiList (Fork)](https://github.com/jaredcat/WiFiList) - 'WiFiList' 的分支版本 `Proprietary`

### Power management

* [Batt](https://gitlab.com/narektor/batt) - 一個簡單的應用程式，可在 Android 14 及更高版本上顯示電池狀態資訊。 `GPL-3.0`
* [Extinguish](https://play.google.com/store/apps/details?id=own.moderpach.extinguish) - 熄滅關閉螢幕，但保持裝置喚醒狀態 `Proprietary`
* [rebootmenu](https://github.com/ryuunoakaihitomi/rebootmenu)- 使用快捷方式鎖定螢幕或開啟電源選單。如果您的電源按鈕壞了，這很有用。 `MIT`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 關閉 Android 螢幕而不進入待機/睡眠模式 `Proprietary`

### Quick Settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一個用於切換「息屏顯示（Always on Display）」的 Android 快捷設定 `MIT` [(原始碼)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本上帶回獨立的 Wi-Fi 和移動資料磁貼，並提供更好的統一網路磁貼 `GPL-3.0` [(原始碼)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 透過快捷設定啟用/停用裝置感測器 `Apache-2.0`
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 用於切換當前私有 DNS 伺服器的快捷設定磁貼 `MIT`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - 用於開啟或關閉私有 DNS 設定的快捷磁貼 `GPL-3.0` [(原始碼)](https://github.com/flashsphere/private-dns-qs)
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - 提供用於切換 USB 除錯和切換私有 DNS 主機的快捷磁貼 `GPL-3.0` [(原始碼)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [Ultimate Settings](https://play.google.com/store/apps/details?id=com.precisebytes.androidtoggles.free.release) `Ads` - 可從小部件/應用/通知/鎖屏通知直接切換 Wi-Fi、藍牙、行動網路、飛航模式、GPS、NFC、Wi-Fi/藍牙/USB 網路共享熱點、螢幕亮度、螢幕自動旋轉、LED 燈、鈴聲模式。 `Proprietary`
* [Ultimate Settings PRO](https://play.google.com/store/apps/details?id=com.precisebytes.androidtoggles.pro.release) `Paid` 💰 - 可從小部件/應用/通知/鎖屏通知直接切換 Wi-Fi、藍牙、行動網路、飛航模式、GPS、NFC、Wi-Fi/藍牙/USB 網路共享熱點、螢幕亮度、螢幕自動旋轉、LED 燈、鈴聲模式。 `Proprietary`

### Software management

* [AppDash](https://play.google.com/store/apps/details?id=flar2.appdashboard) `IAP` 💰 - 一個應用程式管理器，可以輕鬆管理裝置上安裝的 APK 和應用程式 `Proprietary`
* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 - 無需root即可管理應用程式許可權 `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - 啟用/停用 Android 元件，例如活動、服務、接收器和提供者 `Apache-2.0`
* [Canta](https://github.com/samolego/Canta)- 無需root即可解除安裝任何應用程式 `LGPL-3.0`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 應用程式可停用未使用的應用程式，同時仍允許方便地訪問它們 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 透過手動或半自動凍結蹩腳軟體來提高裝置的速度和電池壽命`Apache-2.0` [(原始碼)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) 凍結、隱藏或停用任何應用程式。建立並組織可一鍵凍結的應用程式組。 - `GPL-3.0` [(原始碼)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - 使用 Shizuku 凍結或隱藏應用程式 `Proprietary`
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `Paid` 💰 - 適用於 root 和非 root 裝置的 Android 應用程式管理器 `GPL-3.0` [(原始碼)](https://github.com/Hamza417/Inure)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/)- Island 完整的 FLOSS 分叉 `Apache-2.0` [(原始碼)](https://gitlab.com/secure-system/Insular)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔離和複製應用程式以保護隱私和並行執行 `Apache-2.0` [(原始碼)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一應用程式和工作流程啟動器 `MIT`
* [MMRL](https://github.com/DerGoogler/MMRL) `Root` - 管理您的 Magisk 模組儲存庫 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能強大的應用程式，可管理系統和使用者應用程式 `GPL-3.0` [(原始碼)](https://github.com/SmartPack/PackageManager)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 檢查 Android 應用程式、Magisk 模組等的更新！ `GPL-3.0` [(原始碼)](https://github.com/DUpdateSystem/UpgradeAll)

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 適用於 Shizuku 支援的 Android 裝置的本地 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You 重新設計了 aShell 應用程式。 `GPL-3.0`
* [ShizuShell](https://play.google.com/store/apps/details?id=com.noxinfinity.shell) - 使用 Shizuku 的 ADB shell `Proprietary`


> [!NOTE]
> Using [rish](#rish-shell), 您可以使用任何終端模擬器（例如 Termux）建立本地 ADB shell。

### Vendor-specific

#### Google Pixel
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 透過 LG U+ 在 Pixel 6 和 7 上啟用 VoLTE `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可定製的小部件，可以使用 Shizuku 升級 Pixel 裝置上內建的「概覽」小部件`GPL-3.0`

#### Samsung OneUI

* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - 適用於 Samsung OneUI 裝置的自訂系統範圍主題引擎 `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 許可權提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) 執行 OneUI 5 的非 root 裝置上的系統使用者訪問 (UID 1000)。使用 Shizuku 實現自動化`LGPL-2.1`

#### MIUI

* [AppLock](https://github.com/Mufanc/AppLock) - MIUI 12+ 防止應用被側滑或一鍵清理殺死 `GPL-3.0`
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - HyperOS/MIUI 5G快捷開關 `GPL-3.0` - [(原始碼)](https://github.com/ysy950803/FiveGSwitcher)
* [FpsSwitcher](https://play.google.com/store/apps/details?id=com.ysy.fpsswitcher) `Paid` 💰 - HyperOS/MIUI 重新整理率快捷開關 `Proprietary`
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本關閉 MIUI 廣告 `Apache-2.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - 在 MIUI 上以自由格式顯示大多數應用程式 `GPL-3.0`
  * [Flyme-FreeForm](https://github.com/Live-Block/Flyme-FreeForm)- Mi-FreeForm 的分叉 `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 節奏遊戲中啟用 3 鍵導航  `No license`

### Unlisted apps
為了保持主列表乾淨，所有不滿足特定要求的應用程式都儲存在單獨的頁面上： [UNLISTED.md](pages/UNLISTED.md)

我還使用自動爬蟲來搜尋新專案，並在 GitHub 和多個 F-Droid 儲存庫中使用 Shizuku。您可以在此處檢視當前自動生成的爬網報告：[TODO.md](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Shizuku](https://github.com/RikkaApps/Shizuku) - Shizuku系統伺服器、API和應用程式 `Apache-2.0`
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的開發人員檔案，包括示例 `Apache-2.0`

### Filesystem
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常規檔案系統後端的檔案操作庫 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - 使用 Shizuku API 安裝 Android APK 的 Flutter 外掛 `MIT`

### Power

* [PowerAct](https://github.com/ryuunoakaihitomi/PowerAct) - 一個 Android 庫，只需幾行程式碼即可操縱與電源相關的操作`Apache-2.0`


--------------------

## Rish shell

`rish` 是一個 Android 可執行檔案（不是應用程式），用於與在高許可權守護程式上執行的 shell 進行互動。
例如，如果 Shizuku 是使用 ADB 許可權啟動的，那麼 `rish` 還將提供一個維護 ADB 許可權的 shell。

要設定 `rish`，請開啟 Shizuku，導航到 "在終端應用程式中使用 Shizuku"，然後按照設定說明進行操作。請注意，您需要對 shell、終端和基本命令有基本的瞭解，才能有效地使用它。

設定好 `rish` 後，您可以在任何支援呼叫任何 shell 指令碼或可執行檔案的應用程式中使用它，即使應用程式本身不支援 Shizuku。

> [!NOTE]
> 由於 `rish` 的位置不在 `$PATH` 中，因此可能需要指定可執行檔案的路徑才能手動啟動它。如果它位於當前工作目錄中，則使用 `./rish` 啟動它。

**Syntax:**

* `rish`: 啟動預設的互動式 shell（使用 /system/bin/sh）
* `rish exec /path/to/custom/shell`: 啟動自訂/替代互動式 shell
* `rish -c 'whoami'`: 執行shell命令，完成後退出
* `echo 'whoami' | rish`: 從 stdin 讀取 shell 命令，執行它，完成後退出

> [!NOTE]
> `whoami` 用作示例命令，並將返回當前 shell 使用者的名稱。

**Usage examples:**

* 直接在裝置上使用 **Termux** 等終端模擬器開啟互動式 ADB shell
* 使用 **Tasker** 等自動化應用程式在後臺自動觸發高許可權 ADB shell 命令
  * 示例：命令 `rish -c 'reboot'` 將透過 shell 使用 Shizuku 重新啟動裝置

官方的 rish 檔案可以在這裡找到：https://github.com/RikkaApps/Shizuku-API/blob/master/rish/README.md

--------------------

## Annotations

- `Paid` 💰  - 付費應用程式
- `IAP` 💰 - 包含應用內購買
- `Ads`  - 包含廣告
- `Proprietary`  - 缺少許可證或閉源軟體
- `n-day trial` - - `n`天后需要付款
- `Root` - 需要在Root模式下執行Shizuku

--------------------

## License

本列表採用[Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) 許可協議。

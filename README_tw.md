# awesome-shizuku

### 語言
[English](/README.md) | [简体中文](/README_cn.md) | 繁體中文

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku 允許普通應用程式在非root 裝置上使用 ADB 直接使用權限提升的系統 API。本列表彙集了一些已知可利用 Shizuku 功能的應用程式。

更多詳情：https://shizuku.rikka.app/

歡迎拉取請求。有關提示，請參閱 [貢獻](CONTRIBUTING.md)。專有應用程式已列於另一個檔案中。詳情請參閱 [下方](#closed-source-apps)。

> [!NOTE]
> 若要掌握此列表的最新動態，[你可以查看每日更新日誌](https://github.com/timschneeb/changelog-awesome-shizuku)。

<table>
  <tr>
    <td>
      <h2>Shizuku 應用程式商店</h2>   
      <p>
      本列表現已作為一個名為 ShizuStore 的開源 Android 應用程式商店提供。<br/>
        <a href="https://github.com/timschneeb/ShizuStore">下載與原始碼可在 GitHub 上取得。</a>
      </p>
      你可以依分類瀏覽所有 Shizuku 應用程式，依最近新增、GitHub 星號數、下載次數或更新日期排序，並透過 Shizuku 無聲安裝或更新 APK。
      APK 直接從官方開發者透過 GitHub、GitLab、F-Droid 及其他來源下載。
      <br><br>
      <a href="https://github.com/timschneeb/ShizuStore"><img src="https://raw.githubusercontent.com/Kunzisoft/Github-badge/main/get-it-on-github.png" width="240" alt="在 GitHub 上取得"></a>
    </td>
    <td align="right">
      <img src="https://raw.githubusercontent.com/timschneeb/ShizuStore/master/fastlane/metadata/android/en-US/images/phoneScreenshots/2.png" width="800" alt="依分類瀏覽 Shizuku 應用程式">
    </td>
  </tr>
</table>

--------------------


## 目錄

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


* [Porter](https://github.com/d4rken-org/porter) - 精簡且持續維護的 Shizuku 分支，為應用提供 ADB 存取權限並可選支援 root，還為僅支援 Shizuku 的應用提供相容性配套應用 `Apache-2.0`
* [shevery](https://github.com/HmnDev-Tech/shevery) ✨ - Material 3 分支，支援自啟動、TCP 模式、Dhizuku、模組，以及內建整合 AI 的終端
* [Shizako](https://github.com/cr1437/Shizako) - 貓娘形象版 Shizuku，可無縫替代官方管理器，官方 Shizuku-API 應用無需修改即可連線（功能與 shevery 類似） `Apache-2.0`
* [Shizuku (thedjchi's fork)](https://github.com/thedjchi/Shizuku) - Shizuku 分支，支援自啟動、TCP 模式和隱身模式（目前暫停維護） `Apache-2.0`
* [ShizukuPlus](https://github.com/thejaustin/ShizukuPlus) - Shizuku 分支，為開發者提供擴充 API，並支援自啟動、TCP 模式、Dhizuku 等 `Apache-2.0`
* [Stellar](https://github.com/roro2239/Stellar/blob/main/README_en.md) - 另一個 Shizuku 實作，支援自啟動、TCP 模式和簡易終端（可在啟動時自動執行命令） `MPL-2.0`
* [Xhizuku](https://github.com/xeonleonreal/Xhizuku) - Maintained Shizuku fork with Material 3 Expressive UI, ADB module runner, onboarding wizard, server monitor and built-in diagnostics `Apache-2.0`

### AI agents

* [Aether](https://github.com/Zhou-Shilin/Aether) - 在地化、可擴充的通用 AI 代理，適用於 Android、iOS 和 macOS，可選整合 Shizuku 和 Termux 以直接控制裝置。 `GPL-3.0`
* [AndroidHarness](https://github.com/Sanuu7/AndroidHarness) - 裝置端程式設計代理，透過 Shizuku shell UID 轉發特權命令，並以 `termux-` 為前綴的 Linux 工具鏈作為備援方案。 `MIT`
* [AutoXiao'er](https://github.com/Joy-word/AutoXiaoer) - 裝置端 AI 代理，以視覺方式操作 Android 應用程式，支援排程、通知和 ClawBot 任務觸發；同時支援 Shizuku 與無障礙控制。 `MIT`
* [ClawGUI](https://github.com/ZJU-REAL/ClawGUI) - 裝置端 GUI 代理執行器，可在單部手機上部署完整的 ClawGUI 模型堆疊，並透過 Shizuku 控制。 `Apache-2.0`
* [Hermes Agent](https://github.com/adybag14-cyber/hermes-agent) - Hermes Agent 的 Android 移植版，透過 Shizuku 特權 shell 橋接在裝置上執行操作。 `MIT`
* [OmniBot](https://github.com/omnimind-ai/OmniBot) - 裝置端 AI 代理，具備終端、網頁瀏覽、裝置控制和系統整合能力 `GPL-3.0`
* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - 使用 AutoGLM 視覺語言模型在裝置上自動執行操作 `GPL-3.0`
* [OpenCyvis](https://github.com/opencyvis/opencyvis-phone) - 開源 AI 手機助手，能識別螢幕並根據自然語言任務操作應用，可在背景執行 `Apache-2.0`
* [OpenDroid](https://github.com/yashab-cyber/opendroid) - 開源自主式裝置端 AI 代理，透過螢幕自動化規劃並執行多步驟任務 `Apache-2.0`
* [OpenMinis](https://github.com/OpenMinis/OpenMinis) - AI 代理，具備 Linux shell、瀏覽器自動化，並透過 Shizuku 控制系統 `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - Android 上最強大的 AI 代理與 AI 聊天軟體。可使用 Shizuku 執行命令 `LGPL-3.0`
* [rish-mcp](https://github.com/turin-dev/rish-mcp) - 透過出站 WebSocket 中繼，將 Android 裝置的 Shizuku shell 作為 MCP `run_shell` 工具提供給 AI——無需 VPN、ADB 或 sshd，即可從 Claude 或任意 MCP 用戶端執行 shell 命令 `MIT`
* [roubao](https://github.com/Turbo1123/roubao/blob/main/README_EN.md) - 基於視覺語言模型的開源裝置端 AI 手機自動化助手，透過 Shizuku 系統權限執行任務，無需電腦。 `MIT` [(原始碼)](https://github.com/Turbo1123/roubao)
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - 基於 AutoGLM 的自動化與多工框架。可建立虛擬螢幕供代理執行應用，並使用多視窗 `Apache 2.0`
* [talon](https://github.com/thefalconry/talon) - Multi-platform agentic AI harness for Telegram/Discord/Teams/terminal with a Flutter companion app; Shizuku enables silent self-updates and elevated access. `Apache-2.0`
* [Zafiro](https://github.com/niki914/zafiro) - 自帶 API Key 的 AI 代理，透過 Shizuku 讀取螢幕並控制裝置，無需 root。 `MIT`

### Android Auto

* [Flywheel](https://github.com/Benjamin-Wiegand/Flywheel) - 針對去 Google 化手機的自由開源 Android Auto 替代方案，相容現有車機；Shizuku 用於應用嵌入和通話音訊擷取。 `GPL-3.0`

### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - 專為 Android TV 設計的 F-Droid 用戶端 `GPL-3.0` [(原始碼)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - 專為 Android TV 設計的檔案管理器和壓縮檔檢視器 `GPL-3.0` [(原始碼)](https://github.com/mlm-games/fluffy)
* [RecentAppsTV](https://github.com/Qutaiba-Khader/RecentAppsTV) - Android TV 的最近使用應用程式懸浮介面 `Propietary`
* [TVPilot](https://github.com/mahmutaunal/TVPilot) - 專為 Android TV / Google TV 設計的遙控優先系統控制與應用程式管理工具，可選透過 Shizuku 執行進階操作 `Apache-2.0`

### Audio

* [allEQ](https://github.com/omixin/allEQ) - 無需 root 的 10 段系統均衡器，透過 Shizuku 攔截輸出混音音訊工作階段。 `GPL-3.0`
* [android-realtime-voice-isolation](https://github.com/sk2andy/android-realtime-voice-isolation) - 使用 Shizuku、GTCRN 和 ONNX Runtime 的裝置端即時語音隔離 `MIT`
* [Castix](https://github.com/elhizazi1/Castix) - 管理背景播放限制，並新增 AMOLED 純黑關螢幕時鐘，支援 Shizuku、Dhizuku、root、LSPosed 或無障礙等多種後端。 `GPL-3.0`
* [centuryplay](https://github.com/g8row/centuryplay) - Streams Android system audio to AirPlay 1/2 speakers; optional Shizuku mode provides silent-phone capture via AudioPolicy loopback and removes capture prompts. `AGPL-3.0`
* [finevolume](https://github.com/broknhrt2562/finevolume) - Pixel-style volume panel with 120-step precision plus per-app and per-stream volume control, using a Shizuku high-precision audio proxy. `Apache-2.0`
* [MicUp](https://github.com/papergray/MicUp) ✨ - 適用於 Android 的即時麥克風音訊處理 `MIT`
* [Mixer (1)](https://github.com/farizanjum/mixer-1) - 攔截硬體按鍵的各應用音量懸浮視窗 `Proprietary`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - 針對非 root Android 裝置的系統級 JamesDSP 音訊處理引擎的實作 `GPL-3.0` [(原始碼)](https://github.com/timschneeb/RootlessJamesDSP)
* [Spotify Ad Skipper](https://github.com/sihooney/spotify-ad-skipper) - 監控 Spotify 通知，透過重新開始播放自動跳過廣告，並使用 Shizuku 從背景重新啟動 `Proprietary`
* [Volume++](https://github.com/noel-digital-fan/volume_plus_plus) - 自訂音量面板，可透過 Shizuku 或 root 進行各應用音訊混合 `MIT`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - 獨立控制每個應用的音量 `GPL-2.0`
* [wecho](https://github.com/qumolangmo/wecho) - 用於全域音訊效果處理的 Android 應用 `GPL-3.0`

### Automation

* [Argus](https://github.com/JackRushante/argus) - Tasker 等級的 Android 自動化工具，由 LLM 將自然語言規則編譯為確定性引擎，可選配 Shizuku shell 閘道。 `GPL-3.0`
* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - 基於 JavaScript 的自動化工具 `MPL-2.0`
* [AutoSlide](https://github.com/tianxing-ovo/AutoSlide/blob/master/README.en.md) - 自動滑動工具，可自動播放短影片和自動翻頁閱讀，並帶有懸浮控制 `Apache-2.0` [(原始碼)](https://github.com/tianxing-ovo/AutoSlide)
* [flowpilot](https://github.com/emi-ran/flowpilot) - 隱私優先的離線自動化引擎，透過 Shizuku 執行行動數據、飛航模式和深色主題等特權系統操作。 `GPL-3.0`
* [IMD](https://github.com/soul-99/SU_IMD) - Geto 的分支，可針對銀行等限制嚴格的應用隱藏開發者選項、ADB、無障礙服務和 Shizuku 本身，之後還能還原 `GPL-3.0`
* [NexaFlow](https://github.com/Alaa91H/NexaFlow) - 情境感知的 Android 自動化引擎，結合觸發器、約束和動作，並透過 Shizuku 執行特權裝置控制。 `MIT`
* [Nothing_Modes](https://github.com/Dvorinka/Nothing_Modes) - 適用於 Nothing 手機的自動化應用（模式、日常程序、Glyph），也可在其他 Android 裝置上執行，可選支援 Shizuku `GPL-3.0`
* [OpenTasker](https://github.com/SysAdminDoc/OpenTasker) - 本機優先的開源 Tasker 替代品，規則易讀、權限提示透明；特權操作透過 Shizuku AIDL 使用者服務執行。 `MIT`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - 可針對特定生活情境自動或一鍵設定裝置 `Apache-2.0`
* [Service-Keeper](https://github.com/shaunkleyn/Service-Keeper) - 監控背景、無障礙和通知監聽服務，並在被系統終止後自動重新啟動它們。 `GPL-3.0`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Tasker 的輔助應用 `Propietary`
* [vFlow](https://github.com/ChaoMixian/vFlow/blob/master/README_EN.md) - 視覺化自動化工具，將點選、識別、分支和系統操作組合為易於上手的工作流 `GPL-2.0`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord 修改工具 `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - 一款簡單的應用，可在您偏好的 Bluesky 用戶端中自動開啟 Bluesky 連結 `MIT` [(原始碼)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CallVault](https://github.com/madkongo/CallVault) - 無需 root 的通話錄音器，支援裝置端轉錄/摘要；可透過內建 ADB 獨立執行，或選用 Shizuku 後端。 `GPL-3.0`
* [cally](https://github.com/LyoSU/cally) - 適用於搭載原生系統的 Pixel 6 及更新機型的通話錄音器，透過 Shizuku shell UID 音訊服務錄製雙向通話，無需 root 或解鎖 bootloader。 `GPL-3.0`
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - 透過藍牙傳送和接收檔案 `MIT` [(原始碼)](https://github.com/kmod-midori/CatShare)
* [ClipShare](https://clipshare.coclyun.top/) - 跨平台剪貼簿同步，支援文字、圖片、檔案和簡訊；Shizuku 可保持 Android 剪貼簿監聽器持續執行。 `GPL-3.0` [(原始碼)](https://github.com/aa2013/ClipShare/blob/master/README_EN.md)
* [GhostMode](https://github.com/Foxlape/GhostMode) - 讓手機在來電時表現為無法接通，同時保持 LTE/5G 資料連線 `Apache-2.0`
* [KDE Connect (Shizuku)](https://github.com/Batestinha/kdeconnect-android-shizuku) - 非官方 KDE Connect 分支，透過 Shizuku 和 AIDL 回呼在 Android 10+ 上新增自動背景剪貼簿同步。 `GPL-2.0`
* [KettuManager](https://github.com/C0C0B01/KettuManager) - Discord 修改工具。已廢棄的 BunnyManager 專案的延續 `OSL-3.0`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - 這是一款簡單的應用程式，可在您喜歡的 Lemmy 用戶端中自動啟動 Lemmy 連結。 `MIT` [(原始碼)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - 這是一個簡單的應用程式，可在您喜歡的 Mastodon 用戶端中自動啟動 fediverse 連結。 `MIT` [(原始碼)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord 修改工具。已廢棄的 Bunny-Manager 專案的另一延續 `OSL-3.0`
* [RivoPhoneApp](https://github.com/user-grinch/RivoPhoneApp) - Material 3 撥號與聯絡人應用，透過 Shizuku 實現無需 root 的通話錄音 `GPL-3.0`
* [ShizuCallRecorder](https://github.com/kitsumed/ShizuCallRecorder) ✨ - ShizuCallRecorder 藉助 Shizuku 提供的 ADB 權限，在未 root 的裝置上錄製通話！ `GPL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - 讓您透過簡訊瀏覽網頁的應用程式 `GPL-3.0`

### Customization

* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - 基於環境光的智慧深色模式 `GPL-3.0` [(原始碼)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - 將 Now Playing 從 Pixels 移植到其他 Android 裝置 `GPL-3.0`
* [android-perapp-language-selector](https://github.com/TakeruF/android-perapp-language-selector) - 在 Android 13+ 上無需 root 強制設定各應用語言，即使應用本身沒有內建語言選項 `Apache-2.0`
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - 使用指定應用程式時自動切換勿擾模式的簡單工具 `AGPL-3.0` [(原始碼)](https://github.com/im030/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - 管理 Android 手機各螢幕的自動旋轉 `GPL-3.0`
* [Capsulyric](https://github.com/FrancoGiudans/Capsulyric) - 透過 Android Live Update 和小米超級島在狀態列和鎖定畫面上顯示目前播放歌詞 `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name 是一個非常簡單的應用程式，用於變更未 root 的 Android 裝置上的電信公司名稱 `GPL-3.0`
* [cebian](https://github.com/qpst4/cebian) - 一體化的手勢與單手導航套件，包含邊緣面板、懸浮游標、離線 OCR 懸浮球、應用凍結，以及透過 Shizuku 實現的自由視窗。 `AGPL-3.0`
* [CleanBar](https://github.com/sachinmandawi/CleanBar) - 一鍵隱藏狀態列和系統圖示（時鐘、電池等），無需 root `MIT`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - 修改裝置 Material You 顏色的應用程式 `GPL-3.0`
* [Commander](https://github.com/astroboii47/Commander) - 鍵盤優先的命令欄和通知中心；使用 Shizuku 切換最近應用並執行特權 shell 控制。 `MIT`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - 更精細地自訂動畫速度 `GPL-3.0` [(原始碼)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ-Reborn](https://github.com/Arora-Sir/DarQ-Reborn) - 適用於 Android 10 及以上、可按應用選擇的強制深色模式選項 `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - 一些 Android 應用小工具和動態桌布 `GPL-3.0`
* [DevBay-Launcher](https://github.com/Zoder-Studio/DevBay-Launcher) - Developer-focused launcher with debug app sections, folders, gestures and Quick toggle chips for developer options, animations, fonts and wireless ADB via Shizuku. `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - 高度可自訂、基於手勢的 Android 啟動器，注重速度與效率 `GPL-3.0` [(原始碼)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - 並排視窗管理器、三星 DeX 替代品、彈出式應用啟動器 `Proprietary`
* [duo-open](https://github.com/marcoazeem/duo-open) - System-wide iPhone-Duo frosted-glass fold effect for book-style foldables, driven by the real hinge angle as an accessibility overlay or live wallpaper, with optional Shizuku. `MIT`
* [DuoFold-Android](https://github.com/jcx396905-gif/DuoFold-Android) - 全域 iPhone Duo 風格摺疊錯覺效果，利用 OpenGL ES 根據裝置運動重新投影整個螢幕，由 Shizuku 驅動。 `MIT`
* [EdgeGesture](https://github.com/Evilgodxu/EdgeGesture) - Edge-gesture app built on accessibility plus Shizuku: edge swipes, back-tap, floating music and task panels, freeform and app-kill actions. `AGPL-3.0`
* [essentials](https://github.com/sameerasw/essentials) ✨ - 適用於 Pixel 的必備工具、修改和變通方案，也相容其他裝置 `MIT`
* [expressive-cutout](https://github.com/EvanKoe/expressive-cutout) - 遵循 Material Expressive 設計的離線動態島，支援通知、即時圖塊和 Material You 顏色 `GPL-3.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - 在智慧型手機的 Android 作業系統上新增類似桌面的多視窗支援。 `GPL-3.0`
* [FreeformShell](https://github.com/bravoyush/FreeformShell) - 實驗性自由視窗管理器輔助工具，透過 Shizuku 系統 API 新增標題列、可調整大小的邊框和顯示縮放。 `Apache-2.0`
* [gama](https://github.com/palincat/gama) - 可透過設定 `debug.hwui.renderer` 系統屬性在 OpenGL 和 Vulkan 渲染器之間切換 `MIT`
* [Google-Shortcuts-Launcher](https://github.com/WSTxda/Google-Shortcuts-Launcher) - Launcher app-drawer shortcut hub for Google app features; Shizuku launches otherwise inaccessible Google components. `GPL-3.0`
* [GSplit](https://github.com/Salat39/GSplit) - Split-screen and freeform multi-window presets with scheduling, boot autostart and overlays; an optional Shizuku ADB shell configures splits. `Proprietary`
* [HyperBridge](https://github.com/D4vidDf/HyperBridge) - 透過將通知橋接到相機挖孔 UI，為 HyperOS 帶來原生 HyperIsland 體驗，支援主題和小工具 `Apache-2.0`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - 雙螢幕遊戲裝置啟動器。使用 Shizuku 將其中一個觸控式螢幕對應為手把輸入 `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - 允許使用者選擇個別應用程式的語言（Android 13+） `Apache-2.0`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - 使用 Material3 還原 Android 12 以前的 URL 應用程式連結選擇器 `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - 在鎖定畫面上顯示小工具。僅在 Android 13 及更高版本需要 Shizuku `MIT` [(原始碼)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - 如果原始裝置製造商（小米）不允許您在裝置的地區設定中新增額外的（或 "不支援的"）語言，那麼這款簡單的應用程式就能幫您達成這一功能。 `MIT`
* [O.status](https://github.com/CATCHINGL/O.status) - 簡潔的狀態列指示器，用於 Wi-Fi、行動網路和電池，可選整合 Shizuku 以配合系統圖示顏色。 `Proprietary`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - 鍵盤優先的 Android 命令面板，將應用/裝置搜尋和系統工具統一到懸浮介面中 `GPL-3.0`
* [Renoir](https://github.com/exaclast/renoir) - Material You 主題設計工具，透過 Shizuku shell 命令應用自訂覆蓋層。 `Proprietary`
* [SetEditPlus](https://github.com/kerneldroid/SetEditPlus) - Android System/Secure/Global 設定表編輯器，支援 Shizuku/Root 模式、變更追蹤和開機後持續套用。 `Proprietary`
* [sharemove](https://github.com/thejaustin/sharemove) - 透過 Shizuku 或 root 暫停或停用元件，將應用從 Android 的分享、「開啟方式」和 APK 安裝器選擇介面中隱藏。 `GPL-3.0`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - 為 shell 命令建立啟動器捷徑 `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - 包含一些易於使用的工具，超越 Android 系統允許的控制層級 `GPL-3.0`
* [Smart Dock](https://f-droid.org/packages/cu.axel.smartdock/) - 將手機變為桌面環境，提供工作列、最近應用和開始選單 `GPL-3.0` [(原始碼)](https://github.com/axel358/smartdock)
* [Smart Edge](https://f-droid.org/en/packages/com.imi.smartedge.sidebar.panel/) - 受 OriginOS 啟發的高度可自訂 Android 側邊面板 `MIT` [(原始碼)](https://github.com/Imtiaz-Official/Smart-Edge)
* [Smart Island](https://github.com/agupta07505/SmartIsland) - 輕量級 Android 懸浮介面，將通知、通話和媒體播放彙集為可快速瀏覽的懸浮島 `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Smartspacer 外掛 `GPL-3.0`
* [SuperShade](https://github.com/thejaustin/SuperShade) - 通知面板替代品，透過 Shizuku shell 命令控制亮度、狀態列展開和電源操作。 `Proprietary`
* [SysReadout-Launcher](https://github.com/AndSni/SysReadout-Launcher) - Terminal-style launcher that turns the home screen into a live system monitor with pinned status rows, process/connection/DNS tables and an event log, reading system data through Shizuku. `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - 檢視和修改 Android 裝置上的隱藏設定 `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - 將裝置背面的雙擊功能從 Android 12 移植到任何 Android 7.0+ 裝置 `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - 清除分享連結中的追蹤參數，支援自訂 URL 重寫規則 `GPL-3.0` [(原始碼)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - 使用開始選單存取應用程式。Shizuku 可解鎖其他功能 `Apache-2.0` [(原始碼)](https://github.com/farmerbb/Taskbar)
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU 和電池小工具 `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - 適用於 Android 的完整桌面體驗層 `GPL-3.0`

### Development utilities

* [80bee-app](https://github.com/Endda/80bee-app) - 無需 root 的裝置端 ADB/Fastboot 工具箱：透過 Shizuku 實現啟動模式、DPI、DNS、應用精簡和繞過 sideload 安裝限制，還支援 USB-OTG 主機模式。 `Apache-2.0`
* [ActivityLauncherShizukuPlugin](https://github.com/ActivityLauncher/ActivityLauncherShizukuPlugin) - 基於 Shizuku 的 [Activity Launcher](https://github.com/butzist/ActivityLauncher) 外掛，可啟動私有（未匯出）Activity。 `GPL-3.0`
* [ActivityManager](https://github.com/sdex/ActivityManager) - 無需 root 直接啟動隱藏和未匯出的 Activity `Apache-2.0`
* [ADB Captain](https://github.com/eatenlamp/adbcaptain) - 透過 Shizuku 執行 shell 命令、應用管理和日誌存取的 ADB 工具箱，無需 root。 `AGPL-3.0`
* [Android Code Studio](https://github.com/AndroidCSOfficial/android-code-studio) - 用於建置基於 Gradle 的 Android 專案的裝置端 IDE；Shizuku 可在建置後無聲安裝 APK。 `GPL-3.0`
* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - 匯出已為使用者註冊帳號的應用程式套件名稱。 `Proprietary`
* [Cosmic-IDE](https://github.com/aload0/Cosmic-IDE) - 用於 JVM 開發的 IDE。使用 Shizuku 作為嵌入式 shell `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - 使用 Shizuku 備份/還原可偵錯應用的私有資料 `GPL-3.0`
* [DEVTools](https://github.com/MetxStudio/DEVTools) - 一體化 Android 開發工具箱：終端、感測器監視器、應用/檔案管理器，以及 Shizuku shell 助手。 `MIT`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - 一個簡單的應用程式，旨在幫助使用者透過 DSU 的 Android 功能輕鬆安裝 GSI。 `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - 修復了 HostProfile 應用程式和 WorkProfile/DualApp/MultiApp 之間的 MediaStore 和檔案 IO 相容性問題。 `Proprietary`
* [FPS-Meter-Android](https://github.com/rdevz-ph/FPS-Meter-Android) - 受三星 Perf Z 啟發的高效能輕量 FPS 監控懸浮視窗，適用於遊戲和效能測試 `MIT`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - 帶圖表的 FPS 檢視懸浮視窗 `Proprietary`
* [FrameX-Android](https://github.com/MaheshSharan/FrameX-Android) - 適用於 Android 的即時效能懸浮視窗 `MIT`
* [get_event](https://github.com/lalakii/get_event) - 讀取 /dev/input/event* `Proprietary`
* [IntentX](https://github.com/wxxsfxyzm/IntentX) - Explores installed apps and activities and crafts, tests and launches intents with normal, root or Shizuku access; saves intents as shortcuts. `GPL-3.0`
* [LibChecker](https://github.com/LibChecker/LibChecker) - 用於檢視裝置上的應用程式中所用函式庫的應用程式。使用 Shizuku 確定其他應用程式的安裝來源。 `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - 另一個適用於 Android 的 logcat 閱讀器 `GPL-3.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - 利用 Shizuku 呼叫 AppOps API，實現精細的應用權限控制 `MIT`
* [panda-ide](https://github.com/ferelking242/panda-ide) - 行動裝置優先的 Flutter IDE，包含程式碼編輯器、PTY 終端、Git 和 VS Code 擴充功能；Shizuku 橋接提供 ADB 級 shell，用於在裝置上執行 flutter run。 `MIT`
* [roamer](https://github.com/eigenlux-ai/roamer) - 開發者工具，可透過 Shizuku 覆寫 SIM 的 ISO 國碼和電信業者名稱，並可選擇同步各應用程式的地區設定。 `MIT`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - 啟動/互動（未）匯出的活動、服務和接收器。支援 Shizuku 和 root。 `GPL-3.0` [(原始碼)](https://github.com/zacharee/RootActivityLauncher)
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - 用於切換無線偵錯的小工具和快速設定圖塊（與 KDE Connect 整合） `GPL-3.0`

### Device owner (DPM)

* [Déchaîner](https://github.com/warleysr/dechainer) - 以裝置擁有者身分封鎖成人內容；Shizuku 執行 dpm set-device-owner 設定命令。 `Apache-2.0`
* [Dhizuku](https://github.com/iamr0s/Dhizuku) - 受 Shizuku 啟發的應用程式，允許將 DeviceOwner 權限分享給第三方應用程式 `GPL-3.0`
* [harbor](https://f-droid.org/packages/com.monstera.harbor/) - 工作資料管理器，可選配 Shizuku 工具實現自動化 `Apache-2.0` [(原始碼)](https://github.com/Stem0794/harbor)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - 使用裝置擁有者權限管理您的裝置 `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - OwnDroid 的分支，增加了額外功能 `GPL-3.0`

### Display management
* [Adaptive-Hz](https://github.com/mahmutaunal/Adaptive-Hz) - 根據使用者互動在 60Hz 和 120Hz 之間自動切換顯示更新率。專為不支援真正自適應更新率的三星裝置設計 `MIT`
* [akiHz](https://github.com/anlaki-py/akihz) - 輕量級更新率切換器，具備快速設定圖塊、自動更新率偵測和懸浮 FPS 監視器 `MIT`
* [android-display-extend](https://github.com/jqssun/android-display-extend) ✨ - 適用於實體和虛擬顯示器的顯示管理器，內建虛擬觸控式螢幕。非常適合在 PC 上配合 `scrcpy --new-display` 使用 `GPL-3.0`
* [android-display-mirror](https://github.com/jqssun/android-display-mirror) ✨ - 螢幕鏡射中心，支援透過 AirPlay、Moonlight/Sunshine 和 DisplayLink 分享螢幕內容 `GPL-3.0`
* [BetterNightLight](https://github.com/paulsnuff/BetterNightLight) - Grants advanced control over Android's native Night Light: scheduling, boost phases and precise colour temperature through Shizuku or root secure-settings access. `GPL-3.0`
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - 將手機變為觸控板和鍵盤，用於控制在外接有線顯示器上執行的單個應用 `GPL-3.0`
* [Dextop](https://github.com/NarYuki/Dextop) - 使用三星 DeX 或 Shizuku 的桌面環境，支援多工和自訂解析度 `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - 在可摺疊裝置上的各種螢幕摺疊狀態之間切換 `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - 讓手機大部分時間保持單色，但允許相機等應用顯示彩色 `GPL-3.0`
* [magicdesk](https://github.com/mekhontsev/magicdesk) - 開源 Android 15+ 工作站，透過 Shizuku 提供原生視窗、外接顯示器、桌面和 Termux 整合 `GPL-3.0`
* [PortalPad](https://github.com/Smart-Home-User/PortalPad) - 將手機變為觸控板、空中滑鼠和遙控器，用於 AR 眼鏡、顯示器和電視等外接顯示裝置 `MIT`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - 為 Android 裝置提供更好的螢幕鏡射 `Apache-2.0` [(原始碼)](https://github.com/farmerbb/SecondScreen)
* [Tideo Auto Brightness](https://github.com/faded-penguin021/Tideo-Auto-Brightness) - 可解釋的自適應亮度替代方案，決策透明並支援晝夜節律。 `MIT`

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi 的分支，具有動畫支援和使用 Shizuku 的外掛管理。 `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - 匯出從 Android 版嗶哩嗶哩下載的影片 `GPL-3.0` [(原始碼)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - 將嗶哩嗶哩快取檔案合併並匯出為 MP4，支援手機和電腦用戶端 `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - 使用 Shizuku 進行外掛管理的漫畫閱讀器。Tachiyomi 的獨立後繼者。 `Apache-2.0`
  * Mihon/Tachiyomi 還有其他幾個活躍的分支，包括 [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) 和 [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [Buge-Files](https://bugestudio.website/files/) - Material 3 Expressive 檔案管理器，除儲存瀏覽和管理外，還可透過 Shizuku 安裝 APK。 `GPL-3.0` [(原始碼)](https://github.com/BugeStudioTeam/Buge-Files)
* [Butler](https://github.com/d4rken-org/butler) `IAP` 💰 - 針對高階使用者的快速、私密檔案瀏覽器，具備標籤頁、回收站、正規表達式搜尋、應用管理以及 root/Shizuku 支援 `GPL-3.0`
* [FileExplorer](https://github.com/SysAdminDoc/FileExplorer) - 支援本機、root、壓縮檔、網路共用、雲端、保險庫和儲存分析的檔案管理器 `MIT`
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - 專為 Android TV 設計的檔案管理器和壓縮檔檢視器 `GPL-3.0` [(原始碼)](https://github.com/mlm-games/fluffy)
* [immich-cloud-media](https://github.com/Dreaming-Codes/immich-cloud-media) - 雲端媒體提供者，在 Android 系統相片選取器中顯示自託管的 Immich 媒體庫，可透過 Shizuku 或 ADB 設定。 `GPL-3.0`
* [KArchiver](https://github.com/sysrv64/KArchiver) - 以封存為核心的 Android 檔案管理器：瀏覽儲存空間，無需解壓縮即可開啟並就地編輯 ZIP/TAR/7Z，可在檔案與封存內搜尋，並可選 Shizuku 或 root 引擎存取受限路徑 `GPL-3.0`
* [MaterialFiles](https://github.com/zhanghai/MaterialFiles) - 適用於 Android 的 Material Design 檔案管理器 `GPL-3.0`
* [MP-Manager](https://github.com/AbdurazaaqMohammed/MP-Manager) - Dual-pane Material file manager focused on APKs as an open-source MT Manager alternative, with root and Shizuku privileged file management. `GPL-3.0`
* [NFile](https://github.com/Senzme/NFile) - 使用 Shizuku 存取 Android 資料夾的檔案管理器 `GPL-3.0`
* [plain-app](https://github.com/plainhub/plain-app) - 自託管 Web 控制面板，可從瀏覽器管理檔案、媒體、聯絡人、簡訊和通話，並透過 Shizuku 執行特權簡訊刪除。 `AGPL-3.0`
* [RippleFiles](https://github.com/GokulSB/RippleFiles-FileManager) - Expressive Material 檔案管理器，支援本機和雲端儲存，並透過 Shizuku 存取 Android/data。 `MIT`
* [ROSE](https://github.com/NarayanChetri/ROSE) - 現代化檔案管理器，採用 Material 3 UI，支援壓縮檔、回收站，並可透過 Shizuku 無需 root 存取 Android/data 和 Android/obb。 `GPL-3.0`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE 是 Android 最徹底的清理工具 `GPL-3.0` [(原始碼)](https://github.com/d4rken-org/sdmaid-se)
* [sync-to-android-data](https://github.com/kamren-zirger/sync-to-android-data) - 在目標應用開啟或關閉時，同步 Android/data 受限資料夾中的檔案（匯入/匯出） `MIT`
* [twig](https://github.com/dev2ex/twig) - 體積優先的雙欄檔案管理器（約 7MB），支援本機、壓縮檔、FTP/SFTP/SMB/WebDAV/S3/restic/Jellyfin `GPL-3.0`
* [UnscopeMyData](https://github.com/kepatotorica/UnscopeMyData) - 使用 Shizuku 提升檔案存取權限，將應用資料移入/移出分區儲存資料夾。 `GPL-3.0`
* [XArchiver](https://github.com/Xtra-Manager-Software/XArchiver) - 內建壓縮檔支援的檔案管理器 `MIT`
* [XClean](https://github.com/utopiafar/XClean) - 基於規則的清理工具，具備普通、Shizuku 和 Root 三種引擎，用於清除應用垃圾。 `Proprietary`
* [XFiles](https://github.com/Local1stDotApp/XFiles) - 離線檔案管理器，支援 root 和 Shizuku，可完整存取檔案系統 `GPL-3.0`
* [ZenFile](https://github.com/l930203811/ZenFile) - NFile 的分支，內建遠端檔案伺服器支援 `GPL-3.0`
* [ZhuFiler](https://github.com/Artzhu86/ZhuFiler) - 開源 Material You 檔案管理器，具備壓縮檔、編輯器、媒體播放、APK 處理以及由 Shizuku 支援的特權存取。 `MIT`

> [!註]
> [點此查看更多檔案管理工具（閉源軟體）](pages/CLOSED_SOURCE_tw.md#file-management)

### Games

* [ADOFAI-Key-Viewer-Mobile](https://github.com/QuyetGD-15/ADOFAI-Key-Viewer-Mobile) - Overlay key visualizer for ADOFAI and rhythm games; reads hardware input events through Shizuku getevent for ultra-low-latency touch visualization, KPS tracking and click counting. `Proprietary`
* [Ascent](https://github.com/4o3F/Ascent) - 用於取得米哈遊遊戲抽卡歷史連結的工具  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - 《BrownDust II》Mod 管理器 `Proprietary`
* [Cinderbox-Companion](https://github.com/ObfuscatedVoid/Cinderbox-Companion) - 《星露谷物語》Android 版配套應用，支援 Steam 雲端存檔同步、遊戲檔案下載和 SMAPI Mod 管理 `MIT`
* [CloudSync-Mobile](https://github.com/StardewValleyMods/CloudSync-Mobile) - 可在多臺裝置間同步《星露谷物語》存檔的應用 `GPL-3.0`
* [ex-astris-save-editor](https://github.com/Ncorror/ex-astris-save-editor) - Unofficial Ex Astris save editor: inventory editing, verified backups and Arknights skin switching, with automatic save discovery through Root or Shizuku. `GPL-3.0`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - 管理「洛杉磯犯罪」遊戲的地圖、桌布和螢幕截圖 `GPL-3.0`
* [linkura-localify](https://github.com/ChocoLZS/linkura-localify) - 《Link！Like！LoveLive！》的在地化外掛，透過 LLM 翻譯遊戲文字 `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - 遊戲「Last Origin」的 Mod 管理器 `Proprietary`
* [MAA-Meow](https://github.com/Aliothmoon/MAA-Meow/blob/main/README_EN.md) - 在 Android 上原生執行 MAA，一鍵完成《明日方舟》每日任務，支援前景和背景模式 `AGPL-3.0`
* [mt-en-applier](https://github.com/Aikiooo/mt-en-applier) - 《無職轉生》手遊非官方英文補丁的一鍵安裝器，透過 Shizuku 複製檔案，無需 root 或電腦。 `Proprietary`
* [Nibnya](https://github.com/yinghuajimew/Nibnya) - 適用於 Minecraft 基岩版的 Android NBT 編輯器，由 Shizuku 提供 /data 存取權限 `AGPL-3.0`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - 用於在地化 Android 版《CHAOS;CHILD》視覺小說的配套應用 `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - 輕鬆匯入與分享 Polyfield 地圖 `GPL-3.0`
* [pogoplusle](https://github.com/Mygod/pogoplusle) - 連線 Pokémon GO Plus 時跳過配對對話方塊 `Apache-2.0`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - 《原神》自動對話點擊器 `MIT`
* [stalker](https://github.com/onerdna/stalker) - 《暗影格鬥 2》存檔檢視與編輯器 `GPL-3.0`
* [SwiftSense](https://github.com/itsmelissadev/SwiftSense) - 遊戲調優工具，使用 Shizuku 凍結背景應用、停用套件並提高感測器取樣率。 `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order 遊戲翻譯專案 `MIT`

### Input methods

* [8bitdo-xbox-bridge](https://github.com/BoredNewCoder/8bitdo-xbox-bridge) - 透過逆向工程的 GIP 協定和 Shizuku uinput 注入，讓 8BitDo Ultimate Xbox 有線控制器在 Android TV 上作為真正的全域手把使用。 `MIT`
* [BiBi Keyboard](https://github.com/BryceWG/BiBi-Keyboard/blob/main/README_EN.md) - AI 語音輸入法鍵盤；Shizuku 或 root 可保持其懸浮球和音量鍵背景服務存活。 `Apache-2.0`
* [ButtonSilencer](https://github.com/EithonX/ButtonSilencer) - 封鎖故障耳機及入耳式耳機（IEM）的線控按鈕，同時不影響手機自身按鍵；Shizuku 為關閉螢幕時的耳機輸入保護提供特權通道。 `MIT`
* [C9](https://github.com/austinauyeung/C9) - 在傳統游標之外提供高效的網格游標。僅在 Android 11 上需要 Shizuku。 `Apache-2.0`
* [GameShift](https://github.com/tientien17/GameShift) - 遊戲手把連線時自動切換預設桌面啟動器，斷開時恢復；使用 Shizuku，無需 root。 `Apache-2.0`
* [Joycon2Android](https://github.com/JoeGeC/joycon2android) - 透過 BLE 連線 Nintendo Switch 2 Joy-Con 控制器，並透過 Shizuku UHID 中繼將其用作全域虛擬手把。 `GPL-3.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - 一款 Android 應用程式，可改變您裝置上按鈕的功能！ `GPL-3.0` [(原始碼)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - 在 Android 裝置上使用滑鼠和鍵盤玩遊戲；遊戲按鍵對應工具 `Apache-2.0`
* [OpenMapper](https://github.com/kinou-p/android-open-mapper) - 免費開源的遊戲手把按鍵對應工具，使用 Shizuku 進行亞毫秒級延遲的觸控注入；Mantis 和 Panda 的替代品。 `PolyForm-Noncommercial-1.0.0`
* [pastiera](https://github.com/palsoftware/pastiera) - 專為實體鍵盤裝置設計的 Android 鍵盤。使用 Shizuku 實現觸控板手勢 `GPL-3.0`
* [Steam Controller for Android](https://github.com/SonicDX12/SteamController-Android) - 透過由 Shizuku 支援的 Linux uinput，將 Steam Controller 2026 用作真正的 Android 手把；支援 USB、接收器或 BLE。 `MIT`
* [TitanPad](https://github.com/sztupy/TitanPad) - 將 Titan2 實體鍵盤的電容輸入轉換為滑鼠和滾動手勢。使用 Shizuku 讀取觸控板輸入並設定虛擬 HID 裝置 `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - 適用於 Android x86 的鍵盤對應器 `GPL-3.0`


### Installer & app stores

* [APKUpdater](https://github.com/DmitryN71/apkupdater) - APKUpdater 分支，在其 APKMirror、Aptoide、F-Droid 和 IzzyOnDroid 來源之外，新增基於 Shizuku 的無聲安裝。 `GPL-3.0`
* [AuroraDroid](https://f-droid.org/packages/com.aurora.adroid/) - 自由開源的 F-Droid 用戶端，支援透過 Shizuku/root 無聲安裝和自動更新 `GPL-3.0` [(原始碼)](https://gitlab.com/AuroraOSS/auroradroid)
* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - Google Play 商店的開源替代品，注重隱私且設計現代 `GPL-3.0` [(原始碼)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - 輕鬆下載、安裝和分享模組 `Proprietary`
* [Discoverium](https://github.com/cygnusx-1-org/Discoverium) - Obtainium 分支，用於從來源發現並安裝應用，支援 Shizuku、Dhizuku 和 Sui 安裝後端。 `GPL-3.0`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid 用戶端 `GPL-3.0` [(原始碼)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater：重視隱私的瀏覽器的更新程式 `GPL-3.0` [(原始碼)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F-Droid 用戶端 `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - 用於 GitHub Release 的應用商店，具備發現功能 `Apache-2.0` [(原始碼)](https://github.com/kurikomi-labs/komi-store)
* [instafel](https://github.com/mamiiblt/instafel) - Instafel（Instagram Mod）的更新應用 `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - 現代且實用的 Android 應用安裝程式替代品 `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - 簡單的應用程式使用 Shizuku 在裝置上安裝 APK，並提供高階選項 `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - IzzyOnDroid F-Droid 儲存庫的非官方用戶端 `GPL-3.0`
* [KingInstaller](https://github.com/fcaronte/KingInstaller) - APK 安裝器，可偽裝成 Play 商店安裝器身分以繞過應用可見性限制，支援透過 intent、Shizuku 或 root 安裝 `GPL-3.0`
* [LocalAndroidStore](https://github.com/SysAdminDoc/LocalAndroidStore) - 私有應用目錄，可安裝經過簽名的 GitHub 和 F-Droid 版本，可選透過 Shizuku 持有的安裝工作階段進行安裝。 `MIT`
* [multistore](https://github.com/FedeFluork/multistore) - 將第三方應用商店聚合為一個目錄，用於搜尋、比較、下載和更新 APK `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - 具有現代 UI 和大量額外功能的 F-Droid 用戶端 `GPL-3.0` [(原始碼)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - 直接從來源取得 Android 應用程式更新 `GPL-3.0`
  * [ObtainX](https://f-droid.org/packages/dev.bikram.obtainx/) - Obtainium 分支，重新設計了 Material 3 UI `GPL-3.0` [(原始碼)](https://github.com/bikram-agarwal/ObtainX)
* [Omnify](https://github.com/Victor-root/Omnify) - F-Droid 用戶端分支，還可安裝來自外部來源的應用，具備 Shizuku 安裝器和「支援 Shizuku」探索列。 `GPL-3.0`
* [OpenLoader](https://github.com/thebytearray/OpenLoader) - 為 Android 開發者驗證時代打造的 APK 安裝器，使用 Shizuku 執行特權安裝。 `GPL-3.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - Mod 應用商店 `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - 允許覆寫套件請求者和執行者的套件安裝程式 `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android 分割 APK 安裝程式 `GPL-3.0` [(原始碼)](https://github.com/Aefyr/SAI)
* [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch) - 由 Shizuku 驅動的應用管理器，支援無聲安裝、更新和批次操作 `GPL-3.0`
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - 輕量級應用安裝器替代品，支援分割 APK `Apache-2.0`
* [ShizuStore](https://github.com/timschneeb/ShizuStore) ✨ - Shizuku 應用商店。基於這份 awesome-shizuku 列表，直接從上游來源安裝 APK `GPL-3.0`
* [tern](https://github.com/munzzyy/tern) - Obtainium-style updater that verifies package name, signing certificate and publisher checksums before installing via Shizuku, Dhizuku, root or the system installer on phones, tablets and TV. `GPL-3.0`
* [universal-installer](https://github.com/pass-with-high-score/universal-installer) - 安裝和管理 APK 套件，支援分割 APK、透過 Shizuku 無聲安裝以及 VirusTotal 惡意軟體掃描 `GPL-3.0`
* [Vyxel Apps](https://github.com/NikhilKain/vyxel-apps) `IAP` 💰 - 由 GitHub 支援的應用商店，具備簽名驗證和透過 Shizuku 的無聲安裝。 `AGPL-3.0`
* [yuki](https://github.com/carlelieser/yuki) - Catalog and storefront for open-source Shizuku apps, crawled from GitHub `MIT`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - Android 內建 `dex2oat` 工具的圖形介面，可重新最佳化已安裝應用的 DEX 程式碼 `Apache-2.0`
* [CaptureCap](https://github.com/yepgoryo/CaptureCap) - 螢幕和音訊錄製及串流應用，無需 root `MIT`
* [Fern](https://github.com/wized2/Fern) - Material 3 live system monitor for CPU, RAM, storage, battery, thermal and network, with an optional Shizuku shell for elevated readings. `Proprietary`
* [ghostlock-app](https://github.com/YuKongA/ghostlock-app) - One-tap CVE-2026-43499 privilege-escalation app granting temporary uid 0 across many stock devices; Shizuku-required kernel profiles run through a shell Shizuku. `Apache-2.0`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - 找出狀態列鬧鐘圖示處於作用中的原因 `Proprietary`
* [IrisShot](https://github.com/raging-flames/IrisShot) - 適用於 Android 遊戲的長截圖工具，使用 MediaProjection 或由 Shizuku 驅動的 shell 截圖自動滾動並拼接長截圖。 `Proprietary`
* [KeiOS](https://github.com/hosizoraru/KeiOS) - 系統工具主控台，內建本機 MCP 伺服器、GitHub 發行追蹤，可透過 Shizuku 或 root 執行特權安裝，並提供 Blue Archive 輔助工具 `Apache-2.0`
* [kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) - Home Assistant 專用展示模式：語音衛星、同步音樂和照片螢幕保護程式，並使用 Shizuku 執行特權 APK 更新和裝置橋接。 `Proprietary`
* [krude](https://github.com/KusStar/krude) - 多合一應用程式和工作流程啟動器 `MIT`
* [Mafza](https://github.com/yshalsager/Mafza) - 緊急操作執行器，支援單一可設定設定檔、外部緊急觸發器以及安全的試執行模式 `Proprietary`
* [NekokoLPA2](https://github.com/iebb/NekokoLPA2) - 跨平台 eSIM/eUICC 管理器；在 Android 上透過 Shizuku 開啟僅 shell 可用的 QRTR 通訊端，以執行 Telephony/TMAPI 設定檔操作 `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - 使用 Shizuku 讓通知保持常駐/無法清除的 Android 工具 `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - 離開選定應用時自動關閉它們，以節省電量和記憶體 `Apache-2.0`
* [overlay-translator](https://github.com/ciddwd/overlay-translator) - 適用於遊戲、視覺小說和漫畫的即時螢幕翻譯器，支援裝置端/雲端 OCR 和懸浮視窗 `Apache-2.0`
* [PhoneDiagnosticTool](https://github.com/ScoobyDouche/PhoneDiagnosticTool) - 裝置端手機診斷工具，涵蓋 CPU、GPU、電池、RAM、儲存、感測器和螢幕，可選透過 Shizuku/root 提權讀取。 `MIT`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - 利用 CVE-2024-31317 進行 Zygote 注入，整合遠端終端和檔案傳輸功能 `MIT`
* [Rainy Screenshot](https://github.com/CATMIAOZHI/RainyScreenShot/blob/main/README_EN.md) - 透過 Shizuku 或 Porter 特權 shell 而非 MediaProjection 進行無聲截圖和螢幕錄製。 `Proprietary`
* [Screen Recorder](https://github.com/muhammadhaseebiqbal-dev/Screen-Recorder) - 螢幕錄製器，透過 Shizuku 擷取內部音訊。 `MIT`
* [silent-alarm](https://github.com/izumisagirii/silent-alarm) - 耳機優先的鬧鐘，在背景管控嚴格的 OEM ROM 上透過 Shizuku 或 root 看門狗重新啟動應用程式來保持鬧鐘運作。 `AGPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - 一個簡單的應用程式，用於透過 WearOS 手錶控制 Android 裝置 `Apache-2.0` [(原始碼)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - 透過 Telegram 訊息遠端控制裝置 `BSD 3-Clause`
* [VineOS](https://github.com/Hexadecinull/VineOS) - Android 虛擬機器引擎；Shizuku 探測 shell 權限，以支援無需 root 的 ADB 和無線偵錯路徑。 `GPL-3.0`

### Network

* [ADNS](https://github.com/eyalm2000/adns) - 適用於 Android 的 DNS 廣告攔截器 `MIT`
* [Bluetooth Bouncer](https://github.com/harvzor/android-bluetooth-bouncer) - 針對各個已配對裝置控制藍牙自動連線並保持配對；策略透過 Shizuku 強制執行。 `GPL-3.0`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - 可在 Android 上讀取基地台資訊 `MIT` [(原始碼)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - 無需 VPN 的應用防火牆；還可管理套件 `MIT`
* [delta](https://github.com/supershadoe/delta) - 使用 Shizuku 的熱點管理器 `BSD-3-Clause`
* [Dolphy-App](https://github.com/unvoiddd/Dolphy-App) - 用於無線協定研究的 NFC、BLE 和紅外線多功能工具 `GPL-3.0`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - 可透過藍牙遠端開啟熱點的應用——類似 Apple 的「接續互通」，但人人都能用 `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Google FindMyDevice 服務的安全且開源替代方案 `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - 雙模式防火牆：可使用 Shizuku、標準本機 VPN 介面或兩者同時阻止網際網路存取。 `MIT`
* [hikari-adblock](https://github.com/codegeasse1/hikari-adblock) - 無需 root 的廣告/追蹤器/惡意軟體攔截器，具備本機 VPN DNS 過濾以及 Shizuku iptables/nftables 防火牆模式 `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - 預覽和編輯 /etc/hosts 檔案 `MIT`
* [hotspot_channel_setter](https://github.com/Lorax121/hotspot_channel_setter) - Lists and applies the Wi-Fi hotspot SoftAP 2.4/5 GHz channel via Shizuku or root and persists the choice across reboots. `Proprietary`
* [MaybeEdgeScanner](https://github.com/maybeknott/MaybeEdgeScanner) - 路由配對網路掃描器，探測 TCP/TLS/HTTP 目標，可選 Shizuku 輔助的射頻診斷。 `AGPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - 一個在 Android 上執行 Naiveproxy 的簡單應用程式 `MIT`
* [NetManager](https://github.com/DottoXD/NetManager) - Material 風格的 4G/5G NR 行動網路監測工具，具備基地台地圖、路測和速度測試；Shizuku shell 橋接可解鎖額外網路資料。 `GPL-3.0`
* [NetSwitcher](https://github.com/nd4y/netswitcher) - 透過應用、捷徑、小工具或快速設定圖塊，使用 Shizuku 或 root 快速切換 Wi-Fi、行動數據和乙太網。 `Proprietary`
* [NetToggle](https://github.com/Dhangofa/NetToggle) - 輕量級 Android 快速設定圖塊，使用 Root 或 Shizuku 強制僅 5G、僅 4G 和偏好的網路模式 `GPL-3.0`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - 用於 4G/5G 網路模式切換的 Android 應用 `GPL-3.0`
* [nobita](https://github.com/duhow/nobita) - 使用 Shizuku 在裝置上將藍牙 HCI 流量記錄為 Wireshark 相容的 PCAPNG 檔案。 `Proprietary`
* [Quintz](https://github.com/corgilittlelegs/Quintz) - 無需 root 的 Wi-Fi 頻段鎖定和 BSSID 引導工具，透過 Shizuku 將 Android 固定在 5/6 GHz，具備 AP 遙測和射頻測向功能。 `MIT`
* [RKNHardering](https://github.com/xtclovver/RKNHardering) - 使用社群驗證的檢查在裝置上偵測 VPN/代理規避工具，並透過 Shizuku 或 Root 執行特權探測。 `AGPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - 不依賴 VPN 或 root 的開源應用防火牆 `GPL-3.0`
* [Shizzi](https://github.com/carlelieser/shizzi) - 透過 Shizuku 無需 root 繞過 Wi-Fi 網路共用限制 `Proprietary`
* [sing-box](https://f-droid.org/packages/io.nekohasekai.sfa/) - 通用代理平台。使用 Shizuku 實現各應用代理 `GPL-3.0` [(原始碼)](https://github.com/SagerNet/sing-box)
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - 狀態列中的常駐網速追蹤器 `GPL-3.0` [(原始碼)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - WireGuard 和 AmneziaWG 的 FOSS Android 用戶端，支援自動隧道功能 `MIT`
* [WiFi Portal](https://github.com/lovitus/wifiportal) - 透過 Shizuku 套用強制門戶探測設定，支援備份、寫入前驗證和地區預設。 `Proprietary`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - 使用 Shizuku 管理和檢視已儲存 Wi-Fi 密碼的簡單應用 `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - 在 Android 11 及更高版本上檢視您儲存的 Wi-Fi 密碼，無需 root `Proprietary` [(原始碼)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - 延伸自 LSPosed 的免 root Xposed 框架 `GPL-3.0`
* [Morphe](https://morphe.software/) - 基於 Universal-ReVanced-Manager 的易用 YouTube 補丁工具 `GPL-3.0` [(原始碼)](https://github.com/MorpheApp/morphe-manager)
* [NPatch](https://github.com/7723mod/NPatch) - 基於 LSPosed 的免 root Xposed 框架，可將 Xposed API 注入目標 APK `GPL-3.0`
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - 具備官方管理器所沒有的額外功能的 ReVanced 補丁工具 `GPL-3.0`

### Power management

* [Amply](https://github.com/d4rken-org/amply) - 輕鬆控制充電上限。可臨時允許一次完整充電，然後自動還原您的保護性充電上限 `GPL-3.0`
* [BatStats](https://github.com/mlm-games/BatStats) - 透過 Shizuku 提供統計資訊的電池監視器 `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - 一個簡單的應用程式，可在 Android 14 及更高版本上顯示電池狀態資訊。 `GPL-3.0`
* [Battery](https://github.com/zhyang18/Battery/blob/main/README_EN.md) - 電池健康和硬體分析；Shizuku 提供提權 shell 以深入讀取電池參數。 `MIT`
* [Battery Health Tracker](https://github.com/FrancescoMin/batteryhealthtracker) - 適用於 Oppo、OnePlus 和 Realme 裝置的電池健康診斷與實際化學容量追蹤，透過 Shizuku 實現。 `Apache-2.0`
* [Battery-Monitor](https://github.com/tswistak/Battery-Monitor) - 使用 Shizuku 長期追蹤並記錄電池容量和參數 `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - 透過 Shizuku 直觀修改電池資料的開源應用 `GPL-3.0`
* [DozeTap](https://github.com/dhruvanbhalara/DozeTap) - 畫面逾時預設，透過 Shizuku 一鍵授予 WRITE_SECURE_SETTINGS 權限。 `Apache-2.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - 螢幕關閉後立即啟用 Doze 模式並關閉動作感測，以獲得最佳電池續航 `GPL-3.0` [(原始碼)](https://github.com/Akylas/EnforceDoze)
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - 設定後無需打理的程式，用於阻止 Android 應用在背景執行 `GPL-3.0` [(原始碼)](https://github.com/adil192/no_more_background)
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - 支援 Shizuku 的高階重新啟動選單 `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - 關閉 Android 螢幕而不進入待機/睡眠模式 `Proprietary`
* [sleep-timer](https://github.com/Xitee1/sleep-timer) - 睡眠定時器，可暫停媒體並關閉 Wi-Fi/藍牙/螢幕 `GPL-3.0`
* [USB PD Bypass](https://github.com/ONDER1E/usbpdbs) - 透過 Shizuku 在充電閾值時切換 USB PD 電池旁路模式，具備自癒恢復功能。 `Proprietary`
* [volt](https://github.com/lebiggg/volt) - Greenify 的繼任者：透過 Shizuku 實現評分式應用休眠和 UnifiedPush 推送喚醒 `GPL-3.0`
* [wakelogs](https://github.com/dernikiausd/wakelogs) - 透過基於 Shizuku 的系統診斷分析螢幕喚醒、CPU 活動、鬧鐘和裝置休眠。 `GPL-3.0`
* [zukulock](https://github.com/tiendnm/zukulock) - 非常輕量的應用，啟動時鎖定螢幕，有助於減少電源鍵磨損 `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok：一鍵隱藏您的私人檔案和 Android 應用程式。 `Apache-2.0` [(原始碼)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - 旨在默默保護使用者資料免受強大對手侵害的應用 `GPL-3.0`
* [anubis](https://github.com/sogonov/anubis) - 應用管理器，透過 Shizuku pm disable 根據 VPN 狀態凍結/解凍應用組，使被凍結的應用無法偵測或繞過 VPN。 `MIT`
* [AppLock](https://github.com/aload0/AppLock) ✨ - 使用 PIN 鎖定敏感應用程式，並可選擇搭配生物辨識。 `MIT`
* [AppOpsNext](https://github.com/1zumiii/AppOpsNext) - 適用於 Android 15+ 的 AppOps 管理器，具備權限範本、批次變更、安裝歷史和透過 Shizuku 的診斷 `Proprietary`
* [AvarionX-Android-Antivirus](https://github.com/phsycologicalFudge/AvarionX-Android-Antivirus) - 裝置端防毒軟體，具備本機惡意軟體/APK 掃描、下載監控和 DNS 過濾；Shizuku 支援勒索軟體式行為監控 `MPL-2.0`
* [Monica](https://github.com/Monica-Pass/Monica) - 本機優先的 Bitwarden/KeePass 密碼保險庫，支援 TOTP；Shizuku 可保持自動填入保護在背景執行。 `GPL-3.0`
* [Privacify](https://github.com/robinsrk/privacify) - 隱私控制中心：權限掃描器、感測器使用時間軸和隱私評分，並可透過 Root/Shizuku 進行高階硬體控制。 `Apache-2.0`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - 根據鎖定/解鎖狀態管理裝置隱私 `MIT` [(原始碼)](https://github.com/dorumrr/privacyflip)

### Productivity

* [Blink](https://github.com/character-flat/Blink) - 常駐且高度可自訂的 20-20-20 護眼定時器，使用 Shizuku 將自身加入 Android 電池最佳化白名單 `GPL-3.0`
* [Cresto](https://github.com/Nevodev/Cresto) - 待辦應用，具備 AI 快速記錄、日曆同步和提醒；其快速設定中的畫面擷取功能透過 Shizuku shell 取得螢幕畫面。 `Apache-2.0`
* [Curbox](https://f-droid.org/packages/neth.iecal.curbox/) ✨ - 減少螢幕成癮並檢視使用分析的工具 `GPL-3.0` [(原始碼)](https://github.com/curbox-app/curbox-android)
* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - 數位排毒：讓您使用手機，而不是讓手機使用您 `GPL-3.0`
* [HyperCopy](https://github.com/1812z/HyperCopy) - 剪貼簿直達應用工具：監控複製的連結，並透過 Shizuku 或 LSPosed 直接在對應應用中開啟。 `Proprietary`
* [input-leaf](https://github.com/anasvhora284/input-leaf) - Input Leap/Deskflow 的 Android 用戶端：透過區域網路使用 PC 滑鼠和鍵盤控制手機，使用 Shizuku 輸入注入，無需 root。 `Apache-2.0`
* [quickdash](https://github.com/Balajitechlabs/quickdash) - 懸浮生產力面板，具備 UPI/PayPal 收款和聊天捷徑；Shizuku 橋接可解鎖特權系統功能。 `Proprietary`
* [Sefirah](https://github.com/shrimqy/Sefirah-Android) - Windows-Android 整合工具，實現剪貼簿、通知、檔案、簡訊和通話同步；Shizuku 可在 Android 10+ 上啟用剪貼簿。 `GPL-3.0`

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一個用於切換「隨顯螢幕（Always on Display）」的 Android 快速設定 `MIT` [(原始碼)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - 在 Android 12 或更高版本上帶回獨立的 Wi-Fi 和行動數據圖塊，並提供更好的統一網路圖塊 `GPL-3.0` [(原始碼)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DataSimTile](https://github.com/Mygod/DataSimTile) - 用於切換預設行動數據 SIM 卡的圖塊 `Apache-2.0`
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - 提供快速設定圖塊和捷徑，可在不鎖定螢幕或停止前景執行應用的情況下關閉螢幕 `MIT` [(原始碼)](https://github.com/UlyssesZh/DisplayToggle)
* [DNS Toggle](https://f-droid.org/packages/com.ericlowry.dnstoggle/) - 用於切換和設定私有 DNS 的快速設定圖塊，可選高階自動化。 `MIT` [(原始碼)](https://github.com/ELowry/DNSToggle)
* [ManualRotate](https://github.com/Verisonder/ManualRotate) - 無需旋轉手機即可切換直向/橫向畫面的快速設定圖塊；可選透過 Shizuku 覆寫應用的方向鎖定。 `GPL-3.0`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - 用於開啟或關閉私有 DNS 設定的快捷圖塊 `GPL-3.0` [(原始碼)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - 用於切換目前私有 DNS 伺服器的快速設定圖塊 `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - 提供用於切換 USB 偵錯和切換私有 DNS 主機的快捷圖塊 `GPL-3.0` [(原始碼)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - 透過快速設定啟用/停用裝置感測器 `Apache-2.0`
* [Tooler](https://github.com/jehan593/tooler) - 用於鎖定畫面、私有 DNS、灰階和充電的快速設定圖塊，透過 Shizuku 執行。 `MIT`

### Software management

* [AppControlX](https://github.com/risunCode/AppControl-X) - 凍結、強制停止、解除安裝應用，變更背景最佳化等 `GPL-3.0`
* [AppDualZuku](https://github.com/nathanatgit/AppDualZuku) - 使用 Shizuku 在隔離或共用工作區（受管理設定檔）中管理多個應用實例，可選 root 後端。 `Proprietary`
* [AppManagerNG](https://github.com/SysAdminDoc/AppManagerNG) - [AppManager](https://github.com/muntashirakon/appmanager) 的分支，用於檢查、精簡、備份、凍結和控制 Android 應用；支援 Shizuku、ADB、Dhizuku 或 root。 `GPL-3.0`
* [Appslim](https://github.com/Horizen5/Appslim/blob/master/docs/README_en.md) - Android 執行階段分析器，分析啟動行為、CPU/記憶體和 Dex 呼叫，然後透過鉤子、規則以及 Shizuku 或 root 操作精簡應用。 `Proprietary`
* [AppVaultX](https://github.com/sunilpaulmathew/AppVaultX) - 由 Shizuku 驅動的高效能應用管理器 `GPL-3.0`
* [Blocker](https://github.com/lihenggui/blocker) - 啟用/停用 Android 元件，例如活動、服務、接收器和提供者 `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - 專注於權限管理的應用管理器 `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - 無需 root 即可解除安裝任何應用程式 `LGPL-3.0` [(原始碼)](https://github.com/samolego/Canta)
* [CloneCat](https://github.com/AhmetCanArslan/CloneCat) - 跨工作資料夾、私人空間、雙應用程式和次要使用者複製和管理應用，並提供主螢幕捷徑 `Proprietary`
* [Dexor](https://github.com/DeveshTone/Dexor) - 針對 Android 應用的提前（AOT）位元組碼編譯和 dexopt 執行階段管理器 `MIT`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android 應用程式可停用未使用的應用程式，同時仍允許方便地存取它們 `MIT`
* [DroidUtility](https://github.com/DroidUtility/DroidUtility) - 無需 root 的工具套件，透過 Shizuku 進行應用精簡、系統調整和特權 shell 執行，針對僅使用手機的開發者。 `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - 透過手動或半自動凍結品質不佳的軟體來提高裝置的速度和電池續航 `Apache-2.0` [(原始碼)](https://github.com/FreezeYou/FreezeYou)
* [Guest-Manager](https://github.com/dlawoals2713/Guest-Manager) - 在廠商已停用訪客和多使用者模式的裝置上，透過 Shizuku shell 無需 root 啟用這些隱藏模式。 `Proprietary`
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - 凍結、隱藏或停用任何應用程式。建立並組織可一鍵凍結的應用程式組。 `GPL-3.0` [(原始碼)](https://github.com/aistra0528/Hail)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Island 完整的 FLOSS 分支 `Apache-2.0` [(原始碼)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - 適用於 root 和非 root 裝置的 Android 應用程式管理器 `GPL-3.0` [(原始碼)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - 隔離和複製應用程式以保護隱私和並行執行 `Apache-2.0` [(原始碼)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - 多合一應用程式和工作流程啟動器 `MIT`
* [Minimal Kernel Manager](https://github.com/abhay-byte/mkm) - 核心管理器和系統監視器，具備電池統計、開機時自動套用以及透過 Shizuku 或 root 支援隱藏應用。 `GPL-3.0`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - 管理您的 Magisk 模組儲存庫 `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - 功能強大的應用程式，可管理系統和使用者應用程式 `GPL-3.0` [(原始碼)](https://github.com/SmartPack/PackageManager)
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - 具備凍結和安裝功能的應用管理器。 `GPL-3.0` [(原始碼)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - 檢查 Android 應用程式、Magisk 模組等的更新！ `GPL-3.0` [(原始碼)](https://github.com/DUpdateSystem/UpgradeAll)

### Task manager

* [KillMyApps](https://github.com/dedeadend/KillMyApps) - 透過 Shizuku 或 root 結束背景行程，以改善電池續航和效能 `GPL-3.0`
* [memhogs](https://github.com/cicerothoma/memhogs-android) - 檢視哪些應用在消耗手機記憶體。透過 Shizuku 提供各應用明細，輔助行程會歸類到擁有它們的應用程式底下 `MIT`
* [MemorySnapshot](https://github.com/RyensX/MemorySnapshot/blob/master/docs/README_EN.md) - 裝置端 Android 記憶體觀察器：依應用程式/行程追蹤 PSS、儲存及比較快照，透過 Shizuku 或 root 收集資料。 `Proprietary`
* [Pensum](https://github.com/troikoss/Pensum) ✨ - Android 版 Windows 風格工作管理員 `GPL-3.0`
* [ProcessLens](https://github.com/Dreamucxe/ProcessLens) - 使用 Shizuku 取得 ADB 級 CPU、記憶體、執行緒、喚醒鎖定和各應用電池讀數的行程觀察器。 `MIT`
* [ReAppzuku](https://github.com/gree1d/ReAppzuku) - 控制和管理背景應用。shappky 的分支 `GPL-3.0`
* [Recents](https://github.com/tymwitko/Recents) - 不依賴啟動器的系統「最近使用」選單替代品，透過 Shizuku 支援結束應用 `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - 監控 Android 裝置上執行的服務 `MIT` [(原始碼)](https://github.com/biplobsd/running_services_monitor)
* [RvSystem Monitor](https://github.com/Rve27/RvSystem-Monitor) - 高效能系統監視器（Compose + Rust），透過 Shizuku 提供 CPU 和硬體洞察 `GPL-3.0`
* [shappky](https://github.com/YasserNull/shappky) ✨ - 透過停止背景應用來提升效能的簡單應用。 `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - 適用於 Android 的工作管理員。結束行程需要 root 權限。 `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - 適用於由 Shizuku 驅動的 Android 裝置的本機 ADB shell `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - aShell 應用程式的 Material You 重新設計版。 `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - 適用於 Android 的終端、SSH、VNC、RDP、SFTP 和雲端儲存用戶端 `AGPL-3.0` [(原始碼)](https://github.com/GlassHaven/Haven)

> [!NOTE]
> Using [rish](pages/RISH_tw.md), 您可以使用任何終端模擬器（例如 Termux）建立本機 ADB shell。

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - 一個用於切換「隨顯螢幕（Always on Display）」的 Android 快速設定 `MIT` [(原始碼)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [carrier-ims-for-pixel](https://github.com/ryfineZ/carrier-ims-for-pixel) - 持續維護的 Pixel IMS 工具包：透過 Shizuku 調整 VoLTE/VoWi-Fi/VoNR、5G 圖示顯示和電信業者設定 `Apache-2.0`
* [hilight-studio](https://github.com/DhananjayBhosale/hilight-studio) - Pixel 11 HiLight LED 控制器，可自訂通知和狀態燈效果 `MIT`
* [Pixel-IMS-5G](https://github.com/barrylk/Pixel-IMS-5G) - 在 Google Pixel 裝置上啟用 5G 獨立組網（5G SA）和 VoNR `GPL-3.0`
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - 為 LG U+ 電信業者在 Pixel 6 和 7 上啟用 VoLTE `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - 在 Pixel 裝置上為不受支援地區的電信業者啟用 VoLTE `GPL-3.0`
* [Root-My-Pixel](https://github.com/alex193a/Root-My-Pixel) - 利用 CVE-2026-43499 漏洞為 Pixel 裝置自動取得 root `Proprietary`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - 可自訂的小工具，可以使用 Shizuku 升級 Pixel 裝置上內建的「概覽」小工具 `GPL-3.0`
* [TensorIMS](https://github.com/Pixel-Tailor-CN/TensorIMS) - 適用於 Tensor Pixel 裝置的 IMS 設定工具；Shizuku 可應用 VoLTE、VoWi-Fi、VT 和 VoNR 開關。 `Apache-2.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - 適用於 Google Pixel 裝置的增強 IMS 設定工具 `Apache-2.0`
* [Video Boost AO](https://github.com/AgusRomeroL/video-boost-ao) - 在 Pixel Pro 相機上保持 Video Boost 啟用，每次相機開啟時重新啟用。Shizuku 為隨選模式授予 WRITE_SECURE_SETTINGS 權限 `MIT`

#### Samsung OneUI

* [4Zones](https://github.com/mr-biz-apps/4zones) - 在三星 DeX 和 Android 桌面模式下恢復四區域視窗並排，支援點選貼齊和鍵盤快捷鍵 `Apache-2.0`
* [android-battery-health](https://github.com/willbilec/android-battery-health) - 三星電池健康與充電循環次數檢視器，透過 Shizuku 提供對螢幕閱讀器友善的版面設定。 `Proprietary`
* [duo-fold-live](https://github.com/joeconsorti/duo-fold-live) - Live hinge-driven iPhone-Duo fold animation for Galaxy Z Fold 8 with windowed glass, live cover previews and smooth display handoff, reading the true hinge angle via Shizuku. `MIT`
* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 免 root 字型安裝器 `GPL-3.0` [(原始碼)](https://codeberg.org/dryerlint/fontsmanager)
* [galaxy-auto-brightness-offset](https://github.com/fullmetalsonic/galaxy-auto-brightness-offset) - Samsung Galaxy adaptive-brightness offset for screens that feel too dark or too bright, including under privacy films: applies a fixed correction to the auto-brightness curve via Shizuku. `Proprietary`
* [pearity](https://github.com/thejaustin/pearity) - 逐項將三星 One UI 系統設定對應至 iOS 預設值（Android/自訂/iOS 三種狀態），並透過 Shizuku 或 root 寫入安全設定。 `Proprietary`
* [Root-My-Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy) - 使用 CVE-2026-43499 為受支援的三星 Galaxy 韌體安裝 KSU `Apache-2.0`
* [SamsungRegionOverride](https://github.com/Ritel-T/SamsungRegionOverride) - 臨時變更 Galaxy Store 及其他區域鎖定應用所見的 SIM 地區，無需 root，一鍵還原 `MIT`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - 在三星裝置電池溫度達到特定值時啟用或停用快速充電模式  `Proprietary`
* [ScamsungFonts](https://github.com/KhunHtetzNaing/ScamsungFonts) - 透過系統 shell 或 Root 為三星 Galaxy（OneUI）管理字型 `No license`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - 在 CSC 設定為強制快門聲的特定國家/地區的三星裝置上停用相機快門聲 `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - 權限提升漏洞[(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253)，可在執行 OneUI 5 及以下版本的非 root 裝置上的系統使用者存取 (UID 1000)。使用 Shizuku 自動化 `LGPL-2.1`
* [ZFold-Multi-DPI](https://github.com/balamurugan15/ZFold-Multi-DPI) - 為三星 Galaxy Z Fold 裝置的外螢幕和內螢幕套用獨立的螢幕縮放和 DPI 預設 `Proprietary`

#### MIUI

* [Aura](https://github.com/tgvdufuture/Aura) - 適用於 POCO X8 Pro 的自訂 RGB 通知 LED 應用，支援依應用程式、聯絡人和群組設定顏色和動畫 `MIT`
* [CodecTweaker](https://github.com/Halo0sama/CodecTweaker) - Bluetooth codec fix for Xiaomi HyperOS: restores each earphone's chosen codec and bitrate after A2DP reconnects using Shizuku plus accessibility UI automation. `GPL-3.0`
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) `Paid` 💰 - HyperOS/MIUI 5G 快捷開關 `GPL-3.0` [(原始碼)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - 以最低成本關閉 MIUI 廣告 `Apache-2.0`
* [HyperOS FCM Fix](https://github.com/dingwen07/hyperos-fcm-fix) - 在 HyperOS 上保持 Google Play 服務不受限制，確保 FCM 推送通知準時送達 `GPL-3.0`
* [HyperOS-MTZ-Studio](https://github.com/GloriousApps/HyperOS-MTZ-Studio/blob/main/readme_en.md) - 針對小米 HyperOS 的 MTZ 主題工作區；可匯入、組合、翻譯和應用主題，使用 Shizuku 或 Shevery 並以無需 root 的方式套用。 `Proprietary`
* [HyperOS3ScrollSetter](https://github.com/BlizzardAn225/HyperOS3ScrollSetter) - 在 HyperOS 3/4 上恢復捲動桌布並停用強制變暗，透過 Shizuku.newProcess 或 root 模組應用安全設定並重新啟動相關行程。 `GPL-3.0`
* [HyperOSUnfcker](https://github.com/Enki013/hyperosunfcker) - 解鎖 HyperOS/MIUI 裝置上隱藏的效能、顯示、記憶體、電池和視覺設定 `LGPL-3.0`
* [IslandRecorder](https://github.com/wxxsfxyzm/IslandRecorder) - 針對小米裝置的螢幕錄製器，支援超級島控制 `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - Mix Flip 外螢幕一鍵設定：使用任意應用並將系統應用還原為預設樣式 `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - 在 MIUI / HyperOS 節奏遊戲中啟用 3 鍵導覽  `Proprietary`

#### Other

* [BooxUltimatum](https://github.com/huuunleashed/BooxUltimatum) - Open-source suite for BOOX E Ink tablets: high-contrast home, sleep screens, instant pen ink, battery log and reversible tweaks, using Shizuku for privileged tweak tiers. `GPL-3.0`
* [buttonoo](https://github.com/bractstudio/buttonoo) - 將 Nothing 的 Essential 鍵重新對應為任意按壓模式；Shizuku 啟用特權輸入通道。 `GPL-3.0`
* [Calibrate-SoC](https://github.com/mayusi/Calibrate-SoC) - 針對 Android 遊戲掌機的 SoC 調校、監控和基準測試套件，具備目標導向調速器和即時 HUD。 `Apache-2.0`
* [DiAuto](https://github.com/shihabal3amri/DiAuto) - Wireless and USB Android Auto receiver for BYD DiLink head units; runs entirely on the car display and uses Shizuku or root for privileged setup. No phone companion app or dongle. `AGPL-3.0`
* [Evolve_Launcher_v2](https://github.com/JarJarBlinkz/Evolve_Launcher_v2) - 適用於 Meta Quest 頭戴式裝置的可自訂桌面啟動器，具備應用整理、遊戲時長追蹤和由 Shizuku 支援的清除資料/快取操作。 `Proprietary`
* [flipx](https://github.com/jlgrimes/flipx) - 根據 Anbernic RG Rotate 的轉軸狀態將首頁鍵路由到不同的啟動器 `Proprietary`
* [GlyphBarty](https://github.com/Link2011-Act2/GlyphBarty) - 適用於 Nothing Phone 的可自訂 Glyph 視覺化工具，支援音樂同步、快速設定開關和充電狀態顯示 `MIT`
* [Heimdall-AYN-Thor-Assistant](https://github.com/mastercook777/Heimdall-AYN-Thor-Assistant) - 適用於 AYN Thor 的下螢幕遊戲助手，具備設定檔、巨集、觸控、地圖和由 Shizuku 驅動的觸控注入。 `Apache-2.0`
* [MindControl](https://github.com/Dinico414/MindControl) - 適用於 iKKO MindOne 的硬體按鍵重新對應和隨顯螢幕工具包，透過 Shizuku getevent 監控實體按鍵，並支援 root 備援。 `Proprietary`
* [panel-assistant](https://github.com/panel-assistant/android) - Home Assistant 壁掛面板儀表板，具備實體過濾、MQTT 裝置控制，以及由 Shizuku/root 支援的佈建和經驗證的安裝流程。 `Apache-2.0`
* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control 可精確控制 Nothing Phone (3) 的錄製指示燈 `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - 適用於 Nubia Red Magic 手機的全域肩鍵 `MIT`
* [Thor SidePad](https://github.com/bentolanh/thor-sidepad) - 將 AYN Thor 下螢幕變為虛擬手把；Shizuku 將其按壓轉換為原生手把輸入。 `MIT`
* [thor-pathfinder](https://github.com/KaitonGxx/thor-pathfinder) - AYN Thor dual-screen companion: swaps running apps between screens and maps button/combo shortcuts per game profile, using Shizuku to move windows to the other display. `GPL-3.0`
* [thor-wayfinder](https://github.com/Thor-Wayfinder/thor-wayfinder) - 透過返回鍵手勢在 AYN Thor 的兩塊螢幕之間移動應用 `CC-BY-NC-ND-4.0`
* [Thors-Lightning](https://github.com/HughesTechNZ/Thors-Lightning) - 適用於 AYN Thor 的手把驅動雙螢幕亮度控制，並可選用需 Shizuku 權限的輸入錄製。 `MIT`
* [ThorVolumeLink](https://github.com/pth2000/ThorVolumeLink) - AYN Thor 雙螢幕的同步音量控制 `MIT`

### Closed-source apps

閉源應用程式已移至獨立的子清單中。[您可在此處查看。](pages/CLOSED_SOURCE_tw.md) 


> [!NOTE]
> **為何專有軟體會被列在獨立清單中？**
> Shizuku 會授予應用程式高階的 ADB 存取權限。基於安全考量，此主目錄僅收錄開源及提供原始碼的應用程式，因為任何人都能檢視其程式碼以確認是否存在可疑行為，並可在自己的電腦上自行編譯。
>
> 完全專有的應用程式需要使用者盲目信任，因此被列在獨立清單中。

### Unlisted apps
為了保持主列表乾淨，所有不滿足特定要求的應用程式都儲存在單獨的頁面上： [ARCHIVED.md](pages/ARCHIVED.md)

> [!NOTE]
> 我還使用自動爬蟲來搜尋新專案，並在 GitHub 和多個 F-Droid 儲存庫中使用 Shizuku。您可以在此處檢視當前自動生成的爬網報告：[TODO.md](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Porter API](https://github.com/d4rken-org/porter-api) - Porter（持續維護的 Shizuku 分支）的 Android SDK，提供相容的 Shizuku API 和直接的 Porter 支援 `MIT`
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Shizuku 和 Sui 的開發人員說明文件，包含範例 `Apache-2.0`
* [Shizuku-API-Flutter-Plugin](https://github.com/runoob-coder/shizuku-api-flutter-plugin) - 一個用於串接 Shizuku API 的 Flutter 外掛。 `MIT`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - 適用於 Flutter 應用的 Shizuku API 繫結 `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android 上適合協程、Kotlin 優先的套件安裝器擴充套件，支援 Shizuku `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - 具有 Shizuku、root 和常規檔案系統後端的檔案操作函式庫 `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - 相容 Shizuku 的 Xamarin android/data 存取 - AIDL 函式庫 `MIT`


### System

* [droid-mcp](https://github.com/stixez/droid-mcp) - Android SDK，為本機 LLM/AI 應用提供裝置上手機資料的結構化存取，並透過 Shizuku 實現 shell 級控制 `Apache-2.0`
* [libterm](https://github.com/niki914/libterm) - Kotlin 優先的 Android 終端工作階段函式庫，在單一 API 後提供 User、Root、Shizuku 和 SSH 後端 `Proprietary`
* [Priv Kit](https://github.com/priv-kit/priv-kit) - 輕量級特權執行階段函式庫，可在自己的應用中實現 Root、ADB 或 Shizuku 支援的 Binder 存取 `Proprietary`

--------------------

## Miscellaneous content

### Command-line utilities

* [AndroSH](https://github.com/ahmed-alnassif/AndroSH) - 透過 Shizuku/ADB 在 Android 上執行無需 root 的多發行版 Linux：可執行 Arch、Fedora、Alpine、Debian、Ubuntu、Kali、Void、Manjaro、OpenSUSE 和 Chimera，具備完整系統整合、proot 隔離和 Termux:X11 圖形介面。 `GPL-3.0`

### Flows for [Automate](https://llamalab.com/automate/)

* [Better Shizuku Starter](https://llamalab.com/automate/community/flows/50863) - 使用 *免費* 版 Automate，在關鍵事件發生時透過無線偵錯檢查並自動啟動 Shizuku **13.6**。 `MIT`
* [Shizuku Keeper](https://llamalab.com/automate/community/flows/51118) - 使用 Automate *Premium*，透過 USB 偵錯讓 Shizuku **13.6** 或 **ADB** 無需 root、Wi-Fi 或傳輸線即可不間斷執行。 `MIT`
  * [Shizuku Keeper Lite](https://llamalab.com/automate/community/flows/51012) - 使用 *免費* 版 Automate，定期檢查 Shizuku **13.6** 並在需要時透過無線偵錯自動重新啟動它。 `MIT`
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

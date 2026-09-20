# awesome-shizuku

### Languages
English | [简体中文](/README_cn.md) | [繁體中文](/README_tw.md)

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku allows normal apps to use system APIs directly with elevated privileges using ADB on non-rooted devices. This list compiles a few apps that are known to make use of Shizuku's capabilities.

More details: https://shizuku.rikka.app/

Pull requests are welcome. See [Contributing](CONTRIBUTING.md) for hints. Closed-source apps are listed in a separate file. See [below](#closed-source-apps) for details.

> [!NOTE]
> To stay up-to-date with this list, [you can check the daily changelogs](https://github.com/timschneeb/changelog-awesome-shizuku).


--------------------


## Table of contents

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

> [!NOTE]
> The official Shizuku app by RikkaApps has not been updated in over a year and is currently broken on Android 17.
> Below, you can find forks of Shizuku with new features and fixes.
> 
> You should uninstall your current Shizuku version before installing any of the replacements below, otherwise, you may run into installation conflicts.

* [shevery](https://github.com/HmnDev-Tech/shevery) ✨ - Material 3 fork with autostart, TCP mode, Dhizuku, module support and a built-in terminal with AI integration `Apache-2.0` 
* [Shizako](https://github.com/xm1437/Shizako) - A catgirl-mascot edition of Shizuku, a drop-in replacement manager that official Shizuku-API apps connect to without modification (with similar features like shevery) `Apache-2.0`
* [Shizuku (thedjchi's fork)](https://github.com/thedjchi/Shizuku) - Fork of Shizuku with autostart, TCP mode and stealth mode (maintenance currently paused) `Apache-2.0`
* [ShizukuPlus](https://github.com/thejaustin/ShizukuPlus) - Shizuku fork with an extended API surface for developers, autostart, TCP mode, Dhizuku and more `Apache-2.0`
* [Stellar](https://github.com/roro2239/Stellar/blob/main/README_en.md) - Another Shizuku implementation with autostart, TCP mode and a simple terminal (can run commands automatically on startup) `MPL-2.0`

### AI agents

* [Aether](https://github.com/Zhou-Shilin/Aether) - Localized, extensible general-purpose AI agent for Android, iOS and macOS, with optional Shizuku and Termux integration for direct device control. `GPL-3.0`
* [ClawGUI](https://github.com/ZJU-REAL/ClawGUI) - On-device GUI-agent runner deploying the full ClawGUI brain stack on one phone controlled via Shizuku. `Apache-2.0`
* [OmniBot](https://github.com/omnimind-ai/OmniBot) - On-device AI agent with terminal, web browsing, device control, and system integration `GPL-3.0`
* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - Automates actions on your device using the AutoGLM vision language model `GPL-3.0`
* [OpenCyvis](https://github.com/opencyvis/opencyvis-phone) - Open-source AI phone that sees your screen and operates apps from natural language tasks, works in the background `Apache-2.0`
* [OpenDroid](https://github.com/yashab-cyber/opendroid) - Open-source autonomous on-device AI agent that plans and executes multi-step tasks via screen automation `Apache-2.0`
* [OpenMinis](https://github.com/OpenMinis/OpenMinis) - AI-powered agent with Linux shell, browser automation, and system control via Shizuku `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - The most powerful AI agent and AI chat software on Android. Can run commands using Shizuku `LGPL-3.0`
* [rish-mcp](https://github.com/turin-dev/rish-mcp) - Exposes an Android device's Shizuku shell to AIs as an MCP `run_shell` tool over an outbound WebSocket relay — run shell commands from Claude or any MCP client with no VPN, ADB, or sshd `MIT`
* [roubao](https://github.com/Turbo1123/roubao/blob/main/README_EN.md) - Open-source on-device AI phone automation assistant based on vision-language models that performs tasks via Shizuku system permissions, no PC needed. `MIT` [(Source code)](https://github.com/Turbo1123/roubao)
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - Automation and Multitasking Framework using AutoGLM. Can create virtual screens that agents can run apps on and use multi-window `Apache 2.0`


### Android Auto

* [Flywheel](https://github.com/Benjamin-Wiegand/Flywheel) - Free and open source alternative to Android Auto aimed at de-googled phones, compatible with existing headunits; Shizuku is used for app embedding and call-audio capture. `GPL-3.0`

### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - An F-Droid client designed for Android TVs `GPL-3.0` [(Source code)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer designed for Android TVs `GPL-3.0` [(Source code)](https://github.com/mlm-games/fluffy)
* [RecentAppsTV](https://github.com/Qutaiba-Khader/RecentAppsTV) - Recent Apps overlay for Android TV `Propietary`

### Audio

* [android-realtime-voice-isolation](https://github.com/sk2andy/android-realtime-voice-isolation) - On-device real-time voice isolation using Shizuku, GTCRN, and ONNX Runtime `MIT`
* [Castix](https://github.com/elhizazi1/Castix) - Manages background playback restrictions and adds an AMOLED black-screen clock, with Shizuku, Dhizuku, root, LSPosed or accessibility backends. `GPL-3.0`
* [MicUp](https://github.com/papergray/MicUp) ✨ - Real-time microphone audio processing for Android `MIT`
* [Mixer (1)](https://github.com/farizanjum/mixer-1) - Per-app volume overlay intercepting hardware keys `Proprietary`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - An implementation of the system-wide JamesDSP audio processing engine for non-rooted Android devices `GPL-3.0` [(Source code)](https://github.com/timschneeb/RootlessJamesDSP)
* [Spotify Ad Skipper](https://github.com/sihooney/spotify-ad-skipper) - Watches Spotify notifications and auto-skips ads by restarting playback, using Shizuku to relaunch from background. `Proprietary`
* [Volume++](https://github.com/noel-digital-fan/volume_plus_plus) - Custom volume panel with per-app audio mixing via Shizuku or root `MIT`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - Control each app's volume independently `GPL-2.0`
* [wecho](https://github.com/qumolangmo/wecho) - An Android application for global audio effects processing `GPL-3.0`

### Automation

* [Argus](https://github.com/JackRushante/argus) - Tasker-class Android automation where an LLM compiles natural-language rules into a deterministic engine, with an optional Shizuku shell gateway. `GPL-3.0`
* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - JavaScript-based automation tool `MPL-2.0`
* [AutoSlide](https://github.com/tianxing-ovo/AutoSlide/blob/master/README.en.md) - Auto-slide tool that auto-plays short videos and flips reading pages, with floating controls `Apache-2.0` [(Source code)](https://github.com/tianxing-ovo/AutoSlide)
* [flowpilot](https://github.com/emi-ran/flowpilot) - Privacy-first offline automation engine running privileged system actions such as mobile data, airplane mode and dark theme through Shizuku. `GPL-3.0`
* [IMD](https://github.com/soul-99/SU_IMD) - Fork of Geto that hides developer options, ADB, accessibility services and Shizuku itself for restrictive apps like banking, then restores them `GPL-3.0`
* [NexaFlow](https://github.com/Alaa91H/NexaFlow) - Context-aware Android automation engine combining triggers, constraints and actions, with Shizuku execution for privileged device controls. `MIT`
* [Nothing_Modes](https://github.com/Dvorinka/Nothing_Modes) - Automation app for Nothing phones (modes, routines, Glyph) that also runs on other Android devices with optional Shizuku `GPL-3.0`
* [OpenTasker](https://github.com/SysAdminDoc/OpenTasker) - Local-first, open-source Tasker alternative with readable rules and honest permission gates; privileged actions run through a Shizuku AIDL user service. `MIT`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - Allows automatic or one-click configuration of your device for specific life situations `Apache-2.0`
* [Service-Keeper](https://github.com/shaunkleyn/Service-Keeper) - Watches background, accessibility and notification-listener services and auto-restarts ones the system kills. `GPL-3.0`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Helper app for Tasker `Propietary`
* [vFlow](https://github.com/ChaoMixian/vFlow/blob/master/README_EN.md) - Visual automation tool that combines tapping, recognition, branching, and system actions into approachable workflows `GPL-2.0`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord modding tool `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - A simple app for automatically launching Bluesky links in your preferred Bluesky client `MIT` [(Source code)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CallVault](https://github.com/madkongo/CallVault) - Non-root call recorder with on-device transcripts/summaries; self-contained over embedded ADB or via an optional Shizuku backend. `GPL-3.0`
* [cally](https://github.com/LyoSU/cally) - Call recorder for stock Pixel 6+ devices that captures both call directions via a Shizuku shell-UID audio service, without root or unlocked bootloader. `GPL-3.0`
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - Send and receive files over Bluetooth `MIT` [(Source code)](https://github.com/kmod-midori/CatShare)
* [GhostMode](https://github.com/Foxlape/GhostMode) - Makes the phone appear unavailable for incoming calls while keeping LTE/5G data active `Apache-2.0`
* [KDE Connect (Shizuku)](https://github.com/Batestinha/kdeconnect-android-shizuku) - Unofficial KDE Connect fork adding automatic background clipboard sync on Android 10+ via Shizuku and AIDL callbacks. `GPL-2.0`
* [KettuManager](https://github.com/C0C0B01/KettuManager) - Discord modding tool. Continuation of the abandoned BunnyManager project `OSL-3.0`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - A simple app for automatically launching Lemmy links in your preferred Lemmy client. `MIT` [(Source code)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - A simple app for automatically launching fediverse links in your preferred Mastodon client. `MIT` [(Source code)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord modding tool. Another continuation of the abandoned Bunny-Manager project `OSL-3.0`
* [RivoPhoneApp](https://github.com/user-grinch/RivoPhoneApp) - Material 3 dialer and contacts app with Shizuku-powered call recording without root `GPL-3.0`
* [ShizuCallRecorder](https://github.com/kitsumed/ShizuCallRecorder) ✨ - ShizuCallRecorder empowers ADB through Shizuku to record phone calls on non-rooted device! `GPL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - An app that lets you browse the web over SMS `GPL-3.0`

### Customization

* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - Smart dark mode based on ambient light `GPL-3.0` [(Source code)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - Port of Now Playing from Pixels to other Android devices `GPL-3.0`
* [android-perapp-language-selector](https://github.com/TakeruF/android-perapp-language-selector) - Force per-app language settings on Android 13+ without root, even for apps without built-in language options `Apache-2.0`
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - A simple tool to toggle DND automatically when using specified apps `AGPL-3.0` [(Source code)](https://github.com/im030/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - Manage automatic rotation of different screens on Android phones `GPL-3.0`
* [Capsulyric](https://github.com/FrancoGiudans/Capsulyric) - Displays now-playing lyrics on the status bar and lock screen via Android Live Update and Xiaomi Super Island `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name is a very simple app to change the carrier names on unrooted Android devices `GPL-3.0`
* [cebian](https://github.com/qpst4/cebian) - All-in-one gesture and one-hand navigation suite with edge panels, floating cursor, offline OCR ball, app freezer and freeform windows via Shizuku. `AGPL-3.0`
* [CleanBar](https://github.com/sachinmandawi/CleanBar) - 1-tap status bar and system icon hider to hide clock, battery, and icons, no root required `MIT`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - An application to modify Material You colors of your device `GPL-3.0`
* [Commander](https://github.com/astroboii47/Commander) - Keyboard-first command bar and notification hub; uses Shizuku for recent-app switching and privileged shell controls. `MIT`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - Customize animation speeds on a more fine-grained level `GPL-3.0` [(Source code)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ-Reborn](https://github.com/Arora-Sir/DarQ-Reborn) - Per-app selectable force dark option for Android 10 and above `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - Some Android app widgets and live wallpapers `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - Highly customizable, gestures based Android launcher focused on speed and efficiency `GPL-3.0` [(Source code)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - Tiling window manager, Samsung DEX replacement, popup app launcher `Proprietary`
* [DuoFold-Android](https://github.com/jcx396905-gif/DuoFold-Android) - System-wide iPhone Duo-style fold illusion that reprojects the whole screen from device motion with OpenGL ES, powered by Shizuku. `MIT`
* [essentials](https://github.com/sameerasw/essentials) ✨ - Essential tools, mods and workarounds for Pixels. Also compatible with other devices `MIT`
* [expressive-cutout](https://github.com/EvanKoe/expressive-cutout) - Offline Dynamic Island following Material Expressive design with notifications, live tiles, and Material You colors `GPL-3.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - Adds desktop-like multi-window support on Android for smartphones. `GPL-3.0`
* [FreeformShell](https://github.com/bravoyush/FreeformShell) - Experimental freeform window-manager helper adding title bars, resize borders and display scaling through Shizuku system APIs. `Apache-2.0`
* [gama](https://github.com/palincat/gama) - Can switch between OpenGL and Vulkan renderers by setting the `debug.hwui.renderer` system property `MIT`
* [HyperBridge](https://github.com/D4vidDf/HyperBridge) - Brings the native HyperIsland experience to HyperOS by bridging notifications into the camera cutout UI with themes and widgets `Apache-2.0`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - Launcher for dual-screen gaming devices. Uses Shizuku to map on of the touch screens to controller inputs `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - Allows users to select individual app languages (Android 13+) `Apache-2.0`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - Restore the Android <12 Url-App-Link-Chooser with Material3 `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - Display widgets on the lockscreen. Shizuku is only required on Android 13 and later `MIT` [(Source code)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - A simple app that enables you to add additional (or "unsupported") languages to your device's locale settings, if the OEM (Xiaomi) doesn't let you `MIT`
* [O.status](https://github.com/CATCHINGL/O.status) - Minimal status-bar indicator for Wi-Fi, cellular and battery that uses optional Shizuku integration to match system icon colors. `Proprietary`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - A keyboard-first Android command palette that unifies app/device search, and system utilities into an overlay `GPL-3.0`
* [SetEditPlus](https://github.com/kerneldroid/SetEditPlus) - Editor for Android System/Secure/Global settings tables with Shizuku/Root modes, change tracking and boot persistence. `Proprietary`
* [sharemove](https://github.com/thejaustin/sharemove) - Hides apps from Android's share, 'Open with' and APK-installer chooser sheets by suspending or disabling components via Shizuku or root. `GPL-3.0`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - Create launcher shortcuts for shell commands `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - Contains some easy-to-use tools to go beyond the level of control allowed by Android System `GPL-3.0`
* [Smart Dock](https://f-droid.org/packages/cu.axel.smartdock/) - Transform your phone into a desktop environment with taskbar, recent apps, and start menu `GPL-3.0` [(Source code)](https://github.com/axel358/smartdock)
* [Smart Edge](https://f-droid.org/en/packages/com.imi.smartedge.sidebar.panel/) - A highly customizable Android side panel inspired by OriginOS `MIT` [(Source code)](https://github.com/Imtiaz-Official/Smart-Edge)
* [Smart Island](https://github.com/agupta07505/SmartIsland) - A lightweight Android overlay that turns notifications, calls, and media playback into a floating glanceable island `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Plugins for Smartspacer `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - View and modify hidden settings on Android devices `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - Port of the double tap on the back of the device feature from Android 12 to any Android 7.0+ device `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - Clean up tracking from sharing links. Supports custom URL rewrite rules `GPL-3.0` [(Source code)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - Use a start menu to access apps. Shizuku can unlock additional features `Apache-2.0` [(Source code)](https://github.com/farmerbb/Taskbar)
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU and battery widgets `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - A full desktop experience layer for Android `GPL-3.0`
* [YoukiShell](https://github.com/mrYouki/YoukiShell-Android-Desktop) - Plugin-driven Android shell with a taskbar, floating windows and a built-in plugin store; some features need Root or Shizuku `GPL-3.0`

### Development utilities

* [80bee-app](https://github.com/Endda/80bee-app) - Root-free on-device ADB/Fastboot toolbox: boot modes, DPI, DNS, debloater and sideload bypass via Shizuku, plus USB-OTG host mode. `Apache-2.0`
* [ActivityLauncherShizukuPlugin](https://github.com/ActivityLauncher/ActivityLauncherShizukuPlugin) - A Shizuku-based plugin for [Activity Launcher](https://github.com/butzist/ActivityLauncher) that allows launching private (non-exported) activities. `GPL-3.0`
* [ActivityManager](https://github.com/sdex/ActivityManager) - Launch hidden and unexported activities directly without root `Apache-2.0`
* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - Dump package names of apps that have registered an account for a user. `Proprietary`
* [Cosmic-IDE](https://github.com/aload0/Cosmic-IDE) - IDE for JVM development. Uses Shizuku for an embedded shell `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - Backup/restore private app data of debuggable apps using Shizuku `GPL-3.0`
* [DEVTools](https://github.com/MetxStudio/DEVTools) - All-in-one Android dev toolkit: terminals, sensor monitor, app/file managers plus a Shizuku shell helper. `MIT`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - A simple app made to help users easily install GSIs via DSU's Android feature. `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - Fixes MediaStore & File IO compatibility issues between HostProfile App and WorkProfile/DualApp/MultiApp. `Proprietary`
* [FPS-Meter-Android](https://github.com/rdevz-ph/FPS-Meter-Android) - High-performance lightweight FPS monitoring overlay inspired by Samsung Perf Z for gaming and performance testing `MIT`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - FPS viewer overlay with graph `Proprietary`
* [FrameX-Android](https://github.com/MaheshSharan/FrameX-Android) - Real-time performance overlay for Android `MIT`
* [get_event](https://github.com/lalakii/get_event) - Read /dev/input/event* `Proprietary`
* [LibChecker](https://github.com/LibChecker/LibChecker) - An app to view libraries used in apps on your device. Uses Shizuku to determine the installation source of other apps. `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - Yet another logcat reader for Android `GPL-3.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - Utilizes Shizuku to call AppOps APIs for fine-grained app permission control `MIT`
* [panda-ide](https://github.com/ferelking242/panda-ide) - Mobile-first Flutter IDE with code editor, PTY terminal, Git and VS Code extensions; a Shizuku bridge provides ADB-level shell for on-device flutter run. `MIT`
* [roamer](https://github.com/eigenlux-ai/roamer) - Developer tool overriding SIM country ISO and carrier name via Shizuku, with optional per-app locale syncing. `MIT`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - Launch/interact with (un)exported activities, services, and receivers. Supports Shizuku alongside root. `GPL-3.0` [(Source code)](https://github.com/zacharee/RootActivityLauncher)
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - Widgets & quick settings tile to toggle wireless debugging (with KDE Connect integration) `GPL-3.0`

### Device owner (DPM)

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - Shizuku-inspired app that allows sharing DeviceOwner permissions to third-party apps `GPL-3.0`
* [harbor](https://f-droid.org/packages/com.monstera.harbor/) - Work-profile manager with optional Shizuku tools for automation `Apache-2.0` [(Source code)](https://github.com/Stem0794/harbor)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - Manage your device with Device owner privileges `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - Fork of OwnDroid with added features `GPL-3.0`

### Display management
* [Adaptive-Hz](https://github.com/mahmutaunal/Adaptive-Hz) - Automatically switches display refresh rate between 60Hz and 120Hz based on user interaction. Designed for Samsung devices without true adaptive refresh `MIT`
* [akiHz](https://github.com/anlaki-py/akihz) - Lightweight refresh rate switcher with Quick Settings tile, automatic rate detection, and floating FPS monitor `MIT`
* [android-display-extend](https://github.com/jqssun/android-display-extend) ✨ - Display manager for physical and virtual displays with a built-in virtual touchscreen. Great for use with `scrcpy --new-display` on a PC `GPL-3.0`
* [android-display-mirror](https://github.com/jqssun/android-display-mirror) ✨ - Screen mirroring hub with support for sharing screen content over AirPlay, Moonlight/Sunshine, and DisplayLink `GPL-3.0`
* [Castla](https://github.com/Suprhimp/castla) - Creates a virtual display, runs apps on it, and streams screen, touch, and audio into a remote browser over local Wi-Fi `Apache-2.0`
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - Turns your phone into a touchpad and keyboard for a single app running on a wired external display `GPL-3.0`
* [Dextop](https://github.com/NarYuki/Dextop) - Desktop environment using Samsung DeX or Shizuku with multitasking and custom resolution `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - Switch between various display folding states on foldable devices `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - Keep your phone mostly monochrome, but allow apps like camera to be in color `GPL-3.0`
* [magicdesk](https://github.com/mekhontsev/magicdesk) - Open-source Android 15+ workstation with native windows, external displays, desktops and Termux integration via Shizuku `GPL-3.0`
* [PortalPad](https://github.com/Smart-Home-User/PortalPad) - Turns your phone into a trackpad, air mouse, and remote for external displays like AR glasses, monitors, and TVs `MIT`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - Better screen mirroring for Android devices `Apache-2.0` [(Source code)](https://github.com/farmerbb/SecondScreen)
* [Tideo Auto Brightness](https://github.com/faded-penguin021/Tideo-Auto-Brightness) - Glass-box adaptive-brightness replacement with explainable decisions and circadian support. `MIT`

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork with anime support and plugin management using Shizuku. `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - Export videos downloaded from the Android version of Bilibili `GPL-3.0` [(Source code)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - Merge and export BiliBili cache files into MP4, supports mobile and computer client `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - Manga reader using Shizuku plugin management. Independent successor of Tachiyomi. `Apache-2.0`
  * Mihon/Tachiyomi has several other active forks, including [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) and [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [Buge-Files](https://bugestudio.website/files/) - Material 3 Expressive file manager that installs APKs through Shizuku in addition to storage browsing and management. `GPL-3.0` [(Source code)](https://github.com/BugeStudioTeam/Buge-Files)
* [Butler](https://github.com/d4rken-org/butler) `IAP` 💰 - Fast, private file explorer for power users with tabs, trash bin, regex search, app manager, and root/Shizuku support `GPL-3.0`
* [FileExplorer](https://github.com/SysAdminDoc/FileExplorer) - File manager for local, root, archives, network shares, cloud, vaults and storage analysis `MIT`
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer with Android TV support. Supports full file access using Shizuku, if enabled in settings `GPL-3.0` [(Source code)](https://github.com/mlm-games/fluffy)
* [immich-cloud-media](https://github.com/Dreaming-Codes/immich-cloud-media) - Cloud media provider that surfaces a self-hosted Immich library in Android's system photo picker, configured via Shizuku or ADB. `GPL-3.0`
* [NFile](https://github.com/Senzme/NFile) - File manager with Android folder access using Shizuku `GPL-3.0`
* [plain-app](https://github.com/plainhub/plain-app) - Self-hosted web dashboard to manage files, media, contacts, SMS and calls from a browser, with Shizuku for privileged SMS deletion. `AGPL-3.0`
* [RippleFiles](https://github.com/GokulSB/RippleFiles-FileManager) - Expressive Material file manager with local and cloud storage plus Shizuku-gated Android/data access. `MIT`
* [ROSE](https://github.com/NarayanChetri/ROSE) - Modern file manager with Material 3 UI, archive support, recycle bin and Shizuku access to Android/data and Android/obb without root. `GPL-3.0`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE is Android's most thorough cleaning tool `GPL-3.0` [(Source code)](https://github.com/d4rken-org/sdmaid-se)
* [sync-to-android-data](https://github.com/kamren-zirger/sync-to-android-data) - Syncs files in and out of restricted Android/data folders when target apps open or close `MIT`
* [twig](https://github.com/dev2ex/twig) - Size-first dual-pane file manager (~7MB) for local, archives, FTP/SFTP/SMB/WebDAV/S3/restic/Jellyfin `GPL-3.0`
* [XArchiver](https://github.com/Xtra-Manager-Software/XArchiver) - File manager with built-in archive support `MIT`
* [XFiles](https://github.com/Local1stDotApp/XFiles) - Offline file manager with root and Shizuku support for full filesystem access `GPL-3.0`
* [ZenFile](https://github.com/l930203811/ZenFile) - NFile fork with built-in remote file server support `GPL-3.0`
* [ZhuFiler](https://github.com/Artzhu86/ZhuFiler) - Open-source Material You file manager with archive, editor, media playback, APK handling and Shizuku-backed privileged access. `MIT`

> [!NOTE]
> [See here more file managers (closed-source)](pages/CLOSED_SOURCE.md#file-management)

### Games

* [Ascent](https://github.com/4o3F/Ascent) - A tool for retrieving gacha history links from Mihoyo games  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - Browndust II Mod manager `Proprietary`
* [Cinderbox-Companion](https://github.com/ObfuscatedVoid/Cinderbox-Companion) - Companion app for Stardew Valley on Android with Steam Cloud save sync, game file download, and SMAPI mod management `MIT`
* [CloudSync-Mobile](https://github.com/StardewValleyMods/CloudSync-Mobile) - An app that allows you to sync your Stardew Valley saves across multiple devices `GPL-3.0`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - Manage maps, wallpapers, and screenshots for the game 'Los Angeles Crimes' `GPL-3.0`
* [linkura-localify](https://github.com/ChocoLZS/linkura-localify) - Localization plugin for Link! Like! LoveLive! that translates game text via LLM `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - Mod manager for the game 'Last Origin' `Proprietary`
* [MAA-Meow](https://github.com/Aliothmoon/MAA-Meow/blob/main/README_EN.md) - Run MAA natively on Android for one-click Arknights daily tasks with foreground and background modes `AGPL-3.0`
* [mt-en-applier](https://github.com/Aikiooo/mt-en-applier) - One-tap installer for the unofficial English patch of the Mushoku Tensei mobile game, copying files via Shizuku with no root or PC. `Proprietary`
* [Nibnya](https://github.com/yinghuajimew/Nibnya) - An Android NBT editor for Minecraft Bedrock, powered by Shizuku for /data access `AGPL-3.0`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - Companion app for localizing the Android version of CHAOS;CHILD visual novel `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - Easily import and share Polyfield maps `GPL-3.0`
* [pogoplusle](https://github.com/Mygod/pogoplusle) - Skip the pairing dialog when connecting a Pokémon GO Plus `Apache-2.0`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - Genshin Impact Auto-Conversation Clicker `MIT`
* [stalker](https://github.com/onerdna/stalker) - Save data viewer & editor for Shadow Fight 2 `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order game translation project `MIT`

### Input methods

* [8bitdo-xbox-bridge](https://github.com/BoredNewCoder/8bitdo-xbox-bridge) - Makes the 8BitDo Ultimate Wired Controller for Xbox work as a real system-wide gamepad on Android TV via the reverse-engineered GIP protocol and Shizuku uinput injection. `MIT`
* [BiBi Keyboard](https://github.com/BryceWG/BiBi-Keyboard/blob/main/README_EN.md) - AI-powered voice input method keyboard; Shizuku or root keeps its floating-ball and volume-key background service alive. `Apache-2.0`
* [ButtonSilencer](https://github.com/EithonX/ButtonSilencer) - Blocks faulty headset and IEM remote buttons without disabling the phone's own buttons; Shizuku provides the privileged path for screen-off headset input protection. `MIT`
* [C9](https://github.com/austinauyeung/C9) - Efficient grid-based cursor provided alongside a traditional cursor. Shizuku is only required on Android 11. `Apache-2.0`
* [GameShift](https://github.com/tientien17/GameShift) - Auto-switches the default home launcher when a game controller connects and restores it on disconnect, using Shizuku without root. `Apache-2.0`
* [Joycon2Android](https://github.com/JoeGeC/joycon2android) - Connects Nintendo Switch 2 Joy-Con controllers over BLE and exposes them as system-wide virtual gamepads via a Shizuku UHID relay. `GPL-3.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - An Android app that changes what the buttons do on your devices! `GPL-3.0` [(Source code)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - Play games using mouse and keyboard on Android device; keymapper for games `Apache-2.0`
* [OpenMapper](https://github.com/kinou-p/android-open-mapper) - Free open-source gamepad keymapper using Shizuku for touch injection with sub-millisecond latency; alternative to Mantis and Panda. `PolyForm-Noncommercial-1.0.0`
* [pastiera](https://github.com/palsoftware/pastiera) - Android keyboard specialized for Physical Keyboard Devices. Uses Shizuku for trackpad gestures `GPL-3.0`
* [Steam Controller for Android](https://github.com/SonicDX12/SteamController-Android) - Uses the Steam Controller 2026 as a real Android gamepad via Shizuku-backed Linux uinput; USB, dongle or BLE. `MIT`
* [TitanPad](https://github.com/sztupy/TitanPad) - Converts the Titan2's Physical Keyboard's capacitive input into mouse and scroll gestures. Uses Shizuku for reading the trackpad input and setting up virtual HID devices `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - Keymapper for Android x86 `GPL-3.0`


### Installer & app stores

* [AuroraDroid](https://f-droid.org/packages/com.aurora.adroid/) - FOSS F-Droid client with silent installs via Shizuku/root and automatic updates `GPL-3.0` [(Source code)](https://gitlab.com/AuroraOSS/auroradroid)
* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - An open-source alternative to Google Play Store with privacy and modern design `GPL-3.0` [(Source code)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - Download, install and share mods easily `Proprietary`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid client `GPL-3.0` [(Source code)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater: Updater for privacy-friendly browser `GPL-3.0` [(Source code)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F‑Droid Client `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - App store for GitHub releases with discovery function `Apache-2.0` [(Source code)](https://github.com/kurikomi-labs/komi-store)
* [instafel](https://github.com/mamiiblt/instafel) - Updater app for Instafel, an Instagram mod `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - Modern and functional Android app installer replacement `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) - Simple-ish app using Shizuku to install APKs on-device with advanced options `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - An unofficial client for IzzyOnDroid F-Droid Repository `GPL-3.0`
* [KingInstaller](https://github.com/fcaronte/KingInstaller) - APK installer that spoofs the Play Store installer identity to bypass app-visibility restrictions, installing via intents, Shizuku or root `GPL-3.0`
* [multistore](https://github.com/FedeFluork/multistore) - Aggregates third-party app stores into one catalogue to search, compare, download, and update APKs `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - An F-Droid client with modern UI and an arsenal of extra features `GPL-3.0` [(Source code)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - Get Android App Updates Directly From the Source `GPL-3.0`
  * [ObtainX](https://f-droid.org/packages/dev.bikram.obtainx/) - Obtainium fork with Material 3 UI redesign `GPL-3.0` [(Source code)](https://github.com/bikram-agarwal/ObtainX)
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - App store for modded apps `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - Package installer that allows overwriting the package requester and executor `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android split APKs installer `GPL-3.0` [(Source code)](https://github.com/Aefyr/SAI)
* [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch) - Shizuku-powered app manager with silent installs, updates, and batch operations `GPL-3.0`
* [ShizuStore](https://github.com/timschneeb/ShizuStore) ✨ - App store for Shizuku apps. Based on this awesome-shizuku list and installs APKs straight from their upstream sources `GPL-3.0`
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - A lightweight app installer replacement with split APK support `Apache-2.0`
* [universal-installer](https://github.com/pass-with-high-score/universal-installer) - Install and manage APK packages with split APK support, silent install via Shizuku, and VirusTotal malware scanning `GPL-3.0`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - GUI for Android's builtin `dex2oat` utility, allowing DEX code of installed apps to be re-optimized `Apache-2.0`
* [CaptureCap](https://github.com/yepgoryo/CaptureCap) - Screen and audio recording and streaming app, no root required `MIT`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - Find the reason why the alarm icon is active in the status bar `Proprietary`
* [IrisShot](https://github.com/raging-flames/IrisShot) - Scrolling-screenshot tool for Android games that auto-scrolls and stitches long captures using MediaProjection or Shizuku-powered shell capture. `Proprietary`
* [kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) - Home Assistant kiosk: voice satellite, synchronized music and photo screensaver, with Shizuku used for privileged APK updates and device bridging. `Proprietary`
* [krude](https://github.com/KusStar/krude) - All-in-one app and workflow launcher. Uses Shizuku for process killing and file management `MIT`
* [Mafza](https://github.com/yshalsager/Mafza) - Emergency actions runner with one configurable profile, external emergency triggers, and a safe Dry Run mode `Proprietary`
* [NekokoLPA2](https://github.com/iebb/NekokoLPA2) - Cross-platform eSIM/eUICC manager; on Android it asks Shizuku to open the shell-only QRTR socket for Telephony/TMAPI profile operations `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - Android utility to make notifications persistent/undismissable using Shizuku `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - Automatically close selected apps when you exit them to save power and memory `Apache-2.0`
* [overlay-translator](https://github.com/ciddwd/overlay-translator) - Real-time on-screen translator for games, visual novels, and manga with on-device/cloud OCR and floating overlay `Apache-2.0`
* [PhoneDiagnosticTool](https://github.com/ScoobyDouche/PhoneDiagnosticTool) - On-device phone diagnostics for CPU, GPU, battery, RAM, storage, sensors and display, with optional Shizuku/root elevated readings. `MIT`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - Exploits CVE-2024-31317 for Zygote injection, integrating remote terminal and file transfer capabilities `MIT`
* [silent-alarm](https://github.com/izumisagirii/silent-alarm) - Earphone-first alarm clock that keeps alarms alive on aggressive OEM ROMs with a Shizuku or root watchdog that restarts the app. `AGPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - A simple app for controlling your Android devices from your WearOS watch `Apache-2.0` [(Source code)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - Remote control your device via Telegram messages `BSD 3-Clause`

### Network

* [ADNS](https://github.com/eyalm2000/adns) - DNS-based ad blocker for Android `MIT`
* [Bluetooth Bouncer](https://github.com/harvzor/android-bluetooth-bouncer) - Per-device Bluetooth auto-connect control that stays paired; policy enforced via Shizuku. `GPL-3.0`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - Can read cell tower info on Android `MIT` [(Source code)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - App firewall without using an VPN; can also manage packages `MIT`
* [delta](https://github.com/supershadoe/delta) - Hotspot manager using Shizuku `BSD-3-Clause`
* [Dolphy-App](https://github.com/unvoiddd/Dolphy-App) - NFC, BLE, and IR multi-tool for wireless protocol research `GPL-3.0`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - An app that allows you to turn on your hotspot remotely via Bluetooth - think Apple Continuity, but for everyone `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Secure & open-source alternative to Google's FindMyDevice service. `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - Dual-mode firewall: blocks internet access using Shizuku or a standard local VPN interface or both. `MIT`
* [hikari-adblock](https://github.com/codegeasse1/hikari-adblock) - No-root ad/tracker/malware blocker with local VPN DNS filter plus Shizuku iptables/nftables firewall modes `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - Preview & edit the /etc/hosts file `MIT`
* [MaybeEdgeScanner](https://github.com/maybeknott/MaybeEdgeScanner) - Route-pairing network scanner probing TCP/TLS/HTTP targets, with optional Shizuku-assisted radio diagnostics. `AGPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - A simple application to run Naiveproxy on Android `MIT`
* [NetManager](https://github.com/DottoXD/NetManager) - Material cell-network monitor for 4G/5G NR with tower map, drive tests and speed tests; a Shizuku shell bridge unlocks extra network data. `GPL-3.0`
* [NetSwitcher](https://github.com/nd4y/netswitcher) - Fast Wi-Fi, mobile-data and Ethernet switching via app, shortcut, widget or QS tile using Shizuku or root. `Proprietary`
* [NetToggle](https://github.com/Dhangofa/NetToggle) - A lightweight Android Quick Settings tile to force 5G Only, 4G Only and preferred network modes using Root or Shizuku `GPL-3.0`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - Android app for 4G/5G network mode switching `GPL-3.0`
* [nobita](https://github.com/duhow/nobita) - Records Bluetooth HCI traffic into Wireshark-compatible PCAPNG files on-device using Shizuku. `Proprietary`
* [Quintz](https://github.com/corgilittlelegs/Quintz) - Rootless Wi-Fi band locker and BSSID steering tool that pins Android to 5/6 GHz via Shizuku, with AP telemetry and an RF direction finder. `MIT`
* [RKNHardering](https://github.com/xtclovver/RKNHardering) - Detects VPN/proxy circumvention tooling on-device using community-verified checks, with privileged probes via Shizuku or Root. `AGPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - Open-source app firewall that doesn't depend on VPNs or root `GPL-3.0`
* [Shizzi](https://github.com/carlelieser/shizzi) - Rootless Wi-Fi tethering bypass via Shizuku `Proprietary`
* [sing-box](https://f-droid.org/packages/io.nekohasekai.sfa/) - Universal proxy platform. Uses Shizuku for per-app proxying `GPL-3.0` [(Source code)](https://github.com/SagerNet/sing-box)
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - A persistent network speed tracker in your status bar `GPL-3.0` [(Source code)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - A FOSS Android client for WireGuard and AmneziaWG with auto-tunneling. `MIT`
* [WiFi Portal](https://github.com/lovitus/wifiportal) - Applies captive-portal probe settings via Shizuku with backup, verify-before-write and regional presets. `Proprietary`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - Simple app using Shizuku to manage & view saved Wi-Fi passwords `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - View your saved WiFi passwords on Android 11 and later without root `Proprietary` [(Source code)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - A non-root Xposed framework extending from LSPosed `GPL-3.0`
* [Morphe](https://morphe.software/) - User-friendly YouTube patcher based on Universal-ReVanced-Manager `GPL-3.0` [(Source code)](https://github.com/MorpheApp/morphe-manager)
* [NPatch](https://github.com/7723mod/NPatch) - Rootless LSPosed-based Xposed framework that injects the Xposed API into target APKs `GPL-3.0`
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - ReVanced patcher that has extra features the official manager doesn't have `GPL-3.0`

### Power management

* [Amply](https://github.com/d4rken-org/amply) - Easy control of charging limits. Temporarily allows one full charge, then automatically restores your protective charge limit `GPL-3.0`
* [BatStats](https://github.com/mlm-games/BatStats) - Battery monitor with stats via Shizuku `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - A simple app that shows battery status information on Android 14 and later. `GPL-3.0`
* [Battery-Monitor](https://github.com/tswistak/Battery-Monitor) - Track and log battery capacity and parameters over time using Shizuku `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - Open source app to visually change battery data via Shizuku `GPL-3.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - Enable Doze mode immediately after screen off and turn off motion sensing to get best battery life `GPL-3.0` [(Source code)](https://github.com/Akylas/EnforceDoze)
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - A fire-and-forget program to stop Android apps from running in the background `GPL-3.0` [(Source code)](https://github.com/adil192/no_more_background)
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - Advanced reboot menu with Shizuku support `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - Turn off your Android's screen without entering standby/sleep mode `Proprietary`
* [sleep-timer](https://github.com/Xitee1/sleep-timer) - Sleep timer that can pause media, and turn off WIFI/Bluetooth/Display `GPL-3.0`
* [USB PD Bypass](https://github.com/ONDER1E/usbpdbs) - Toggles USB PD battery-bypass mode at charge thresholds via Shizuku with self-healing recovery. `Proprietary`
* [volt](https://github.com/lebiggg/volt) - Greenify successor: scored app hibernation with UnifiedPush wake-on-push via Shizuku `GPL-3.0`
* [wakelogs](https://github.com/dernikiausd/wakelogs) - Analyzes display wakeups, CPU activity, alarms and device rest with Shizuku-based system diagnostics. `GPL-3.0`
* [zukulock](https://github.com/tiendnm/zukulock) - Very lightweight app that locks the screen when launched. Helps reduce wear on the power button `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Hide your private files and Android apps with just one click `Apache-2.0` [(Source code)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - An application designed to silently protect user data from powerful adversaries `GPL-3.0`
* [anubis](https://github.com/sogonov/anubis) - App manager that freezes/unfreezes app groups based on VPN state via Shizuku pm disable, so frozen apps cannot detect or bypass the VPN. `MIT`
* [AppLock](https://github.com/aload0/AppLock) ✨ - Lock sensitive apps with a PIN and optionally biometrics `MIT`
* [AppOpsNext](https://github.com/1zumiii/AppOpsNext) - Android 15+ AppOps manager with permission templates, batch changes, install history and diagnostics via Shizuku `Proprietary`
* [AvarionX-Android-Antivirus](https://github.com/phsycologicalFudge/AvarionX-Android-Antivirus) - On-device antivirus with local malware/APK scanning, download monitoring and DNS filtering; Shizuku powers ransomware-style behaviour monitoring `MPL-2.0`
* [Monica](https://github.com/Monica-Pass/Monica) - Local-first Bitwarden/KeePass password vault with TOTP; Shizuku keeps autofill protection running in the background. `GPL-3.0`
* [Privacify](https://github.com/robinsrk/privacify) - Privacy control center: permission scanner, sensor-usage timeline and privacy score, with Root/Shizuku advanced hardware controls. `Apache-2.0`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - Manage your device privacy based on lock/unlock state `MIT` [(Source code)](https://github.com/dorumrr/privacyflip)

### Productivity

* [Blink](https://github.com/character-flat/Blink) - A persistent, highly customizable 20-20-20 rule eye-care timer that uses Shizuku to whitelist itself from Android's battery optimizations `GPL-3.0`
* [Cresto](https://github.com/Nevodev/Cresto) - To-do app with AI capture, calendar sync and reminders; its Quick Settings current-screen extraction captures the screen through Shizuku shell access. `Apache-2.0`
* [Curbox](https://f-droid.org/packages/neth.iecal.curbox/) ✨ - Tool to reduce screen addiction and view usage analytics `GPL-3.0` [(Source code)](https://github.com/curbox-app/curbox-android)
* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - Digital Detoxing: Use your phone rather than letting your phone use you `GPL-3.0`
* [HyperCopy](https://github.com/1812z/HyperCopy) - Clipboard-to-app jump tool watching copied links and opening them directly in the right app via Shizuku or LSPosed monitoring. `Proprietary`
* [input-leaf](https://github.com/anasvhora284/input-leaf) - Android client for Input Leap/Deskflow: control your phone with your PC mouse and keyboard over LAN using Shizuku input injection, no root. `Apache-2.0`
* [quickdash](https://github.com/Balajitechlabs/quickdash) - Floating productivity dashboard with UPI/PayPal collection and chat shortcuts; a Shizuku bridge unlocks privileged system capabilities. `Proprietary`
* [Sefirah](https://github.com/shrimqy/Sefirah-Android) - Windows-Android integration for clipboard, notification, file, SMS and call sync; Shizuku enables clipboard on Android 10+. `GPL-3.0`

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - An Android quick setting to toggle Always on Display `MIT` [(Source code)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - Bring back Wi-Fi and mobile data tiles on Android 12 or higher + a better-unified internet tile `GPL-3.0` [(Source code)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DataSimTile](https://github.com/Mygod/DataSimTile) - Tile to switch the default mobile data SIM `Apache-2.0`
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - Provides quick settings tile and shortcuts to turn off the display without locking the screen or stopping foreground running apps `MIT` [(Source code)](https://github.com/UlyssesZh/DisplayToggle)
* [DNS Toggle](https://f-droid.org/packages/com.ericlowry.dnstoggle/) - Quick Settings tile for Private DNS toggling and configuration, with optional advanced automation. `MIT` [(Source code)](https://github.com/ELowry/DNSToggle)
* [ManualRotate](https://github.com/Verisonder/ManualRotate) - Quick-settings tile switching portrait/landscape without rotating the phone; optional Shizuku override for apps that lock orientation. `GPL-3.0`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - QS tile for toggling the private DNS setting on or off `GPL-3.0` [(Source code)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - Quick settings tile to switch active private DNS server `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - QS tiles for toggling USB debugging and switching private DNS hosts `GPL-3.0` [(Source code)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - Enable/Disable device sensors via quick settings `Apache-2.0`

### Software management

* [AppControlX](https://github.com/risunCode/AppControl-X) - Freeze, force stop, uninstall apps, change background optimization and more `GPL-3.0`
* [AppDualZuku](https://github.com/nathanatgit/AppDualZuku) - Manages multiple app instances in isolated or shared workspaces (managed profiles) using Shizuku, with an optional root backend. `Proprietary`
* [AppManagerNG](https://github.com/SysAdminDoc/AppManagerNG) - Fork of [AppManager](https://github.com/muntashirakon/appmanager) to inspect, debloat, back up, freeze and control Android apps; works with Shizuku, ADB, Dhizuku or root. `GPL-3.0`
* [Appslim](https://github.com/Horizen5/Appslim/blob/master/docs/README_en.md) - Android runtime analyzer profiling launch behavior, CPU/memory and Dex calls, then slimming apps through hooks, rules and Shizuku or root actions. `Proprietary`
* [AppVaultX](https://github.com/sunilpaulmathew/AppVaultX) - High-performance app manager powered by Shizuku `GPL-3.0`
* [Blocker](https://github.com/lihenggui/blocker) - Enable/disable Android components such as activities, services, receivers, and providers `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - An app manager focusing on permission management `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - Uninstall any app without root `LGPL-3.0` [(Source code)](https://github.com/samolego/Canta)
* [CloneCat](https://github.com/AhmetCanArslan/CloneCat) - Clone and manage apps across work profile, private space, dual apps, and secondary users with home screen shortcuts `Proprietary`
* [Dexor](https://github.com/DeveshTone/Dexor) - Ahead-of-time (AOT) bytecode compilation and dexopt runtime manager for Android applications `MIT`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android app that disables unused apps while still allowing convenient access to them `MIT`
* [DroidUtility](https://github.com/DroidUtility/DroidUtility) - Non-root utility suite for debloating, system tweaks and privileged shell execution through Shizuku, aimed at mobile-only developers. `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - Improve your device's speed and battery life by freezing crappy software manually or semi-automatically `Apache-2.0` [(Source code)](https://github.com/FreezeYou/FreezeYou)
* [Guest-Manager](https://github.com/dlawoals2713/Guest-Manager) - Enables hidden Guest and multi-user modes on devices where the maker disabled them, via Shizuku shell without root. `Proprietary`
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - Freeze, hide, or disable any app. Create and organize app groups that can be frozen with one click. `GPL-3.0` [(Source code)](https://github.com/aistra0528/Hail)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Complete FLOSS fork of Island `Apache-2.0` [(Source code)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - Android app manager for both rooted and non-rooted devices `GPL-3.0` [(Source code)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - Isolate and clone apps for privacy protection and parallel running `Apache-2.0` [(Source code)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - All-in-one app and workflow launcher `MIT`
* [Minimal Kernel Manager](https://github.com/abhay-byte/mkm) - Kernel manager and system monitor with battery stats, apply-on-boot and hidden-app support via Shizuku or root. `GPL-3.0`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - Manage your Magisk module repository `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - A powerful app to manage both system and user apps `GPL-3.0` [(Source code)](https://github.com/SmartPack/PackageManager)
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - App manager with freeze and install capabilities. `GPL-3.0` [(Source code)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - Check updates for Android apps, Magisk modules and more! `GPL-3.0` [(Source code)](https://github.com/DUpdateSystem/UpgradeAll)

### Task manager

* [KillMyApps](https://github.com/dedeadend/KillMyApps) - Background process killer to improve battery life and performance via Shizuku or root `GPL-3.0`
* [memhogs](https://github.com/cicerothoma/memhogs-android) - Which apps are eating your phone's memory. Per-app breakdown via Shizuku, helpers grouped under the app that owns them `MIT`
* [MemorySnapshot](https://github.com/RyensX/MemorySnapshot/blob/master/docs/README_EN.md) - On-device Android memory observer: per-app/process PSS tracking, snapshot save and compare, with data gathered via Shizuku or root. `Proprietary`
* [Pensum](https://github.com/troikoss/Pensum) ✨ - Windows-style Task Manager for Android `GPL-3.0`
* [ReAppzuku](https://github.com/gree1d/ReAppzuku) - Control and manage background applications. Fork of shappky `GPL-3.0`
* [Recents](https://github.com/tymwitko/Recents) - Launcher-agnostic replacement for the system Recents menu, with app-kill support via Shizuku `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - Monitor running services on your Android device `MIT` [(Source code)](https://github.com/biplobsd/running_services_monitor)
* [RvSystem Monitor](https://github.com/Rve27/RvSystem-Monitor) - High-performance system monitor (Compose + Rust) with Shizuku-fed CPU and hardware insights `GPL-3.0`
* [shappky](https://github.com/YasserNull/shappky) ✨ - A simple app to boost performance by stopping background apps. `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - A Task Manager for Android. Killing processes requires root access. `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - A local ADB shell for Shizuku-powered Android devices `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You Redesign of aShell app. `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - Terminal, SSH, VNC, RDP, SFTP & cloud storage client for Android `AGPL-3.0` [(Source code)](https://github.com/GlassHaven/Haven)

> [!NOTE]
> Using [rish](pages/RISH.md), you can create a local ADB shell with any terminal emulator, such as Termux.

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - Toggle Always on Display from the quick settings panel `MIT` [(Source code)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [carrier-ims-for-pixel](https://github.com/ryfineZ/carrier-ims-for-pixel) - Maintained Pixel IMS toolkit: tune VoLTE/VoWiFi/VoNR, 5G display and carrier config via Shizuku `Apache-2.0`
* [hilight-studio](https://github.com/DhananjayBhosale/hilight-studio) - Pixel 11 HiLight LED controller for custom notification and status light effects `MIT`
* [Pixel-IMS-5G](https://github.com/barrylk/Pixel-IMS-5G) - Enable 5G standalone (5G SA) and VoNR on Google Pixel devices `GPL-3.0`
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - Enable VoLTE on Pixel 6 & 7 with LG U+ `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - Enable VoLTE for carriers in unsupported regions on Pixel devices `GPL-3.0`
* [Root-My-Pixel](https://github.com/alex193a/Root-My-Pixel) - Root automation for Pixel devices via CVE-2026-43499 exploit `Proprietary`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - Customizable widget, can upgrade the built-in 'At a glance' widget on Pixel devices using Shizuku `GPL-3.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - Enhanced IMS Configuration Tool for Google Pixel devices `Apache-2.0`
* [Video Boost AO](https://github.com/AgusRomeroL/video-boost-ao) - Keeps Video Boost enabled on Pixel Pro cameras, re-enabling it every time the camera opens. Shizuku grants WRITE_SECURE_SETTINGS for the on-demand mode `MIT`

#### Samsung OneUI

* [4Zones](https://github.com/mr-biz-apps/4zones) - Restores four-zone window tiling on Samsung DeX and Android desktop mode with tap-to-snap and keyboard shortcuts `Apache-2.0`
* [android-battery-health](https://github.com/willbilec/android-battery-health) - Samsung battery health and cycle-count viewer with screen-reader-friendly layout via Shizuku. `Proprietary`
* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 rootless font installer `GPL-3.0` [(Source code)](https://codeberg.org/dryerlint/fontsmanager)
* [Root-My-Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy) - KSU installer for supported Samsung Galaxy firmware with CVE-2026-43499 `Apache-2.0`
* [pearity](https://github.com/thejaustin/pearity) - Matches Samsung One UI system settings to iOS defaults one toggle at a time (three-state Android/Custom/iOS), writing secure settings via Shizuku or root. `Proprietary`
* [SamsungRegionOverride](https://github.com/Ritel-T/SamsungRegionOverride) - Temporarily change the SIM region seen by Galaxy Store and other region-locked apps, no root, one-tap restore `MIT`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - Enable or disable fast charging mode on Samsung devices when the battery temperature reaches a certain point  `Proprietary`
* [ScamsungFonts](https://github.com/KhunHtetzNaing/ScamsungFonts) - Font manager for Samsung Galaxy (OneUI) via System shell or Root `No license`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - Disable the forced camera shutter sounds on Samsung devices that have their CSC set to certain countries with this restriction `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - Privilege escalation exploit [(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) to system user access (UID 1000) on non-rooted devices running up to OneUI 5. Uses Shizuku for automation `LGPL-2.1`
* [ZFold-Multi-DPI](https://github.com/balamurugan15/ZFold-Multi-DPI) - Applies separate screen zoom and DPI presets for the cover and inner displays of Samsung Galaxy Z Fold devices `Proprietary`

#### MIUI

* [Aura](https://github.com/tgvdufuture/Aura) - Custom RGB notification LED app for POCO X8 Pro with per-app, per-contact, and per-group colors and animations `MIT`
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) `Paid` 💰 - 5G shortcut switch for HyperOS/MIUI `GPL-3.0` [(Source code)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - Turn off MIUI ads with minimal cost `Apache-2.0`
* [HyperOS FCM Fix](https://github.com/dingwen07/hyperos-fcm-fix) - Keeps Google Play services unrestricted on HyperOS so FCM push notifications arrive on time `GPL-3.0`
* [HyperOS-MTZ-Studio](https://github.com/GloriousApps/HyperOS-MTZ-Studio/blob/main/readme_en.md) - MTZ theme workspace for Xiaomi HyperOS; imports, composes, translates and applies themes, using Shizuku or Shevery for rootless theme application. `Proprietary`
* [HyperOS3ScrollSetter](https://github.com/BlizzardAn225/HyperOS3ScrollSetter) - Restores scrolling wallpapers and disables forced darkening on HyperOS 3/4, applying secure settings and restarts through Shizuku.newProcess or a root module. `GPL-3.0`
* [HyperOSUnfcker](https://github.com/Enki013/hyperosunfcker) - Unlocks hidden performance, display, memory, battery, and visual settings on HyperOS/MIUI devices `LGPL-3.0`
* [IslandRecorder](https://github.com/wxxsfxyzm/IslandRecorder) - Xiaomi-focused screen recorder with Super Island controls `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - One-click configuration for Mix Flip's outer screen: Use any apps and restore system apps to default style `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - Enable 3-button navigation in rhythm games for MIUI / HyperOS  `Proprietary`

#### Other

* [Calibrate-SoC](https://github.com/mayusi/Calibrate-SoC) - SoC tuner, monitor and benchmark suite for Android gaming handhelds with goal-seeking governor and live HUD. `Apache-2.0`
* [Evolve_Launcher_v2](https://github.com/JarJarBlinkz/Evolve_Launcher_v2) - Customizable home launcher for Meta Quest headsets with app organization, playtime tracking and Shizuku-powered clear data/cache actions. `Proprietary`
* [flipx](https://github.com/jlgrimes/flipx) - Routes the home button to different launchers based on Anbernic RG Rotate hinge state `Proprietary`
* [GlyphBarty](https://github.com/Link2011-Act2/GlyphBarty) - Customizable Glyph visualizer for Nothing Phone with music sync, Quick Settings toggle, and charging status display `MIT`
* [Heimdall-AYN-Thor-Assistant](https://github.com/mastercook777/Heimdall-AYN-Thor-Assistant) - Lower-screen game assistant for the AYN Thor with profiles, macros, touch controls, maps and Shizuku-powered touch injection. `Apache-2.0`
* [MindControl](https://github.com/Dinico414/MindControl) - Hardware button remapper and AOD toolkit for the iKKO MindOne that monitors physical keys through Shizuku getevent, with a root fallback. `Proprietary`
* [panel-assistant](https://github.com/panel-assistant/android) - Home Assistant wall-panel dashboard with entity filtering, MQTT device controls and Shizuku/root-powered provisioning and verified installs. `Apache-2.0`
* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control gives precise control over the Nothing Phone (3)'s recording light `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - System-wide shoulder triggers for Nubia Red Magic phones `MIT`
* [thor-wayfinder](https://github.com/Thor-Wayfinder/thor-wayfinder) - Moves apps between the two AYN Thor screens with back-button gestures `CC-BY-NC-ND-4.0`
* [Thors-Lightning](https://github.com/HughesTechNZ/Thors-Lightning) - Controller-driven dual-screen brightness control for the AYN Thor, with optional Shizuku-privileged input recording. `MIT`
* [ThorVolumeLink](https://github.com/pth2000/ThorVolumeLink) - Synchronized volume control for the dual displays of the AYN Thor `MIT`

### Closed-source apps

Closed-source apps have been moved into a separate sublist. [You can view them here.](pages/CLOSED_SOURCE.md) 

> [!NOTE]
> **Why are closed-source apps in a separate list?**
> Shizuku gives apps high-level ADB access. For security reasons, this main directory only includes open-source and source-available apps, as anyone can check their code to make sure they aren't doing anything shady and compile them on their own machine.
>
> Fully closed-source apps require blind trust, so they are kept in a separate list. 
> Almost all closed-source apps have already open-source counterparts that implement the same (if not even more) features anyways.

### Unlisted apps
To keep the main list clean, all apps that have been deprecated or abandoned are stored on a separate page: [ARCHIVED.md](pages/ARCHIVED.md)

> [!NOTE]
> I'm also using an automated crawler that searches for new projects, making use of Shizuku across GitHub and several F-Droid repos. You can view the [current auto-generated crawl report here](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Porter API](https://github.com/d4rken-org/porter-api) - Android SDK for Porter, a maintained Shizuku fork, offering compatible Shizuku APIs with direct Porter support `MIT`
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Developer documentation for Shizuku and Sui, including examples `Apache-2.0`
* [Shizuku-API-Flutter-Plugin](https://github.com/runoob-coder/shizuku-api-flutter-plugin) - A Flutter plugin to interact with the Shizuku API. `MIT`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - Shizuku API bindings for Flutter apps `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android Coroutines-friendly Kotlin-first Package Installer extensions with Shizuku support `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - A file operation library with Shizuku, root, and regular filesystem backends `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`


### System

* [droid-mcp](https://github.com/stixez/droid-mcp) - Android SDK giving local LLM/AI apps structured on-device access to phone data, plus shell-level control via Shizuku `Apache-2.0`
* [libterm](https://github.com/niki914/libterm) - Kotlin-first Android terminal session library with User, Root, Shizuku, and SSH backends behind one API `Proprietary`
* [Priv Kit](https://github.com/priv-kit/priv-kit) - Lightweight privileged-runtime library for Root, ADB, or Shizuku-backed Binder access in your own app `Proprietary`

--------------------

## Miscellaneous content

### Command-line utilities

* [AndroSH](https://github.com/ahmed-alnassif/AndroSH) - No-Root Multi-Distro Linux on Android via Shizuku/ADB - Run Arch, Fedora, Alpine, Debian, Ubuntu, Kali, Void, Manjaro, OpenSUSE & Chimera with full system integration, proot isolation & Termux:X11 GUI `GPL-3.0`

### Flows for [Automate](https://llamalab.com/automate/)

* [Better Shizuku Starter](https://llamalab.com/automate/community/flows/50863) - Check and automatically start Shizuku **13.6** on key events via wireless debugging with the *free* version of Automate. `MIT`
* [Shizuku Keeper](https://llamalab.com/automate/community/flows/51118) - Continuously run Shizuku **13.6** or **ADB** uninterrupted without root, Wi-Fi, or cables via USB debugging with Automate *Premium.* `MIT`
  * [Shizuku Keeper Lite](https://llamalab.com/automate/community/flows/51012) - Check Shizuku **13.6** at regular intervals and automatically restart it via wireless debugging with the *free* version of Automate. `MIT`
--------------------

## Annotations
- ✨ - My personal recommendation: makes extensive use of Shizuku or is a unique/hidden gem
- `Paid` 💰 - Paid application
- `IAP` 💰 - Contains in-app purchases
- `Ads` - Contains ads
- `Proprietary` - Not licensed under a FOSS license. Applies to closed-source software or source-available projects.
- `n-day trial` - Payment required after `n` days
- `Root` - Requires Shizuku to run in Root mode

--------------------

## License

This list is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/deed.en) License.

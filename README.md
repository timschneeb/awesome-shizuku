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

### AI agents

* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - Automates actions on your device using the AutoGLM vision language model `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - The most powerful AI agent and AI chat software on Android. Can run commands using Shizuku `LGPL-3.0`
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - Automation and Multitasking Framework using AutoGLM. Can create virtual screens that agents can run apps on and use multi-window `Apache 2.0`


### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - An F-Droid client designed for Android TVs `GPL-3.0` [(Source code)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer designed for Android TVs `GPL-3.0` [(Source code)](https://github.com/mlm-games/fluffy)


### Audio

* [MicUp](https://github.com/papergray/MicUp) ✨ - Real-time microphone audio processing for Android `MIT`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - An implementation of the system-wide JamesDSP audio processing engine for non-rooted Android devices `GPL-3.0` [(Source code)](https://github.com/timschneeb/RootlessJamesDSP)
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - Control each app's volume independently `GPL-2.0`
* [wecho](https://github.com/qumolangmo/wecho) - An Android application for global audio effects processing `MIT`

### Automation

* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - JavaScript-based automation tool `MPL-2.0`
* [Geto](https://github.com/JackEblan/Geto) - Automatically change device settings when a specific app is launched. `GPL-3.0`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - Allows automatic or one-click configuration of your device for specific life situations `Apache-2.0`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - Helper app for Tasker `Propietary`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Discord modding tool `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - A simple app for automatically launching Bluesky links in your preferred Bluesky client `MIT` [(Source code)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - Send and receive files over Bluetooth `MIT` [(Source code)](https://github.com/kmod-midori/CatShare)
* [Kettu](https://github.com/C0C0B01/Kettu) - Discord modding tool. Continuation of the abandoned Bunny-Manager project `BSD-3-Clause`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - A simple app for automatically launching Lemmy links in your preferred Lemmy client. `MIT` [(Source code)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - A simple app for automatically launching fediverse links in your preferred Mastodon client. `MIT` [(Source code)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Discord modding tool. Another continuation of the abandoned Bunny-Manager project `OSL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - An app that lets you browse the web over SMS `GPL-3.0`

### Customization

* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - Smart dark mode based on ambient light `GPL-3.0` [(Source code)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - Port of Now Playing from Pixels to other Android devices `GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) - A small Android app to let you schedule dark mode On/Off `MIT` [(Source code)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - A simple tool to toggle DND automatically when using specified apps `AGPL-3.0` [(Source code)](https://github.com/dic1911/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - Manage automatic rotation of different screens on Android phones `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name is a very simple app to change the carrier names on unrooted Android devices `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - An application to modify Material You colors of your device `GPL-3.0`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - Customize animation speeds on a more fine-grained level `GPL-3.0` [(Source code)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ](https://github.com/KieronQuinn/DarQ) ✨ - DarQ provides a per-app selectable force dark option for Android 10 and above `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - Some Android app widgets and live wallpapers `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - Highly customizable, gestures based Android launcher focused on speed and efficiency `GPL-3.0` [(Source code)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - Tiling window manager, Samsung DEX replacement, popup app launcher `Proprietary`
* [essentials](https://github.com/sameerasw/essentials) ✨ - Essential tools, mods and workarounds for Pixels. Also compatible with other devices `MIT`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - Adds desktop-like multi-window support on Android for smartphones. `GPL-3.0`
* [gama](https://github.com/palincat/gama) - Can switch between OpenGL and Vulkan renderers by setting the `debug.hwui.renderer` system property `MIT`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - Launcher for dual-screen gaming devices. Uses Shizuku to map on of the touch screens to controller inputs `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - Allows users to select individual app languages (Android 13+) `Apache-2.0`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - Restore the Android <12 Url-App-Link-Chooser with Material3  `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - Display widgets on the lockscreen. Shizuku is only required on Android 13 and later `MIT` [(Source code)](https://github.com/zacharee/LockscreenWidgets/)
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - A simple app that enables you to add additional (or "unsupported") languages to your device's locale settings, if the OEM (Xiaomi) doesn't let you  `MIT`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - A keyboard-first Android command palette that unifies app/device search, and system utilities into an overlay `GPL-3.0`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - Create launcher shortcuts for shell commands `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - Contains some easy-to-use tools to go beyond the level of control allowed by Android System `GPL-3.0`
* [Smart Edge](https://f-droid.org/en/packages/com.imi.smartedge.sidebar.panel/) - A highly customizable Android side panel inspired by OriginOS `MIT` [(Source code)](https://github.com/Imtiaz-Official/Smart-Edge)
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Plugins for Smartspacer `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - View and modify hidden settings on Android devices `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - Port of the double tap on the back of the device feature from Android 12 to any Android 7.0+ device `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) - Clean up tracking from sharing links. Supports custom URL rewrite rules `GPL-3.0` [(Source code)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - Use a start menu to access apps. Shizuku can unlock additional features `Apache-2.0` [(Source code)](https://github.com/farmerbb/Taskbar)
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - CPU and battery widgets `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - A full desktop experience layer for Android `GPL-3.0`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - Dump package names of apps that have registered an account for a user. `Proprietary`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - Detect Treble, GSI, Mainline, APEX, system-as-root(SAR), A/B, etc. `Apache-2.0` [(Source code)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) - IDE for JVM development. Uses Shizuku for an embedded shell `GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity) - A current activity monitor `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - Backup/restore private app data of debuggable apps using Shizuku `GPL-3.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - A simple app made to help users easily install GSIs via DSU's Android feature. `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - Fixes MediaStore & File IO compatibility issues between HostProfile App and WorkProfile/DualApp/MultiApp. `Proprietary`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - FPS viewer overlay with graph `Proprietary`
* [FrameX-Android](https://github.com/MaheshSharan/FrameX-Android) - Real-time performance overlay for Android `MIT`
* [get_event](https://github.com/lalakii/get_event) - Read /dev/input/event*  `Proprietary`
* [KeyAttestation](https://github.com/vvb2060/KeyAttestation) - Supports generating, saving, loading, parsing and verifying Android key and ID attestation data. `Proprietary`
* [LibChecker](https://github.com/LibChecker/LibChecker) - An app to view libraries used in apps on your device. Uses Shizuku to determine the installation source of other apps. `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - Yet another logcat reader for Android  `GPL-3.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - Utilizes Shizuku to call AppOps APIs for fine-grained app permission control `MIT`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - Launch/interact with (un)exported activities, services, and receivers. Supports Shizuku alongside root. `GPL-3.0` [(Source code)](https://github.com/zacharee/RootActivityLauncher)
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - Widgets & quick settings tile to toggle wireless debugging (with KDE Connect integration) `GPL-3.0`

### Device owner (DPM)

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - Shizuku-inspired app that allows sharing DeviceOwner permissions to third-party apps `GPL-3.0`
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - Manage your device with Device owner privileges `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - Fork of OwnDroid with added features `GPL-3.0`

### Display management
* [android-display-extend](https://github.com/jqssun/android-display-extend) ✨ - Display manager for physical and virtual displays with a built-in virtual touchscreen. Great for use with `scrcpy --new-display` on a PC `GPL-3.0`
* [ConnectScreen](https://connect-screen.com/) - Launch single apps to display in fullscreen on external displays. Can use the primary screen of the mobile as a virtual touchpad to control external display. Can rotate the screen for applications like TikTok `GPL-3.0` [(Source code)](https://gitee.com/connect-screen/connect-screen)
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - Turns your phone into a touchpad and keyboard for a single app running on a wired external display `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - Switch between various display folding states on foldable devices `Apache-2.0`
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - Keep your phone mostly monochrome, but allow apps like camera to be in color `GPL-3.0`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - Better screen mirroring for Android devices `Apache-2.0` [(Source code)](https://github.com/farmerbb/SecondScreen)

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork with anime support and plugin management using Shizuku. `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - Export videos downloaded from the Android version of Bilibili `GPL-3.0` [(Source code)](https://github.com/10miaomiao/bili-down-out)
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - Merge and export BiliBili cache files into MP4, supports mobile and computer client  `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - Manga reader using Shizuku plugin management. Independent successor of Tachiyomi. `Apache-2.0`
  * Mihon/Tachiyomi has several other active forks, including [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) and [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - An file manager and archive viewer with Android TV support. Supports full file access using Shizuku, if enabled in settings `GPL-3.0` [(Source code)](https://github.com/mlm-games/fluffy)
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) `IAP` 💰 - SD Maid 2/SE is Android's most thorough cleaning tool `GPL-3.0` [(Source code)](https://github.com/d4rken-org/sdmaid-se)

> [!NOTE]
> [See here more file managers (closed-source)](pages/CLOSED_SOURCE.md#file-management)

### Games

* [Ascent](https://github.com/4o3F/Ascent) - A tool for retrieving gacha history links from Mihoyo games  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - Browndust II Mod manager `Proprietary`
* [blocktopograph](https://github.com/Blocktopograph/Blocktopograph) - Blocktopograph is an app server for MCBE, it includes a world, NBT editor for local worlds `Apache-2.0`
* [CloudSync-Mobile](https://github.com/FawazTakahji/CloudSync-Mobile) - An app that allows you to sync your Stardew Valley saves across multiple devices `GPL-3.0`
* [HandheldExp](https://github.com/Teppichseite/HandheldExp) - In-game menu for EmulationStation (ES-DE) on Android  `MIT`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - Manage maps, wallpapers, and screenshots for the game 'Los Angeles Crimes' `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - Mod manager for the game 'Last Origin' `Proprietary`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - Companion app for localizing the Android version of CHAOS;CHILD visual novel `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - Easily import and share Polyfield maps `GPL-3.0`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - Genshin Impact Auto-Conversation Clicker `MIT`
* [stalker](https://github.com/onerdna/stalker) - Save data viewer & editor for Shadow Fight 2 `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order game translation project `MIT`

### Input methods

* [andRemote2](https://github.com/c0dev0id/andRemote2) - Emulates the DMD Remote 2 for map apps `Proprietary`
* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - Show customized taps upon touches `GPL-3.0`
* [C9](https://github.com/austinauyeung/C9) - Efficient grid-based cursor provided alongside a traditional cursor. Shizuku is only required on Android 11. `Apache-2.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - An Android app that changes what the buttons do on your devices! `GPL-3.0` [(Source code)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - Play games using mouse and keyboard on Android device; keymapper for games `Apache-2.0`
* [pastiera](https://github.com/palsoftware/pastiera) - Android keyboard specialized for Physical Keyboard Devices. Uses Shizuku for trackpad gestures `GPL-3.0`
* [TitanPad](https://github.com/sztupy/TitanPad) - Converts the Titan2's Physical Keyboard's capacitive input into mouse and scroll gestures. Uses Shizuku for reading the trackpad input and setting up virtual HID devices `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - Keymapper for Android x86  `GPL-3.0`


### Installer & app stores

* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - An open-source alternative to Google Play Store with privacy and modern design `GPL-3.0` [(Source code)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - Download, install and share mods easily `Proprietary`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid client `GPL-3.0` [(Source code)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater: Updater for privacy-friendly browser `GPL-3.0` [(Source code)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Material3 F‑Droid Client `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - App store for GitHub releases with discovery function `Apache-2.0` [(Source code)](https://github.com/OpenHub-Store/GitHub-Store)
* [instafel](https://github.com/mamiiblt/instafel) - Updater app for Instafel, an Instagram mod `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - Modern and functional Android app installer replacement `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) -  Simple-ish app using Shizuku to install APKs on-device with advanced options `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - An unofficial client for IzzyOnDroid F-Droid Repository `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - An F-Droid client with modern UI and an arsenal of extra features `GPL-3.0` [(Source code)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - Get Android App Updates Directly From the Source `GPL-3.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - App store for modded apps `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - Package installer that allows overwriting the package requester and executor `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Android split APKs installer `GPL-3.0` [(Source code)](https://github.com/Aefyr/SAI)
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - A lightweight app installer replacement with split APK support `Apache-2.0`
* [universal-installer](https://github.com/pass-with-high-score/universal-installer) - Install and manage APK packages with split APK support, silent install via Shizuku, and VirusTotal malware scanning `GPL-3.0`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - GUI for Android's builtin `dex2oat` utility, allowing DEX code of installed apps to be re-optimized `Apache-2.0`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - Find the reason why the alarm icon is active in the status bar `Proprietary`
* [krude](https://github.com/KusStar/krude) - All-in-one app and workflow launcher. Uses Shizuku for process killing and file management `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - Android utility to make notifications persistent/undismissable using Shizuku `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - Automatically close selected apps when you exit them to save power and memory `Apache-2.0`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - Exploits CVE-2024-31317 for Zygote injection, integrating remote terminal and file transfer capabilities `MIT`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - A simple app for controlling your Android devices from your WearOS watch `Apache-2.0` [(Source code)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - Remote control your device via Telegram messages `BSD 3-Clause`


### Network

* [ADNS](https://github.com/eyalm2000/adns) - DNS-based ad blocker for Android `MIT`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - Can read cell tower info on Android `MIT` [(Source code)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - App firewall without using an VPN; can also manage packages `MIT`
* [delta](https://github.com/supershadoe/delta) - Hotspot manager using Shizuku `BSD-3-Clause`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - An app that allows you to turn on your hotspot remotely via Bluetooth - think Apple Continuity, but for everyone `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Secure & open-source alternative to Google's FindMyDevice service. `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - Dual-mode firewall: blocks internet access using Shizuku or a standard local VPN interface or both. `MIT`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - Preview & edit the /etc/hosts file `MIT`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - A simple application to run Naiveproxy on Android `MIT`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - Android app for 4G/5G network mode switching `GPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - Open-source app firewall that doesn't depend on VPNs or root `GPL-3.0`
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - A persistent network speed tracker in your status bar `GPL-3.0` [(Source code)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - A FOSS Android client for WireGuard and AmneziaWG with auto-tunneling. `MIT`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - Simple app using Shizuku to manage & view saved Wi-Fi passwords  `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - View your saved WiFi passwords on Android 11 and later without root `Proprietary` [(Source code)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - A non-root Xposed framework extending from LSPosed `GPL-3.0`
* [Morphe](https://morphe.software/) - User-friendly YouTube patcher based on Universal-ReVanced-Manager `GPL-3.0` [(Source code)](https://github.com/MorpheApp/morphe-manager)
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - ReVanced patcher that has extra features the official manager doesn't have  `GPL-3.0`

### Power management

* [BatStats](https://github.com/mlm-games/BatStats) - Battery monitor with stats via Shizuku `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - A simple app that shows battery status information on Android 14 and later. `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - Open source app to visually change battery data via Shizuku `GPL-3.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) - Enable Doze mode immediately after screen off and turn off motion sensing to get best battery life `GPL-3.0` [(Source code)](https://github.com/farfromrefug/EnforceDoze)
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) - A fire-and-forget program to stop Android apps from running in the background `GPL-3.0` [(Source code)](https://github.com/adil192/no_more_background)
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - Advanced reboot menu with Shizuku support `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - Turn off your Android's screen without entering standby/sleep mode `Proprietary`
* [sleep-timer](https://github.com/Xitee1/sleep-timer) - Sleep timer that can pause media, and turn off WIFI/Bluetooth/Display `GPL-3.0`
* [zukulock](https://github.com/tiendnm/zukulock) - Very lightweight app that locks the screen when launched. Helps reduce wear on the power button `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Hide your private files and Android apps with just one click `Apache-2.0` [(Source code)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - An application designed to silently protect user data from powerful adversaries `GPL-3.0`
* [AppLock](https://github.com/aload0/AppLock) ✨ - Lock sensitive apps with a PIN and optionally biometrics `MIT`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - Manage your device privacy based on lock/unlock state `MIT` [(Source code)](https://github.com/dorumrr/privacyflip)

### Productivity

* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - Digital Detoxing: Use your phone rather than letting your phone use you `GPL-3.0`
* [digipaws](https://f-droid.org/packages/nethical.digipaws/) ✨ - Tool to reduce screen addiction by regulating app usage through a gamified experience `GPL-3.0` [(Source code)](https://github.com/nethical6/digipaws)

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - An Android quick setting to toggle Always on Display `MIT` [(Source code)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - Bring back Wi-Fi and mobile data tiles on Android 12 or higher + a better-unified internet tile `GPL-3.0` [(Source code)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DataSimTile](https://github.com/Mygod/DataSimTile) - Tile to switch the default mobile data SIM `Apache-2.0`
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - Provides quick settings tile and shortcuts to turn off the display without locking the screen or stopping foreground running apps `MIT` [(Source code)](https://github.com/UlyssesZh/DisplayToggle)
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - QS tile for toggling the private DNS setting on or off  `GPL-3.0` [(Source code)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - Quick settings tile to switch active private DNS server  `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - QS tiles for toggling USB debugging and switching private DNS hosts `GPL-3.0` [(Source code)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - Enable/Disable device sensors via quick settings `Apache-2.0`

### Software management

* [AppControlX](https://github.com/risunCode/AppControl-X) - Freeze, force stop, uninstall apps, change background optimization and more `GPL-3.0`
* [Blocker](https://github.com/lihenggui/blocker) - Enable/disable Android components such as activities, services, receivers, and providers `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - An app manager focusing on permission management `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) - Uninstall any app without root `LGPL-3.0` [(Source code)](https://github.com/samolego/Canta)
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android app that disables unused apps while still allowing convenient access to them `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - Improve your device's speed and battery life by freezing crappy software manually or semi-automatically `Apache-2.0` [(Source code)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - Freeze, hide, or disable any app. Create and organize app groups that can be frozen with one click. `GPL-3.0` [(Source code)](https://github.com/aistra0528/Hail)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Complete FLOSS fork of Island `Apache-2.0` [(Source code)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - Android app manager for both rooted and non-rooted devices `GPL-3.0` [(Source code)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - Isolate and clone apps for privacy protection and parallel running `Apache-2.0` [(Source code)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - All-in-one app and workflow launcher `MIT`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - Manage your Magisk module repository `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - A powerful app to manage both system and user apps `GPL-3.0` [(Source code)](https://github.com/SmartPack/PackageManager)
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - App manager with freeze and install capabilities. `GPL-3.0`  [(Source code)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - Check updates for Android apps, Magisk modules and more! `GPL-3.0` [(Source code)](https://github.com/DUpdateSystem/UpgradeAll)

### Task manager

* [Pensum](https://github.com/troikoss/Pensum) ✨ - Windows-style Task Manager for Android `GPL-3.0`
* [ReAppzuku](https://github.com/gree1d/ReAppzuku) - Control and manage background applications. Fork of shappky `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - Monitor running services on your Android device `MIT` [(Source code)](https://github.com/biplobsd/running_services_monitor)
* [shappky](https://github.com/YasserNull/shappky) ✨ - A simple app to boost performance by stopping background apps. `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) - A Task Manager for Android. Killing processes requires root access. `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - A local ADB shell for Shizuku-powered Android devices `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You Redesign of aShell app. `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - Terminal, SSH, VNC, RDP, SFTP & cloud storage client for Android `AGPL-3.0` [(Source code)](https://github.com/GlassOnTin/Haven)
* [ReTerminal](https://github.com/RohitKushvaha01/ReTerminal) ✨ - Sleek, Material 3-inspired terminal emulator based on Termux's robust TerminalView `MIT`

> [!NOTE]
> Using [rish](pages/RISH.md), you can create a local ADB shell with any terminal emulator, such as Termux.

### Vendor-specific

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - Toggle Always on Display from the quick settings panel `MIT` [(Source code)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - Enable VoLTE on Pixel 6 & 7 with LG U+ `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - Enable VoLTE for carriers in unsupported regions on Pixel devices `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - Customizable widget, can upgrade the built-in 'At a glance' widget on Pixel devices using Shizuku `GPL-3.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - Enhanced IMS Configuration Tool for Google Pixel devices `Apache-2.0`

#### Samsung OneUI

* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - One UI 8 rootless font installer `GPL-3.0` [(Source code)](https://codeberg.org/dryerlint/fontsmanager)
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - Enable or disable fast charging mode on Samsung devices when the battery temperature reaches a certain point  `Proprietary`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - Disable the forced camera shutter sounds on Samsung devices that have their CSC set to certain countries with this restriction `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - Privilege escalation exploit [(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) to system user access (UID 1000) on non-rooted devices running up to OneUI 5. Uses Shizuku for automation `LGPL-2.1`

#### MIUI

* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - 5G shortcut switch for HyperOS/MIUI `GPL-3.0` [(Source code)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - Turn off MIUI ads with minimal cost `Apache-2.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - Display most apps in the form of freeform on MIUI `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - One-click configuration for Mix Flip's outer screen: Use any apps and restore system apps to default style `GPL-3.0`
* [mtbtool-android-app](https://github.com/h3nnes/mtbtool-android-app) - Perform bandlock and edit EFS NV items on qualcomm-based Xiaomi devices without root  `MIT`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - Enable 3-button navigation in rhythm games for MIUI / HyperOS  `Proprietary`

#### Other

* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - Recording Light Control gives precise control over the Nothing Phone (3)'s recording light `Proprietary`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - System-wide shoulder triggers for Nubia Red Magic phones `MIT`

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

* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Developer documentation for Shizuku and Sui, including examples `Apache-2.0`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - Shizuku API bindings for Flutter apps `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Android Coroutines-friendly Kotlin-first Package Installer extensions with Shizuku support `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - A file operation library with Shizuku, root, and regular filesystem backends `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - Flutter plugin for installing Android APKs using Shizuku API `MIT`

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

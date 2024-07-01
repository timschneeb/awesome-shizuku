# awesome-shizuku

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku allows normal apps to use system APIs directly with elevated privileges using ADB on non-rooted devices. This list compiles a few apps that are known to make use of Shizuku's capabilities.

More details: https://shizuku.rikka.app/

Pull requests are welcome. See [Contributing](CONTRIBUTING.md) for hints.

--------------------


## Table of contents

- [Apps](#apps)
  - [Audio](#audio)
  - [Automation](#automation)
  - [Communication](#communication)
  - [Customization](#customization)
  - [Development utilities](#development-utilities)
  - [Education](#education)
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

* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - An implementation of the system-wide JamesDSP audio processing engine for non-rooted Android devices `GPL-3.0` [(Source code)](https://github.com/ThePBone/RootlessJamesDSP)

### Automation

* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - Allows automatic or one-click configuration of your device for specific life situations `Apache-2.0`
* [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) `Ads` `IAP` 💰 - Automation app for Android devices. Version 5.46 and later introduces Shizuku support. `Proprietary`

### Communication

* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - A simple app for automatically launching lemmy links in your preferred Lemmy client. `MIT` [(Source code)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - A simple app for automatically launching fediverse links in your preferred Mastodon client. `MIT` [(Source code)](https://github.com/zacharee/MastodonRedirect)
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - An app that lets you browse the web over SMS `GPL-3.0`
* [Vendetta-Manager](https://github.com/vendetta-mod/VendettaManager) - Patch manager for the Discord Vendetta mod `OSL-3.0`


### Customization

* [AAAD](https://github.com/shmykelsa/AAAD) `IAP` 💰 - Downloads popular Android Auto 3rd party apps and installs on Android Auto `Proprietary`
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - Port of Now Playing from Pixels to other Android devices `GPL-3.0`
* [Android-Screener](https://github.com/jiesou/Android-Screener) - A tool for easily adjusting screen resolution and frame rate `MIT`
* [Android-Show-Taps](https://github.com/k3x1n/Android-Show-Taps) - Show customized taps upon touches `GPL-3.0`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark/) - A small Android app to let you schedule dark mode On/Off `MIT` [(Source code)](https://github.com/0ranko0P/AutoDark)
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - A simple tool to toggle DND automatically when using specified apps `AGPL-3.0` [(Source code)](https://github.com/dic1911/android_AutoDND)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - Bring back Wi-Fi and mobile data tiles on Android 12 or higher + a better-unified internet tile `GPL-3.0` [(Source code)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
  * [Better Internet Tiles Libre](https://github.com/D3SOX/Better-Network-Tiles-Libre) - Libre fork of Better Internet Tiles without proprietary libraries `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name is a very simple app to change the carrier names on unrooted Android devices `GPL-3.0`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) - An application to modify Material You colors of your device `GPL-3.0`
* [DarQ](https://github.com/KieronQuinn/DarQ) - DarQ provides a per-app selectable force dark option for Android 10 and above `Apache-2.0`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - Allows users to select individual app languages (Android 13+) `Apache-2.0`
* [LinkSheet](https://github.com/1fexd/LinkSheet) - Restore the Android <12 Url-App-Link-Chooser with Material3  `Modified MPL-2.0`
* [NoPopping](https://play.google.com/store/apps/details?id=rikka.nopeeking) `IAP` 💰 - Auto Do-Not-Disturb mode `Proprietary`
* [Repainter](https://play.google.com/store/apps/details?id=dev.kdrag0n.dyntheme) `IAP` 💰 - Install custom Material You designs on your device `Proprietary`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) - Contains some easy-to-use tools to go beyond the level of control allowed by Android System `No license`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Plugins for Smartspacer `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - View and modify hidden settings on Android devices `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) - Port of the double tap on the back of the device feature from Android 12 to any Android 7.0+ device `GPL-3.0`
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - Use a start menu to access apps. Shizuku can unlock additional features `Apache-2.0` [(Source code)](https://github.com/farmerbb/Taskbar)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) - Manage your device with Device owner privileges `GPL-3.0`

### Development utilities

* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - Dump package names of apps that have registered an account for a user. `No license`
* [AndroidLowLevelDetector](https://play.google.com/store/apps/details?id=net.imknown.android.forefrontinfo) - Detect Treble, GSI, Mainline, APEX, system-as-root(SAR), A/B, etc. `Apache-2.0` [(Source code)](https://github.com/imknown/AndroidLowLevelDetector)
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) IDE for JVM development. Uses Shizuku for an embedded shell - `GPL-3.0`
* [CurrentActivity](https://github.com/Omico/CurrentActivity) - A current activity monitor `GPL-3.0`
* [get_event](https://github.com/lalakii/get_event) - Read /dev/input/event*  `No license`
* [LibChecker](https://github.com/LibChecker/LibChecker) - An app to view libraries used in apps on your device. Uses Shizuku to determine the install source of other apps. `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) - Yet another logcat reader for Android  `GPL-3.0`
* [Logra](https://github.com/wingio/Logra) - Material You logcat viewer for Android `GPL-2.0` 
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher&hl=en&gl=US) `Paid` 💰 - Launch/interact with (un)exported activities, services, and receivers. Supports Shizuku alongside root. `Proprietary` [(Source code)](https://github.com/zacharee/RootActivityLauncher)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - Enable/Disable device sensors via quick settings `Apache-2.0`
* [TakoStats](https://play.google.com/store/apps/details?id=rikka.fpsmonitor) `IAP` 💰 - FPS and performance overlay with detailed real-time system information `Proprietary`
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) Widgets & quick settings tile to toggle wireless debugging (with KDE Connect integration) - `GPL-3.0`

### Education

* [Quiz-Platform](https://github.com/Yugyd/quiz-platform) - Quiz Platform is a Open Source knowledge testing platform for Android based on Jetpack Compose and Google solutions. `Apache-2.0` [(Source code)](https://github.com/Yugyd/quiz-platform)

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Tachiyomi fork with anime support and plugin management using Shizuku. `Apache-2.0`
* [BilibiliCacheVideoMerge](https://github.com/molihuan/BilibiliCacheVideoMerge) - Export BiliBili video cache files to MP4 `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - Manga reader with plugin management using Shizuku. Independent successor of Tachiyomi. `Apache-2.0`
  * Mihon/Tachiyomi has several other active forks, including [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) and [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)
* [lac-tool](https://github.com/aliernfrog/lac-tool) - Manage maps, wallpapers, and screenshots for the game 'Los Angeles Crimes' `MIT`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - Mod manager for the game 'Last Origin' `No license`
* [Panda Gamepad Pro](https://play.google.com/store/apps/details?id=com.panda.gamepad) `Paid` `IAP` 💰 - Keymapper for games `Proprietary`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - Easily import and share Polyfield maps `MIT`
* [translatefgo](https://github.com/rayshift/translatefgo) - Fate/Grand Order game translation project `CC BY-NC-SA 4.0`

### File management
* [AirData UAV](https://play.google.com/store/apps/details?id=com.airdata.uav.app) - Drone flight analysis and fleet management platform with [access to /Android/Data](https://app.airdata.com/wiki/Help/Granting+Permissions+in+Android+13+and+14) `Proprietary`
* [FV File Manager](https://play.google.com/store/apps/details?id=com.folderv.file) - File manager to [access Android/data and Android/obb](https://folderv.com/2023/11/24/access-Android-data-and-Android-obb-on-Android-14/) `Proprietary`
* [MiXplorer](https://xdaforums.com/t/app-2-2-mixplorer-v6-x-released-fully-featured-file-manager.1523691/#post-23109280) - File manager that can batch install APKs and access Android/data and obb using Shizuku `Proprietary`
* [MT Manager](https://mt2.cn) - Split-screen file manager. Can install APKs and access Android/data and Android/obb using Shizuku `Proprietary`
* [X-Plore](https://play.google.com/store/apps/details?id=com.lonelycatgames.Xplore) - File manager that can access Android/data and obb using Shizuku `Proprietary`
* [ZArchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) `IAP` 💰 - Archive management program. Supports editing files using Root/Shizuku. `Proprietary`

### Installer & app stores

* [AuroraStore](https://f-droid.org/en/packages/com.aurora.store/) - An open-source alternative to Google Play Store with privacy and modern design `GPL-3.0` [(Source code)](https://gitlab.com/AuroraOSS/AuroraStore)
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Material F-Droid client `GPL-3.0` [(Source code)](https://github.com/Droid-ify/client)
* [fdroid_shizuku_privileged_extension](https://depau.github.io/fdroid_shizuku_privileged_extension/fdroid/repo/) - F-Droid Privilege Extension that works with Shizuku `Apache-2.0` [(Source code)](https://github.com/depau/fdroid_shizuku_privileged_extension)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater: Updater for privacy-friendly browser `GPL-3.0` [(Source code)](https://github.com/Tobi823/ffupdater)
* [glassdown](https://github.com/Sinneida/glassdown) - Client for APKMirror `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) -  Simple-ish app using Shizuku to install APKs on-device with advanced options `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - An unofficial client for IzzyOnDroid F-Droid Repository `GPL-3.0`
* [Obtainium](https://github.com/ImranR98/Obtainium) - Get Android App Updates Directly From the Source `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - Package installer that allows overwriting the package requester and executor `MIT`
* [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) - Android split APKs installer `GPL-3.0` [(Source code)](https://github.com/Aefyr/SAI)
* [skydroid](https://github.com/redsolver/skydroid) - A decentralized domain-based App Store for Android `GPL-3.0`

### Miscellaneous

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok: Hide your private Files and Android APPs with just one click. `Apache-2.0` [(Source code)](https://github.com/deltazefiro/Amarok-Hider)
* [Anywhere](https://github.com/zhaobozhen/Anywhere-/) - An activity and shell shortcut folder `Apache-2.0`
* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - A local ADB shell for Shizuku powered android devices `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Material You Redesign of aShell app. `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - A simple app that shows battery status information on Android 14 and later. `GPL-3.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - A simple app made to help users easily install GSIs via DSU's Android feature. `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - Fixes MediaStore & File IO compatibility issues between HostProfile App and WorkProfile/DualApp/MultiApp. `No license`
* [EDS Full - Encrypted Data Store Full](https://sovworks.com/eds/index.php) `Paid` 💰 - Virtual disk encryption software for Android, which allows you to store your files in an encrypted container. Wide, rich range of features for root and non-root, too many to list here (see site). Shizuku control via Android intents (see FAQ). `Proprietary`
  * [EDS Lite - Encrypted Data Store Lite](https://sovworks.com/eds/index.php) - Free version of EDS Full. Limited features but still robust. Non-root and root funcionality. Non-mounted mode only (see site for description). `GPL-2.0` [(Source code)](https://github.com/sovworks/edslite)
* [Extinguish](https://play.google.com/store/apps/details?id=own.moderpach.extinguish) - Extinguish turn your screen off but keep your device wake `Proprietary`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - An Android app that changes what the buttons do on your devices! `GPL-3.0` [(Source code)](https://github.com/keymapperorg/KeyMapper)
* [LSPatch](https://github.com/LSPosed/LSPatch) - A non-root Xposed framework extending from LSPosed `GPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - A simple application to run Naiveproxy on Android `MIT`
* [RealMouse](https://play.google.com/store/apps/details?id=com.redlee90.realmouse) - Control the mouse using a virtual touchpad. Designed for secondary displays. `Proprietary`
* [rebootmenu](https://github.com/ryuunoakaihitomi/rebootmenu) - Lock the screen or open the power menu using shortcuts. Useful if your power button is broken. `MIT`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - Turn off your Android's screen without entering standby/sleep mode `Proprietary`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) - SD Maid 2/SE is Android's most thorough cleaning tool `GPL-3.0` [(Source code)](https://github.com/d4rken-org/sdmaid-se)
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - Better screen mirroring for Android devices `Apache-2.0` [(Source code)](https://github.com/farmerbb/SecondScreen)
* [Show taps](https://play.google.com/store/apps/details?id=show.taps) `Ads` - Displays the location of touch events on the screen `Proprietary`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - A simple app for controlling your Android devices from your WearOS watch `Apache-2.0` [(Source code)](https://github.com/SimpleAppProjects/SimpleWear)
* [SwiftBackup](https://play.google.com/store/apps/details?id=org.swiftapps.swiftbackup) `IAP` 💰 - Swift Backup can backup your important data in minutes `Proprietary`
* [XtMapper](https://github.com/Xtr126/XtMapper) - Keymapper for Android x86  `GPL-3.0`

### Network

* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - Can read cell tower info on Android `MIT` [(Source code)](https://github.com/zacharee/CellReader)
* [FindMyDevice](https://gitlab.com/Nulide/findmydevice) - Secure & open-source alternative to Google's FindMyDevice service. `GPL-3.0`
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - Quick settings tile to switch active private DNS server  `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - View your saved WiFi passwords on Android 11 and later without root `Proprietary` [(Source code)](https://github.com/zacharee/WiFiList)
* [WiFiList (FOSS)](https://github.com/jaredcat/WiFiList) - FOSS fork of 'WiFiList'  `Missing license`

### Software management

* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 -  Manage application permissions without root `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - Enable/disable Android components such as activities, services, receivers, and providers `Apache-2.0`
* [Canta](https://github.com/samolego/Canta) - Uninstall any app without root `LGPL-3.0`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - Android app that disables unused apps while still allowing convenient access to them `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - Improve your device's speed and battery life by freezing crappy software manually or semi-automatically `Apache-2.0` [(Source code)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) Freeze, hide or disable any app. Create and organize app groups that can be frozen with one click.  - `GPL-3.0` [(Source code)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - Freeze or hide apps using Shizuku `Proprietary`
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `Paid` 💰 - Android app manager for both rooted and non-rooted devices `GPL-3.0` [(Source code)](https://github.com/Hamza417/Inure)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Complete FLOSS fork of Island `Apache-2.0` [(Source code)](https://gitlab.com/secure-system/Insular)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - Isolate and clone apps for privacy protection and parallel running `Apache-2.0` [(Source code)](https://github.com/oasisfeng/island)
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - A highly powerful app to manage both system and user apps `GPL-3.0` [(Source code)](https://github.com/SmartPack/PackageManager)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - Check updates for Android apps, Magisk modules and more! `GPL-3.0` [(Source code)](https://github.com/DUpdateSystem/UpgradeAll)

### Vendor-specific

#### Google Pixel
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - Enable VoLTE on Pixel 6 & 7 with LG U+ `GPL-3.0`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - Customizable widget, can upgrade the built-in 'At a glance' widget on Pixel devices using Shizuku `GPL-3.0`

#### Samsung OneUI

* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - Custom system-wide theming engine for Samsung OneUI devices `Proprietary` 
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - Privilege escalation exploit [(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/CVE-2019-16253) to system user access (UID 1000) on non-rooted devices running up to OneUI 5. Uses Shizuku for automation `LGPL-2.1`

#### MIUI

* [AppLock](https://github.com/Mufanc/AppLock) - Prevent apps from being killed by side slide or one-click cleanup on MIUI 12+  `GPL-3.0` 
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - 5G shortcut switch for MIUI `GPL-3.0` - [(Source code)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - Turn off MIUI ads with minimal cost `Apache-2.0`
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - Display most apps in the form of freeform on MIUI `GPL-3.0`
  * [Flyme-FreeForm](https://github.com/Live-Block/Flyme-FreeForm) - Fork of Mi-FreeForm `GPL-3.0`


### Unlisted apps
To keep the main list clean, all apps that do not meet certain requirements are stored on a separate page: [UNLISTED.md](pages/UNLISTED.md)

I'm also using an automated crawler that searches for new projects, making use of Shizuku across GitHub and several F-Droid repos. You can view the current auto-generated crawl report here: [TODO.md](pages/TODO.md).


--------------------

## Development libraries

### Core

* [Shizuku](https://github.com/RikkaApps/Shizuku) - Shizuku system server, API, and app `Apache-2.0` 
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Developer documentation for Shizuku and Sui, including examples `Apache-2.0` 

### Filesystem
* [LintFile](https://github.com/lumkit/LintFile) - A file operation library with Shizuku, root, and regular filesystem backends `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Shizuku compatible android/data access from Xamarin - AIDL library `MIT`
* [shizuku_apk_installer](https://github.com/re7gog/shizuku_apk_installer) - Flutter plugin for installing Android APKs using Shizuku API `MIT`

### Power

* [PowerAct](https://github.com/ryuunoakaihitomi/PowerAct) - An Android library that can manipulate power-related actions with just a few lines of code `Apache-2.0`

--------------------

## Similar projects

* [Dhizuku](https://github.com/iamr0s/Dhizuku) - Shizuku-inspired app that allows sharing DeviceOwner permissions to third-party apps `GPL-3.0`

--------------------

## Rish shell

`rish` is an Android executable (not an app) for interacting with a shell that runs on a high-elevated daemon process. 
For example, if Shizuku was launched using ADB privileges, then `rish` will also provide a shell that maintains ADB privileges.

To set up `rish`, open Shizuku, navigate to 'Use Shizuku in terminal apps', and follow the setup instructions. Please note that you need a basic understanding of shells, terminals, and essential commands to use this efficiently.

After `rish` is set up, you can use it together with any apps that support calling any shell script or executable, even if the app doesn't support Shizuku itself.

> [!NOTE] 
> Because `rish`'s location is not in `$PATH`, you may need to specify the path to the executable to launch it manually. If it is located in your current working directory, use `./rish` to launch it.

**Syntax:**

* `rish`: Launch the default interactive shell (uses /system/bin/sh)
* `rish exec /path/to/custom/shell`: Launch custom/alternative interactive shell
* `rish -c 'whoami'`: Execute shell command and exit once completed
* `echo 'whoami' | rish`: Read shell command from stdin, execute it, and exit once completed

> [!NOTE]
> `whoami` is used as an example and would return the name of the current shell user.

**Usage examples:**

* Open an interactive ADB shell using a terminal emulator like **Termux** directly on your device
* Trigger high-privilege ADB shell commands using automation apps like **Tasker** automatically in the background
  * Example: Command `rish -c 'reboot'` would reboot the device using Shizuku via the shell

The official rish documentation is available here: https://github.com/RikkaApps/Shizuku-API/blob/master/rish/README.md

--------------------

## Annotations

- `Paid` 💰 - Paid application
- `IAP` 💰 - Contains in-app-purchases
- `Ads` - Contains ads
- `Proprietary` - Missing license or closed-source software
- `n-day trial` - Payment required after `n` days

--------------------

## License

This list is under the [Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) License.

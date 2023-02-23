# awesome-shizuku

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Shizuku allows normal apps to use system APIs directly with elevated privileges using ADB on non-rooted devices. This list compiles a few apps that are known to make use with Shizuku's capabilities.

More details: https://shizuku.rikka.app/

Pull requests are welcome. See [Contributing](CONTRIBUTING.md) for hints.

--------------------


## Table of contents

- [Apps](#apps)
  - [Audio](#audio)
  - [Customization](#customization)
  - [Development utilities](#development-utilities)
  - [Entertainment](#entertainment)
  - [Installer & app stores](#installer--app-stores)
  - [Miscellaneous](#miscellaneous)
  - [Software management](#software-management)
  - [Vendor-specific](#vendor-specific)
    - [Google Pixel](#google-pixel)
    - [Samsung OneUI](#samsung-oneui)
    - [MIUI](#miui)
- [Development libraries](#development-libraries)
  - [Core](#core)
  - [Power](#power)

- [Annotations](#annotations)
- [License](#license)

--------------------

## Apps


### Audio

* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - An implementation of the system-wide JamesDSP audio processing engine for non-rooted Android devices `GPL-3.0` [(Source code)](https://github.com/ThePBone/RootlessJamesDSP)

### Customization

* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - Port of Now Playing from Pixels to other Android devices `Proprietary`
* [AutoDark](https://f-droid.org/packages/me.ranko.autodark) - A small Android app to let you schedule dark mode On/Off `MIT` [(Source code)](https://github.com/0ranko0P/AutoDark)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - Bring back Wi-Fi and mobile data tiles on Android 12 or higher + a better unified internet tile `GPL-3.0` [(Source code)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - Carrier Vanity Name is a very simple app to change the carrier names on unrooted Android devices `No license`
* [DarQ](https://github.com/KieronQuinn/DarQ) - DarQ provides a per-app selectable force dark option for Android 10 and above `Apache-2.0`
* [Repainter](https://play.google.com/store/apps/details?id=dev.kdrag0n.dyntheme) `IAP` 💰 -  Install custom Material You designs on your device `Proprietary`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - View and modify hidden settings on Android devices `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) - Port of the double tap on back of device feature from Android 12 to any Android 7.0+ device `GPL-3.0`

### Development utilities

* [Logra](https://github.com/wingio/Logra) - Material You logcat viewer for Android `GPL-2.0` 
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher&hl=en&gl=US) `Paid` 💰 -  Launch/interact with (un)exported activities, services, and receivers. Supports Shizuku alongside root. `Proprietary` [(Source code)](https://github.com/zacharee/RootActivityLauncher)

### Entertainment

* [Aniyomi](https://github.com/jmir1/aniyomi) - Tachiyami fork with anime support and plugin management using Shizuku. `Apache-2.0`
* [Tachiyomi](https://github.com/tachiyomiorg/tachiyomi) - Manga reader with plugin management using Shizuku. `Apache-2.0`

### Installer & app stores

* [Droid-ify](https://f-droid.org/packages/com.looker.droidify) - Material F-Droid client `GPL-3.0` [(Source code)](https://github.com/Iamlooker/Droid-ify)
* [fdroid_shizuku_privileged_extension](https://depau.github.io/fdroid_shizuku_privileged_extension/fdroid/repo/) - F-Droid Privilege Extension that works with Shizuku `Apache-2.0` [(Source code)](https://github.com/depau/fdroid_shizuku_privileged_extension)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater: Updater for privacy friendly browser `GPL-3.0` [(Source code)](https://github.com/Tobi823/ffupdater)
* [SAI](https://play.google.com/store/apps/details?id=com.aefyr.sai) - Android split APKs installer `GPL-3.0` [(Source code)](https://github.com/Aefyr/SAI)
* [skydroid](https://github.com/redsolver/skydroid) - A decentralized domain-based App Store for Android `GPL-3.0`

### Miscellaneous

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Amarok: Hide your private Files and Android APPs with just one click. `Apache-2.0` [(Source code)](https://github.com/deltazefiro/Amarok-Hider)
* [Anywhere](https://github.com/zhaobozhen/Anywhere-/) - An activity and shell shortcut folder `Apache-2.0`
* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - A local ADB shell for Shizuku powered android devices `GPL-3.0`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - A simple app made to help users easily install GSIs via DSU's Android feature. `Apache-2.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1) - An Android app that change what the buttons do on your devices! `GPL-3.0` [(Source code)](https://github.com/keymapperorg/KeyMapper)
* [LSPatch](https://github.com/LSPosed/LSPatch) - A non-root Xposed framework extending from LSPosed `GPL-3.0`
* [rebootmenu](https://github.com/ryuunoakaihitomi/rebootmenu) - Lock the screen or open the power menu using shortcuts. Useful if your power button is broken. `MIT`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - Turn off your Android's screen without entering standby/sleep mode `Proprietary`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - Better screen mirroring for Android devices `Apache-2.0` [(Source code)](https://github.com/farmerbb/SecondScreen)
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist&hl=gsw&gl=US) `Paid` 💰 - View your saved WiFi passwords on Android 11 and later without root `Proprietary` [(Source code)](https://github.com/zacharee/WiFiList)

### Software management

* [App Ops](https://play.google.com/store/apps/details?id=rikka.appops) `Ads` `IAP` 💰 -  Manage application permissions without root `Proprietary`
* [Blocker](https://github.com/lihenggui/blocker) - Enable/disable Android components such as activities, services, receivers, and providers `Apache-2.0`
* [FreezeYou](https://play.google.com/store/apps/details?id=cf.playhi.freezeyou) - Improve your device's speed and battery life by freezing crappy software manually or semi-automatically `Apache-2.0` [(Source code)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) Freeze, hide, or disable any app. Create and organize app groups that can be freezed with one-click.  - `GPL-3.0` [(Source code)](https://github.com/aistra0528/Hail)
* [Ice Box](https://play.google.com/store/apps/details?id=com.catchingnow.icebox) `IAP` 💰 - Freeze or hide apps using Shizuku `Proprietary`
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - Isolate and clone apps for privacy protection and parallel running `Apache-2.0` [(Source code)](https://github.com/oasisfeng/island)
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - A highly powerful app to manage both system and user apps `GPL-3.0` [(Source code)](https://github.com/SmartPack/PackageManager)

### Vendor-specific

#### Google Pixel
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - Enable VoLTE on Pixel 6 & 7 with LG U+ `GPL-3.0`

#### Samsung OneUI

* [Hex Installer: OneUI themes](https://play.google.com/store/apps/details?id=project.vivid.hex.bodhi) `IAP` 💰 - Custom system-wide theming engine for Samsung OneUI devices `Proprietary` 

#### MIUI

* [AppLock](https://github.com/Mufanc/AppLock) - Prevent apps from being killed by side slide or one-click cleanup on MIUI 12+  `GPL-3.0` 
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) - 5G shortcut switch for MIUI `GPL-3.0` - [(Source code)](https://github.com/ysy950803/FiveGSwitcher)
* [Mi-FreeForm](https://github.com/sunshine0523/Mi-FreeForm) - Display most apps in the form of freeform on MIUI `GPL-3.0` 

_________

## Development libraries

### Core

* [Shizuku](https://github.com/RikkaApps/Shizuku) - Shizuku system server, API, and app `Apache-2.0` 
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Developer documentation for Shizuku and Sui including examples `Apache-2.0` 

### Power

* [PowerAct](https://github.com/ryuunoakaihitomi/PowerAct) - An Android library that can manipulate power-related actions with just few lines of code `Apache-2.0`

--------------------

## Annotations

- `Paid` 💰 - Paid application
- `IAP` 💰 - Contains in-app-purchases
- `Ads` - Contains ads
- `Proprietary` - Missing license or closed-source software

--------------------

## License

This list is under the [Creative Commons Attribution-ShareAlike 3.0 Unported](LICENSE) License.

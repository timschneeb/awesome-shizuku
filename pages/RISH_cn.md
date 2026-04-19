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

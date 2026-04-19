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

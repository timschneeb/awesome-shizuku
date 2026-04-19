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
> `whoami` is used as an example command and would return the name of the current shell user.

**Usage examples:**

* Open an interactive ADB shell using a terminal emulator like **Termux** directly on your device
* Trigger high-privilege ADB shell commands using automation apps like **Tasker** automatically in the background
  * Example: Command `rish -c 'reboot'` would reboot the device using Shizuku via the shell

The official rish documentation is available here: https://github.com/RikkaApps/Shizuku-API/blob/master/rish/README.md

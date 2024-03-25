# chromedriver-manager
chromedriver-manager 是一个自动下载和安装 ChromeDriver 的 Python 脚本，脚本会使用 `webdriver_manager` 从 ChromeDriver 的官方网站下载最新版本的 ChromeDriver，并将其移动到你指定的系统 PATH 中的某个目录下，从而完成 ChromeDriver 的安装和更新工作。

## 运行条件
- 安装了 Python 3.0 或更高版本。
- 安装了必要的第三方库：selenium、webdriver_manager。（可以通过 `pip3 install selenium webdriver_manager` 安装）
- 安装了 Chrome 浏览器。

## 使用方法
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改 `start.command (Mac)` 或 `start.bat (Win)` 中的路径，以指向你保存的 `chromedriver-manager.py` 脚本。
3. 打开 `chromedriver-manager.py` 脚本，按需要修改 `destination_path` 参数，设置 ChromeDriver 的安装路径（请确保选择的安装目录存在并且已经被添加到了 PATH 环境变量中，同时你也需要有足够的权限来写入目标目录，Windows 用户在设置路径时请参考此格式：`C:\\WebDrivers\\chromedriver.exe`）。
4. 双击运行 `start.command` 或 `start.bat` 脚本以执行 `chromedriver-manager.py` 脚本。
5. 脚本将开始下载最新版本的 ChromeDriver，然后将其移动到指定的路径完成安装，并在控制台显示版本更新信息。
<br>

# chromedriver-manager
chromedriver-manager is a Python script that automatically downloads and installs ChromeDriver. The script utilizes `webdriver_manager` to download the latest version of ChromeDriver from the official website and moves it to a directory specified in your system's PATH, thus completing the installation and updating of ChromeDriver.

## Requirements
- Installed Python 3.0 or higher.
- Installed required third-party libraries: selenium, webdriver_manager. (Install with `pip3 install selenium webdriver_manager`)
- Installed Chrome browser.

## Usage
1. Clone or download the repository to a directory on your computer.
2. Modify the path in `start.command (Mac)` or `start.bat (Win)` to point to the `chromedriver-manager.py` script you saved.
3. Open the `chromedriver-manager.py` script and modify the `destination_path` parameter as needed to set the installation path for ChromeDriver. (Ensure that the selected installation directory exists, has been added to the PATH environment variable, and that you have sufficient permissions to write to the target directory. For Windows users, use this format when setting the path: `C:\\WebDrivers\\chromedriver.exe`).
4. Double-click `start.command` or `start.bat` to execute the `chromedriver-manager.py` script.
5. The script will start downloading the latest version of ChromeDriver, then move it to the specified path to complete the installation, and display the version update information in the console.

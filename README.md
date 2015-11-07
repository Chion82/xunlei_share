#Xunlei Share

Based on the idea of sharing, XunleiShare is a command-line interface tool to directly get download links on Xunlei Lixian servers with the help of the maintainer's Xunlei VIP account. You do not have to acquire a VIP.

Backend server : https://github.com/Chion82/ThunderHack.git

XunleiShare是一个CLI下的迅雷离线下载地址获取工具，可将原下载链接直接转换为迅雷离线地址并输出为Aria2下载命令。 本工具基于分享原则，由维护者提供大容量VIP离线空间，因此你甚至不需要登录。

##Installation

```
$ sudo pip install xunleishare
```

##Usage

```
$ xunleishare "DOWNLOAD_LINK"
```
Then execute the generated ```xunlei_output``` shell.

or

``
$ xunleishare "DOWNLOAD_LINK" -o "OUTPUT_SHELL_FILE"
``

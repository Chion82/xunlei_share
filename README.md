#Xunlei Share

[![PyPI version](https://badge.fury.io/py/xunleishare.svg)](https://badge.fury.io/py/xunleishare)
[![Code Health](https://landscape.io/github/Chion82/xunlei_share/master/landscape.svg?style=flat)](https://landscape.io/github/Chion82/xunlei_share/master)
![python](https://img.shields.io/badge/python-2.7-green.svg)
![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)

XunleiShare is a command-line interface tool to directly get download links on Xunlei Lixian servers with the help from the maintainer's Xunlei VIP account. You don't have to acquire a Xunlei VIP account.

Backend server : https://github.com/Chion82/ThunderHack.git

XunleiShare是一个CLI下的迅雷离线下载地址获取工具，可将原下载链接直接转换为迅雷离线地址并输出为Aria2下载命令。 本工具基于分享原则，由维护者提供大容量会员离线空间，因此你无需购买迅雷会员。

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

```
$ xunleishare "DOWNLOAD_LINK" -o "OUTPUT_SHELL_FILE"
```

Add switch ```-a``` if you want to download all files simultaneously.

# pychrome
## 声明：pychrome非本人所作，我只是在pychrome上做了一些画蛇添足的工作，满足我的想法而已。原著：https://github.com/fate0/pychrome
我在此项目上添加了更容易调用的接口(事件回调时获得tab对象)。应用场景举例：网页加载完成时，返回响应报文和DOM树后自动关闭。添加接口也许画蛇添足，如果你有更好的方法，请赐教！  
我的初衷想法：1.弥补python的Requset库无法处理动态网页的问题；2.[crawlergo](https://github.com/0Kee-Team/crawlergo)返回的网页信息太少了，pychrome可以返回CDP定义的所有内容。基于此两点需求，在我准备实现CDP协议时，看见pychrome这个项目，感谢原作者[fate0](https://github.com/fate0)。  
pychrome是对CDP协议的封装，使用时有不懂的地方，或想加什么功能，我愿意帮助你！cdpcrawler.py是我写的一个可以在完成任务后自动关闭的例子  
我的研究方向是浏览器内核安全，对chromium源码比较熟悉，编译技术我也算熟悉。喜欢chromium源码的同学，欢迎一起交流学习。
## 在此特别感谢[TimWhite](https://github.com/timwhitez)、[明天](https://ruo.me)、[精灵](https://github.com/shmilylty)、[李同学](https://strcpy.me)四位前辈的悉心指导。


原著的ReadMe内容如下：

[![Build Status](https://travis-ci.org/fate0/pychrome.svg?branch=master)](https://travis-ci.org/fate0/pychrome)
[![Codecov](https://img.shields.io/codecov/c/github/fate0/pychrome.svg)](https://codecov.io/gh/fate0/pychrome)
[![Updates](https://pyup.io/repos/github/fate0/pychrome/shield.svg)](https://pyup.io/repos/github/fate0/pychrome/)
[![PyPI](https://img.shields.io/pypi/v/pychrome.svg)](https://pypi.python.org/pypi/pychrome)
[![PyPI](https://img.shields.io/pypi/pyversions/pychrome.svg)](https://github.com/fate0/pychrome)

A Python Package for the Google Chrome Dev Protocol, [more document](https://fate0.github.io/pychrome/)

## Table of Contents

* [Installation](#installation)
* [Setup Chrome](#setup-chrome)
* [Getting Started](#getting-started)
* [Tab management](#tab-management)
* [Debug](#debug)
* [Examples](#examples)
* [Ref](#ref)


## Installation

To install pychrome, simply:

```
$ pip install -U pychrome
```

or from GitHub:

```
$ pip install -U git+https://github.com/fate0/pychrome.git
```

or from source:

```
$ python setup.py install
```

## Setup Chrome

simply:

```
$ google-chrome --remote-debugging-port=9222
```

or headless mode (chrome version >= 59):

```
$ google-chrome --headless --disable-gpu --remote-debugging-port=9222
```

or use docker:

```
$ docker pull fate0/headless-chrome
$ docker run -it --rm --cap-add=SYS_ADMIN -p9222:9222 fate0/headless-chrome
```

## Getting Started

``` python
import pychrome

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# create a tab
tab = browser.new_tab()

# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab 
tab.start()

# call method
tab.Network.enable()
# call method with timeout
tab.Page.navigate(url="https://github.com/fate0/pychrome", _timeout=5)

# wait for loading
tab.wait(5)

# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()

# close tab
browser.close_tab(tab)

```

or (alternate syntax)

``` python
import pychrome

browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()

def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))


tab.set_listener("Network.requestWillBeSent", request_will_be_sent)

tab.start()
tab.call_method("Network.enable")
tab.call_method("Page.navigate", url="https://github.com/fate0/pychrome", _timeout=5)

tab.wait(5)
tab.stop()

browser.close_tab(tab)
```

more methods or events could be found in
[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/tot/)


## Debug

set DEBUG env variable:

![pychrome_with_debug_env](https://raw.githubusercontent.com/fate0/pychrome/master/docs/images/pychrome_with_debug_env.png)


## Tab management

run `pychrome -h` for more info

example:

![pychrome_tab_management](https://raw.githubusercontent.com/fate0/pychrome/master/docs/images/pychrome_tab_management.png)


## Examples

please see the [examples](http://github.com/fate0/pychrome/blob/master/examples) directory for more examples


## Ref

* [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface/)
* [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/tot/)

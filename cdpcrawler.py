#G.Y.
import subprocess
import pychrome
import time

try:
    cmd = ["./chrome-linux/chrome", "--remote-debugging-port=9222"]
    ChromeProcess = subprocess.Popen(cmd)
except Exception as e:
    print(e)
# create a browser instance
time.sleep(2)#等待Popen打开
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# create a tab
tab = browser.new_tab()

# register callback if you want
def save_dom(**kwargs):
    document = kwargs.get('self').DOM.getDocument()
    print(document)#要执行的业务
    kwargs.get('self').stop()#这句执行时会有报错，但不影响程序正常结果，更不影响业务执行.如果你有好的处理方法，请告诉我，感谢！

tab.Page.loadEventFired = save_dom

# start the tab
tab.start()

# call method
tab.Network.enable()
tab.DOM.enable()
tab.Page.enable()
# call method with timeout
tab.Page.navigate(url="https://www.baidu.com", _timeout=5)

# wait for loading
tab.wait()
ChromeProcess.kill()
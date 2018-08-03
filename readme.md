## 自制的登陆汕头移动的portal认证脚本

采用phantomjs做为登陆的浏览器，模拟登陆到认证界面的页面，然后每10秒获取一起网址，如果不是登陆成功的网址，就重新执行一次登陆的过程，重新登陆系统。如果是登陆成功的网址，就什么都不执行，继续休眠10秒。然后再继续。

仅作为内部登陆汕头移动https://auth.st.gmcc.net/dana/home/infranet.cgi 之用，可以作为练习此类的参考，如果不是内部登陆汕头移动，不可直接使用

#### 配置文件
conf.ini配置文件只有两个参数
* username：portal账号
* password：portal账号的密码

**password字段:**采取了加密后的内容，需要采用encode_util做加密后再填入这个字段

**encode_util.py**文件是一个将密码进行加密的工具，加密后的password字段，不会轻易的被人明文查看到密码，因为conf.ini文件是随便就可以打开的。


#### 其他事项
预备制作一个直接使用request登陆的版本中，不要使用浏览器，缩小打包后的整体文件大小

关于api-ms-win-crt-runtimel1-1-0.dll缺失的解决方案
在打包成exe移植到其他的win系统中，在运行时，可能出现报错api-ms-win-crt-runtimel1-1-0.dll缺失，应该是处在与win7或win8.1及以下的window系统中，解决的办法可以自行上网查找

#### 最近更新
添加一个如果portal登陆到达上限，踢掉一个IP继续登陆
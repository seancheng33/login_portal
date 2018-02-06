import base64
from time import sleep
import configparser ,sys
from selenium import webdriver
from tkinter import *

#
# driver =webdriver.Chrome(executable_path='./2.34/chromedriver.exe')

userAgent= ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 100
cap["phantomjs.page.settings.userAgent"] = userAgent
cap["phantomjs.page.customHeaders.User-Agent"] = userAgent
#https的网址连接，需要service_args中的这三项内容,不然会连接失败
service_args = ['--ignore-ssl-errors=yes','--web-security=false','--ssl-protocol=any']

driver = webdriver.PhantomJS(executable_path="./lib/phantomjs.exe", desired_capabilities=cap,service_args=service_args)
driver.set_window_size(1366,768)
driver.set_page_load_timeout(30)

conf = configparser.ConfigParser()
with open('conf.ini','r') as conf_file:
    conf.read_file(conf_file)

def login_to():
    driver.get("https://auth.st.gmcc.net/dana-na/auth/welcome.cgi")
    username = conf.get('config','username')
    password = base64.b64decode(conf.get('config','password'))#密码是加密的，需要解密出来
    password = str(password,'utf-8')#解密出来的内容是byte，需要转换成str
    driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[4]/td[1]/table/tbody/tr[1]/td[3]/input').send_keys(username)
    driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[4]/td[1]/table/tbody/tr[2]/td[3]/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[4]/td[1]/table/tbody/tr[5]/td[3]/input').submit()
    print('登陆成功')

if __name__ == "__main__":
    try:
        login_to()
    except Exception as e:
        print('错误信息：',str(e))
        sys.exit(0)

    while True:
        try:
            #无限循环，没隔一段时间就判断是否是登陆成功的网站，如果不是，就重新执行登陆
            sleep(10)
            currenturl = driver.current_url
            if currenturl != 'https://auth.st.gmcc.net/dana/home/infranet.cgi':
                print('登陆状态失效，重新登陆...')
                login_to()
        except Exception as error:
            #报错后重新登陆
            print(str(error))
            print('登陆状态失效，重新登陆...')
            login_to()
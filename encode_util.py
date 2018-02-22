'''
密码加密生成器，用于生成加密的密码密文，配置conf.ini文件的password字段，需要用经过加密的密码。
'''
import base64

in_string = input("输入需要加密的字段,输入 q 退出:")

while in_string != 'q':
    out_string=base64.b64encode(in_string.encode('utf-8'))
    print(str(out_string,'utf-8'))
    in_string = input("输入需要加密的字段,输入 q 退出:")
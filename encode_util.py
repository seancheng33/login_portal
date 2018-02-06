import base64

in_string = input("输入需要加密的字段,输入 q 退出:")

while in_string != 'q':
    out_string=base64.b64encode(in_string.encode('utf-8'))
    print(str(out_string,'utf-8'))
    in_string = input("输入需要加密的字段,输入 q 退出:")
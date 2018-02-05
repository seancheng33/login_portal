from tkinter import *
from tkinter.messagebox import askyesno


def close_win():
    #确认框，在点击退出按键或点关闭窗口时调用
    ans = askyesno(title='确定退出？',message='退出本脚本，也将退出认证。\n确定退出？')
    if ans:
        root.destroy()
    else:
        return



root = Tk()
root.title("自动登录portal脚本")#标题
root.resizable(0,0)#禁止调整窗口大小
root.protocol('WM_DELETE_WINDOW',close_win)# 添加窗体关闭事件
photo = PhotoImage(file='img/link-broken-8x.png')
icon_label = Label(root,image=photo,justify=LEFT)
icon_label.pack(padx=10, pady=10,side=LEFT)
icon_label = Label(root,text='正在连接。。。',justify=LEFT)
icon_label.pack(padx=10, pady=10,side=LEFT)
login_bt = Button(root,text='刷新状态')
login_bt.pack(padx=10, pady=10,side=LEFT)
exit_bt = Button(root,text='退出脚本',command=close_win)
exit_bt.pack(padx=10, pady=10,side=LEFT)

root.update_idletasks()

root.mainloop()
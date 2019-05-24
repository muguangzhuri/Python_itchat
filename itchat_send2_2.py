import itchat
import datetime
import time
def itchat_users(x1):
    global userName
    users = itchat.search_friends(name = x1)
    userName = users[0]['UserName']
##    print(users,userName)
    return userName
    


def itchat_time():
    
    now = datetime.datetime.now()
    global now_strs
    now_strs = now.strftime('%Y/%m/%d %H:%M:%S')
    global now_str
    now_str = now_strs[11:]
##    print(now_str)
##    print(now_strs)
    return now_strs,now_str


##def itchat_send(m,userName):
##
##    itchat.send(m,toUserName = userName)
##    
##
##        
##def itchat_prin(x,y,now_strs):
##    print("给：{} 发送的：{} 消息于时间：{}发送成功".format(x,y,now_strs))

def itchat_if(n1, m1, t):
    
    if now_str in [t]:
        itchat.send(m1,toUserName = userName)
        print("给：{} 发送的：{} ,消息于时间：{},发送成功。".format(n1,m1,now_strs))    

def itchat_sends(n2, m2, t1,t2):
    
    itchat_users(n2)


    while 1:
        itchat_time()
        itchat_if(n2, m2, t1)
        itchat_if(n2, m2, t2)
        time.sleep(1)


######def itchat_input():
######    global n, m, times
######    times = []
######    n = input("请输入发送人的名字：")
######    m = input("请输入发送的内容：")
######    num = eval(input("请输入你要发送几个时间点："))
######    for i in range(num):
######        t = input("请输入发送的时间(00:00:00)：")
######        times.append(t)
######   
######    return n,m,times

    
if __name__ == '__main__':
    
    try:
        #itchat_input()
       
        itchat.auto_login(hotReload = True)
        itchat_sends('武璟珺','刘家庄小学__王国庆__安全','07:01:00','20:01:00')
        #itchat_sends(n, m,times)
        itchat.run()
    except Exception as e:
         print("{}时间出现过错误".format(now_strs))
##        for i in range(10):
##            while not itchat.load_login_status():
##                time.sleep(30)
##                itchat.auto_login(hotReload = True)
##        itchat_sends('武璟珺','刘家庄小学__王国庆__安全','07:01:00','20:01:00')
##        itchat.logout()
##        print(e)
##        now = datetime.datetime.now()
##        now_strs = now.strftime('%Y/%m/%d %H:%M:%S')
##        now_str = now_strs[11:]
       
               

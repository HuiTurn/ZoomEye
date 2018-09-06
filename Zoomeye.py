#coding:utf-8
#!/usr/bin/python3
import requests
import json
import time
import getopt
import sys

headers = {
    "Host": "www.zoomeye.org",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Cube-Authorization": "修改此处",
    "Cookie": "修改此处",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0"
}

def getJson(application,port,pageNumber):

    url='https://www.zoomeye.org/api/search?q=app:"{}" +port:"{}"&t=host&p={}'.format(application,port,pageNumber)
    global headers
    headers["Referer"] = "https://www.zoomeye.org/searchResult?q=app%3A%22{}%22%20%2Bport%3A%22{}%22&t=host".format(application,port)
    s = requests.session()
    r=s.get(url,headers=headers)
    return r.text

def wirteText(content):

    for i in json.loads(content)['matches']:
        f=open('ips.txt','a+')
        if type(i['ip'])==str:
            print(i['ip']+":"+str(i["portinfo"]["port"]))
            f.write(i['ip']+":"+str(i["portinfo"]["port"])+'\n')
        elif type(i['ip'])==list:
            print(i['site']+":80")
            f.write(i['site']+":80\n")
        else:
            pass

def readJson(application,port):

    try:
        for i in range(1, 101):  # 循环100次，页码自增1
            time.sleep(5)
            content = getJson(application, port, i)
            if json.loads(content)["status"] != 200:
                print(json.loads(content)["msg"])
                break
            elif json.loads(content)["status"] == 200:
                wirteText(content)
    except json.decoder.JSONDecodeError:
        print('Cookies has expired.')


def run(argv):

    application=''
    port=''
    try:
        if len(argv)==4:
            opts, args = getopt.getopt(argv, "ha:p:")
        else:
            print('Python Zoomeye.py -a <application> -p <port>')
    except getopt.GetoptError:
        print('Python Zoomeye.py -a <application> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Python Zoomeye.py -a <application> -p <port>')
            sys.exit()
        elif opt in ("-a"):
            application = arg
        elif opt in ("-p"):
            port = arg
    readJson(application,port)

if __name__ == '__main__':


    print("""
    
 _____
/__  /  ____  ____  ____ ___  ___  __  _____
  / /  / __ \/ __ \/ __ `__ \/ _ \/ / / / _ \\
 / /__/ /_/ / /_/ / / / / / /  __/ /_/ /  __/
/____/\____/\____/_/ /_/ /_/\___/\__, /\___/
                                /____/
     
    """)
    run(sys.argv[1:])


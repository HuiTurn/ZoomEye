#coding:utf-8
#!/usr/bin/python3
import requests
import json
import time

def getJson(Keyword,Bcountry,pageNumber):

    url='https://www.zoomeye.org/api/search?q={} +country:"{}"&t=all&p={}'.format(Keyword,Bcountry,pageNumber)
    headers={
        "Host": "www.zoomeye.org",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-GB,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.zoomeye.org/searchResult?q={}%20%2Bcountry:%22{}%22&t=all".format(Keyword,Bcountry),
        "Cube-Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjkwODc4MzY0N0BxcS5jb20iLCJ1dWlkIjoiY2I1MTg2NGI4ZTJhOThkMDdkNWI4NzM3YWQwNTc0YTAiLCJpYXQiOjE1MzU0NTI3NzIsImV4cCI6MTUzNTUzOTE3Mn0.h7aHKFYj21fsLCHZoUxnog4PcQahSFWedwqi19lN1bU",
        "Cookie": "__jsluid=eb52d6a6aa569c576703f7b2e405e035; Hm_lvt_3c8266fabffc08ed4774a252adcb9263=1535361030,1535361060,1535452769; __jsl_clearance=1535452765.973|0|hrEYpghty%2FoY3bD6di1a7NEWsok%3D; Hm_lpvt_3c8266fabffc08ed4774a252adcb9263=1535452772",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"
    }
    s = requests.Session()


    try:
        req=s.get(url, headers=headers)
        if req.cookies.get_dict():
            s.cookies.update(req.cookies)
    except Exception, e:
        print e
    #r=requests.get(url,headers=headers)
    #print(r.text)
    return req.text

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

def readJson():
    f=open('geo.json', 'r')
    jsons=json.load(f)
    for x in jsons:#循环列出国家
        print("===================={}=======================".format(x))
        for i in range(1, 101):  # 循环100次，页码自增1
            time.sleep(5)
            content =getJson('weblogic', x, i)
            wirteText(content)

def run():
    readJson()

if __name__ == '__main__':
    run()
    print('Crawl completion')

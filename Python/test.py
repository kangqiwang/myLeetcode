<<<<<<< HEAD
#!/usr/bin/python  
# -*- coding: utf-8 -*-
#coding=utf-8

import time
import random
import urllib.request
import urllib.parse
import copy
import json
from io import StringIO

# 
iheaders = {"Accept":" text/plain, */*; q=0.01",
            "Accept-Encoding":" gzip, deflate, br",
            "Accept-Language":" en-GB,en-US;q=0.9,en;q=0.8",
            "Content-Type":" application/json",
            "Host":"127.0.0.1:5601",
            "kbn-version":" 6.3.2",
            "Origin":"http://127.0.0.1:5601",
            "Referer":"http://127.0.0.1:5601/app/kibana",
            "Sec-Fetch-Mode":" cors",
            "Sec-Fetch-Site":" same-origin",
            "User-Agent":" Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
            }

gzipFlag = True # False#
url = "http://127.0.0.1:9200/test5/sensordata/"
count = 1
timeSleep = 1
httpMethod = "POST"  # "GET" # "POST" #


def create_data():
    """
    global count
    t_dir = {}
    t_index_dir = {}
    t_index_dir["_id"] = count
    t_dir["index"] = t_index_dir
    index_str = json.dumps(t_dir)
    count = count + 1
    """

    locationList = []
    for i in range(20):
        locationList.append([str(random.uniform(50, 58)), str(random.uniform(2, 7))])
    # for j in range(100):
    i = random.randint(1, 10)
    datetime = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
    dataitem = {}
    dataitem["sensorid"] = i // 100
    dataitem["coordinate"] = {'lat': locationList[i // 50][0], 'lon': locationList[i // 50][1]}
    dataitem["datetime"] = datetime
    dataitem["temperature"] = random.uniform(1, 100)
    # return postData
    data_str = json.dumps(dataitem)
    # return "["+ index_str + "," + data_str + "]"
    # print('THIS IS MY DATA',data_str)
    return data_str

def send_data(url):

    print (url)
    data = ""
    if httpMethod == "GET":
        # t = urllib.request.urlopen(url, timeout=60)
        # print (t)
        # print (t.read())
        data = urllib.request.urlopen(url,timeout=60).read()
    if httpMethod == "POST":
        request = urllib.request.Request(url, data=create_data().encode("utf-8")
                                         , headers = {"Content-Type": "application/json"}, method = "POST")

        data = urllib.request.urlopen(request).read()
    if httpMethod == "PUT":
        request = urllib.request.Request(url, data=urllib.parse.urlencode(create_data()).encode("utf-8")
                                         , headers={"Content-Type":"application/json"},method="PUT")

        data = urllib.request.urlopen(request).read()
    # if httpMethod == "PUT":
    #     data = urllib.request.Request(url,data=urllib.urlencode(create_data()), headers={}, method="put")

    #print urllib.urlencode(create_data())

    # print (data)



if __name__=='__main__':
    while 1:
        
        send_data(url)
        # print ("sleep in "+str(timeSleep)+"s")
        time.sleep(timeSleep)
=======
nums=[1,5,3,4]
target=7
for i in range(len(nums)):
    a = target - nums.pop(0)
    if a in nums:
        print([i, nums.index(a)+i+1])

>>>>>>> 8fea8a3803b5213706d7ed1990850fd4ffc566f9

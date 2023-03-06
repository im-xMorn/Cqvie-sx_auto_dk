import requests
import json
import re
import datetime

"""
@author:icdox.
@time:
@py:本脚本实现每日实习自动打卡
"""
    
def everyday_dk(lng,lat,sign_date_time):
    url = 'https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord'
    headers = {
        'Authorization': 'Bearer XXXXXXXXXXXXXXXXXXXXXX',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'XXXXXXXXXXXXXXXXXXXXXX7'
    }
    cookies = {
        'Cookie': 'XXXXXXXXXXXXXXXXXXXXXX'
    }
    data = {
        "signDate":sign_date_time,
        "signAddress":'重庆市九龙坡区渝州路8号11-6-1号',
        # "latitude":"27.003384","longitude":"104.572374"
        "latitude":lat,"longitude":lng
    }
    data = json.dumps(data)
    response = requests.post(url=url,headers=headers,cookies=cookies,data=data).text
    return response
    
if __name__ =='__main__':
    now=datetime.datetime.now()
    sign_date_time = now.strftime("%Y-%m-%dT%H:%M:%S.999Z")
    # 获取坐标/经纬度 106.489876,29.536867
    lng = '106.489876'
    lat = '29.536867'
    Qd_info = everyday_dk(lng,lat,sign_date_time)
    print(Qd_info)

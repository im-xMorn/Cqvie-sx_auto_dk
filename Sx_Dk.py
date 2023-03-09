import requests
import json
import datetime
import os

"""
@author:icdox.
@time:2023-2-21
@py:本脚本实现实习指定位置打卡
"""

def Yj_Qd_Fp(lng,lat,sign_date_time,token):
    url = 'https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord'
    headers = {
        'Authorization': 'Bearer '+str(token.split('Admin-Token=')[1])[:-17],
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }
    cookies = {
        'Cookie': 'muyun_sign_javascript=291084d14dd7e8a7236f80d4c031a1a1; muyun_sign_cookie='+token
    }
    data = {
        "signDate":sign_date_time,
        "signAddress":'重庆市九龙坡区渝州路8号11-6-1号',
        # "latitude":"27.003384","longitude":"104.572374"
        "latitude":lat,"longitude":lng
    }
    data = json.dumps(data)
    response = requests.post(url=url,headers=headers,cookies=cookies,data=data).text
    print(response)


# 格式化 Cookie 值
def reset_token(token):
    return str(token.split('muyun_sign_cookie=')[1])


if __name__ =='__main__':
    token = input('请输入 Cookie 值:')
    os.system('cls')

    # 获取时间戳
    now=datetime.datetime.now()
    sign_date_time = now.strftime("%Y-%m-%dT%H:%M:%S.999Z")

    # 坐标/经纬度 106.489876,29.536867
    lng = '106.489876'
    lat = '29.536867'
    token = reset_token(token)

    # 签到
    Yj_Qd_Fp(lng,lat,sign_date_time,token)

    os.system("pause")

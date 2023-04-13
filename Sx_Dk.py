import requests
import json
import datetime
import os

"""
--------------------------------
@author:xMorn.
@time:2023-2-21
@py:本脚本实现实习指定位置签到，补签
--------------------------------
Cookie 值 仅为 
    muyun_sign_javascript;
    muyun_sign_cookie;
    Admin-Token  
三个字段的值
如:
muyun_sign_javascript=291084d14dd7e8a7236f80d4c031a1a1; muyun_sign_cookie=793f08ffcb895fef025336d3764204e3; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImJlMjMxMTRhLTMwMTgtNGQ1Ni1iODY4LWU5Njg0NTMwYTA5NCJ9.U-0bL_Q6kuAyWY2HYNnzzqfdWC_9JVgHyFRy2tT2L0zm07jNWARMRk6H7wP0dmEJDhdfljkKVn84UtEm21_-Aw
补签——修改日期时间即可
"""

def Yj_Qd_Fp(lng,lat,Qd_date_time,token):
    url = 'https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord'
    headers = {
        'Authorization': 'Bearer '+str(token.split('Admin-Token=')[1]),
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
    }
    cookies = {
        'Cookie': 'muyun_sign_javascript=291084d14dd7e8a7236f80d4c031a1a1; muyun_sign_cookie='+token
    }
    
    data = {
        "signDate":Qd_date_time,
        "signAddress":'重庆市九龙坡区渝州路8号11-6-1号',
        # "latitude":"27.003384","longitude":"104.572374"
        "latitude":lat,"longitude":lng
    }
    data = json.dumps(data)
    response = requests.post(url=url,headers=headers,cookies=cookies,data=data).text
    # 判断是否成功
    If_Qd = response.split('"code":')[1][0:3]
    if If_Qd == '500':
        print('已签到或 Cookie 值错误和 UA 标识过期!')
    elif If_Qd == '200':
        print('签到成功!')


# 格式化 Cookie 值
def reset_token(token):
    return str(token.split('muyun_sign_cookie=')[1])


if __name__ =='__main__':
    token = input('请输入 Cookie 值:')
    os.system('cls')

    # 获取时间戳
    now=datetime.datetime.now()
    # sign_date_time = now.strftime("%Y-%m-%dT%H:%M:%S.999Z")
    # 补签 修改下面括号内容日期即可
    Qd_date_time = now.strftime("2023-04-13T12:13:31.999Z")
    # 2023-03-27T21:54:42.999Z
     
    # 坐标/经纬度 106.489876,29.536867
    lng = '106.489876'
    lat = '29.536867'
    token = reset_token(token)

    # 签到
    # Yj_Qd_Fp(lng,lat,'2023-%m-%dT%H:%M:%S.999Z',token)
    Yj_Qd_Fp(lng,lat,Qd_date_time,token)
    
    os.system("pause")

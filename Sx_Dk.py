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
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJs2dpbl91c2VyX2tleSI6IjNkNzhiZTQ2LTQ2YjEtNGMyMC05NDcwLWFlYzU3NzIzYWI3MSJ9.IBSujNynZ2DrQAib-XQGyFmj2SPs0Ub8rod_fX1oGFJ1LjhV19FGmeC5t9pqWshwt0tVnIV1IBNBnLrTnhvlhg',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
    }
    cookies = {
        'Cookie': 'muyun_sign_javascript=291084d14dd7e8a7236f80d4c031a1a1; muyun_sign_cookie=c101f478d4e678d61c5c335b65dced16; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjNkNzhiZTQ2LTQ2YjEtNGMyMC05NDcwLWFlYzU3NzIzYWI3MSJ9.IBSujNynZ2DrQAib-XQGyFmj2SPs0Ub8rod_fX1oGFJ1LjhV19FGmeC5t9pqWshwt0tVnIV1IBNBnLrTnhvlhg; sidebarStatus=1'
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
    Qd_info = everyday_dk(lng[0],lat[0],sign_date_time)
    print(Qd_info)

import requests
import json
import re
"""
@author:icdox.
@time:
@py:本脚本实现每日实习自动打卡
"""
    
    
def everyday_dk():
    url = 'https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImM4ODAzYTIyLWI1ZjUtNGQyOS1hN2M4LWY4N2JmNDU2M2Q3MiJ9.32qK_-VxH2cYwmPjrMJoVOhIeUHxeT4c8OKQ7RuXt0McbErOCXdDC94kegEFmmV-J2vZXHMrn7O18Qghuyw1rg',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; TAS-AN00 Build/TAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 AXINFU2.0'
    }
    cookies = {
        'Cookie': 'wxSignUrl=https://dgsx.cqvie.edu.cn/mobile/index; sidebarStatus=0; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImM4ODAzYTIyLWI1ZjUtNGQyOS1hN2M4LWY4N2JmNDU2M2Q3MiJ9.32qK_-VxH2cYwmPjrMJoVOhIeUHxeT4c8OKQ7RuXt0McbErOCXdDC94kegEFmmV-J2vZXHMrn7O18Qghuyw1rg'
    }
    data = {
        "signDate":"2022-11-14T22:35:41.999Z",
        "signAddress":"暂未获取到位置信息，请参考经纬度！",
        # "latitude":"27.003384","longitude":"104.572374"
        "latitude":"27.003384","longitude":"104.572374"
    }
    data = json.dumps(data)
    response = requests.post(url=url,headers=headers,cookies=cookies,data=data).text
    print(response)

if __name__ =='__main__':
    xx_dz = '重庆工程职业技术学院'
    city = '重庆'
    url = 'https://api.map.baidu.com/geocoder?address={}&output=json&key=E4805d16520de693a3fe707cdc962045&city={}'.format(xx_dz,city)
    headers ={
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; TAS-AN00 Build/TAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 AXINFU2.0'
    }
    map_info = requests.get(url=url,headers=headers).text
    # 获取坐标/经纬度
    lng = re.findall('"lng":(.*?),',map_info)
    lat = re.findall('"lat":(.*?)\n',map_info)
    print(lng,lat)
    everyday_dk()
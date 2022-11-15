import requests
import json
import re
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
"""
@author:icdox.
@time:
@py:本脚本实现每日实习自动打卡
"""
    
def everyday_dk(token_value,lng,lat,sign_date_time,xxdz):
    url = 'https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': 'Bearer '+token_value,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; TAS-AN00 Build/TAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 AXINFU2.0'
    }
    cookies = {
        'Cookie': 'wxSignUrl=https://dgsx.cqvie.edu.cn/mobile/index; sidebarStatus=0; Admin-Token='+token_value
    }
    data = {
        # 登录时间
        "signDate":sign_date_time,
        # 登录地址
        "signAddress":xxdz,
        # 经纬度
        # "latitude":"27.003384","longitude":"104.572374"
        "latitude":lat,"longitude":lng
    }
    data = json.dumps(data)
    response = requests.post(url=url,headers=headers,cookies=cookies,data=data).text
    return response

def to_mail():
    my_sender = ''  # 发件人邮箱账号
    my_pass = '  # 发件人邮箱授权码，第一步得到的
    users = '' # 收件人邮箱账号
    ret = True
    try:
        mail_msg = f"""
                        <p>'今日已签到！'</p>
                   """
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(["发件人昵称", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([str(users), users])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "实习自动签到"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465，固定的，不能更改 使用SSL模式
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.set_debuglevel(1)
        server.sendmail(my_sender, [users, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件信息
        server.quit()  # 关闭连接
    except Exception as err:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False 
    return ret

if __name__ =='__main__':
    now=datetime.datetime.now()
    sign_date_time = now.strftime("%Y-%m-%dT%H:%M:%S.999Z")
    # Cookie 值
    tooken_value = ''
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
    dk_info = everyday_dk(tooken_value,lng[0],lat[0],sign_date_time,xx_dz)
    if  dk_info== '{"msg":"请求访问：/internship_pending/signrecord，认证失败，无法访问系统资源","code":401}':
        print('Cookie值已过期，请及时更新!')
    else:
        print(dk_info)
        to_mail()

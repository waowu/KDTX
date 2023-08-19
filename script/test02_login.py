# 需求：  登陆成功

# 导包
import requests


# 发送接口请求
url = 'http://kdtx-test.itheima.net/api/login'
header_data = {
    'Contenet-Type': 'application/json'
}
login_data ={
    'username' : 'admin',
    'password': 'HM_2023_test',
    'code' : 2,
    'uuid' : 'e412d43ebd49417aad73b20587497261'
}
respond = requests.post(url= url, headers= header_data, json= login_data)

# 查看响应结果
print(respond.json())   # 获取json响应数据

print(respond.status_code)  #获取状态码
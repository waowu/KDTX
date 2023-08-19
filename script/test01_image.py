# 获取 验证码 和图片

# 导包
import requests

# 发送接口请求
respond = requests.get(url='http://kdtx-test.itheima.net/api/captchaImage')

# 查看响应
print(respond.status_code)   #响应状态码
print(respond.text)        # 文本格式响应数据
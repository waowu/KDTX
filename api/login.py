# 登陆接口的封装与调用

# 1.导包
import requests
import config

# 2.创建接口类

class LoginAPI:

    # 初始化
    def __init__(self):
        # self.url_verify = 'http://kdtx-test.itheima.net/api/captchaImage'
        self.url_verify = config.BASE_URL + '/api/captchaImage'
        self.url_login = config.BASE_URL + '/api/login'
        # self.url_login = 'http://kdtx-test.itheima.net/api/login'

    # 获取验证码接口
    def get_verify_code(self):
        return requests.get(url=self.url_verify)

    # 获取登陆接口
    def login(self, test_data):
        return  requests.post(url=self.url_login, json= test_data)
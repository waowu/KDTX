# 合同上传接口封装

# 导包
import requests
import config
# 创建接口类
class ContractAPI:
    def __init__(self):
        # 初始化
        # self.url_upload = "http://kdtx-test.itheima.net/api/common/upload"
        # self.add_contrat = "http://kdtx-test.itheima.net/api/contract"
        self.url_upload = config.BASE_URL + "/api/common/upload"
        self.add_contrat = config.BASE_URL + "/api/contract"

    # 合同上传接口
    def upload_contrast(self, test_data , token):
        return requests.post(url= self.url_upload,files={"file": test_data},  headers= {"Authorization": token})



     # 合同新增
    def add_contract(self, test_data, token):
        return requests.post(url=self.add_contrat, json=test_data, headers={"Authorization": token})
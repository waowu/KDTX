# 导包
import requests
import config
# 创建接口类
class CourseAPI:
    # 初始化
    def __init__(self):
        # self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"
        # self.url_select_course = "http://kdtx-test.itheima.net/api/clues/course/list"
        self.url_add_course = config.BASE_URL + "/api/clues/course"
        self.url_select_course = config.BASE_URL + "/api/clues/course/list"

    #添加课程
    def add_course(self, test_data, token):
        return requests.post(url=self.url_add_course, json= test_data, headers={"Authorization": token})


    # 查询课程
    def select_course(self , test_data, token):
        return requests.get(url= self.url_select_course + f"/{test_data}", headers={"Authorization" : token})


    # 修改课程
    def upload_course(self,test_data , token):
        return requests.put(url=self.url_add_course, json=test_data, headers={"Authorization" :token})

    #删除课程
    def delete_course(self, test_data, token):
        return requests.delete(self.url_add_course + f"/{test_data}" , headers={"Authorization" : token})
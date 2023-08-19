# 导包
from api.login import  LoginAPI
from api.course import CourseAPI

# 创建删除课程类
class TestCourseAPI:
    token =None
    # 前置处理
    def setup(self):
        # 实例化
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

        # 登陆成功
        # 获取验证码
        respond = self.login_api.get_verify_code()
        test_data = {
        "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": respond.json().get("uuid")
        }
        # 获取登陆接口
        res = self.login_api.login(test_data=test_data)
        TestCourseAPI.token = res.json().get("token")
        # 课程ID存在
    # 后置处理
    def teardown(self):
        pass

    # 课程删除成功(课程ID存在)
    def test01_delete_course_success(self):
        respond = self.course_api.delete_course(test_data=110, token= TestCourseAPI.token)
        # 断言 响应状态码 200
        assert 200 == respond.status_code
        #断言 响应数据 msg 操作成功
        assert "操作成功" in respond.text
        # 断言 响应数据 code 200
        assert  200 == respond.json().get("code")


    # 课程删除失败(课程ID不存在)
    def  test02_delete_course_fail_id_not_exist(self):
        respond = self.course_api.delete_course(test_data=102345, token=TestCourseAPI.token)
        # 断言 响应状态码 200
        assert 200 == respond.status_code
        # 断言 响应数据 msg 操作失败
        assert "失败" in respond.text
        # 断言 响应数据 code 500
        assert 500 == respond.json().get("code")


    # 课程删除失败(用户未登录)
    def test_03_delete_course_fail_without_users(self):
        respond = self.course_api.delete_course(test_data=94, token="###")
        # 断言 响应状态码 200
        assert 200 == respond.status_code
        # 断言 响应数据 msg 操作失败
        assert "认证失败" in respond.text
        # 断言 响应数据 code 500
        assert 401 == respond.json().get("code")
# 导包
from api.course import CourseAPI
from  api.login import LoginAPI

# 创建测试类
class TestCourseAPI:
    # 初始化
    token = None

    # 前置处理
    def setup(self):
        # 登陆接口实例化
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

        # 获取验证码成功
        respond=self.login_api.get_verify_code()
        # 获取uuid
        print(respond.json().get("uuid"))

        # 获取登陆接口成功
        test_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": respond.json().get("uuid")
        }
        res = self.login_api.login(test_data=test_data)
        # 获取token
        TestCourseAPI.token = res.json().get("token")
        print(TestCourseAPI.token)

    # 后置处理
    def teardown(self):
        pass




# 添加课程成功
    def test01_add_course_success(self):
        test_data = {
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2"
        }
        respond = self.course_api.add_course(test_data= test_data, token = TestCourseAPI.token)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据  操作成功
        assert "成功" in respond.text
        # 断言 code
        assert 200 == respond.json().get("code")


#添加课程失败（未登录）
    def test02_add_course_fail(self):
        test_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2"
        }
        respond = self.course_api.add_course(test_data=test_data, token="###")

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据  操作成功
        assert "认证失败" in respond.text
        # 断言 code
        assert 401 == respond.json().get("code")

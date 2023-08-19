# 导包
from api.course import CourseAPI
from api.login import LoginAPI

# 创建 课程查询 接口
class TestCourseAPI:
    # 初始化
    token = None
    # 前置处理
    def setup(self):
        # 实例化
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

    # 获取验证码成功
        respond = self.login_api.get_verify_code()
    # 登陆成功
        test_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": respond.json().get("uuid")
        }
        res = self.login_api.login(test_data=test_data)
        TestCourseAPI.token  = res.json().get("token")
        print(TestCourseAPI.token)
    # 存在对应课程记录



    # 后置处理
    def teardown(self):
        pass

    # 查询成功（输入存在的课程名称）
    def test01_select_course_success(self):
        respond = self.course_api.select_course(test_data="?name = 测试开发提升课01", token=TestCourseAPI.token)
        # 查询存在的课程
        print(respond.json())

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据msg中 指定文字
        assert "成功" in respond.text
        # 断言 响应数据 code 为200
        assert 200 == respond.json().get("code")

    #查询失败（用户未登录）
    def test02_select_course_fail(self):
        respond = self.course_api.select_course(test_data="?subject = 6", token="###")

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据msg中 指定文字
        assert "失败" in respond.text
        # 断言 响应数据 code 为200
        assert 401 == respond.json().get("code")
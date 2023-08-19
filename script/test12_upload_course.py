# 导包
from api.course import CourseAPI
from api.login import LoginAPI

# 创建课程修改接口类
class TestCourseAP:
    token = None


    # 前置处理
    def setup(self):
        # 实例化
        self.course_api = CourseAPI()
        self.login_api = LoginAPI()

        # 登陆成功
        respond = self.login_api.get_verify_code()
        test_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": respond.json().get("uuid")
        }
        res = self.login_api.login(test_data=test_data)
        TestCourseAP.token = res.json().get("token")
        #课程ID存在



    # 后置处理

    def teardown(self):
        pass

    # 课程修改成功
    def test01_upload_course_sucess(self):
        test_data = {
            "id": 109,
            "name": "接口测试001",
            "subject": "6",
            "price": 998,
            "applicablePerson": "2",
            "info": "课程介绍001"
        }
        respond = self.course_api.upload_course(test_data=test_data, token=TestCourseAP.token)
        # 断言状态响应码 200
        assert 200 == respond.status_code
        # 断言 响应数据 msg 操作成功
        assert "成功" in respond.text
        # 断言  响应状态码 code 200
        assert 200 == respond.json().get("code")

    # 课程修改失败(未登录  )
    def test02_upload_course_fail(self):
            test_data = {
                "id": 109,
                "name": "接口测试001",
                "subject": "6",
                "price": 998,
                "applicablePerson": "2",
                "info": "课程介绍001"
            }
            respond = self.course_api.upload_course(test_data=test_data, token="##")
            # 断言状态响应码 200
            assert 200 == respond.status_code
            # 断言 响应数据 msg 认证失败
            assert "认证失败" in respond.text
            # 断言  响应状态码 code 401
            assert 401 == respond.json().get("code")
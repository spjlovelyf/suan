import allure
import pytest


class Test:
    def test_002(self):
        with open("F:\\就业班01\\APP测试\\app08\\2345截图20190525160854.png","rb") as f:
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    # @allure.step(title='这是一个测试步骤')
    # def test_001(self):
    #     print("hello python")
    #     allure.attach("标题", "标题内容")
            allure.attach("截图",f.read(),allure.attach_type.PNG)
            assert True

    #
    # @allure.step(title='这是另一个测试步骤')
    # def test_002(self):
    # #     print("hello world")
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # @allure.step(title='这是一个测试步骤')
    # def test_002(self):
    #     print("hello python")
    #     allure.attach("标题", "标题内容")
    #     assert True

    # @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    # @allure.step(title='这是一个测试步骤')
    # def test_003(self):
    #     print("hello python")
    #     allure.attach("标题", "标题内容")
    #     assert True
    #
    # @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    # @allure.step(title='这是一个测试步骤')
    # def test_004(self):
    #     print("hello python")
    #     allure.attach("标题", "标题内容")
    #     assert True

    # @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    # @allure.step(title='这是一个测试步骤')
    # def test_005(self):
    #     print("hello python")
    #     allure.attach("标题", "标题内容")
    #     assert True

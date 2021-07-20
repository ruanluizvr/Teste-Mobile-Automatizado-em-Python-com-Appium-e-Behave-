from appium import webdriver
from helpers.calculator import Calculator


def before_scenario(context, scenario):
    pass


def before_feature(context, feature):
    context.driver = webdriver.Remote(
        "http://127.0.0.1:4723/wd/hub",
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "8.0",
            "deviceName": "Emulador_8",
            "automationName": "UiAutomator2",
            "appPackage": "com.android.calculator2",
            "app": "F:/Automação - Python/TesteTopaz/Calculator.apk",
            "appActivity": "com.android.calculator2.Calculator",
        },
    )
    context.driver.implicitly_wait(15)
    context.calculator = Calculator(context.driver)


def after_scenario(context, scenario):
    context.calculator.get_element_by_id("CLR").click


def after_feature(context, feature):
    context.driver.quit()

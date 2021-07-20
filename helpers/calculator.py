class Calculator:
    def __init__(self, driver):
        self.driver = driver

    def get_calculator_button_id(self, value):
        button = {
            "1": "com.android.calculator2:id/digit_1",
            "2": "com.android.calculator2:id/digit_2",
            "3": "com.android.calculator2:id/digit_3",
            "4": "com.android.calculator2:id/digit_4",
            "5": "com.android.calculator2:id/digit_5",
            "6": "com.android.calculator2:id/digit_6",
            "7": "com.android.calculator2:id/digit_7",
            "8": "com.android.calculator2:id/digit_8",
            "9": "com.android.calculator2:id/digit_9",
            "0": "com.android.calculator2:id/digit_0",
            "=": "com.android.calculator2:id/eq",
            "+": "com.android.calculator2:id/op_add",
            "-": "com.android.calculator2:id/op_sub",
            "*": "com.android.calculator2:id/op_mul",
            "/": "com.android.calculator2:id/op_div",
            "CLR": "com.android.calculator2:id/clr",
        }

        return button[value]

    def get_result(self):
        return self.driver.find_element_by_id("com.android.calculator2:id/result").text

    def get_element_by_id(self, value):
        id = self.get_calculator_button_id(value)
        return self.driver.find_element_by_id(id)

    def get_string_clr(self):
        return("CLR")


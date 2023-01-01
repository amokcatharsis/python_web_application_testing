from random import randrange


class TestCase:

    def __init__(self, name):
        self.name = name
        self.id = randrange(100, 1000)
        self.steps = {}

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        del self.steps[step_number]

    def get_steps(self):
        return self.steps.values()

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        test_case = {
            'id': self.id,
            'Название': self.name,
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }

        print(test_case)

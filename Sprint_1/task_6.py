class Tester:

    def __init__(self, name):
        self.name = name

    def work_hard(self, deadline=True):

        if deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')
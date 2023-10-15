class BankInfo:#класс для работы с информацией, поступающей с сервера computer vision
    """класс для работы с информацией, поступающей с сервера computer vision"""
    id = int()
    waiting_time = float()#время ожидания
    _number_of_people = int()# количество людей
    _number_of_staff = int()# количество персонала
    _number_of_salers = int()# количество консультантов 
    _math_expectation = int()# мат ожидания на конкретном участке 

    def __init__(
        self, id, number_of_people, number_of_staff, number_of_salers, math_expectation
    ):
        self.waiting_time = (
            (number_of_people - number_of_staff) / number_of_salers * math_expectation
        )
        if self.waiting_time < 0:
            self.waiting_time = 0
        self._number_of_staff = number_of_staff
        self._number_of_salers = number_of_salers
        self._math_expectation = math_expectation
        self._number_of_people = number_of_people
        self.id = id
        return None

    def update_info(
        self,
        number_of_staff=None,
        number_of_salers=None,
        number_of_people=None,
        math_expectation=None,
    ):
        if number_of_staff:
            self._number_of_staff = number_of_staff
        if number_of_salers:
            self._number_of_salers = number_of_salers
        if number_of_people:
            self._number_of_people = number_of_people

        self.waiting_time = (
            (number_of_people - number_of_staff)
            / number_of_salers
            * self._math_expectation
        )
        if self.waiting_time < 0:
            self.waiting_time = 0
        return self.waiting_time

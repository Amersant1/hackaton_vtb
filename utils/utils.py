def some_func():
    return None


def average_time(lst_income: list, lst_outcome: list):
    ln_people_inside = len(lst_outcome)
    lst_income = lst_income[:ln_people_inside]
    return (sum(lst_outcome) - sum(lst_income)) / ln_people_inside


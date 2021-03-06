# 这个脚本是用来计算伤害个税的


def get_pure_salary(income, deduction=0):
    insurance_rate = 0.175
    max_base = 21396
    min_base = 4279

    free = 5000

    level = {
        0: (0, 0.03),
        1: (3000, 0.1),
        2: (12000, 0.2),
        3: (25000, 0.25),
        4: (35000, 0.3),
        5: (55000, 0.35),
        6: (80000, 0.45)
    }

    tax = 0
    insurance = min(max(income, min_base), max_base) * insurance_rate
    salary = income - insurance
    temp = salary - free - deduction
    for i in range(0, 7):
        if temp <= 0:
            break
        rate = level[i][1]
        if i == 6:
            tax += temp * rate
        else:
            margin = level[i+1][0]-level[i][0]
            tax += min(margin, temp) * rate
            temp = temp - margin
    return salary - tax


def get_saved_salary(income, cur_deduct, pre_deduct=0):
    return get_pure_salary(income, cur_deduct) - get_pure_salary(income, pre_deduct)


if __name__ == "__main__":
    print(get_saved_salary(40000, 3000))

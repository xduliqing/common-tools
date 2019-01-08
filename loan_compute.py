# Author: Elvis Li
# Created: 2018/11/13 15:52

from functools import partial

start_month = 2
months = 30
rate = 6.3
loan = 125000
monthly_rate = rate / 100 / 12
payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
capital_left = loan
interest_total = 0
print("月份\t序号\t剩余本金\t已还本金\t当月利息\t总利息\t每月还款")
round2 = partial(round, ndigits=2)
for i in range(months):
    cur_month = (start_month +i- 1) % 12 + 1
    monthly_interest = capital_left*monthly_rate
    interest_total += monthly_interest
    capital_payed = payment - monthly_interest
    capital_left = capital_left - capital_payed
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(cur_month, i, round2(capital_left),
                                  round2(capital_payed), round2(monthly_interest),
                                     round2(interest_total), round2(payment)))

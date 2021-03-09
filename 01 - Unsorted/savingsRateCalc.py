#monthly returns of MSCI World (2020)
list_of_returns = [0.60, -7.78, -13.37, 11.00, 3.03, 1.52, -0.57, 5.33, -1.68, -2.49, 9.70, 1.81]
#savings rate per month in EUR

monthly_savings_rate = float(input('Enter monthly savings rate: '))

month = 1
total_amount = 0.0

for x in list_of_returns:
    total_amount += monthly_savings_rate
    total_amount += total_amount * x / 100

    temp_txt = '{m}: \t {ta:.2f} \t r= \t {r:.2f}'
    print(temp_txt.format(m=month, ta=total_amount, r=x))
    month += 1

txt = 'Total: \t {temp:.2f}'
print(txt.format(temp=total_amount))
print('Savings: \t' + str((month - 1) * monthly_savings_rate))

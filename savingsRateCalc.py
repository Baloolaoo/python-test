#monthly returns of MSCI World (2020)
listOfReturns = [0.60, -7.78, -13.37, 11.00, 3.03, 1.52, -0.57, 5.33, -1.68, -2.49, 9.70, 1.81]
#savings rate per month in EUR
monthlySavingsRate = 100.0

temp = 0.0

for x in listOfReturns:
    temp += monthlySavingsRate + (temp * x/100)
    print(str(listOfReturns.index(x)+1) + ":\t " + str(temp) + "\t r=\t" + str(x))

txt = "Total: \t {temp:.2f}"
print(txt.format(temp=temp))

# Enter your code here. Read input from STDIN. Print output to STDOUT

x_variable = 80

x = [95,85,80,70,60]
y = [85,95,70,65,70]

sum_x = 390
length_x = 5
sum_y = 385
length_y = 5
average_x = sum_x / length_x
average_y = sum_y / length_y

x_squared = 0

for i in x:
    x_squared += (pow(i,2))


xy = 0

for i in range(len(x)):
    xy += (x[i] * y[i])


b = ((length_x * xy) - (sum_x * sum_y)) / ((length_x * x_squared) - (pow(sum_x,2)))

a = average_y - (b * average_x)

y = (x_variable * b) + a
print(y)

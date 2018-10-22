# if 语句是从上到下的执行的，执行下列语句
x = input('input a number')
if float(x)< 15:
	print('x is smaller than 15')
elif float(x) > 10:
	print('x is bigger than 10')
else:
	print('fuck')

# if语句是可以不执行的，执行下列语句,shit+clt+e执行部分代码

x = input('input a number')
if float(x)< 15:
	print('x is smaller than 15')
elif float(x) > 20:
	print('x is bigger than 20')
print('Done')
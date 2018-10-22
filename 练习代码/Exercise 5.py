num = 0
aver = 0.0
while True:    #无限循环
	user_num = input('Enter a number')
	if user_num == 'done':
		break
	try:
		number = float(user_num)
	except:
		print('Invalid input')
		continue  #回到顶部，可以继续输入数字，否则程序退出
	print(number)
	num = num + 1
	aver = aver + number #这里必须要用number，number和aver的数据结构都是float，user_num 的数据结构是str
print('一共有多少数字',num,'平均数',aver/num)
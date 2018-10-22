#  None 是一个控制的类型
   is 是一个内置的函数，比 == 强，因为is 还考虑类型
   例如，0 == 0.0 是ture
        但是0 is 0.0 是false
complex = None
for y in [0,25,65,84,24,22,50,910,51,99]:
	if complex is None:
		complex = y
	elif complex < y:
		comlex = y
		print(complex,y )
print('Done')

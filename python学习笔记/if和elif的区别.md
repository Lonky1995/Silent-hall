  
# if 和elif 是有区别的   

ifa = True   
b=True   
if a:   
print(“代码块1”)   
if b:   
print(“代码块2”)   
代码块1和代码块2都会被输出，而再想一下如果是使用elif:   
a = True   
b=True   
if a:   
print(“代码块1”)   
elif b:   
print(“代码块2”)   
只会输出代码块1，而不会输出代码块2了   
    

largest = -float('inf')   
smallest = float('inf')   
while True:   
 num = input('put a number')   
 if num == 'done': break   
 try:   
 float(num)   
 except:   
 print('Invalid input')   
 continue   
 if float(num) > float(largest):   
 largest = float(num)   
 if float(num) < float(smallest):   
 smallest = float(num)   
print('Maximum',largest)   
print('Minimum',smallest)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzg2Mjc0MzJdfQ==
-->
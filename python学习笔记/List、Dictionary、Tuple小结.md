 1. List
     集合。用中括号 []表示。
 - 定义List
`list = ['BOB',2,3] list = []`item
 - list的排序是从0开始的，打印list。
```
print(L[0]) #打印第一个元素 
print(L[-1])#打印最后一个元素`
```
 - List通过内置的append()方法来添加到尾部，通过insert()方法添加到指定位置（下标从0开始）
```
L = [1,2]	
`L.append = ('jack')
print (L)
L = [1,2,'jack']
L.insert = (1,'hel')
print(L)`
L = [1,'hel',2,'jack']
````
-List 可以用过pop来进行删除操作
```
L.pop()    #默认删除最后一个
L.pop(x)  #删除第x个
````
- list 可以进行排序操作
```
list.sort(cmp=None, key=None, reverse=False)
```
cmp 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
 key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True  降序，  reverse = False  升序（默认）。

- 可以用len计算长度
- 用下标访问内容

2.tuple
不可改变的list，用小括号()。没有append、sort、pop等函数
`(1,2) =('bob','car')` 

 - 可以用len计算长度
 - 用下标（位置）访问内容
 - 
3.dictionary
类似于数据库，是key-value对，用大括号{}定义
```
D = {
'Alice'  :1
'bob' : 2
}
```
- 直接通过健值对添加
`D['fuck'] = 66`
- 通过查找key访问内容
-
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NDk4ODI4MTIsLTExMTA3NDczMDBdfQ
==
-->
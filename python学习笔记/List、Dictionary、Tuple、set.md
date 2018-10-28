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
- 通过字典进行计数
`hi[x] = hi.get(x,0) + 1 #对于list x 中每个数进行遍历，产生字典hi，字典的key是list中的每个元素，key对应的健值是list中元素的出现次数`
 - Key不可变，且不可重复，Value可变。一旦一个键值对加入dict后，它对应的key就不能再变了，但是Value是可以变化的。所以List不可以当做Dict的Key，但是可以作为Value
 -  两个dictionary可以合并
 ```
 d1 = {'mike':12, 'jack':19} 
 d2 = {'jone':22, 'ivy':17} 
 dMerge = dict(d1.items() + d2.items()) 
 print dMerge
{'mike': 12, 'jack': 19, 'jone': 22, 'ivy': 17}
````
4. set
set就像是把Dict中的key抽出来了一样，类似于一个List，但是内容又不能重复，通过调用set()方法创建：
`s = set(['A', 'B', 'C'])`
对于访问一个set的意义就仅仅在于查看某个元素是否在这个集合里面：
```
print 'A' in s
True
print 'D' in s
False
```
- set对于元素的大小写是敏感的。

- 也通过for来遍历：

```
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)]) #tuple
for x in s:
	print (x[0],':',x[1]) 
Lisa : 85
Adam : 95
Bart : 59
```
- 通过add和remove来添加、删除元素（保持不重复），添加元素时，用set的add()方法：
```
 s = set([1, 2, 3]) 
 s.add(4) 
 print s
set([1, 2, 3, 4])
```
- 如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了：
```
 s = set([1, 2, 3])
 s.add(3) 
 print s
set([1, 2, 3])
```
- 删除set中的元素时，用set的remove()方法：
```
s = set([1, 2, 3, 4]) 
s.remove(4) 
print s
set([1, 2, 3])
```
- 如果删除的元素不存在set中，remove()会报错：
```
s = set([1, 2, 3]) 
s.remove(4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module> KeyError: 4
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgxMjczOTA0NV19
-->
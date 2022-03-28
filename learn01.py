"""
> 大於
< 小於
>= 大於等於
<= 小於等於
== 等於
!== 不等於
--------------------------
true 真
false 假
and 且
or 或
not 非(負號)
-------------------------
\   續行(放句尾)
\\   反單斜號
\'   單引號
\''  雙引號
\n   換行
\r   
\t   tab 
-------------------------
if ___ or ____ :
    _______
elif ______ :
    _______
else:
    
for _ in range (n,m) n~m-1
for [變數名稱] in range(n): (縮排) print([變數名稱])

-------------------------
"Ro"+"ger"== "Roger"
-------------------------
list列表(陣列)

scores = [0,1,2,3,4,5,6,7]
print(score[-2]) 倒數第二位
frt = ["一","二"]
print(frt[0])
print(scores[1:4]) 1~3
print(scores[1:])  1~end
print(scores[:4])  0~3


list1.extend(list2)  list1後面接上ist2
list.append(x): 把變數x塞到list的最後面
list.insert(i, x): 把變數x塞到i這個位置上
list.remove(x): 會把第一個出現的變數x拿掉
list.clear(): 把list內的資料全部清光
list.pop(): 把list的最後一格丟掉
list.pop(i): 把list的第i格丟掉
list.sort()： 從小到大排列
list.reverse()：列表反轉
list.index(x)：找第一個x
list.count(x)：數有幾個x
max(list): 找出list中最大值
min(list): 找出list中最小值
sum(list): 找出list數字總和
len(list): 長度

二為列表
num = [[1,2],[3,4]]
print(num[1][0]) 

!! row = 行  / column = 列  !!


touple 元祖 
-> 不能修改 !!!
score = (1 , 2 , 3 , 4 , 5 , 6)
print(score)
*就是為了防止被修改*

slice語法：
list[start: end]，start和end都可以省略不寫
start的預設為0
end的預設為len(list)
liest[ :end]代表 0~end-1
list[start: ]代表start~len(list)-1
list[ : ]代表0~len(list)-1

x="Hello"
print(x[1:3]) el
.lower() 換成小寫
.upper() 換成大寫
.islower()
.isupper()
print(Word[0]) 輸出W
.index("W") 找W位置 0
.replace("W","w")  w替換W
-------------------------
function 函式

def hello():       定義
    print("hello")

hello()            呼叫

def hellop(name , age):
    print("hello"+ name + "你今年" + str(age) + "歲")

hellop("林鈺翔" , 18)

def add(a , b):
    return a+b
-------------------------
if 條件(一):
    程式碼(一)
elif 條件(二):
    程式碼(二)
else:
    程式碼(三)
-------------------------
dictionary 字典 
-> key    value
-> 鍵       值

dic = {0:"appke" , 1:"banana" , 2:"cat" , 3:"dog"}
print(dic[0])
-------------------------
while 迴圈

i=1
while i<=5:
    print(i)
    i += 1
-------------------------
for 迴圈

for 變數 in 字串or列表:
    程式碼

for letter in "早安午安晚安":
    print(letter)
    
for num in [1,2,3,4]:
    print(num)

for num in range(5): 
    print(num)      (1~4)

-------------------------
巢狀迴圈
for row in 
-------------------------
檔案讀、寫入

-------------------------  
int('') 
float(' ')
str(' ')

abs(100) 取絕對值
pow(2,4) 2的4次方
max(1,2,3,...)
min(1,2,3,...)
round(1.5) 4捨5入

from math import * 
fkloor()無條件捨去
ceil()無條件進位
sqrt()開根號
------------------------
%d  整數
%f  浮點數
%s  字串
%x  16進制數字
-----------------------
"""

print('RR\nRRRR\riiiiir'+'ttt'\
      +'RRRR')
  
num1 = float(input("請輸入第一個數"))
op = input("請輸入運算符號：")
num2 = float(input("請輸入第一個數"))

if op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1 - num2)
elif op=="*":
    print(num1 * num2)
elif op=="/":
    print(num1 / num2)
else:
    print("輸入錯誤")
    
dic = { 1:"apple" , 2:"banana" , 3:"cat" , 4:"dog"}
print(dic[1])


num = [[1,2],[3,4]]
print(num[1][0]) 

    



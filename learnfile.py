"""
open("檔案路徑" , mode="開啟模式")
絕對路徑 ex:D:/高師課程/程式設計/python學習/file01.txt
相對路徑 ex:file01.txt
 
mode = "r" 讀取
mode = "w" 覆寫
mode = "a" 在原先資料後寫東西

file = open("file01.txt" , mode = "r") 
print(file.read())
print(file.readline())  #讀第一行
for line in file :
    print(line)
file.close() 

file = open("file01.txt" , mode = "w" , encoding="utf-8") 
file.write("hello") 把hello寫入
file.close() 

file = open("file01.txt" , mode = "a" , encoding="utf-8")
file.write("晚安")
file.close() 

with file = open("file01.txt" , mode = "a" , encoding="utf-8") as file
    file.write("hello")

 XX file.close() XX
"""
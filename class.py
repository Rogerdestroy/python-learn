"""
class 類別  、 object 物件

class Phone:
    def __init__(self,os,number,is_water_proof):
        self.os = os 
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios" , 123 , True)

"""
from question import Question

class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os 
        self.number = number
        self.is_waterproof = is_waterproof
#物件函式 
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
            
    print("你得到" + str(score) + "分 , 共" + str(len(questions)) + "題")
    
phone1 = Phone("ios" , 123 , True)
phone2 = Phone("android" , 223 , True)

print(phone1.is_ios())

print(phone1.os)
print(phone2.number)
print(phone2.is_waterproof)

test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n" ,
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n" ,
    "香蕉英文?\n(a) appe\n(b) banana\n(c) cat\n\n"
]

questions = [
    Question(test[0],"c")  ,  
    Question(test[1],"b")  ,
    Question(test[2],"b")    
]

run_test(questions)




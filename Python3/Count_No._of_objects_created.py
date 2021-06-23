class Test:
    count=0
    def __init__(self):
        Test.count+=1
    @classmethod
    def getCount(cls):
        print("No. of objects created :",cls.count)

print(Test.count) # 0
t1=Test()
t2=Test()
t3=Test()
t4=Test()
t5=Test()
print(Test.getCount()) #5
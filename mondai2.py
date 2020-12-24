import matplotlib.pyplot as plt
import random
class Record:
    def __init__(self, h):
        self.height = h
        self.weight = []
        self.BMI = []
    def setWeight(self,w):
        self.weight.append(w)
        self.BMI.append(w/(h*0.01)**2)
    def getWeight(self):
        self.weight = [-1]
    def getBMI(self):
        self.BMI = [-1]
    def plotWeight(self):
        plt.plot(weight) #5kaijyugyoukadai
    def plotBMI(self):
        plt.plot(BMI)
height = float(input('身長を cm 単位で入力してください>'))
record = Record(height)
for i in range(10):
    kotae = 0
    print("体重測定")
    record.setWeight(random.randint(60, 75)) #kyoukasyo318
    print('あなたの体重は{}kgで、'.format(self.weight))
    print('{}').format(self.BMI)
    if self.weight <= 18.5:
        kotae = '低体重'
    elif 18.5<self.weight<25:
        kotae = '標準体重'
    elif 25<=self.weight<30:
        kotae = '肥満(Ⅰ度)'
    elif 30<=self.weight<35:
        kotae = '肥満(Ⅱ度)'
    else:
        kotae = '高度肥満'
print()
print("体重の推移をグラフ化します")
record.plotWeight()
print("BMI の推移をグラフ化します")
record.plotBMI()
















class Date():
    def __init__(self, sal, mah, ruz):
        self.sal = sal
        self.mah = mah
        self.ruz = ruz

    def show(self):
        print(self.sal,"/",self.mah,"/",self.ruz)

    def sum(self,d):
        result = Date(None,None,None)
        result.sal = self.sal + d.sal
        result.mah = self.mah + d.mah
        result.ruz = self.ruz + d.ruz
        if result.mah > 12 :
            result.mah -= 12
            result.sal += 1
        if result.ruz > 30:
            result.ruz -= 30
            result.mah += 1
        return result

    def sub(self, d):
        result = Date(None,None,None)
        result.sal = self.sal - d.sal
        result.mah = self.mah - d.mah
        result.ruz = self.ruz - d.ruz
        if result.mah < 0 :
            result.mah += 12
            result.sal -= 1
        if result.ruz < 0:
            result.ruz += 30
            result.mah -= 1
        if result.sal < 0:
            result.sal = -(result.y)
        return result

date1 = Date(2022, 11, 27)
date2 = Date(2023, 02, 13)

result_sum = date1.sum(date2)
print("Date sum: ")
result_sum.show()
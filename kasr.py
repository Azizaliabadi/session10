class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def show(self):
        print(self.soorat, "/" ,self.makhraj)

    def sub(self, f):
        result = Fraction(None, None)
        result.soorat = (self.soorat * f.makhraj)-(self.makhraj * f.soorat)
        result.makhraj = self.makhraj * f.makhraj
        return result

    def div(self, f):
        result = Fraction(None ,None)
        result.soorat = self.soorat * f.makhraj
        result.makhraj = self.makhraj * f.soorat
        return result

fraction1 = Fraction(2 , 3)
fraction2 = Fraction(3 , 5)


result_sub = fraction1.sub(fraction2)
result_div = fraction1.div(fraction2)


result_sub.show()
result_div.show()
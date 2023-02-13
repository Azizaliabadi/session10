class Time():
    def __init__(self,h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def show(self):
        print(self.h,":",self.m,":",self.s)

    def sum(self, t):
        result = Time(None ,None ,None)
        result.h = self.h + t.h
        result.m = self.m + t.m
        result.s = self.s + t.s
        if result.m >= 60:
            result.m -= 60
            result.h += 1
        if result.s >= 60:
            result.s -= 60
            result.m += 1
        if result.h >= 24:
            result.h -= 24
        return result

    def sub(self, t):
        result = Time(None, None, None)
        result.h = self.h - t.h
        result.m = self.m - t.m
        result.s = self.s - t.s
        if result.m <= 60:
            result.m += 60
            result.h -= 1
        if result.s <= 60:
            result.s += 60
            result.m -= 1
        if result.h >= 24:
            result.h += 24
        if result.h < 0:
            result.h += 24
        return result
    def tabdil_s_to_z(self):
        while True:
            if self.s >= 60:
                self.s -= 60
                self.m += 1
            if self.m >= 60:
                self.m -= 60
                self.h += 1
            if self.s < 59 and self.m < 59:
                break
        print(self.h,":",self.m,":",self.s)

    def tabdil_z_to_s(self):
        while True:
            if self.h > 0:
                self.h -= 1
                self.m += 60
            if self.m > 0 :
                self.m -= 1
                self.s += 60
            if self.h == 0 and self.m == 0:
                break
        print(self.h,":",self.m,":",self.s)

time1 = Time(10 ,20 ,25)
time2 = Time(8 ,30 ,40)
sum_result = time1.sum(time2)
print("sum:")
sum_result.show()
sub_result = time1.sub(time2)
print("sub")
sub_result.show()
print("tabdil sanie b zaman:")
time1.tabdil_s_to_z()
print("tabdil zaman b sanie:")
time1.tabdil_z_to_s()
class reg:
    x=0;y=0
    def __init__(self,a,b):
        reg.x=a
        reg.y=b
    def area(self):
        return reg.x*reg.y
    def peri(self):
        return (reg.x+reg.y)*2
class squ(reg):
    def __init__(self,c,d):
        super().__init__(c,d)
    def s_area(self):
        if reg.x==reg.y:
            return reg.x**2
        else:
            return self.area()
    def s_peri(self):
        if reg.x==reg.y:
            return reg.x*4
        else:
            return self.peri()
#===================================
obj=squ(6,6)
print(obj.area())
print(obj.peri())
print(obj.s_area())
print(obj.s_peri())

class r:
    def __init__(self,w):
        self.s=w

    def rw(self):
        return self.s[::-1]

wo=input("ENTER WORD TO BE REVERSED: ")
ro= r(wo)
re=ro.rw()
print("REVERSED STRING: ",re)

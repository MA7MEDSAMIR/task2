def calc(a,b,operation):
     if operation=="add"  :
        return a+b
     if operation=="subtract" :
        return a-b
     if operation=="multiply":
        return a*b
     if operation=="divide":
        if b!=0:
            return a/b
        else:
            print("math error")
print(calc(5,5,"divide"))
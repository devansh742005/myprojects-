ia = input("Give the binary: ")

def todecimal(ia):
    r = 0
    qwe = "not found"
    
    for i in range(len(ia)):
        if(int(ia[i])==0):
         D = int(ia[i])
         r= r * 2 + D
         return r
        else:
            return qwe
    

re= todecimal(ia)
print(re)

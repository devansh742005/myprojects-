class solution:
 def isu (n):
     g = [2,3,5]
     lis = []
     for i in range (2,n):
          if (n%i==0):
              lis.append(i)
     for i in range(len(lis)):
         if lis[i] in g:
             return True
         else:
              False
              break
              
 h = int(input())
 j = isu(h)
 print(j)
    
             
          
           
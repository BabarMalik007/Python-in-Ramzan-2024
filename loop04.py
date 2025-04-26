#num = [1,2,3,4 ,5,6,7]

#for val in num:
  #  print (val)


#str = ("lucky")
#for char in str:
 #   if (char =='k'):
  #      print ("o found")
   #     break
    #print (char)


#else :
#    print ("end")


num = [1,4,8,12,16,44,64,128,777,981]

x = 777

idx = 0

for el in num:
    if (el==x):
       print ("number found at idx", idx)

       break    
    idx  +=1
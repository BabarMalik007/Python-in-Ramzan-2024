### recursive function

#def show (n) :
 #   if (n == 0):
  #      return
  #  print (n)
   # show (n-1)

#show (5) 

### Recursion function


#def fact (n) :
 #   if (n == 0 or n == 1):
  #        return 1
   # return n* fact (n-1)
#print (fact (6))
### calculate the sum of natural numbers
#def cal_sum (n) :
 #    if (n ==0):
  #        return 0
  #   return cal_sum (n-1) +n

#sum = cal_sum (5) 
#print (sum)


###recursive function to print all elements in a list & indx as parameters

def print_list(list, idx=0):
    if (idx == len(list)):
         return
    print (list [idx])
    print_list(list, idx+1)
fruits = ["mango", "lichi", "banana", "apple", "graps"]
print_list(fruits)
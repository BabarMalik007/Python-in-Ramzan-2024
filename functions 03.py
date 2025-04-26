cities = [ "karachi", "lahore", "islamabad", "multan"]
fruits  = ["apple ", "bnanana", "mango", "orange", "strawberry"]
num = [1, 2, 3, 4, 5, 6, 7]

print (cities[0], end = " ")
print (cities[1], end = "\n")

def print_len(list):
    print (len(list))

print_len(cities)
print_len(fruits)
print_len(num)


# 2nd function

def print_list(list):
    for item in list:
        print (item, end = " ")

print_list(cities)


print_list(fruits)
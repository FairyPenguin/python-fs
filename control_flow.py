# control flow - if statement

# if 5 < 4:
#     print("YES")
# elif 5 == 5:
#     print ("They are Euqal")
# elif 5 > 3 and 5 > 4:
#     print ("it's Bigger")
# else: 
#     print("NO")

# control flow - while loop

# counter = 0

# while counter <= 10:
#     print(counter)
#     counter +=1

# control flow - for loop

# numbers_list = [1,2,3,4,5,6,7,8,9,10]

# for x in numbers_list:
#     print(x)

# numbersdictionary = {1:"apple",2:"orange",3:"watermelon"}

# # .keys .values .items
# for x in numbersdictionary.items():
#     print(x)


# for x,y in numbersdictionary.items():
#     print(x,y)

# control flow - truthy && flasy values

# 0 - empty_string "" - empty containers is falsy
#everything else is truthy


list = (1,2,3,4,5)

# for x in list:
    
#     if x == 2:
#         print("the value is 2")
#     while x ==5:
#         print("last item \n" * 6 )
#         x += 1
#     else:
#         print("the value is not 2")

counter = 0

for x in list:
    if x == 2:
        print("2")
    else:
        print("Not 2")
while counter <= 6:
    print("last item")
    counter +=1
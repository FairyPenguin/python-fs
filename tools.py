# f strings ==> template litreals - string interpolation


user_name = "Johny"

user_age = 10

user_name_and_age = f"{user_name} is {user_age}"

print(user_name_and_age)

# single line if ststement
user_age= 20
user_status = "Adult" if user_age >=20 else "teenager"
print(user_status)

#list comperhension 

list = [i for i in range(0,11,1)]

# for i in range(0,11,1):
#     list.append(i)

print(list)


# lambda functions
double_value = lambda num: num * 5
print(double_value(2))


#exercise

battleship_board = [f"{j}{i}"  for j in ("a","b","c","d","e") for i in range(1,6,1)  if f"{j}{i}" != "c3"] 

# if battleship_board == "c3":
#     battleship_board.remove()
# else:
print(battleship_board)
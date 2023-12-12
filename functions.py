# custom function 

def this_is_function(parameter,loop_value = 5,value=0):
    counter = value
    print(global_var)
    while counter <=loop_value:
        print(counter,parameter)
        counter += 1
    return "The function return"

# calling the function 
global_var = "global_var"

func = this_is_function(parameter="argument",loop_value=6,value=0)

print(func)

# function

def shouter(string = "I'm the default",number = 8):
   counter = 0
   if number > 10:
       print("Don't Contuine")
   else:   
     while counter <=number:
        
       cap = string.upper()
       print(cap)
       counter+=1
     return "Done"

shouter("print me",3)

def shout(string = "default string",number = 8):
    if number > 10:
        print("don't continue")
    else:
        #range for loop over an intger
        for i in range(number):
            print(string.upper())
    
    return "Done"
    
    

shout("string",4)
    
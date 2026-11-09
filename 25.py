#Dictionaries and Functions

# def print_number(x):
#     print("NUMBERS IS", x)

# rename_print = print_number
# rename_print(100)
# print_number(100)


# color = "Red"
# corvette = {
#     "color": color
# }

# print("LITTLE", corvette["color"], "CORVETTE")



def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette["color"], "can go")
corvette["run"]() #it's pointing to the bring out the value of run, 
                   #which is a function and that's where the "()" since it's run, 
                   # #it needs to be run() to bring out the value


#get the run function out of the corvette dict
myrun = corvette["run"]
#run it
myrun()


from sys import argv

input_file = "ex20_test.txt" 

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline()) #reads one line

current_file = open(input_file) #opens the input_file

print("First let's print the whole file: \n") #The first thing that is printed

print_all(current_file) #carries out the defined function "print_all" which reads the current_file, and current_file = open(input_file)


print("Now let's rewind, kind of like a tape.") #This prints the string

rewind(current_file) #carries out the defined "rewind" function. The .seek() method is used to change the position of the file pointer (cursor) within an open file. The seek(0) returns it to the default position/beginning of the file.

print("Let's print three lines:") #This prints the string

current_line = 1
print_a_line(current_line, current_file) #carries out the defined function "print_a_line"

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
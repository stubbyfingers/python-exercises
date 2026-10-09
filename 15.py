from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file name {filename}:") #this only prints "Here's your filename 15_sample.txt" and not what the file contains
print(txt.read()) #this prints out what is in the file
print(txt.close()) #it closes it and returns none

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again) #this opens the file, it can be another file too
print(txt_again.read()) #this prints out what is in the file

#looks complicated but is easy to read
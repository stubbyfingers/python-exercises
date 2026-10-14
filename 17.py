from sys import argv #import is a way to get a ton of free code other programmers have written so you do not have to write it
from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)  # indata = open(from_file).read, then remove the in_file.close() at the end
indata = in_file.read() #for line 10 and they open the from_file and write/read it in the variable "indata"

print(f"The input file is {len(indata)} bytes long")
 
print(f"Does the output file exist? {exists(to_file)}") #exists command returns TRUE if the file exists and returns FALSE if not.
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input() #this is not entirely necessary

out_file = open(to_file, 'w') 
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
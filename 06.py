x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print(x) #Expected output is "There are 10 types of people" because the 10 is to replace the formatter
print(y) #Expected output is "Those who know binary and those who don't" because the binary variable contains binary and do_not variable contains don't


print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print(w+e)
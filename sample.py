#This function takes an input name and occupation and reverses it through the negative slicing
# Recall...
# stuff = "Something"
# stuff[:] gives back all the value of stuff
# stuff[2:] gives back values from index 2 to the end
# stuff[0::2] gives back values from index 0 to the end but with a step of 2. that is it skips one 
# Remember we can use negative indexing to retrieve values from the last we use thesame concept to slice in the reverse order
# So stuff[6:1:-1] returns from i backwardss to o

def reversed(name, occupation):
	reversed_name = name[len(name)::-1]
	reversed_occupation = occupation[len(occupation)::-1]
	return reversed_name + " is a " + reversed_occupation

print(reversed("Hannatu", "student"))

# Note that you can't perform the same indexing or slicing on an integer.
# What you need to do is first convert the int to a string using the .str() built in function
# for example a way to reverse an integer;
# num = 12345
# ***convert the num to a string***
# str_num = str(num)
# ***reverse the string***
# str_num_reversed = str_num[len(str_num)::-1] ----- should return '54321'
# to convert it back to int you use the .int() function
# int(str_num_reversed) ---- should return 54321

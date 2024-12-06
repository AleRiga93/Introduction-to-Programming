"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
#missing space between "def" and "tract"
def tract_and_rearrange(string):
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    #split function was misspelled 
    str_2 = "".join(string[6:13].split('ro'))
    #join was not defined
    #the str3 variable had a spelling mistake, corrected it with str_3 instead 
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))
    str_4 = "".join(string[21:29].split(string[23:28]))
#SyntaxError, missing (+) sign before "str_4"
    return str_1 + " " + str_2 + " " + str_3 + " " + str_4
#colon missing after the def function
def ultra_extrct_and_rearrange(string):
    #the function (tract_and_rearrange) was written right
    first_transform = tract_and_rearrange(string)
    return first_transform
#the function (ultra_extrct_and_rearrange) had a spelling mistake, an underscore was missing between "and" and "rearrange"
#the string had extra (") at the end
print(ultra_extrct_and_rearrange("egthb quirock nwoGrb forijmpxv"))


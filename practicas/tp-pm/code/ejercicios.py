#Exercive 1
#Find the existence of a character in a string
#In: The character and the string
#Out: True or False if it finds the character
#WorstCase: m is length of String O(m)
def existChar(String,c):
    for i in String:
        if i == c:
            return True
    return False
newstr = ""
def remove_v(n):
    newstr = n
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for x in n:
        if x in vowels:
            newstr = newstr.replace(x,"")
    return newstr
userin = input("Input: ")
print(remove_v(userin))
string  = str(input("Enter a String: "))
print(string)

letter = str(input("Enter a letter to remove: "))
print(letter)

if letter in string:
    nstring = string.replace(letter, "")
    print(nstring)
else:
    print('Your letter is not there')

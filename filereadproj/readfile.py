f = ('')
file = input("Enter a file: ")
try:
    f = open(file)

except:
    print("That is not a file")
    exit()
shows = [line.strip().split(',') for line in f.readlines()]
f.close()

print(shows)

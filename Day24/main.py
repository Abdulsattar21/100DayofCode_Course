file = open("text.txt")

print(file.read())
file.close()


with open("text.txt", mode="a") as file: # this will close it automatically
    #content = file.read()
    #print(content)
    file.write("\nThis is me again")
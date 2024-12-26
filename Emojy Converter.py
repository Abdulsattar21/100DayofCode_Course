enter = input(">")
words = enter.split(' ')
emojy = {
     ":)": "😄",
     ":(": "😟",
     ":'(": "😥"
}
output = ''
for word in words:
    output += emojy.get(word, word) + " "
print(output)

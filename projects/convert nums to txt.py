number = input("Write your Phone: ")
mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "Eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for num in number:
    output += mapping.get(num, "!") + " "
print(output)
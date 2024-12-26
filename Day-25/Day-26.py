txt = "What is the Airspeed Velocity of an Unladen Swallow?"

txt_list = txt.split()

result = {word: len(word) for word in txt_list}
print(result)

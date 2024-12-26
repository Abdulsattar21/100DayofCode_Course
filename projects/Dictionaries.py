'''
 Dictionary is just like structures in C language, like we have for exam an customers and we need to store
 the customers name, email, numbers... so that where we need to use Dictionaries in Python
'''
customers = {
    "name": "John smith",
    "age":30,
    "is_verified": True
}
customers["name"]
customers["name"] = "Abdu"
customers["birthday"] = "21 jan 2021"
print(customers.get("Name"))# if we used the .get("") we don't get an error we just get a None word as an output
print(customers.get("selam","This is a mesasge error we can say whatever we want"))
 
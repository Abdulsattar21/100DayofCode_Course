from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter


with open("(3) Abdulsattar Mouray _ Facebook.html", errors="ignore", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
names = []
links = []

print("1")
names_testing = soup.select(selector="div div div  a", class_="x78zum5 x1q0g3np x1a02dak x1qughib")
print("3")

n=0
print(names_testing)
for friend in names_testing:
    name = friend.getText()
    names.append(name)
    link = friend.get("href")
    links.append(link)
    print("Start Here -----------------------------")
    print(name)
    print(n)
    n += 1
    print("_____________________________________________")
    print(link)
    print(" ----------------------------- Finish Here")
    print(" ")

print("2")
# df_1 = pd.DataFrame(names)
# df_2 = pd.DataFrame(links)
# print(df_2)
# print(df_1)
# df_3 = pd.DataFrame(zip(names, links))
# print()
# with pd.ExcelWriter("D:\sile\multi_sheet.xlsx") as writer:
#     df_1.to_excel(writer, sheet_name="names", index=False)
#     df_2.to_excel(writer, sheet_name="links", index=False)
#     df_3.to_excel(writer, sheet_name="both", index=False)


#
# names = names[47:]
# links = links[47:]
# names.reverse()
# links.reverse()
# print(names)
# print(links)
# print(len(links))
# print(len(names))
# x, y, z = 0, 0, 0
#
# try:
#     for n in range(301):#int(len(names)/3)):
#         x = (n * 3)
#         y = (n * 3) + 1
#         z = (n * 3) + 2
#         del names[x]
#         del names[z]
#         del links[x]
#         del links[z]
# except:
#     pass
#
# print(names)
# print(links)
# print(len(links))
# print(len(names))
#
#
# # names = [name.getText() for name in soup.find_all(name= "div", class_= "x1iyjqo2 x1pi30zi")]
# # links = [name.get("href") for name in soup.find_all(name= "div", class_= "x1iyjqo2 x1pi30zi")]
# # print(names)
# # print(links)
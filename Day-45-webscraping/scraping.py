from bs4 import BeautifulSoup
import pandas as pd
import xlsxwriter
with open("Movies.html", errors="ignore") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")


titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with xlsxwriter.Workbook('test.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(titles):
        worksheet.write_row(row_num, 0, data)


# df = pd.DataFrame(titles)
# writer = pd.ExcelWriter("test.xlsx", engine="xlsxwriter")
# df.to_excel(writer, sheet_name="welcome", index="false")
# writer.save()



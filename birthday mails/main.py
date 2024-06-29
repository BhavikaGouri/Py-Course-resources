import datetime as dt
import smtplib
import pandas
import random


data = pandas.read_csv("birthday mails/birthdays.csv")
now = dt.datetime.now()
today = (now.month, now.day)

PASSWORD = "APP PASSWORD(generated)"
EMAIL = "<SENDER'S MAIL ID>@gmail.com"

data_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
person = data_dict[today]["name"]


if today in data_dict:
    with open(f"birthday mails/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", person)
        birthday_letter = new_letter.replace("Angela", "<YOUR NAME>")

    # for g-mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=data_dict[today]["email"],
                            msg=f"Subject:HAPPY BIRTHDAY!\n\n{birthday_letter}")

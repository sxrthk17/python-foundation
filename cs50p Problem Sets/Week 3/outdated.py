months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date = input("Date: ")
if "/" in date:
    date_format = date.split("/")
elif "," in date:
    date.split(" ")

print(date_format)

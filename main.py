import datetime
from dateutil import relativedelta


if __name__ == '__main__':
    now = datetime.datetime.now()
    format_scheme = "%m/%d/%Y"
    users_name = input("Hello, please enter your name.\n> ")
    birthday_dt = datetime.datetime.strptime(input("When is your birthday? (ex. 05/02/1982)\n> "), format_scheme)
    birthday_this_year = birthday_dt.replace(year=now.year)
    birthday_next_year = birthday_dt.replace(year=now.year + 1)

    if birthday_this_year.date() >= now.date():
        next_birthday = birthday_this_year
        turning_age = relativedelta.relativedelta(now, birthday_dt).years + 1
    else: 
        next_birthday = birthday_next_year
        turning_age = relativedelta.relativedelta(now, birthday_dt).years + 1

    difference = next_birthday - now

    print(f"You'll be turning {turning_age} in {difference.days} days!")

    #print(next_birthday)
    #print(turning_age)
    #print(difference)
    #print(now)


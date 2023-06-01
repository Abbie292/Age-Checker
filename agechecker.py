import datetime

while True:
    y = input("Enter year of birth: ")
    m = input("Enter month of birth: ")
    d = input("Enter day of birth: ")
    today = datetime.datetime.now().date()
    dob = datetime.date(int(y), int(m), int(d))
    age = int((today-dob).days / 365.25)
    print(age)
    break

  

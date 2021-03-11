print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)

#inputs
age = input("your age :")
unit = input("unit { month , week , day} :").strip().lower()

#time units
month = int(age)*12
week = month*4
day = int(age)*365

#if con
if unit == "month" or unit=="m" :
    print(f" your age in month : {month}")

elif unit == "week" or unit == "w" :
    print(f"your age in weeks : {week}")

elif unit == "day" or unit == "d" :
    print(f"your age in day : {day}")

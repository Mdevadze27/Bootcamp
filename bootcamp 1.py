a = int(raw_input("Enter a value : "))

b = int(raw_input("Enter b value : "))

c = int(raw_input("Enter c value : "))

average = (a + b + c) / 3
print("average is: " str(average))



Cel = raw_input("Enter Celcius : ")
Fahrenheit = (Cel * 9 / 5) + 32
print("Fahrenheit is: " Cel)

# for this one I used internet source
year = 1997

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


try:
    score = float(input("Enter Score: "))
    if score >= 90 and score <= 100 :
        print("A")
    elif score >= 80 and score <= 89 :
        print("B")
    elif score >= 70 and score <= 79 :
        print("C")
    elif score >= 60 and score <= 69 :
        print("D")
    else:
        print("F")
except:
    print("Please enter a number between 0.0 to 1.0")

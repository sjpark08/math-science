number = float(input("enter your number?"))/1


while number != 1:
  if number % 2 == 0:
    number = number / 2
    print(number)
  else:
    number = number * 3 + 1
    print(number)


  

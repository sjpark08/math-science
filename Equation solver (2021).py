def leaner():
  print("This will solve equation")
  print("Only ax+b=0 form")

  print("---------------------------------")

  a = float(input("Enter the a value:   "))
  b = float(
    input("Enter the b value:   "))  #This part gets an input from user.

  print("---------------------------------")

  print("Your equation is ", a, "x +", b, "=0")
  answer = (-b) / a  #This is the basic solving form of linear equation.

  print("---------------------------------")

  print("There are one real solution", answer)  #This part prints the answer.


def quaderatic():
  print("This will solve equation")
  print("Only ax^2+bx+c=0 form")

  print("---------------------------------")

  a = float(input("Enter the a value:   "))
  b = float(input("Enter the b value:   "))
  c = float(
    input("Enter the c value:   "))  #This part gets an input from user.

  print("---------------------------------")

  answer1 = (-b + (b**2 - 4 * a * c)**0.5) / (
    2 * a)  #By using quaderatic formula, we can get answer 1
  answer2 = (-b - (b**2 - 4 * a * c)**0.5) / (
    2 * a)  #By using quaderatic formula, we can get answer 1

  print("Your equation is ", a, "x^2 +", b, "x +", c, "= 0")

  print("---------------------------------")

  if b * b - 4 * a * c < 0:
    print(
      "No real solution"
    )  #if the decriminat is bellow 0, it has no solution, thus it will print "no real solution"

  elif b * b - 4 * a * c == 0:
    print(
      "There are one real solution ", answer1
    )  #if the decriminat is  0, it has one solution, thus it will print "one real solution"

  elif b * b - 4 * a * c > 0:
    print(
      "There are two real solution. First root is ", answer1,
      "Second root is ", answer2
    )  #if the decriminat bigger than 0, it has two real solution, thus it will print "two real solution"


def cubic():
  print("This will solve equation")
  print("Only ax^3+bx^2+cx+d=0 form and a,b,c,d value should be integer")

  print("---------------------------------")

  a = int(input("Enter the a value:   "))
  b = int(input("Enter the b value:   "))
  c = int(input("Enter the c value:   "))
  d = int(input("Enter the d value:   "))  #This part gets an input from user.

  print("---------------------------------")

  ere = ""
  factorlist1 = [1, -1]
  factorlist2 = [
    1, -1
  ]  #Since there are both + and - value for factor of cubic eqaution, I include 1 and -1.

  for h in range(
      2,
      abs(a) + 1
  ):  #abs means absolute value. I did some reaserch for this. I include abs since a could be both + or -.

    ure = abs(a) % h  #This is the remainder

    if ure == 0:
      factorlist1.append(
        h
      )  #This part will add h and -h value (factor of a) if the remainder is 0, which is a is divisible by h.
      factorlist1.append(-h)

  for x in range(2, abs(d) + 1):
    ere = abs(d) % x

    if ere == 0:
      factorlist2.append(
        x
      )  #This part will add h and -h value (factor of d) if the remainder is 0, which is d is divisible by h.
      factorlist2.append(-x)

    #This part find the factor for a and d value.

  candidate1 = len(factorlist1)
  candidate2 = len(
    factorlist2)  #This part is the number of elements in each list.

  factorlist3 = [0]

  for o in range(0, candidate1):
    for p in range(0, candidate2):
      num = factorlist1[o] / factorlist2[p]

      factorlist3.append(
        num
      )  #This part will divide factor of a by factor of d to get factor of this equation.

  print("Factor of this equation is ", factorlist3)

  #This whole part does the synthetic division part 1.

  print("---------------------------------")

  answer = []  #This list will act like a counter.

  for y in range(0, len(factorlist3)):
    q = factorlist3[y]  #q is just the random number from our factor list.

    if a * q * q * q + b * q * q + c * q + d == 0:
      print("Real root is ", q)
      answer.append(
        1
      )  #if q satisfies this equation, q will be the real root of our cubic equation. And we should add 1 for counter
      print("---------------------------------")

      A = a
      B = a * q + b
      C = a * q * q + b * q + c  #This new A,B,C vaule is a b c value for factorised equation.
      #This whole part does the synthetic division part 2. By doing synthetic division, we could easliy factorise cubic equation.

      print("Factorise result is  ( x +(", q, "))((", A, ")x^2 +(", B, ")x +(",
            C, "))")
      print("---------------------------------")

      answer1 = (-B + (B**2 - 4 * A * C)**0.5) / (
        2 * A)  #By using quaderatic formula, we can get answer 1
      answer2 = (-B - (B**2 - 4 * A * C)**0.5) / (
        2 * A)  #By using quaderatic formula, we can get answer 1

      if B * B - 4 * A * C < 0:
        print("Remaning two roots are not real root")
        break  #if the decriminat is bellow 0, it has no solution, thus it will print "Remaning two roots are not real root"

      elif B * B - 4 * A * C == 0:
        print(
          "There are one real root and one non real root"
        )  #if the decriminat is  0, it has one solution, thus it will print "There are one real root and one non real root"
        answer.append(1)  #This part will add 1 at counter
        print(
          round(answer1, 4)
        )  # To improve readibility, I research about round() funtion to round the number such as 0.66666666...
        break

      elif B * B - 4 * A * C > 0:
        print(
          "There are two real root"
        )  #if the decriminat bigger than 0, it has two real solution, thus it will print "two real solution"
        answer.append(1)  #This part will add 1 at counter
        print(
          round(answer1, 4)
        )  # To improve readibility, I research about round() funtion to round the number such as 0.66666666...
        print(round(answer2, 4))
        break

  if len(answer) == 0:
    print(
      "All of them are not real root."
    )  #if the counter (answer list) has no element, it means there arn't any real solution since this program adds elements to answer list if there are real solution.

    #In addition, these are the example that you can test: 6x^3+22x^2+12x or 6x^3-7x^2-7x+6


print(
  "Which equation do you want to solve?")  #This part prints some information
responce = int(input("1 for linear, 2 for quaderatic and 3 for cubic:    "))
if responce == 1:
  leaner()  #if the user chooses 1, this executes leaner()
elif responce == 2:
  quaderatic()  #if the user chooses 2, this executes quaderatic()
elif responce == 3:
  cubic()  #if the user chooses 3, this executes cubic()

# Starting
from typing import Literal


Num1 = int(input("Input a number: "))


if (Num1 % 2 == 0):
      Calc = Num1 * 3 + 1
      ResultEven = print(f"{Calc}".format(Num1))
      for u in range(1):
          if (ResultEven % 2 != 0):
                      Calc2 = Num1 / 2
                      Result2 = (print(f"{Calc2}".format(ResultEven)))
                      print(Result2)
                      break
      for i in range(1):
       if (ResultEven % 2 == 0):
        Result2 = print(f"{Calc}".format(ResultEven))
        print(Result2)
        break


elif (Num1 % 2 != 0):
      Calc2 = Num1 / 2
      ResultOdd = print(f"{Calc2}".format(Num1))


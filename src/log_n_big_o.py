#
#  time complexity -- big O notation
#
def fun1(n):
   i = n
   print(f"i={i}")
   while i > 0:  # problem size is becoming 50% smaller
      k = 2 + 2
      i = i // 2   # dividing by 2 , making it half
      print(f"i={i}")

fun1(10000)

# log(10000) # base 2
import math

def P(n, k):
  p = math.factorial(n) / math.factorial(n-k)
  return p

def C(n, k):
  c = math.factorial(n) / (math.factorial(n-k)*math.factorial(k))
  return c

u = 0 # May add "t" in case of invalid inputs.

while u == 0:
  total = int(input("Enter total number of instances: "))
  length = int(input("Enter length of permutation or combination: "))
  prompt = input("Select either Permutation or Combination: ")

  if prompt == "P" or prompt == "p":
    name = "Permutation"
    result = P(total, length)
    u += 1

  elif prompt == "C" or prompt == "c":
    name = "Combination"
    result = C(total, length)
    u += 1

print(f"Number of {name} of {total} instances with length {length} is: {result}")

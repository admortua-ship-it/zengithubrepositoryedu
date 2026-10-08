import math

def P(n, k):
  p = math.factorial(n) / math.factorial(n-k)
  return p

def C(n, k):
  c = math.factorial(n) / (math.factorial(n-k)*math.factorial(k))

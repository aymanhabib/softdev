def string_times(str, n):
  return str * n

def front_times(str, n):
  return str[:3] * n

def string_bits(str):
  new = ''
  for i in range(len(str)):
    if i % 2 == 0:
      new += str[i]
  return new

def string_splosion(str):
  new = ''
  for i in range(len(str) + 1):
    new += str[:i]
  return new


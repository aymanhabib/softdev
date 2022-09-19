def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False
  
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not(a_smile) and not(b_smile):
    return True
  else:
    return False
    
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return 2 * (a + b)

def diff21(n):
  if n <= 21:
    return abs(n - 21)
  else:
    return abs(2 * (n - 21))
  
def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
    else:
      return False
  else:
    return False

    return True
  else: 
    return False

def near_hundred(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  else:
    return False

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  return a * b < 0

def not_string(str):
  if str[:3] == 'not':
    return str
  else:
    return 'not ' + str

def missing_char(str, n):
  return str[0:n] + str[n+1: len(str)]

def front_back(str):
  if len(str) <= 1:
    return str
  return str[len(str) - 1:] + str[1:len(str) - 1] + str[:1]

def front3(str):
  return str[:3] * 3


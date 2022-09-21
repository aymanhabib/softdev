def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  else:
    return False
  
sleep_in(False, False) # True
sleep_in(True, False) # False
sleep_in(False, True) # True

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not(a_smile) and not(b_smile):
    return True
  else:
    return False
  
monkey_trouble(True, True) # True
monkey_trouble(False, False) # True
monkey_trouble(True, False) # False
    
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return 2 * (a + b)

sum_double(1, 2) # 3
sum_double(3, 2) # 5
sum_double(2, 2) # 8
  
def diff21(n):
  if n <= 21:
    return abs(n - 21)
  else:
    return abs(2 * (n - 21))

diff21(19) # 2
diff21(10) # 11
diff21(21) # 0
  
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
  
parrot_trouble(True, 6) # True
parrot_trouble(True, 7) # False
parrot_trouble(False, 6) # False

def near_hundred(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  else:
    return False
  
makes10(9, 10) # True
makes10(9, 9) # False
makes10(1, 9) # True

def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  return a * b < 0

pos_neg(1, -1, False) # True
pos_neg(-1, 1, False) # True
pos_neg(-4, -5, True) # True

def not_string(str):
  if str[:3] == 'not':
    return str
  else:
    return 'not ' + str
  
not_string('candy') # 'not candy'
not_string('x') # 'not x'
not_string('not bad') # 'not bad'

def missing_char(str, n):
  return str[0:n] + str[n+1: len(str)]

missing_char('kitten', 1) # 'ktten'
missing_char('kitten', 0) # 'itten'
missing_char('kitten', 4) # 'kittn'

def front_back(str):
  if len(str) <= 1:
    return str
  return str[len(str) - 1:] + str[1:len(str) - 1] + str[:1]

front_back('code') # 'eodc'
front_back('a') # 'a'
front_back('ab') # 'ba'

def front3(str):
  return str[:3] * 3

front3('Java') # 'JavJavJav'
front3('Chocolate') # 'ChoChoCho'
front3('abc') # 'abcabcabc'

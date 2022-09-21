def string_times(str, n):
  return str * n

string_times('Hi', 2) # 'HiHi'
string_times('Hi', 3) # 'HiHiHi'
string_times('Hi', 1) # 'Hi'

def front_times(str, n):
  return str[:3] * n

front_times('Chocolate', 2) # 'ChoCho'
front_times('Chocolate', 3) # 'ChoChoCho'
front_times('Abc', 3) # 'AbcAbcAbc'

def string_bits(str):
  new = ''
  for i in range(len(str)):
    if i % 2 == 0:
      new += str[i]
  return new

string_bits('Hello') # 'Hlo'
string_bits('Hi') # 'H'
string_bits('Heeololeo') # 'Hello'

def string_splosion(str):
  new = ''
  for i in range(len(str) + 1):
    new += str[:i]
  return new

string_splosion('Code') # 'CCoCodCode'
string_splosion('abc') # 'aababc'
string_splosion('ab') # 'aab'

def last2(str):
    last2 = str[-2:]
    return sum(1 for i in range(len(str)-2) if str[i:i+2] == last2)

last2('hixxhi') # 1
last2('xaxxaxaxx') # 1
last2('axxxaaxx') # 2

def array_count9(nums):
    return nums.count(9)

array_count9([1, 2, 9]) # 1
array_count9([1, 9, 9]) # 2
array_count9([1, 9, 9, 3, 9]) # 3

def array_front9(nums):
    return 9 in nums[:4]

array_front9([1, 2, 9, 3, 4]) # True
array_front9([1, 2, 3, 4, 9]) # False
array_front9([1, 2, 3, 4, 5]) # False

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

array123([1, 1, 2, 3, 1]) # True
array123([1, 1, 2, 4, 1]) # False
array123([1, 1, 2, 1, 2, 3]) # True

def string_match(a, b):
    shorter = min(len(a), len(b))
    return sum(1 for i in range(shorter-1) if a[i:i+2] == b[i:i+2])

string_match('xxcaazz', 'xxbaaz') # 3
string_match('abc', 'abc') # 2
string_match('abc', 'axc') # 0

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

def last2(str):
    last2 = str[-2:]
    return sum(1 for i in range(len(str)-2) if str[i:i+2] == last2)

def array_count9(nums):
    return nums.count(9)

def array_front9(nums):
    return 9 in nums[:4]

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

def string_match(a, b):
    shorter = min(len(a), len(b))
    return sum(1 for i in range(shorter-1) if a[i:i+2] == b[i:i+2])


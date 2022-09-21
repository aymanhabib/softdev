def first_last6(nums):
  return(nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
  return(len(nums) >= 1 and (nums[0] == nums[-1]))

def make_pi():
  piList = [3, 1, 4]
  return piList

def common_end(a, b):
  return(a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
  sum = 0
  for x in nums:
    sum += x
  return sum

def rotate_left3(nums):
  first = nums[0]
  last = nums[-1]
  mid = nums[1]
  rotArr = [mid, last, first]
  return rotArr
  
def reverse3(nums):
  return [nums[-1], nums[1], nums[0]]

def max_end3(nums):
  if nums[-1] > nums[0]:
    return [nums[-1], nums[-1], nums[-1]]
  else:
    return [nums[0], nums[0], nums[0]]
    
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
    
def middle_way(a, b):
  return [a[1], b[1]]
  
def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
    return True
  else:
    return False


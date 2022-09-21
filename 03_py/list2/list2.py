def count_evens(nums):
  sum = 0
  for x in nums:
    if x % 2 == 0:
      sum += 1
  return sum

count_evens([2, 1, 2, 3, 4]) # 3
count_evens([2, 2, 0]) # 3
count_evens([1, 3, 5]) # 0

def big_diff(nums):
  return max(nums) - min(nums)

big_diff([10, 3, 5, 6]) # 7
big_diff([7, 2, 10, 9]) # 8
big_diff([2, 10, 7, 2]) # 8

def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  sum = 0
  for x in nums:
    sum += x
  return sum / len(nums)

centered_average([1, 2, 3, 4, 100]) # 3
centered_average([1, 1, 5, 5, 10, 8, 7]) # 5
centered_average([-10, -4, -2, -4, -2, 0]) # -3

def sum13(nums):
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      sum += 0
    elif i == 0 and nums[0] != 13:
      sum += nums[0]
    elif nums[i-1] == 13:
      sum += 0
    else:
      sum += nums[i]
  return sum

sum13([1, 2, 2, 1]) # 6
sum13([1, 1]) # 2
sum13([1, 2, 2, 1, 13]) # 6

def sum67(nums):
    record = True
    total = 0

    for n in nums:
        if n == 6:
            record = False

        if record:
            total += n
            continue

        if n == 7:
            record = True

    return total

sum67([1, 2, 2]) # 5
sum67([1, 2, 2, 6, 99, 99, 7]) # 5
sum67([1, 1, 6, 7, 2]) # 4

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False
  
has22([1, 2, 2]) # True
has22([1, 2, 1, 2]) # False
has22([2, 1, 2]) # False


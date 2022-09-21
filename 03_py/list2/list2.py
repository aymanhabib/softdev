def count_evens(nums):
  sum = 0
  for x in nums:
    if x % 2 == 0:
      sum += 1
  return sum

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  sum = 0
  for x in nums:
    sum += x
  return sum / len(nums)

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

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False



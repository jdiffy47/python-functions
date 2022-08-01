# def sum_to(n):
#   sum = 0
#   for n in range(1, n + 1):
#     sum += n
#   return sum

# print(sum_to(6))


def largest(*nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest


print(largest(2, 4, 6, 10, 150))
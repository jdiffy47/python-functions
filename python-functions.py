# def sum_to(n):
#   sum = 0
#   for n in range(1, n + 1):
#     sum += n
#   return sum

# print(sum_to(6))


# def largest(*args):
#   largest = 0
#   for arg in args:
#     if arg > largest:
#       largest = arg
#   return largest


# print(largest(2, 4, 6, 10, 150))


# def occurrences(str1, str2):
#   return str1.count(str2)


# print(occurrences('Mooo', 'o'))


def product(*args):
  sum = 0
  for arg in args:
    sum = arg * arg
  return sum

print(product(2, 2))
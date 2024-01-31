def linear_search(source, value):
    result = None
    for (i, val) in enumerate(source):
        if value == val:
            result = i
            break

    return result


def binary_search(source, value):
  left = 0
  right = len(source) - 1

  while left < right:
    middle = (right + left) // 2

    if value > source[middle]:
      left = middle + 1
    elif value < source[middle]:
      right = middle - 1
    else:
      return middle

  return None

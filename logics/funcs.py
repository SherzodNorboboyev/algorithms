def factorial(n: int=1):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def ekub(a, b):
    if a > b:
        mod = a % b
        if mod == 0:
            return b
        else:
            return ekub(b, mod)
    else:
        return ekub(b, a)

def sum_list(data: list):
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        return data[0]
    else:
        return data[0] + sum_list(data[1:])

def count_list(data: list):
    if len(data) == 0:
        return 0
    elif len(data) == 1:
        return 1
    else:
        return 1 + count_list(data[1:])

def max_list(data: list):
    if len(data) == 0:
        return None
    elif len(data) == 1:
        return data[0]
    else:
        next_max = max_list(data[1:])
        return data[0] if data[0] > next_max else next_max

def binary_search():
    # for simple solution no idea in recursion
    pass

if __name__ == '__main__':
    print(max_list([5,32,12,22]))
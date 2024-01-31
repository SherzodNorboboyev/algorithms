# from search.search import linear_search, binary_search
# from sort.sort import selection_sort

# def user_enter_value(source):
#     while True:
#         try:
#             value = input(f'Enter value among {source}: ')
#             value = int(value)
#         except ValueError:
#             print('Please enter only source value or any integer. try again')
#         else:
#             return value

def foo(start, stop, step):
    for i in range(start, stop, step):
       print(i)
elems = [1,5,2]
foo(*elems)
# or
elems = {'start': 1, 'stop': 5, 'step': 2}
foo(**elems)


# if __name__ == '__main__':
#     # while True:
#     #     source = [1,3,4,6,7,8,10,12,23,45,56,78,99]
#     #     user_value = user_enter_value(source=source)

#     #     ind = binary_search(source=source, value=user_value)

#     #     print(f'Index of {user_value} is {ind}')

#     #     answer = input('Continue (y/n): ').lower()

#     #     if answer != 'y':
#     #         break

#     data = [10, 6, 7, 10, 7, 3]
#     print(selection_sort(data=data))






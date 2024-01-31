from datetime import date
def suffix_array(text: str) -> list:
    source = list(text + '$')

    n = len(source)
    p = []
    c = []

    # k - 0
    a = []
    for i in range(n):
        a.append((source[i], i))
        p.append(0)
        c.append(0)
    a.sort()

    for i in range(n):
        p[i] = a[i][1]

    c[p[0]] = 0

    for i in range(1, n):
        if a[i][0] == a[i - 1][0]:
            c[p[i]] = c[p[i - 1]]
        else:
            c[p[i]] = c[p[i - 1]] + 1

    # k -> k + 1
    k = 0

    while ((1 << k) < n):
        a = []

        for i in range(n):
            a.append(((c[i], c[(i + (1 << k)) % n]), i))

        a.sort()

        for i in range(n):
            p[i] = a[i][1]

        c[p[0]] = 0
        for i in range(1, n):
            if a[i][0] == a[i - 1][0]:
                c[p[i]] = c[p[i - 1]]
            else:
                c[p[i]] = c[p[i - 1]] + 1

        k += 1

    # for i in range(n):
    #     print(f'{p[i]} -> {''.join(source[p[i]:])}')

    return p

if __name__ == '__main__':
    src = input('')
    result = suffix_array(src)
    [print(val, end=' ') for val in result[:-1]]
    print(result[-1])
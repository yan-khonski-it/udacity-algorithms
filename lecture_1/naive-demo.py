import time


# 1 operation 1.26 seconds for 2 ^ 24
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z


# Faster version of naive. 1 000 000 operations 2.5 seconds for 2 ^ 24
def naive_improved(a, b):
    res = 0
    if a == 0 or b == 0:
        return 0

    if a == 1:
        return b

    if b == 1:
        return a

    if a < b:
        return naive_improved(b, a)

    a_times = a
    b_times = 1
    while True:
        if b_times + b_times <= b:
            a_times = a_times + a_times
            b_times = b_times + b_times
        else:
            break

    return a_times + naive_improved(a, b - b_times)


# 1 000 000 operations - 0.1 second
def a_times_b(a, b):
    return a * b


powers_2_size = 25

print('naive(3, 5)')
i = 0


def build_powers_2():
    res = [None] * powers_2_size
    for i in range(0, powers_2_size):
        res[i] = 2 ** i
    return res


def calculate_powers_2():
    powers_2_array = build_powers_2()
    print(powers_2_array)
    for pow2 in powers_2_array:
        start = time.time()
        res = naive(pow2, pow2)
        end = time.time()
        total = end - start
        print(str(pow2) + ' ' + str(total) + ' ' + str(res))


def main():
    calculate_powers_2()


if __name__ == "__main__":
    main()

def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res > 1:
            for i in range(2, int(res)):
                if (res % i) == 0:
                    print('Составное')
                    break
            else:
                print('Простое')
        return res

    return wrapper



@is_prime
def sum_three(*args):
    return sum(args)
result = sum_three(2, 3, 6)
print(result)
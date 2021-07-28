from time import time

repeat_in_range = 100

def time_decorator(func):
    def time_wrapper(*args):
        start_time = time()
        for i in range(repeat_in_range):
            func(*args)
        print(f'Czas wykonania funkcji {func} to: {time() - start_time}')
    return time_wrapper


@time_decorator
def palindrome(text):
    if text == text[::-1]:
        print(f'{text} to palindrom')
    else:
        print(f'{text} to nie palindrom')


@time_decorator
def palindrome_v2(text):
    i = 0
    is_palindrome = True
    while i < len(text):
        if text[i] != text[-i - 1]:
            is_palindrome = False
            break
        i += 1

    print(f'{text} to palindrom') if is_palindrome else print(f'{text} to nie palindrom')


palindrome('ala')
palindrome('ala2')

palindrome_v2('ala')
palindrome_v2('ala2')

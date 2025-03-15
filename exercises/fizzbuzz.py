def fizz_buzz(n):
    # fizzbuzz list
    fizzbuzz_ls = []

    for num in range(1, n+1):
        if num % 15 == 0:
            fizzbuzz_ls.append("fizzbuzz")
        elif num % 3 == 0:
            fizzbuzz_ls.append("fizz")
        elif num % 5 == 0:
            fizzbuzz_ls.append("buzz")
        else:
            fizzbuzz_ls.append(num) 

    return fizzbuzz_ls
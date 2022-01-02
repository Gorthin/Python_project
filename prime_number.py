for candidate in range(2,31):
    for divider in range(2, candidate):
        if candidate % divider == 0:
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break
    else:
        print("%2d is prime" % (candidate))
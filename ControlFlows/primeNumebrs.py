def prime_numbers_in_range(start, end):
    prime_numbers = []
    for i in range(start, end+1):
        if(i==0 or i==1):
            continue

        sqrt = int(i**0.5)
        print('i---',i,'-------- sqrt++++++', sqrt)
        has_divider = False
        for j in range(2, sqrt+1):
            print('j------------', j)

            if (i%j == 0):
                has_divider=True
                break

            if j > sqrt:
               break

        if has_divider == False:
            prime_numbers.append(i)
    print('Primes in range ', start ,'- ', end, ' = ', prime_numbers)

prime_numbers_in_range(0,60)
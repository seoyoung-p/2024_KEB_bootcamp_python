#메뉴 1번 섭씨 화씨 / 2번 화씨 섭씨 / 3번 소수 판정 메뉴 추가 / 4번 구간 소수 구하는 메뉴
while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) prime number   "
                 "4) prime number interval    5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    elif menu =='3':
        # prime number
        number = int(input("Input number : "))
        is_prime = True
        if number < 2:
            pass
        else:
            i = 2
            while i < number:
                if number % i == 0:
                    is_prime = False
                    break
                i = i + 1
            if is_prime:
                print(f'{number} is prime number')
            else:
                print(f'{number} is NOT prime number!')
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            is_prime = True

            if number < 2:
                continue
            else:
                for i in range(2, number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime: print(number, end=' ')
        print()
    elif menu == '5':
        print('Terminate Program.')
        break


#연습문제 6.1
for x in range(3,-1,-1):
    print(x)

#연습문제 6.2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break
    number += 1

# 연습문제 6.3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break
    number += 1
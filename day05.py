#prime number
def isprime(n) -> bool:
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean타입으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True, 소수가 아니면 False
    """
    is_prime = True

    if n < 2:
        return False
    else:
        i = 2
        while i*i <= number:
            if number % i == 0:
                is_prime = False
                break
            i +=1
        return True

help(isprime) #함수에 대한 설명 출력

numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2 + 1):
    if isprime(number):
        print(number, end=' ')
print()



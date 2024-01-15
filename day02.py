# (100℉ - 32) * 5/9 = 3.778℃
# (0°C × 9/5) + 32 = 32°F

menu = input("1) Fahrenheit -> Celsius  2) Fahrenheit -> Celsius  3) Quit program : ")

if menu =='1':
    fahrenheit = float(input('Input Fahrenheit : '))
    print(
        f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    # .2f로 소수점 2번쨰자리까지 출력 (f스트링 서식)
elif menu == '2':
    celsius = float(input('Input Celsius : '))
    print(f'celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
else:
    print('Terminate Program.')

# temp = [0]
# temp = []
# if empty list
# if temp:
#     print("원소가 존재하는 리스트")
# else:
#     print("비어있는 리스트")

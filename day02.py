# (100℉ - 32) * 5/9 = 3.778℃
fahrenheit = float(input('Input Fahrenheit : '))
print(f'fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0/9.0):.2f}C')
#.2f로 소수점 2번쨰자리까지 출력 (f스트링 서식)

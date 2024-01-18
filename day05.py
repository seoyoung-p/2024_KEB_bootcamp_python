#연습문제 9.1
def good():
    return ['Henry', 'Ron', 'Hermione']

print(good())

#연습문제 9.2
def get_odd():
     num_list = [n for n in range(10) if n % 2 == 1]
     return num_list[2]

print(get_odd())

#연습문제 9.3
def trance(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, 'start')
        result = func(*args, **kwargs)
        print(func.__name__, 'end')
        return result
    return wrapper
@trance
def test1():
    print("함수를 실행하였습니다")

test1()



#연습문제 8.1
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
#연습문제 8.2
print(e2f.get("walrus"))
#연습문제 8.3
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
#연습문제 8.4
print(f2e.get("chien"))
#연습문제 8.5
print(e2f.values())
#연습문제 8.6
life = {'animals' : {'cats':['Henri', 'Grumpy', 'Lucy'], 'octopi':{}, 'cmus':{}},'plants' : {},'other':{} }
#연습문제 8.7
print(life.keys())
#연습문제 8.8
print(life['animals'].keys())
#연습문제 8.9
print(life['animals']['cats'])
#연습문제 8.10
squares = {key:key*key for key in range(10)}
print(squares)



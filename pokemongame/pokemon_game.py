import random

import pokemon

player = int(input('플레이어 포켓몬을 골라주세요 : \n 1)피카츄 2)꼬북이 3)파이리   '))
while True:
    if player == 1:
        player = pokemon.Pikachu
        break
    elif player == 2:
        player = pokemon.Squirtle
        break
    elif player == 3:
        player = pokemon.Charmander
        break
    else :
        print("입력 값이 잘못되었습니다.")
        break

target = player
while (target == player):
    target = random.choice([pokemon.Squirtle(), pokemon.Pikachu(), pokemon.Squirtle(), pokemon.Charmander(), pokemon.Slowbro()])
    print(f'야생의 {target.name}이(가) 나타났습니다.')
    break;

print("포켓몬 게임을 시작합니다.")
menu = input('menu 1) 공격  2) 도망  3) 진화  4) 종료 : ')

while (target.hp or player <= 0):
    if menu == 1:
        print()
        skill = input('공격을 선택해주세요 : ')
        player.attack(target, skill)


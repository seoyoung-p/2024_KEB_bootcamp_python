import random
import pokemon

player = int(input('포켓몬 게임을 시작합니다! 어느 포켓몬을 데려가시겠습니까? \n 1)피카츄 2)꼬북이 3)파이리'))

while True:
    if player == 1:
        player = pokemon.Pikachu()
        print(f'당신의 포켓몬은 {player.name} 입니다')
        break
    elif player == 2:
        player = pokemon.Squirtle()
        print(f'당신의 포켓몬은 {player.name} 입니다')
        break
    elif player == 3:
        player = pokemon.Charmander()
        print(f'당신의 포켓몬은 {player.name} 입니다')
        break
    else :
        print("입력 값이 잘못되었습니다.")
        break


def target_maker():
    target = random.choice([pokemon.Squirtle(), pokemon.Pikachu(), pokemon.Squirtle(), pokemon.Charmander(), pokemon.Slowbro()])
    print(f'야생의 {target.name}이(가) 나타났습니다.')
    return target

target = target_maker()

while True :
    print("포켓몬 게임을 시작합니다.")
    menu = input('menu 1) 공격  2) 도망  3) 진화  4) 종료 : ')
    if menu == '1':
        player_skill = list(player.skills.keys())
        print(player_skill)
        skill = input('공격을 골라 입력해주세요 : ')
        player.attack(target, skill)
        break
    if menu == '2':
        print("상대할 수 없는 적이 나타났습니다. 후퇴합니다!")
        target_maker()
    if menu == '3':
        pass
    if menu == '4':
        print("게임을 종료합니다.")







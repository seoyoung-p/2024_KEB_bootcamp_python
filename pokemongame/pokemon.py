from random import random


class Pokemon():
    def __init__(self, name, hp, attack_rate, defence_rate):
        self.name = name
        self.hp = hp
        self.attack_rate = attack_rate
        self.defence_rate = defence_rate
    def attack(self, target, skill):
        attack_start = self.attack_rate + self.skills.get(skill) - target.defence_rate
        target.hp -= attack_start
        print(f'{self.name}이(가) {skill}을(를) {target.name}에게 시전!')
        if target.hp > 0 :
            print(f'{target.name}의 hp가 {target.hp} 입니다')
        else :
            print(f'{target.name}이 사망하였습니다.')

    def evolve(self):
        can_evolve = int(random()*3)+1
        print(can_evolve)
        if can_evolve == 2 :
            self.hp = self.hp * 1.2
            self.attack_rate = self.attack_rate * 1.2
            print(f'{self.name}이 {self.new_name}으로 진화하였습니다. 공격력과 hp가 1.2배 상승하였습니다.')
            self.name = self.new_name
        else :
            print("진화에 실패하였습니다 ㅠㅠ 다음에 다시 시도해주세요.")


class Pikachu(Pokemon):
    def __init__(self):
        self.name = "피카츄"
        self.hp = 35
        self.attack_rate = 55
        self.defence_rate = 40
        self.skills = {"정전기":10, "백만볼트":20, "피뢰침":30}
        self.new_name = "라이츄"

class Slowbro(Pokemon):
    def __init__(self):
        self.name = "야도란"
        self.hp = 95
        self.attack_rate = 75
        self.defence_rate = 110
        self.skills = {"물대포":10, "열탕":25, "파도타기":40}
        self.new_name = "슈퍼야도란"

class Charmander(Pokemon):
    def __init__(self):
        self.name = "파이리"
        self.hp = 39
        self.attack_rate = 52
        self.defence_rate = 43
        self.skills = {"불꽃세례":10, "화염방사":20, "불꽃튀기기":30}
        self.new_name = "리자몽"

class Squirtle(Pokemon):
    def __init__(self):
        self.name = "파이리"
        self.hp = 44
        self.attack_rate = 48
        self.defence_rate = 65
        self.skills = {"물대포":10, "급류":20, "하이드로캐논":30}
        self.new_name = "어니부기"
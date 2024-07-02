import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Супер компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print(f"Начало игры: {self.player.name} против {self.computer.name}")
        while self.player.is_alive() and self.computer.is_alive():
            if not self.player_turn():
                print(f"{self.player.name} решил убежать. Игра окончена.")
                break
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден!")
                break
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} побежден!")
                break
        self.display_winner()

    def player_turn(self):
        action = input("Ваш ход! Введите 1 для атаки или 2 для побега: ")
        if action == '1':
            damage = self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name} и наносит {damage} урона.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            return True
        elif action == '2':
            return False
        else:
            print("Неверный выбор, попробуйте снова.")
            return self.player_turn()

    def computer_turn(self):
        damage = self.computer.attack(self.player)
        print(f"{self.computer.name} атакует {self.player.name} и наносит {damage} урона.")
        print(f"У {self.player.name} осталось {self.player.health} здоровья.")

    def display_winner(self):
        if self.player.is_alive() and not self.computer.is_alive():
            print(f"{self.player.name} побеждает!")
        elif self.computer.is_alive() and not self.player.is_alive():
            print(f"{self.computer.name} побеждает!")
        elif not self.player.is_alive() and not self.computer.is_alive():
            print("Оба героя погибли. Ничья!")
        else:
            print("Игра завершена без победителя.")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()

    print("Конец игры.")
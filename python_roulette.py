## Kieran Fane - Own Class
"""Creating a Russian Roulette program"""
from random import randint
from time import sleep

# A list of the Users savedn as a Users class. 
## Also has the saved value of numbers of users and differnet specific getters

class Users:
    def __init__(self, num_of_users):
        self._num_of_users = num_of_users
        self._user_list = []

    def get_num_of_users(self):
        return self._num_of_users

    def set_num_of_users(self, num):
        self._num_of_users = num

    def get_user_list(self):
        return self._user_list

    def get_user(self, pos):
        return self._user_list[pos]

    def add_user(self,name):
        self._user_list.append(name)
        
    def remove_user(self,name):
        self._user_list.remove(name)

# A object that emulates the gun in russian roulette.
## Has the number of chambers, number of bullets, the ammount of bullets in the gun, and a list that places the bullets in the chamber. 
#You can fill the gun and expell bullets when you shoot. 

class Firearm:
    def __init__(self, num_of_bullets, chambers = 6):
        self._chambers = chambers
        self._ammo = num_of_bullets
        self._bullet_list = [False] * chambers
        self._ammo_in_gun = 0

    def fill_gun(self):
        chamber_round_list = []
        while self._ammo > 0:
            current_chamber = randint(0,len(self._bullet_list)-1)
            if current_chamber not in chamber_round_list:
                chamber_round_list.append(current_chamber)
                self._bullet_list[current_chamber] = True
            self._ammo -= 1
            self._ammo_in_gun +=1

    def add_ammo(self, ammount):
        self._ammo = ammount

    def get_ammo(self):
        ammo=self._ammo_in_gun
        return ammo

    def expell_one_bullet(self):
        self._ammo_in_gun -= 1
    
    def get_bullet_list(self):
       return self._bullet_list

    def shoot(self,bullet_list):
        randpos = randint(0,self._chambers-1)
        print(randpos)
        bullet = bullet_list[randpos]
        self._bullet_list[randpos] = False
        return bullet

# Main Function that runs the game.
def main():
    users = Users(0)
    gun = Firearm(0)
    # While loop to take number of users that the player would like to participtate. 
    while True:
        num_of_users = input(f"\t\t> Hello! How many players are playying?(2-5): ")
        try:
            num_of_users = int(num_of_users)
            if num_of_users > 5:
                print()
                print("Too many users, must have less than 5.")
                print("..")
                print("...")
                continue
            elif num_of_users < 2:
                print()
                print("Not enough users, must have at least 2.")
                print("..")
                print("...")
                continue
            else:
                users.set_num_of_users(num_of_users)
                break
        except ValueError:
            print()
            print("Must be of int value.")
            print("..")
            print("...")

    # While loop to take the number of bullets the user would like to emmulate.
    while True:
        num_of_bullets = input(f"\t\t> Alright! How many bullets are we using?(Min: 1, Max: {num_of_users} - 1): ")
        try:
            num_of_bullets = int(num_of_bullets)
            if num_of_users <= num_of_bullets:
                print()
                print("\t\tToo many bullets, must have less than the number of users.")
                print("..")
                print("...")
                continue
            elif num_of_bullets < 1:
                print()
                print("\t\tNot enough bullets, must have at least 1.")
                print("..")
                print("...")
                continue
            else:
                gun.add_ammo(num_of_bullets)
                break
        except ValueError:
            print()
            print("\t\tMust be of int value.")

    # Fill the gun with the ammount of ammo randomly.
    gun.fill_gun()

    # While loop to take user input of name of the players.
    i =0
    while i < num_of_users:
        new_user = input(f"\t\t> Input user ({i+1}) name: ")
        print()
        users.add_user(new_user)
        i+=1

    # While loop to run the game until you run out of ammo or play 39 rounds.
    ## Survivors are displayed at the end.
    i = 0
    ammo_in_gun = gun.get_ammo()
    count = 0
    while ammo_in_gun > 0 and count != 40:
        bullet_list = gun.get_bullet_list()
        print(bullet_list)
        print("---------")
        print(ammo_in_gun)
        user_list = users.get_user_list()
        print("\t\t>Spinning the gun to see who goes...")
        sleep(4)
        print("...")
        sleep(2)
        print("..")
        user_in_turn = user_list[randint(0, len(user_list)-1)]

        print()
        print(f"\t\t>User: {user_in_turn} turn..")
        sleep(2)

        result = gun.shoot(bullet_list)
        if result:
            print("\t\t ***BANGG*** ")
            print()
            sleep(3)
            print(f"User {user_in_turn} has been eliminated.")
            print()
            users.remove_user(user_in_turn)
            gun.expell_one_bullet()
        else:
            print("\t\t ***CLICK*** ")
            print()
            sleep(3)
            print(f"\t\tUser {user_in_turn} has been spared.")
            print()
            print()

        print(f"\t\t>Next turn loading")
        sleep(1)
        print("..")
        sleep(2)
        print("...")
        ammo_in_gun = gun.get_ammo()
        print(ammo_in_gun)
        count+=1

    print()
    print()
    print("Survivor(s): ")
    survivors = users.get_user_list()
    for i in survivors:
        print(i)
        
if __name__ == "__main__":
    main()    



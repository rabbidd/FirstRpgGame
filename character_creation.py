import config
import game_save

class Gladiator():
    health = 1
    strength = 1
    armor = 1
    level = 1
    experience = 1

    def create_character(self):

        print("Let's create a character")

        config.hero_base_level = "1"
        ''' choose gender '''
        print("Are you male or female?")
        config.hero_gender = input(">>")
        if config.hero_gender == "male":
            print("Flex them muscles and get ready to fight!")
        elif config.hero_gender == "female":
            print("Sharpen those nails, you are gonna need them!")
        else:
            print("Please choose male or female.")
            return

        ''' choose class '''
        print("Choose a class.")
        hero_class_array = ["warrior", "mage", "monk"]
        print(hero_class_array)
        config.hero_class = input(">")
        game_save.save_game_settings()


        return
import config
import game_save

def create_character():

    print "Let's create a character"

    config.hero_base_level = "1"
    ''' choose gender '''
    print "Are you male or female?"
    config.hero_gender = raw_input(">>")
    if config.hero_gender == "male":
        print "Flex them muscles and get ready to fight!"
    elif config.hero_gender == "female":
        print "Sharpen those nails, you are gonna need them!"
    else:
        print "Please choose male or female."
        return

        ''' choose class '''

    print "Choose a class."
    hero_class_array = ["warrior", "mage", "monk"]
    print hero_class_array
    config.hero_class = raw_input(">")
    game_save.save_game_settings()


    return

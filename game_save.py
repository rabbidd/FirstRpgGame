import config



def save_game_settings():
    print("Opening the file...")
    target = open("saves\save1.txt", 'w')
    target.truncate()

    print("Writing gender")
    target.write(config.hero_gender)
    target.write("\n")

    print("Writing class")
    target.write(config.hero_class)
    target.write("\n")

    print("Writing level")
    target.write(config.hero_base_level)
    

    print("closing save file")
    target.close()

    return

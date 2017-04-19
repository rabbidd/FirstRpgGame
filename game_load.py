import config



def load_game_settings():
    save_file_elements = []
    with open('saves//save1.txt') as savefile:
        for line in savefile:
            save_file_elements.append(line.rstrip("\n"))


    config.hero_gender = save_file_elements[0]
    config.hero_class = save_file_elements[1]
    config.hero_base_level = save_file_elements[2]


    savefile.close()
    #close('saves//save1.txt')
    #raw_input()

    return

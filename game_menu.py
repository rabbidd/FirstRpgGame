import character_creation
import config
import game_load


def gamemenu():
    main_menu_choice = "0"
    while main_menu_choice < "3":
        print("Main Menu")
        print("1. New Game\n")
        print("2. Load Game\n")
        print("3. Exit\n")
        print("Please make a choice!")
        main_menu_choice = input(">>")
        print(main_menu_choice)


        if main_menu_choice == "1":
            character_creation.create_character()
            "Now to start the game"
        elif main_menu_choice == "2":
            print("Feature in progress")
            game_load.load_game_settings()
            print("I am a %r %r !!!\nMy level is %s and i am ready to enter the arena!" % (config.hero_gender, config.hero_class, config.hero_base_level))

            print("Now to start the game")
        else:
            print("bye")
            exit(0)

    return

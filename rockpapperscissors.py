import random


def wrong_answer():
    answer_types = ['rock', 'paper', 'scissor']
    ai_answer = random.choice(answer_types)
    play_again = "maybe"
    player_choice = (input("Rock, paper, or scissor?: ")).lower()
    if player_choice == ai_answer:
        print("The computer gave " + ai_answer + ". It's a tie!")


        def answer_type1():
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
            elif play_again == "no":
                print("Thanks for playing! Hope you enjoyed it.")
            else:
                print("Looks like you didn't answer properly. Please say\" yes\" or \"no\"!")
                answer_type1()

        answer_type1()

    elif player_choice == "rock":
        if ai_answer == "scissor":
            print("The computer gave " + ai_answer + ". You won!")
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
        if ai_answer == "paper":
            print("The computer gave " + ai_answer + ". Uh oh. You're the loser!")
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
    elif player_choice == "paper":
        if ai_answer == "rock":
            print("The computer gave " + ai_answer + ". You won!")
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
        if ai_answer == "scissor":
            print("The computer gave " + ai_answer + ". Uh oh. You're the loser!")
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
    elif player_choice == "scissor":
        if ai_answer == "paper":
            print("The computer gave " + ai_answer + ". You won!")
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
        if ai_answer == "rock":
            print("The computer gave " + ai_answer + ". Uh oh. You're the loser!")
            play_again = input("want to play again?: yes or no? ").lower()
            if play_again == "yes":
                wrong_answer()
    elif player_choice != "rock":
        if player_choice != "paper":
            if player_choice != "scissor":
                print("Please input a valid answer! The choices are \"rock\", \"paper\", or \"scissor\"!")
                wrong_answer()
            else:
                print("Calculating...")
                print(player_choice)
        else:
            print("Calculating...")
            print(player_choice)
    else:
        print("Calculating...")
        print(player_choice)


wrong_answer()

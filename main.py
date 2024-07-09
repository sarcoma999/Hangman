import random


def handle_try(sel_word: str, user_word: list, symbol: str) -> str:
    for i, char in enumerate(sel_word):
        if char == symbol:
            user_word[i] = symbol
    result = "".join(user_word)
    return result


def is_win(sel_word: list, user_word: str) -> bool:
    return str(sel_word) == user_word


def read_file() -> list:
    with open('words.txt', 'r') as file:
        words = file.readlines()
        words = [word.rstrip('\n') for word in words]
    return words


def main():
    print("\n********Welcome to Hangman by sarcoma999!********\n\n")
    words_list = read_file()
    random_word = random.choice(words_list)
    user_word = ["?" for s in random_word]
    new_user_word = ""
    print(str(user_word))
    is_game_over = False
    tries = len(random_word) + 10
    print("You have " + str(tries) + " tries.")
    for i in range(1, tries + 1):
        print("Try №", i)
        user_symbol = input("\nEnter your guess: ")
        new_user_word = handle_try(str(random_word), user_word, user_symbol)
        print(user_word)
        if is_win(random_word, new_user_word):
            print("Congratulations! You win!")
            return
    print("All tries! Game Over :(\nThe word was " + random_word)


if __name__ == "__main__":
    main()

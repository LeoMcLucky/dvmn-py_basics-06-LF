def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def is_very_long(password):
    total = len(password) >= 12
    return total


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(
        not letter.isalpha() and not letter.isdigit() for letter in password)


def main():

    my_pwd = input("Введите пароль: ")

    def_list = [
        has_digit(my_pwd),
        is_very_long(my_pwd),
        has_lower_letters(my_pwd),
        has_upper_letters(my_pwd),
        has_symbols(my_pwd)
    ]

    score = 0
    for single_def in def_list:
        if single_def:
            score = score + 2

    print(score)


if __name__ == '__main__':
    main()

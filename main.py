import random


def random_game():
    with open('Answers.txt', 'r') as answers:
        answers = answers.readlines()
        for i in range(len(answers)):
            answers[i] = answers[i].rstrip('\n')
    bot_main_number = random.randint(0, 999)
    attempts = 10
    number_list = [i for i in range(1000)]
    print(bot_main_number)
    while attempts >= 1:
        attempts -= 1
        bot_random_number = random.choice(number_list)
        while bot_random_number == bot_main_number:
            bot_random_number = random.choice(number_list)
        print(answers[0], bot_random_number)
        print(answers[1], end='')
        prediction = input()

        while True:
            if type(prediction) == str and prediction in ['up', 'down']:
                break
            else:
                try:
                    prediction = int(prediction)
                    break
                except Exception:
                    print(answers[2], end='')
                    prediction = input()

        if prediction in ['up', 'down']:
            if prediction == 'up' and bot_random_number < bot_main_number:
                number_list = [i for i in range(bot_random_number, number_list[len(number_list) - 1])]
                print(f'{answers[3]}{number_list[0]}{answers[4]}{number_list[len(number_list) - 1]}')

            elif prediction == 'down' and bot_random_number > bot_main_number:
                number_list = [i for i in range(number_list[0], bot_random_number)]
                print(f'{answers[3]}{number_list[0]}{answers[4]}{number_list[len(number_list) - 1]}')

            else:
                print(answers[5])

        elif type(prediction) == int:
            l1 = int(bot_main_number - ((0.01 * attempts) * (len(number_list)) // 2))
            l2 = int(bot_main_number + ((0.01 * attempts) * (len(number_list)) // 2))

            if prediction == bot_main_number:
                print(answers[6])
                break

            elif prediction in [i for i in range(l1, l2)]:
                print(answers[7])
                break

            else:
                print(answers[8])
                attempts -= 1

        else:
            print(answers[9])
    else:
        print('\n', answers[10])


if __name__ == '__main__':
    random_game()
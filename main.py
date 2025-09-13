
# import
import random

# deklaracija pocetnih vrijednosti
programing_lenguages = ['Python', 'Java', 'C#', 'Javascript', 'Typescript', 'Golang', 'Rust', 'Lua']
movies = ['Forrest Gump', 'The Lord of the Rings', 'Star Wars', 'Intersteler', 'Fast and furious', 'Hitch', 'Men in black', 'Deadpool']
sports = ['Football', 'Tennis', 'Basketball', 'Volleyball', 'Handball', 'Baseball', 'Golf', 'Swimming']
celebrities = ['Leonardo DiCaprio',  'Brad Pitt', 'Jhonny Depp', 'Tom Cruise', 'Will Smith', 'Nicolas Cage', 'Bruce Willis', 'Denzel Washington']
languages = ['Italian',  'Spanish', 'Croatian', 'French', 'German', 'Slovenian', 'Turkish', 'Polish']

selected_language_index = random.randint(0, 7)
counter = 0

print('Welcome to the guessing game!')
print()

# glavni dio aplikacije
while True:  # petlja za odabir teme
    print()
    print()
    print('P - programing languages')
    print('M - movies')
    print('S - sports')
    print('C - celebrities')
    print('L - languages') 
    print()
    print()
    users_topic = input('Choose the topic you want to guess: ')


    while True:  # petlja za igru
        if users_topic.upper() == 'P':
            randomly_selected_item = programing_lenguages[selected_language_index]
            #print(randomly_selected_item)  # za test
            if 3 <= counter <= len(randomly_selected_item) + 2:
                hint_length = counter - 2  # broj slova raste sa counter-om, ali max do dužine rijeci
                print(f"HINT - {randomly_selected_item[:hint_length]}")
            elif counter > len(randomly_selected_item) + 2:
                print("That's all I can do...")
            print()

            user_guess = input('Guess the name of the programming language:' )
            counter += 1

            if user_guess.lower() == programing_lenguages[selected_language_index].lower():   # Ako korisnik pogodi
                print(f'Congratulations!! You guessed the programming language on your {counter}th attempt. ')
                counter = 0   # resetiram brojac
                selected_language_index = random.randint(0, 7)  # izaberemo random programm ponovno ako korisnik opet zeli igrati
                print()

                next_round = input('Would you like to try again with another topic? (Yes/No): ') 
                if next_round.lower() == 'no':  # izlazim iz druge petlje
                    break
                elif next_round.lower() == 'yes':  # ulazimo u prvu petlju gdje korisnik bira koju igru zeli
                    break
            else:
                print("Unfortunately, you didn't guess! Please try again. ")



        elif users_topic.upper() == 'M':
            randomly_selected_item = movies[selected_language_index]
            #print(randomly_selected_item)  # za test
            if 3 <= counter <= len(randomly_selected_item) + 2:
                hint_length = counter - 2  # broj slova raste sa counter-om, ali max do dužine rijeci
                print(f"HINT - {randomly_selected_item[:hint_length]}")
            elif counter > len(randomly_selected_item) + 2:
                print("That's all I can do...")
            print()

            user_guess = input('Guess the name of the movie:' )
            counter += 1

            if user_guess.lower() == movies[selected_language_index].lower():   # Ako korisnik pogodi
                print(f'Congratulations!! You guessed the movie on your {counter}th attempt. ')
                counter = 0   # resetiram brojac
                selected_language_index = random.randint(0, 7)  # izaberemo random programm ponovno ako korisnik opet zeli igrati
                print()

                next_round = input('Would you like to try again with another topic? (Yes/No): ')
                if next_round.lower() == 'no':  # izlazim iz druge petlje
                    break
                elif next_round.lower() == 'yes':  # ulazimo u prvu petlju gdje korisnik bira koju igru zeli
                    break
            else:
                print("Unfortunately, you didn't guess! Please try again. ") 



        elif users_topic.upper() == 'S':
            randomly_selected_item = sports[selected_language_index]
            #print(randomly_selected_item)  # za test
            if 3 <= counter <= len(randomly_selected_item) + 2:
                hint_length = counter - 2  # broj slova raste sa counter-om, ali max do dužine rijeci
                print(f"HINT - {randomly_selected_item[:hint_length]}")
            elif counter > len(randomly_selected_item) + 2:
                print("That's all I can do...")
            print()

            user_guess = input('Guess the name of the sport :' )
            counter += 1

            if user_guess.lower() == sports[selected_language_index].lower():   # Ako korisnik pogodi
                print(f'Congratulations!! You guessed the sport on your {counter}th attempt. ')
                counter = 0   # resetiram brojac
                selected_language_index = random.randint(0, 7)  # izaberemo random programm ponovno ako korisnik opet zeli igrati
                print()

                next_round = input('Would you like to try again with another topic? (Yes/No): ')
                if next_round.lower() == 'no':  # izlazim iz druge petlje
                    break
                elif next_round.lower() == 'yes':  # ulazimo u prvu petlju gdje korisnik bira koju igru zeli
                    break
            else:
                print("Unfortunately, you didn't guess! Please try again. ")



        elif users_topic.upper() == 'C':
            randomly_selected_item = celebrities[selected_language_index]
            #print(randomly_selected_item)  # za test
            if 3 <= counter <= len(randomly_selected_item) + 2:
                hint_length = counter - 2  # broj slova raste sa counter-om, ali max do dužine rijeci
                print(f"HINT - {randomly_selected_item[:hint_length]}")
            elif counter > len(randomly_selected_item) + 2:
                print("That's all I can do...")
            print()

            user_guess = input('Guess the name of the celebritie:' )
            counter += 1

            if user_guess.lower() == celebrities[selected_language_index].lower():   # Ako korisnik pogodi
                print(f'Congratulations!! You guessed the celebritie on your {counter}th attempt. ')
                counter = 0   # resetiram brojac
                selected_language_index = random.randint(0, 7)  # izaberemo random programm ponovno ako korisnik opet zeli igrati
                print()

                next_round = input('Would you like to try again with another topic? (Yes/No): ')
                if next_round.lower() == 'no':  # izlazim iz druge petlje
                    break
                elif next_round.lower() == 'yes':  # ulazimo u prvu petlju gdje korisnik bira koju igru zeli
                    break
            else:
                print("Unfortunately, you didn't guess! Please try again. ")

            

        elif users_topic.upper() == 'L':
            randomly_selected_item = languages[selected_language_index]
            #print(randomly_selected_item)  # za test
            if 3 <= counter <= len(randomly_selected_item) + 2:
                hint_length = counter - 2  # broj slova raste sa counter-om, ali max do dužine rijeci
                print(f"HINT - {randomly_selected_item[:hint_length]}")
            elif counter > len(randomly_selected_item) + 2:
                print("That's all I can do...")
            print()

            user_guess = input('Guess the name of the lenguage:' )
            counter += 1

            if user_guess.lower() == languages[selected_language_index].lower():   # Ako korisnik pogodi
                print(f'Congratulations!! You guessed the lenguage on your {counter}th attempt. ')
                counter = 0   # resetiram brojac
                selected_language_index = random.randint(0, 7)  # izaberemo random programm ponovno ako korisnik opet zeli igrati
                print()

                next_round = input('Would you like to try again with another topic? (Yes/No): ')
                if next_round.lower() == 'no':  # izlazim iz druge petlje
                    break
                elif next_round.lower() == 'yes':  # ulazimo u prvu petlju gdje korisnik bira koju igru zeli
                    break
            else:
                print("Unfortunately, you didn't guess! Please try again. ")



    if next_round.lower() == 'no':   # gasimo igricu
        print()
        print('See you next time! 😉 ')
        break
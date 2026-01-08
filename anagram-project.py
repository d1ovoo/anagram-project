#anagram
import math
import itertools
import requests

word = input('Enter a word up to 8 characters:')
while not word.isalpha() or len(word) > 8:
    if not word.isalpha():
        print("That's not a word")
    elif len(word) > 8:
        print("That word has more than 8 characters")
    word = input('Enter another word:')

letters = list(word.lower())
#print(letters)

numerator = math.factorial(len(letters))
unique_letters = (set(letters))

denominator = 1
for letter in unique_letters:
    count = letters.count(letter) 
    denominator *= math.factorial(count)
    #print(denominator)

anagram = numerator/denominator -1
print(f"There are {int(anagram)} theoretical anagrams of that word")

anagrams = set("".join(permutations) for permutations in itertools.permutations(letters))
anagrams.discard(word)
anagrams_list = list(anagrams)
#print(anagrams_list)

def is_valid_word():
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{anagram_word}"
    response = requests.get(url)
    return response.status_code == 200

valid_words = []

for anagram_word in anagrams_list:
    if is_valid_word():
        valid_words.append(anagram_word)

num_valid_words = len(valid_words)
if len(valid_words) != 0:
    if len(valid_words) == 1:
        print(f"There is {num_valid_words} real anagram of {word} which is: {', '.join(valid_words)}")
        user_answer = input("Do you want to know what this word means?(y/n)")
    else: 
        print(f"There are {num_valid_words} real anagrams of {word} which are: {', '.join(valid_words)}")
        user_answer = input("Do you want to know what any of these words mean?(y/n)")
    while user_answer not in ('y', 'n'):
        print('Answer with either y or n')
        user_answer = input("Do you want to know what any of these words mean?(y/n)")
    if user_answer == 'y':
        if num_valid_words == 1:
            for anagram_word in valid_words:
                url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{anagram_word}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    meanings = data[0]['meanings']
                    print(f"\nDefinitions for '{anagram_word}':")
                    for meaning in meanings:
                        part_of_speech = meaning['partOfSpeech']
                        definitions = meaning['definitions']
                        for d in definitions:
                            print(f"- ({part_of_speech}) {d['definition']}")
                else:
                     print(f'No definitions found for {anagram_word}')
        else:
            users_word = input("Which word do you want the definition on?:")
            while users_word not in valid_words:
                print("That's not one of the anagrams")
                users_word = input("Which word do you want the definition on?:")
            for users_word in valid_words:
                url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{users_word}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    meanings = data[0]['meanings']
                    print(f"\nDefinitions for '{users_word}':")
                    for meaning in meanings:
                        part_of_speech = meaning['partOfSpeech']
                        definitions = meaning['definitions']
                        for definitions in definitions:
                            print(f"- ({part_of_speech}) {definitions['definition']}") 
                else:
                     print(f'No definitions found for {users_word}')

        
        
    elif user_answer == 'n':
        print('Alright, have a nice day!')


else:
    print(f"There are 0 real anagrams of {word}")










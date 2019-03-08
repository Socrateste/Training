import random
#############################################################################################################
#                                        Words                                                              #
#############################################################################################################
word_list = {
    'Abduct':'To Kidnap',
    'Brevity':'Breifness',
    'Charlatan':'A Fraud',
    'Demur':'To Protest',
    'Eccentric':'Odd',
    'Feasible':'Practical',
    'Gourmand':'A Glutton',
    'Hackneyed':'Overused',
    'Immutable':'Unchangeable',
    'Judicious':'Wise',
    'Kinetic':'Lively',
    'List':'To Tilt',
    'Magnanimous':'Noble',
    'Novice':'A Beginner',
    'Obdurate':'Stubborn',
    'Parsimony':'Stinginess',
    'Quell':'To Extinguish',
    'Rancor':'Bitterness',
    'Scrupulous':'Careful',
    'Taciturn':'Untalkative',
    'Unkempt':'Disheveled',
    'Variegated':'Diversified',
    'Wrath':'Anger',
    'Xanthic':'Yellowish',
    'Willful':'Headstrong',
    'Zealous':'Fervent',
    'Abridge':'To Shorten',
    'Bequeath':'To Give',
    'Capricious':'Unpredictable',
    'Daunt':'To Intimidate',
    'Effervescent':'Exuberant',
    'Fallacious':'False',
    'Garish':'Gaudy',
    'Hardy':'Robust',
    'Impecunious':'Poor',
    'Jargon':'Professional Language',
    'Kirk':'A Church',
    'Lurid':'Gruesome',
    'Meager':'Scanty',
    'Nuance':'A Shade of Difference',
#############################################################################################################
#                                           FIX THIS BUG                                                    #
#############################################################################################################
    # 'Obscure':['Vague', 'Unknown'],
#############################################################################################################
    'Parochial':'Provincial',
    'Quiescent':'Inactive',
    'Replete':'Full',
    'Sage':'A Wise Person',
    'Temerity':'Audacity',
    'Unwarranted':'Unjustifiable',
    'Vacillate':'To Fluctuate',
    'Warlock':'A Wizard',
    'Xenon':'A Noble Gas',
    'Abate':'To Decrease',
    'Bard':'A Poet',
    'Callow':'Immature',
    'Demure':'Reserved',
    'Elusive':'Baffling',
    'Facile':'Easy',
    'Guile':'Deceit',
    'Hiatus':'A Gap',
    'Idyllic':'Blissful',
    'Jubilant':'Happy',
    'Kindle':'To Inspire',
    'Lucid':'Clear',
    'Marred':'Damaged',
    'Nefarious':'Evil',
    'Protean':'Changeable',
    'Quixotic':'Idealistic',
    'Rash':'Hasty',
    'Subtlety':'Elusiveness',
    'Tacit':'Unspoken',
    'Usurp':'To Seize',
    'Vapid':'Dull',
    'Wanton':'Egregious',
    'Xenophobia':'A Fear of Strangers',
    'Yean':'To Give Birth',
    'Zealot':'A Fanatic',
    'Ascendancy':'Dominance',
    'Belated':'Late',
    'Credulity':'Gullibility',
    'Deluge':'A Flood',
    'Egregious':'Bad',
    'Florid':'Reddish',
    'Germane':'Pertinent',
    'Hapless':'Unlucky',
    'Ignominy':'Shame',
    'Juxtapose':'To Place Side by Side',
    'Parvenu':'An Upstart',
    'Labyrinth':'A Maze',
    'Medley':'A Mixture',
    'Nullify':'To Make Void',
    'Opulent':'Rich',
    'Precipitate':'Hasty',
    'Querulous':'Complaining',
    'Rant':'To Rave',
    'Saccharine':'Sweet',
    'Tangential':'Peripheral',
    'Utopia':'An Ideal Society',
    'Vacuous':'Stupid',
    'Wistful':'Yearning',
    'Yahoo':'A Barbarian',
    'Power':'The Ability to Act',
    'Astute':'Keen',
    'Benign':'Mild',
    'Chagrin':'Humiliation',
    'Deprecate':'To Belittle',
    'Emulate':'To Imitate',
    'Facetious':'Humorous',
    'Garrulous':'Talkative',
    'Halcyon':'Peaceful',
    'Irate':'Angry',
    'Jeopardize':'To Endanger',
    'Kibosh':'To Squelch',
    'Lassitude':'Weariness',
    'Maladroit':'Clumsy',
    'Nonentity':'A Nobody',
    'Obsequious':'Servile',
    'Paltry':'Insignificant',
    'Qualify':'To Modify',
    'Recalcitrant':'Defiant',
    'Sacrosanct':'Sacred',
    'Tenable':'Defensible',
    'Utilitarian':'Useful',
    'Venerate':'To Revere',
    'Wag':'A Joker',
    'Xeno':'Foreign',
    'Yahweh':'God',
    'Zenith':'A High Point',
    'Accentuate':'To Stress',
    'Belie':'To Give False Impression',
    'Chronicle':'A Record',
    'Despot':'A Tyrant',
    'Extant':'In Existence',
    'Fabricate':'To Invent',
    'Genteel':'Refined',
    'Heterogeneous':'Mixed',
    'Implore':'To Beg',
    'Justification':'A Good Reason',
    'Knot':'A Group Of Toads',
    'Lofty':'High',
    'Melancholy':'Sad',
    'Nocturnal':'Occurring At Night',
    'Orator':'A Public Speaker',
    'Prognosticate':'To Predict',
    'Quotidian':'Daily',
    'Rudimentary':'Elementary',
    'Sordid':'Dirty',
    'Trivial':'Unimportant',
    'Unprecedented':'Novel',
    'Viable':'Workable',
    'Wrest':'To Turn',
    'Yore':'Time Long Past',
    'Abhor':'To Hate',
    'Bauble':'A Trinket',
    'Calumny':'Slander',
    'Doleful':'Sorrowful',
    'Extol':'To Praise',
    'Fallacy':'A False Assumption',
    'Gambol':'To Skip',
    'Hacienda':'A Country Estate',
    'Incumbent':'Required',
    'Joust':'To Fight',
    'Kaput':'Broken',
    'Lament':'To Mourn',
    'Muted':'Silent',
    'Nostalgia':'Homesickness',
    'Oust':'To Eject',
    'Placid':'Calm',
    'Quip':'A Joke',
    'Recant':'To Disavow',
    'Savory':'Tasty',
    'Tangible':'Concrete',
    'Urbane':'Polished',
    'Venial':'Forgivable',
    'Wright':'A Worker',
    'Xylograph':'A Woodcut',
    'Yaw':'To Turn',
    'Zest':'A Sraping Of An Orange',
    'Acclaim':'To Praise',
    'Battery':'An Assualt',
    'Conundrum':'A Puzzle',
    'Dispassionate':'Impartial',
    'Emend':'To Edit',
    'Fortuitous':'Accidental',
    'Gambit':'A Calculated Move',
    'Hone':'To Sharpen',
    'Inveigle':'To Entice',
    'Jaded':'Worn Out',
    'Keen':'A Funeral Song',
    'Levity':'Lightheartedness',
    'Myriad':'Many',
    'Nebulous':'Vague',
    'Onerous':'Burdensome',
    'Ponderous':'Massive',
    'Reciprocal':'Mutual',
    'Query':'A Question',
    'Stanza':'A Division of a Poem',
    'Tentative':'Provisional',
    'Unbridled':'Unrestrained',
    'Vagary':'A Whim',
    'Wile':'A Trick',
    'Zephyr':'A Gentle Breeze'
}
# Tells the user how many words they can be tested on + gets the number of words they want to be tested on
print(f'There is a total of {len(word_list)} words that you can be tested on')
tested_amount = int(input('How many words would you like to be tested on?  '))

# Creates a list with the words to be tested on
list_of_words_to_be_tested_on = list(word_list.keys())
random.shuffle(list_of_words_to_be_tested_on)
for i in range(len(word_list) - tested_amount):
    list_of_words_to_be_tested_on.pop()

# TODO Show the number of words to be tested on and their meaning
def show_word(num, word, meaning):
    print(f'{num}) {word} means {meaning}')

for i in range(tested_amount):
    answer = input(f'Are you ready for word # {i + 1}? ').lower()
    if answer in 'yes':
        show_word(i+1,list_of_words_to_be_tested_on[i],word_list[list_of_words_to_be_tested_on[i]])
    # TODO Quits the whole program
    else:
        pass


# TODO Ask if they want to be tested on the meaning to try to remember the word or vice versa
meaning_or_word = input('Would you like to be tested on the word to try to remember the meaning of that word? (Word) \n\n OR \n\nWould you like to be tested on the meaning of a word and try to remember the word? (Meaning) \n\nType out either Word or Meaning \n')
def word_testing(word, meaning):
    '''
    DOCSTRING \n
    INPUT: Word to be tested on (word) \n
    INPUT: Meaning of the word to be tested on (meaning) \n
    OUTPUT: Four different meanings, 1 being the correct one
    '''
    word_list_values = list(word_list.values())

    print(f'What is the meaning of {word}? \nThe possible answers are: ')

    # Creates the list of choices and shuffles them
    random.shuffle(word_list_values)
    word_list_values.remove(meaning)
    testing_choices = random.sample(word_list_values, 3)
    testing_choices.append(meaning)
    random.shuffle(testing_choices)

    # Returns the possible meanings
    return testing_choices


def meaning_testing(word):
    '''
    DOCSTRING \n
    INPUT: The correct word (word) \n
    OUTPUT: The correct word + 3 incorrect words shuffled in random order
    '''

    word_list_keys = list(word_list.keys())
    random.shuffle(word_list_keys)
    word_list_keys.remove(word)
    word_choices = random.sample(word_list_keys, 3)
    word_choices.append(word)
    random.shuffle(word_choices)

    return word_choices


# Use Generator
def tally():
    pass


if meaning_or_word.lower() == 'word':
    print('Would you like to like to be given 4 choices or would you like to try to remember the meaning of the word? \nPlease type either Choices or Hidden')
    answer = input().lower()
    if answer in 'choices':
        random.shuffle(list_of_words_to_be_tested_on)
        for i in range(len(list_of_words_to_be_tested_on)):
            print('\n' * 2)
            answer_choices = word_testing(list_of_words_to_be_tested_on[i], word_list[list_of_words_to_be_tested_on[i]])
            for y in range(4):
                print(f'{y + 1}) {answer_choices[y]}')
            answer = input().lower()
            if answer == word_list[list_of_words_to_be_tested_on[i]].lower():
                # Add to tally function
                print('That\'s correct')
            else:
                # Add to tally function
                print('Sorry that is incorrect')
    elif answer in 'hidden':
        random.shuffle(list_of_words_to_be_tested_on)
        for i in range(len(list_of_words_to_be_tested_on)):
            print(f'What is the meaning of the word {list_of_words_to_be_tested_on[i]}?')
            answer = input().lower()
            if answer == word_list[list_of_words_to_be_tested_on[i]].lower():
                # Add tally func
                print('That\'s correct!')
            else:
                # Add tally func
                print('That\'s incorrect')
    # Breaks out of the program
    else:
        pass

elif meaning_or_word.lower() == 'meaning':
    print('Would you like to see a list of possible word choices or try to remember? \nPlease type either "Choices" or "Hidden"')
    answer = input().lower()
    if answer in 'choices':
        random.shuffle(list_of_words_to_be_tested_on)
        for i in range(len(list_of_words_to_be_tested_on)):
            print(f'What is the word that means {word_list[list_of_words_to_be_tested_on[i]]}?')
            print('It can be any of the following')
            answer_choices = meaning_testing(list_of_words_to_be_tested_on[i])
            for y in range(4):
                print(f'{y + 1}) {answer_choices[y]}')
            answer = input().lower()
            if answer == list_of_words_to_be_tested_on[i].lower():
                # Add tally func
                print('That is correct')
            else:
                # Add tally func
                print('That is incorrect')
    elif answer in 'hidden':
        for i in range(len(list_of_words_to_be_tested_on)):
            print(f'What is the word that belongs to the meaning {word_list[list_of_words_to_be_tested_on[i]]}?')
            answer = input().lower()
            if answer == word_list[list_of_words_to_be_tested_on[i]].lower():
                # Add tally func
                print('That is correct')
            else:
                # Add tally func
                print('That is incorrect')
    else:
        print('I don\'t recognize that input')
# TODO Quits the program
else:
    print('I don\'t recognize that input')
# TODO Takes count of the total incorrect questions and correct one and displays them at the end

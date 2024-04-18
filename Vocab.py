import random
import json
import numpy as np
import math


class GermanVocabulary:
    def __init__(self):
        self.words = {}
        self.weights = {}

    def update(self, word, attribute, value):
        if self.words[word].get(attribute) is None:
            self.words[word][attribute] = value
            self.weights[word][attribute] = 1
        else:
            self.words[word][attribute] = value

    def delete_word(self, word):
        if word in self.words or word in self.weights:
            if word in self.words:
                del self.words[word]
            if word in self.weights:
                del self.weights[word]
            self.save_progress()
            return 1
        else:
            return 0

    def get_word_list(self):
        word_list = []
        reversed_words = list(reversed(self.words.keys()))
        for index, word in enumerate(reversed_words, start=1):
            meaning = self.words[word].get('meaning', '')
            pos = self.words[word].get('pos', '')
            word_list.append(f'{index}. {word} {pos}    {meaning}')

        return word_list

    # generates a list of possible solutions for a given word and attribute
    def get_solution(self, word, attribute, n=3):
        solution_space = []
        for key in self.words:
            if self.words[key].get(attribute) is not None and key != word:
                solution_space.append(self.words[key][attribute])

        solution = [self.words[word][attribute]] + random.sample(solution_space, min(n-1, len(solution_space)))
        random.shuffle(solution)
        return solution

    def save_progress(self, filename='progress.json'):
        data = {'vocabulary': self.words, 'weights': self.weights}
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Progress and vocabulary saved to {filename}.")

    def load_progress(self, filename='progress.json'):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.words = data.get('vocabulary', {})
                self.weights = data.get('weights', {})
            return 1
            # print(f"Progress and vocabulary loaded from {filename}.")
        except FileNotFoundError:
            return 0
            # print("No progress file found. Starting with a fresh vocabulary.")

    def total_length(self):
        length = sum(len(inner_dict) for inner_dict in self.words.values())
        return length

    def get_quiz(self, n, attribute=None):
        words = []
        for word in self.words:
            if self.words[word].get(attribute) is not None:
                words.append(word)
        random.shuffle(words)
        weights = [p(self.weights[word][attribute], 1, 1.5) for word in words]
        # weights = [1/pow(self.weights[word][attribute]-0.3, 3) for word in words]
        probability = [w / sum(weights) for w in weights]
        # print(max(weights), max(probability))
        quest_length = min(n, len(words))
        questions = np.random.choice(words, quest_length, p=probability, replace=False)
        return questions

    # generates n non-repeating quests
    def questions_mixed(self, n):
        weights_words = [sum(info.values()) for info in self.weights.values()]
        weights_words = [w / sum(weights_words) for w in weights_words]
        weights_words = [1-w for w in weights_words]

        words = list(self.words.keys())
        questions = []  # Unique set of questions to avoid repetition
        quest_length = min(n, self.total_length())

        while len(questions) < quest_length:
            # Extract the single element from the list returned by random.choices
            word = random.choices(words, weights_words, k=1)[0]
            attributes = list(self.words[word].keys())
            weights_attributes = [w/sum(self.weights[word].values()) for w in self.weights[word].values()]
            weights_attributes = [1-w for w in weights_attributes]

            practice_type = random.choices(attributes, weights_attributes, k=1)[0]
            question = (word, practice_type)

            if question not in questions:
                questions.append(question)

        return questions

    def gain_points(self, word, attribute):
        self.weights[word][attribute] = min(8, self.weights[word][attribute] + 1)

    def lose_points(self, word, attribute):
        self.weights[word][attribute] = max(1, self.weights[word][attribute] - 1)


class Nomen(GermanVocabulary):

    def add_word(self, noun):
        word, gender, plural, meaning = noun
        word_data = {'gender': gender, 'plural': plural, 'meaning': meaning}

        if word == '':
            return 0

        valid_genders = ['der', 'die', 'das']
        if word in self.words:
            valid_genders.append('')

        if gender in valid_genders:
            for attribute, value in word_data.items():
                if value != '':
                    self.update(word, attribute, value)
            self.save_progress()
            return 1
        else:
            return 0

    def save_progress(self, filename='Nomen.json'):
        super().save_progress(filename)

    def load_progress(self, filename='Nomen.json'):
        super().load_progress(filename)

    def get_word_list(self):
        word_list = []
        reversed_words = list(reversed(self.words.keys()))

        for index, word in enumerate(reversed_words, start=1):
            gender = self.words[word]['gender']
            word_list.append(f'{index}. {gender} {word}')
        return word_list

    def get_hint(self, word, attribute):
        if attribute == 'gender':
            pass

        return None


class Verb(GermanVocabulary):

    def __init__(self):
        super().__init__()
        self.conjugation = {}

    def add_word(self, verb):
        word, ich, du, es, past, meaning = verb
        word_data = {'ich': ich, 'du': du, 'es': es, 'past': past, 'meaning': meaning}

        if word == '':
            return 0

        if word not in self.words:
            self.weights[word] = {key: 1 for key in word_data}

        for attribute, value in word_data.items():
            if value != '':
                self.update(word, attribute, value)

        return 1

    def update_conjugation(self, word, tense, attribute, value):
        if tense not in ['present', 'imperfect', 'perfect', 'pluperfect', 'future']:
            return 0
        self.conjugation[word][tense][attribute] = value
        return 1




    def save_progress(self, filename='Verb.json'):
        super().save_progress('Verb.json')

    def load_progress(self, filename='Verb.json'):
        super().load_progress('Verb.json')

    def get_quiz(self, n, type=1):
        quiz = []
        if type == 1:
            return super().get_quiz(n, 'meaning')
        elif type == 2:
            for word in super().get_quiz(math.floor(n/4), 'ich'):
                quiz.append((word, 'ich'))
            for word in super().get_quiz(math.floor(n/4), 'du'):
                quiz.append((word, 'du'))
            for word in super().get_quiz(math.ceil(n/4), 'es'):
                quiz.append((word, 'es'))
            for word in super().get_quiz(math.ceil(n/4), 'past'):
                quiz.append((word, 'past'))
            random.shuffle(quiz)
            return quiz




class Adjektiv(GermanVocabulary):
    pass


class Mixed(GermanVocabulary):

    def add_word(self, word, meaning, pos):   # pos: part of speech
        if '' in [word, pos, ]:
            return 0
        elif word in self.words:
            if meaning is not None:
                self.update(word, 'meaning', meaning)
            if pos is not None:
                self.update(word, 'pos', pos)
            self.save_progress()
            return 1
        else:
            self.words[word] = {'meaning': meaning, 'pos': pos}
            self.weights[word] = {'meaning': 1, 'pos': None}
            self.save_progress()
            return 1

    def save_progress(self, filename='vocabulary.json'):
        super().save_progress(filename)

    def load_progress(self, filename='vocabulary.json'):
        super().load_progress(filename)




def p(x, mu, sigma):
    return 1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))


# ** 5. Реализовать функцию, возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# in
# 10 True
#
# out
#
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
# 'автомобиль сегодня веселый', 'город позавчера утопичный']
#
# in
# 10 False
#
# ['автомобиль ночью мягкий', 'огонь вчера веселый',
# 'автомобиль позавчера веселый', 'город вчера утопичный',
# 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый',
# 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']

from random import choice


def create_jokes(number_of_jokes, is_unique: bool) -> list:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if is_unique:
        answer_list = []
        for _ in range(min(len(nouns), len(adverbs), len(adverbs))):
            noun_taken = choice(nouns)
            nouns.remove(noun_taken)
            adverb_taken = choice(adverbs)
            adverbs.remove(adverb_taken)
            adjective_taken = choice(adjectives)
            adjectives.remove(adjective_taken)
            answer_list.append(f'{noun_taken} {adverb_taken} {adjective_taken}')
        print(answer_list)
        return answer_list
    else:
        answer_list = [choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives) for _ in range(number_of_jokes)]
        print(answer_list)
        return answer_list


def main() -> None:
    number_of_jokes = 10
    create_jokes(number_of_jokes, False)

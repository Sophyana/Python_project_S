"""
from collections import Counter


def main():
    # Ввод данных
    W = int(input().strip())

    # Чтение многострочного текста
    text_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        text_lines.append(line)

    # Объединение строк в один текст и очистка от не-букв
    text = " ".join(text_lines)
    cleaned_text = re.sub(r'[^a-zA-Z\s]', ' ', text)   # Оставляем только буквы и пробелы
    words = cleaned_text.lower().split()  # Приводим к нижнему регистру и разбиваем на слова

    # Подсчет слов длиной W
    word_counts = Counter(word for word in words if len(word) == W)

    # Если слова найдены, выводим их в отсортированном порядке
    if word_counts:
        popular_words = sorted(word_counts.keys())
        print(" ".join(popular_words))


if __name__ == "__main__":
    main()


# ___________________________________________________________________________________________



# Находим максимальный размер пачки
max_deck_size = 0
for player, decks in player_decks.items():
    total_cards = sum(len(cards) for cards in decks.values())
    max_deck_size = max(max_deck_size, total_cards)

# Собираем имена игроков с максимальной пачкой
winners = [player for player, decks in player_decks.items()
           if sum(len(cards) for cards in decks.values()) == max_deck_size]

# Сортируем имена игроков в алфавитном порядке и выводим
for winner in sorted(winners):
    print(winner)

# Находим максимальный размер пачки
    max_deck_size = 0
    for player, decks in player_decks.items():
        total_cards = sum(len(cards) for cards in decks.values())
        max_deck_size = max(max_deck_size, total_cards)

    # Собираем имена игроков с максимальной пачкой
    winners = [player for player, decks in player_decks.items()
               if sum(len(cards) for cards in decks.values()) == max_deck_size]

    # Сортируем имена игроков в алфавитном порядке и выводим
    for winner in sorted(winners):
        print(winner)



# -----------------------------------------------------------------------------------------------------------------
def main():
    from collections import defaultdict

    # Словарь для хранения колод карт игрока
    player_decks = defaultdict(lambda: defaultdict(set))

    while True:
        line = input().strip()
        if not line:
            break

        if ' / ' in line:
            left, right = line.split(' / ')
            if left.isdigit():  # "номер колоды / название карты"
                deck_number = int(left)
                card_name = right
                # Добавляем карту в соответствующую колоду
                for player, decks in player_decks.items():
                    if deck_number in decks:
                        decks[deck_number].add(card_name)
            else:  # "имя игрока / номер колоды"
                player_name = left
                deck_number = int(right)
                # Создаем новую колоду для игрока
                player_decks[player_name][deck_number] = set()

    # Находим максимальный размер пачки
    max_deck_size = 0
    for player, decks in player_decks.items():
        total_cards = sum(len(cards) for cards in decks.values())
        max_deck_size = max(max_deck_size, total_cards)

    # Собираем имена игроков с максимальной пачкой
    winners = [player for player, decks in player_decks.items()
               if sum(len(cards) for cards in decks.values()) == max_deck_size]

    # Сортируем имена игроков в алфавитном порядке и выводим
    for winner in sorted(winners):
        print(winner)


if __name__ == "__main__":
    main()
"""

"""from collections import defaultdict


def main():
    players_decks = defaultdict(set)
    deck_cards = defaultdict(set)

    while True:
        line = input().strip()
        if not line:
            break

        parts = line.split(" / ")
        if len(parts) != 2:
            continue  # Пропускаем некорректные строки

        first, second = parts

        if first.isdigit():
            # Обработка "номер колоды / название карты"
            deck_number = first
            card_name = second

            deck_cards[deck_number].add(card_name)
        else:
            # Обработка "имя игрока / номер колоды"
            player_name = first
            deck_number = second

            players_decks[player_name].add(deck_number)

    # Подсчет карт для каждого игрока
    player_card_counts = defaultdict(int)

    for player, decks in players_decks.items():
        for deck in decks:
            player_card_counts[player] += len(deck_cards[deck])

    # Находим максимальное количество карт
    max_count = max(player_card_counts.values(), default=0)

    # Получаем имена игроков с максимальным количеством карт
    winners = [player for player, count in player_card_counts.items() if count == max_count]

    # Выводим имена в алфавитном порядке
    for winner in sorted(winners):
        print(winner)


if __name__ == "__main__":
    main()
"""

from collections import defaultdict

players_decks = defaultdict(set)
deck_cards = defaultdict(set)

while True:
    line = input().strip()
    if not line:
        break

    parts = line.split(" / ")
    if len(parts) != 2:
        continue  # Пропускаем некорректные строки

    first, second = parts

    if first.isdigit():
        # Обработка "номер колоды / название карты"
        deck_number = first
        card_name = second

        deck_cards[deck_number].add(card_name)
    else:
        # Обработка "имя игрока / номер колоды"
        player_name = first
        deck_number = second

        players_decks[player_name].add(deck_number)

# Подсчет карт для каждого игрока
player_card_counts = defaultdict(int)

for player, decks in players_decks.items():
    for deck in decks:
        player_card_counts[player] += len(deck_cards[deck])

# Находим максимальное количество карт
max_count = max(player_card_counts.values(), default=0)

# Получаем имена игроков с максимальным количеством карт
winners = [player for player, count in player_card_counts.items() if count == max_count]

# Выводим имена в алфавитном порядке
for winner in sorted(winners):
    print(winner)

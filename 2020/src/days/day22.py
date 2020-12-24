from collections import deque


def main():
    with open("data/day22.txt") as f:
        decks = [deque(int(card) for card in section.splitlines()[1:]) for section in f.read().split("\n\n")]

    part1(decks)
    part2(decks)


def part1(decks):
    deck1, deck2 = decks[0].copy(), decks[1].copy()

    while deck1 and deck2:
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            deck1.extend([card1, card2])
        elif card2 > card1:
            deck2.extend([card2, card1])
        else:
            raise NotImplemented

    winning_deck = deck1 or deck2
    score = sum((i + 1) * card for i, card in enumerate(reversed(winning_deck)))
    print("Day 22 Part 1: %s" % score)


def part2(decks):
    deck1, deck2 = recursive_combat(decks[0].copy(), decks[1].copy())
    winning_deck = deck1 or deck2
    score = sum((i + 1) * card for i, card in enumerate(reversed(winning_deck)))
    print("Day 22 Part 2: %s" % score)


def recursive_combat(deck1, deck2):
    seen = set()
    deck1 = deque(deck1)
    deck2 = deque(deck2)

    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in seen:
            return list(deck1), []
        seen.add((tuple(deck1), tuple(deck2)))

        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = [deck1[i] for i in range(card1)]
            new_deck2 = [deck2[i] for i in range(card2)]
            player1_wins, player2_wins = recursive_combat(new_deck1, new_deck2)
        else:
            player1_wins = card1 > card2
            player2_wins = card2 > card1

        if player1_wins:
            deck1.extend([card1, card2])

        elif player2_wins:
            deck2.extend([card2, card1])

    return list(deck1), list(deck2)


if __name__ == "__main__":
    main()

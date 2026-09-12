"""STARTER CODE: Memory Match. Intentionally uses no Python lists."""


def symbol(position):
    if position == 1 or position == 6:
        return "A"
    if position == 2 or position == 4:
        return "B"
    return "C"


def main():
    print("=== MEMORY MATCH ===")
    print("Cards: 1 2 3 4 5 6")
    matched_a = False
    matched_b = False
    matched_c = False
    score = 0
    turns = 5

    while turns > 0 and score < 3:
        try:
            first = int(input("First card: "))
            second = int(input("Second card: "))
        except ValueError:
            print("Enter numbers only.")
            continue

        if first < 1 or first > 6 or second < 1 or second > 6 or first == second:
            print("Choose two different cards from 1 to 6.")
            continue

        one = symbol(first)
        two = symbol(second)
        print("You revealed", one, "and", two)

        if one == two:
            if one == "A" and not matched_a:
                matched_a = True
                score += 1
            elif one == "B" and not matched_b:
                matched_b = True
                score += 1
            elif one == "C" and not matched_c:
                matched_c = True
                score += 1
            else:
                print("That pair was already found.")

        turns -= 1
        print("Pairs:", score, "Turns left:", turns)

    print("YOU WIN!" if score == 3 else "GAME OVER.")


if __name__ == "__main__":
    main()
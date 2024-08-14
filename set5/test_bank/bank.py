def main():
    words = input("Greeting: ")
    answer = value(words)
    print(f'${answer}')


def value(ask):
    ask = ask.lower()
    findHello  = 'hello' in ask
    findH  = 'h' in ask
    findQ  = "what's" in ask

    if findHello:
        return 0
    elif findH and not findQ:
        return 20
    elif findQ:
        return 100
    else:
        return f'This is outher alternative'


if __name__ == "__main__":
    main()

ask = input("Greeting: ").lower()
findHello  = 'hello' in ask
findH  = 'h' in ask
findQ  = '?' in ask

if findHello:
    print('$0')
elif findH and findQ == False:
    print('$20')
elif findQ:
    print('$100')
else:
    print('This is outher alternative')

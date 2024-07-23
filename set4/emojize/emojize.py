import emoji

messages = input("Input: ")
count = 0
for message in messages:
    if ":" in messages:
        count += count
        match count:
            case 2:
                if messages == " ":
                    part1, part2 = messages.split(" ")
                    part2 = part2.strip()
                    icon = emoji.emojize(part2)
                    print(f"{part1} {icon}")
                else:
                    print(emoji.emojize(messages))
    else:
        print(messages)

import emoji

messages = input("Input: ")

# if "," in messages:
#     part1, part2 = messages.split(" ")
#     part2 = part2.strip()
#     icon = emoji.emojize(part2)
#     print(f"{part1} {icon}")
# else:
print(emoji.emojize(messages))

# integre = None

# while True:
#     try:
#         integre = int(input("Level: "))
#         if integre > 0:
#             break
#     except KeyboardInterrupt:
#         print("\nProgram exited.")
#         break
#     except:
#         pass
# if integre:
#     while True:
#         try:
#             game = int(input("Guess: "))
#             if game == 5: # Put the variable where goint tu random number
#                 print("Just right! ")
#                 break
#         except KeyboardInterrupt:
#             print("\nProgram exited.")
#             break
#         except:
#             pass
import random

num = random.randrange(10)

print(num)

def main():
    mass = float(input('m: '))
    speed_of_light = 300000000
    energy = mass * pow(speed_of_light, 2)
    print(f"E: {energy:0f} \nIt's equal that E=mc²")

main()

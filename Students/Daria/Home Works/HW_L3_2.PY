door = (input("Choose a door (red, blue, green):"))

match door:
    case "red":
        print("Dragon is behind the door! What do you want to do? ")
        if input("1-fight"):
            print("You have won the fight!")
        elif input("2-run"):
            print("You have run away!")

    case "blue":
        print("Enter a secret number:")

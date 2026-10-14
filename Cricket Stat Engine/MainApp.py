from Features.feature_1.Main_F1 import Feature1call
from Features.feature_2.Main_F2 import Feature2call
from Features.feature_3.Main_F3 import Feature3call
import time, os

FeatureNames = ["Archive Scoreboard", "Player Stats", "Stadium Stats"]

print("        Welcome To Rafay's Cricket Stats Engine        ")
print("-"*50)
print(" Stats from 2007 - 2025 of Matches played between test playing nation")
time.sleep(2)

def AskingUser(FeatureNames):
    print("=" * 50)
    print("Features :-")
    print("-" * 12)

    for i, value in enumerate(FeatureNames, 1):
        print(f"{i:>2}. {value}")

    print("-" * 12)

    while True:
        try:
            user = int(input("Enter Your Selection: "))

            if 1 <= user <= len(FeatureNames):
                break
            else:
                print("Please select an index from the given options!")

        except ValueError:
            print("Please enter a valid number!")

    return user

while True:
    user = AskingUser(FeatureNames)

    os.system("cls")

    if   user == 1: Feature1call()
    elif user == 2: Feature2call()
    elif user == 3: Feature3call()

    print("=" * 45)
    print("Press Enter to continue")
    print("To exit, press (X)")
    print("-" * 16)

    proceed = input("Selection: ").strip().capitalize()

    time.sleep(1.5)

    if proceed == "X":
        break
    else:
        os.system("cls")
        
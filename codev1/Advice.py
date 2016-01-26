# This file is used for the pc to give advice to the client about sporting


def main():
    """
    This is the main function and is used to call all other functions
    """


def advice():
    print("A")
    clientWeight = 70
    clientCalories = 600
    clientTag = "Cardio"
    muscleTag = "Arms"
    treadmill = 400
    perTreadmill = 100 * treadmill / clientCalories
    weightlifting = 200
    perWeightlifting = 100 * weightlifting / clientCalories
    rowingMachine = 0
    perRowingMachine = 100 * rowingMachine / clientCalories
    spinningMachine = 0
    perSpinningMachine = 100 * spinningMachine / clientCalories
    climbingStairs = 0
    perClimbingStairs = 100 * climbingStairs / clientCalories

    print("Uw gewicht is ", clientWeight, "kg")
    print("U heeft deze maand", clientCalories, "kcal verbrand")
    if clientTag == "Cardio":
        if perTreadmill + perSpinningMachine + perClimbingStairs >= 70:
            print("U bent goed bezig met het cardio trainen")
        else:
            print("U bent aan het sporten met niet cardio-apperaten probeer wat vaker op de spinning fiets of de "
                  "loopband te staan")
    if clientTag == "Kracht":
        if perWeightlifting + perRowingMachine >= 70:
            print("U bent goed bezig met het krachttrainen")
        else:
            print("U bent niet genoeg aan het trainen met krachtapperaten probeer wat meer gewicht te heffen"
                  " en te roeien")

    if muscleTag == "Arms":
        if perRowingMachine >= 55:
            print("U bennt goed bezig met het versterken van u armen. Ga zo door ")
        else:
            print("U bent wat minder bezig met roeien, hierdoor haalt u misschien u doel niet voor meer spieren in u "
                  "armen")

advice()

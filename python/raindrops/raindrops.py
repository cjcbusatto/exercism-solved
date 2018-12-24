def raindrops(number):
    raindrop_speak = ""
    if number % 3 == 0:
        raindrop_speak += "Pling"
    if number % 5 == 0:
        raindrop_speak += "Plang"
    if number % 7 == 0:
        raindrop_speak += "Plong"

    # if the number has not 3,5 or 7 as factor, returns the number itself casted to string
    return raindrop_speak if len(raindrop_speak) > 0 else str(number)

def IntToRome(user_input):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i = 12
    RomanNumeral = ""
    while user_input != 0:
        if numbers[i] <= user_input:
            RomanNumeral += roman[i]
            user_input = user_input - numbers[i]
        else:
            i -= 1
    return RomanNumeral

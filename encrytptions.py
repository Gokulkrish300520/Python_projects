def encrypted(sentence):
    translated=""
    for letters in sentence:
        if letters in "Aa":
            translated += "1"
        elif letters in "Bb":
            translated += "2"
        elif letters in "Cc":
            translated += "3"
        elif letters in "Dd":
            translated += "4"
        elif letters in "Ee":
            translated += "5"
        elif letters in "Ff":
            translated += "6"
        elif letters in "Gg":
            translated += "7"
        elif letters in "Hh":
            translated += "8"
        elif letters in "Ii":
            translated += "9"
        elif letters in "Jj":
            translated += "!"
        elif letters in "Kk":
            translated += "@"
        elif letters in "Ll":
            translated += "#"
        elif letters in "Mm":
            translated += "$"
        elif letters in "Nn":
            translated += "%"
        elif letters in "Oo":
            translated += "^"
        elif letters in "Pp":
            translated += "&"
        elif letters in "Qq":
            translated += "*"
        elif letters in "Rr":
            translated += "("
        elif letters in "Ss":
            translated += ")"
        elif letters in "Tt":
            translated += "-"
        elif letters in "Uu":
            translated += "+"
        elif letters in "Vv":
            translated += "="
        elif letters in "Ww":
            translated += "|"
        elif letters in "Xx":
            translated += "_"
        elif letters in "Yy":
            translated += "?"
        elif letters in "Zz":
            translated += "/"
        else:
            translated = translated + letters
    return translated

a = input("Enter the text you would like to encrypted")
print(encrypted(a))
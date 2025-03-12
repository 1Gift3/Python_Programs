def validate_password(password):

    if (len(password) < 8):
        return False
    
    has_lower = False
    has_upper = False 
    has_digit = False 
    has_symbol = False

    symbols = "!\"#$%'()*+,-/:;<=>?@[\]^_`{|}~"

    for character in password:

        if character.islower():
            has_lower = True

        if character.isupper():
            has_upper = True

        if character.isdigit():
            has_digit = True   

        if character in symbols:
            has_symbol = True 

    return has_lower and has_upper and \
    has_digit and has_symbol

print(validate_password("TryMe224!?"))           
############################################################################################
# Version 1 of my code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# def encrypt(input_text, shift_amount):
#     encrypted_text = ""
#     for letter in input_text:
#         index = alphabet.index(letter)
#         encrypted_text += alphabet[index + shift_amount]
#     print(encrypted_text)
#
#
# def decrypt(input_text, shift_amount):
#     decrypted_text = ""
#     for letter in input_text:
#         index = alphabet.index(letter)
#         decrypted_text += alphabet[index - shift_amount]
#     print(decrypted_text)
#
#
# exit_game = True
# while exit_game:
#     direction = input("Type 'e' to encrypt, type 'd' to decrypt: and 'q' to quit\n")
#     if direction != "q":
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         if direction == "e":
#             encrypt(text, shift)
#         if direction == "d":
#             decrypt(text, shift)
#     else:
#         exit_game = False
############################################################################################
# Version 2 of my code modified one
import art

exit_game = True


def caesar(input_text, shift_amount, cipher_direction):
    plain_text = ""
    if cipher_direction == "d":
        shift_amount *= -1
    for letter in input_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            plain_text += alphabet[index + shift_amount]
        else:
            plain_text += letter
    print(plain_text)


print(art.logo)
while exit_game:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: and 'q' to quit: \n")
    if direction == 'e' or direction == 'd':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        print(shift)
        caesar(text, shift, direction)
    else:
        exit_game = False

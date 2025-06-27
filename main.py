import art
def caesar(original_text, shift_amount, encode_or_decode):
    new_text = []
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            new_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            new_text.append(alphabet[new_position])
        else:
            new_text.append(letter)

    print(f"Here is the {encode_or_decode}d result: " + "".join(new_text))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = True

print(art.logo)
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    again = input("Do you want to go again? Type 'yes' or 'no'.\n").lower() == "yes"

import string

ALPHABET = string.ascii_uppercase

def generate_keyword_alphabet(keyword):
    keyword = "".join(dict.fromkeys(keyword.upper()))  # remove duplicates
    remaining = "".join([c for c in ALPHABET if c not in keyword])
    return keyword + remaining

def apply_plugboard(text, swaps):
    mapping = {c: c for c in ALPHABET}
    for a, b in swaps:
        mapping[a] = b
        mapping[b] = a
    return "".join(mapping.get(c, c) for c in text)

def shift_alphabet(alphabet, shift):
    shift %= 26
    return alphabet[shift:] + alphabet[:shift]

def enigma_keyword_encrypt(text, keyword, swaps=None):
    if swaps is None:
        swaps = []

    text = text.upper().replace(" ", "")
    base_alpha = generate_keyword_alphabet(keyword)
    result = []
    shift = 0

    for ch in text:
        if ch not in ALPHABET:
            result.append(ch)
            continue

        # plugboard in
        ch = apply_plugboard(ch, swaps)

        # rotor-like shift
        shifted_alpha = shift_alphabet(base_alpha, shift)

        # substitution
        idx = ALPHABET.index(ch)
        enc = shifted_alpha[idx]

        # plugboard out
        enc = apply_plugboard(enc, swaps)

        result.append(enc)

        # rotor steps
        shift += 1

    return "".join(result)

def enigma_keyword_decrypt(text, keyword, swaps=None):
    if swaps is None:
        swaps = []

    text = text.upper().replace(" ", "")
    base_alpha = generate_keyword_alphabet(keyword)
    result = []
    shift = 0

    for ch in text:
        if ch not in ALPHABET:
            result.append(ch)
            continue

        # plugboard in
        ch = apply_plugboard(ch, swaps)

        # rotor-like shift
        shifted_alpha = shift_alphabet(base_alpha, shift)

        # reverse substitution
        idx = shifted_alpha.index(ch)
        dec = ALPHABET[idx]

        # plugboard out
        dec = apply_plugboard(dec, swaps)

        result.append(dec)

        # rotor steps
        shift += 1

    return "".join(result)


# -------------------------
# GAME LOOP
# -------------------------
if __name__ == "__main__":
    print("=== ENIGMA KEYWORD CIPHER GAME ===")

    keyword = input("Enter keyword: ").strip().upper()
    swaps_input = input("Enter plugboard swaps (e.g. AB CD EF): ").upper().split()
    swaps = [(pair[0], pair[1]) for pair in swaps_input]

    while True:
        mode = input("\nEncrypt (E) or Decrypt (D) or Quit (Q): ").upper()
        if mode == "Q":
            break

        message = input("Enter message: ")

        if mode == "E":
            print("Ciphertext:", enigma_keyword_encrypt(message, keyword, swaps))
        elif mode == "D":
            print("Plaintext:", enigma_keyword_decrypt(message, keyword, swaps))
        else:
            print("Invalid option.")

import os

def load_dictionary(file_path='dictionary.txt'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dict_path = os.path.join(script_dir, file_path)
    try:
        with open(dict_path, 'r') as file:
            return set(word.strip().upper() for word in file if len(word.strip()) > 2)
    except FileNotFoundError:
        print(f"Dictionary file not found: {dict_path}")
        print("Please ensure 'dictionary.txt' is in the same directory as this script.")
        return set()

def build_bad_char_heuristic(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = max(1, len(pattern) - i - 1)
    return bad_char

def boyer_moore_search(text, pattern):
    bad_char = build_bad_char_heuristic(pattern)
    m, n = len(pattern), len(text)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return True  # Pattern found
        i += bad_char.get(text[i + m - 1], m)
    return False

def caesar_cipher_decoder(ciphertext, words):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    best_shift = 0
    max_words_found = 0
    all_decryptions = []
    
    for shift in range(26):
        plaintext = ''
        for char in ciphertext.upper():
            if char in alphabet:
                index = (alphabet.index(char) - shift) % 26
                plaintext += alphabet[index]
            else:
                plaintext += char
        
        words_found = sum(1 for word in words if boyer_moore_search(plaintext, word))
        all_decryptions.append((shift, plaintext))
        
        if words_found > max_words_found:
            max_words_found = words_found
            best_shift = shift
    
    return best_shift, all_decryptions[best_shift][1], max_words_found, all_decryptions

def main():
    ciphertext = input("Enter the ciphertext: ").strip()
    
    dictionary = load_dictionary()
    if not dictionary:
        return

    best_shift, best_decryption, word_count, all_decryptions = caesar_cipher_decoder(ciphertext, dictionary)

    print("\nAll Decryptions:")
    for shift, plaintext in all_decryptions:
        print(f"Shift {shift}: {plaintext}")

    print("\nBest Decryption (Dictionary-based):")
    print(f"Best shift: {best_shift}")
    print(f"Decoded text: {best_decryption}")
    print(f"Words found: {word_count}")

if __name__ == "__main__":
    main()

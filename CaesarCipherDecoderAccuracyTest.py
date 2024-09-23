import random
from CaesarDecoder import caesar_cipher_decoder, load_dictionary

def generate_realistic_text(dictionary, num_words):
    return ' '.join(random.choice(list(dictionary)) for _ in range(num_words))

def caesar_encrypt(text, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for char in text.upper():
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + shift) % 26]
        else:
            result += char
    return result

def generate_test_cases(dictionary, num_cases, min_words=5, max_words=20):
    test_cases = []
    for _ in range(num_cases):
        plaintext = generate_realistic_text(dictionary, random.randint(min_words, max_words))
        shift = random.randint(1, 25)
        ciphertext = caesar_encrypt(plaintext, shift)
        test_cases.append((plaintext, ciphertext, shift))
    return test_cases

def test_decoder_accuracy(test_cases, dictionary):
    correct_decryptions = 0
    total_cases = len(test_cases)
    
    for plaintext, ciphertext, actual_shift in test_cases:
        best_shift, decryption, _, _ = caesar_cipher_decoder(ciphertext, dictionary)
        if best_shift == actual_shift:
            correct_decryptions += 1
    
    accuracy = (correct_decryptions / total_cases) * 100
    return accuracy

def main():
    dictionary = load_dictionary()
    num_test_cases = 100  # You can adjust this number
    
    print("Generating realistic test cases...")
    test_cases = generate_test_cases(dictionary, num_test_cases)
    
    print("Testing decoder accuracy...")
    accuracy = test_decoder_accuracy(test_cases, dictionary)
    
    print(f"Decoder Accuracy: {accuracy:.2f}%")
    print(f"Total test cases: {num_test_cases}")

if __name__ == "__main__":
    main()

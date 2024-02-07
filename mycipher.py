import sys

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            # Convert to uppercase
            char = char.upper()
            # Shift the letter
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += shifted_char

    return encrypted_message

def print_blocks_of_five(encrypted_message):
    for i in range(0, len(encrypted_message), 5):
        print(encrypted_message[i:i+5], end=' ')

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar_cipher.py <shift>")
        sys.exit(1)

    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("Invalid shift value. Please provide an integer.")
        sys.exit(1)

    # Read message from the keyboard
    for line in sys.stdin:
        message = line.strip()

    # Convert the message to uppercase and apply Caesar Cipher
    encrypted_message = caesar_cipher(message, shift)

    # Print the final encoded message in blocks of five letters
    print_blocks_of_five(encrypted_message)

if __name__ == "__main__":
    main()

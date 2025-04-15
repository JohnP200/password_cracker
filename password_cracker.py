import hashlib

def crack_password(hash_to_crack, wordlist):
    print("[*] Starting password cracking...\n")

    for word in wordlist:
        word = word.script()
        word_hash = hashlib.sha256(word.encode()).hexdigest()

        if word_hash == hash_to_crack:
            print(f"[+] Password found: {word}")
            return word
        print("[-] Password not found.")
        return None

if __name__ == "__main__":
    hash_input = input("Enter the SHA-256 hash to crack: ")
    # Sample wordlist (can be expanded)
    words = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey"]

    crack_password(hash_input, words)
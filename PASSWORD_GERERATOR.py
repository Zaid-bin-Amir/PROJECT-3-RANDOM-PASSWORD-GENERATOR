import math
import secrets
import string

MIN_LENGTH = 8
RECOMMENDED_LENGTH = 15
MAX_LENGTH = 64


def read_length():
    while True:
        raw = input(f"Enter password length ({MIN_LENGTH}-{MAX_LENGTH}, recommended {RECOMMENDED_LENGTH}+): ").strip()
        if not raw.isdigit():
            print("Invalid input. Please enter a whole number.\n")
            continue
        length = int(raw)
        if length < MIN_LENGTH:
            print(f"Too short. Minimum length is {MIN_LENGTH}.\n")
            continue
        if length > MAX_LENGTH:
            print(f"Too long. Maximum length is {MAX_LENGTH}.\n")
            continue
        return length


def read_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with y or n.\n")


def character_groups(use_symbols):
    groups = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_symbols:
        groups.append(string.punctuation)
    return groups


def generate_password(length, use_symbols=False):
    groups = character_groups(use_symbols)
    pool = "".join(groups)
    characters = [secrets.choice(group) for group in groups]
    characters += [secrets.choice(pool) for _ in range(length - len(characters))]
    secrets.SystemRandom().shuffle(characters)
    return "".join(characters), len(pool)


def calculate_entropy(length, pool_size):
    return length * math.log2(pool_size)


def rate_strength(entropy):
    if entropy < 50:
        return "Weak"
    if entropy < 70:
        return "Fair"
    if entropy < 100:
        return "Strong"
    return "Excellent"


def main():
    print("=" * 46)
    print("      DecodeLabs Random Password Generator")
    print("=" * 46)

    length = read_length()
    use_symbols = read_yes_no("Include special characters? (y/n): ")
    count = 1
    if read_yes_no("Generate more than one password? (y/n): "):
        while True:
            raw = input("How many (1-10)? ").strip()
            if raw.isdigit() and 1 <= int(raw) <= 10:
                count = int(raw)
                break
            print("Please enter a number between 1 and 10.\n")

    print()
    for index in range(1, count + 1):
        password, pool_size = generate_password(length, use_symbols)
        entropy = calculate_entropy(length, pool_size)
        print(f"Password {index}: {password}")
        print(f"  Pool size : {pool_size}")
        print(f"  Entropy   : {entropy:.1f} bits")
        print(f"  Strength  : {rate_strength(entropy)}\n")

    if length < RECOMMENDED_LENGTH:
        print(f"Tip: NIST recommends at least {RECOMMENDED_LENGTH} characters for high-security use.")


if __name__ == "__main__":
    main()
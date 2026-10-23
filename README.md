# PROJECT-3-RANDOM-PASSWORD-GENERATOR# Random Password Generator

**Project 3 | Python Programming | DecodeLabs Industrial Training Kit (Batch 2026)**

A command-line tool that asks the user for a password length and generates a random, complex password using letters, numbers and (optionally) special characters. Each password is shown with its entropy in bits and a strength rating.

## Features

- Input validation: only whole numbers between 8 and 64 are accepted, so bad input never crashes the program
- Character sets taken from Python's built-in `string` module instead of typing them by hand
- Cryptographically secure randomness using the `secrets` module (not `random`)
- Guarantees at least one lowercase letter, one uppercase letter, one digit and, if enabled, one symbol
- Efficient string building with `"".join()` instead of repeated `+=`
- Entropy calculation using `E = L x log2(R)` and a strength rating (Weak, Fair, Strong, Excellent)
- Option to generate up to 10 passwords in one run
- NIST-based tip when the chosen length is below 15 characters

## Requirements

- Python 3.6 or newer (the `secrets` module was introduced in 3.6)
- No external packages needed

## How to Run

1. Open a terminal in the folder that contains `password_generator.py`
2. Run:

```
python password_generator.py
```

If that does not work, try `python3 password_generator.py` or `py password_generator.py` (Windows).

## Example Session

```
==============================================
      DecodeLabs Random Password Generator
==============================================
Enter password length (8-64, recommended 15+): 16
Include special characters? (y/n): y
Generate more than one password? (y/n): n

Password 1: S6L^Kv6#%RL[#;:P
  Pool size : 94
  Entropy   : 104.9 bits
  Strength  : Excellent
```

## How It Works

The program follows the Input-Process-Output structure.

| Phase | What happens | Function |
|-------|--------------|----------|
| Input | Read and validate the length and options | `read_length()`, `read_yes_no()` |
| Process | Build the character pool, pick characters securely, shuffle, join | `character_groups()`, `generate_password()` |
| Output | Calculate entropy, rate strength, display results | `calculate_entropy()`, `rate_strength()`, `main()` |

### Why `secrets` and not `random`

The `random` module uses the Mersenne Twister, a deterministic generator. If an attacker knows the seed, the output can be predicted. The `secrets` module uses the operating system's secure entropy source, which makes the output unpredictable and suitable for passwords and tokens.

### Why `.join()` and not `+=`

Python strings are immutable, so every `password += char` creates a brand new string in memory, which is O(N^2) overall. Collecting characters in a list and calling `"".join()` once allocates memory a single time and runs in O(N).

### Entropy and strength

Entropy is calculated as:

```
E = L x log2(R)
```

where `L` is the password length and `R` is the size of the character pool (62 for letters and digits, 94 when symbols are included).

| Entropy (bits) | Rating |
|----------------|--------|
| Below 50 | Weak |
| 50 to 69 | Fair |
| 70 to 99 | Strong |
| 100 and above | Excellent |

### Length over complexity

Following the 2024 NIST guidelines (SP 800-63-4), length matters more than forced complexity. That is why the program recommends 15 or more characters and supports lengths up to 64.

## Project Structure

```
.
├── password_generator.py
└── README.md
```

## Possible Improvements

- Let the user exclude look-alike characters such as `O`, `0`, `l` and `1`
- Add a passphrase mode made of random words
- Copy the generated password to the clipboard
- Check generated passwords against a list of known compromised passwords
- Save the project as a command-line tool with `argparse` flags

## Author

Built as part of the DecodeLabs Python Programming internship, Project 3.

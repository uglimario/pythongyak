import math
from itertools import permutations

def calculate_factorial(n):
    return math.factorial(n)

def generate_variations(elements):
    variations = []
    for p in permutations(elements):
        variations.append(''.join(p))
    return variations

def main():
    # Bemeneti karakterek megadása
    input_characters = input("Karakterek: ")

    # Faktoriálisok kiszámolása
    for i, char in enumerate(input_characters):
        factorial = calculate_factorial(i+1)
        print(f"{char}! = {factorial}")

    # Variációk készítése
    all_variations = generate_variations(input_characters)

    # Eredmények kiíratása
    for i, variation in enumerate(all_variations):
        print(f"Variáció {i+1}: {variation}")

if __name__ == "__main__":
    main()
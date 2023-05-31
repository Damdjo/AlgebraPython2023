word = input(f"Unesite riječ za koju mislite da je palindrom:\n")

wordReversed = word[::-1]

if word == wordReversed:
    print(f"Riječ {word} JE palindrom")
else:
    print(f"Riječ {word} NIJE palindrom")


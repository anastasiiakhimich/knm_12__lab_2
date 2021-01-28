first_or_second_program = input("first or second:")


def a(first):
    ready_text = first.split()
    for i in ready_text:
        if len(i) < 3:
            ready_text.pop(ready_text.index(i))
        i.strip()
        if not i[len(i) - 1].isalnum():
            ready_text[ready_text.index(i)] = i[:len(i) - 1]
    ready_text.sort(key=str.lower)
    for i in ready_text:
        print(i.capitalize())


def b(first):
    ready_text = first.casefold()

    alpha = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
             "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
             "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for i in range(len(first)):
        if not ready_text[i].isalpha():
            continue
        alpha[ready_text[i]] += 1
    for x, y in alpha.items():
        print(x, "=", y)


if first_or_second_program == "first":
    a(input("Enter text:"))
elif first_or_second_program == "second":
    b(input("Enter text:"))
else:
    print("ERROR")

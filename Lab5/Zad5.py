import keyword

slowa = ["for", "print", "break", "done", "bad"]

for s in slowa:
    print(f"{s}: {keyword.iskeyword(s)}")

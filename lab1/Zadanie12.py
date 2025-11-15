

x = float(input("Podaj wartość x: "))

# --- a(x) ---
if x > 0:
    a = 2 * x
elif x == 0:
    a = 0
else:  # x < 0
    a = -3 * x

# --- b(x) ---
if x >= 1:
    b = x ** 2
else:  # x < 1
    b = x

# --- c(x) ---
if x > 2:
    c = 2 + x
elif x == 2:
    c = 8
else:  # x < 2
    c = x - 4

print(f"a({x}) = {a}")
print(f"b({x}) = {b}")
print(f"c({x}) = {c}")

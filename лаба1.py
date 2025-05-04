def hamming_distance (s, t):
    return -1 if len(s) != len(t) else sum(a != b for a, b in zip(s, t))
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = hamming_distance (s, t)
print(f"Расстояние Хэмминга равно: {distance}")


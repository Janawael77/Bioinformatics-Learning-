s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = 0

for i in range(len(s)):
    if s[i] != t[i]:
        distance = distance + 1

print(distance)

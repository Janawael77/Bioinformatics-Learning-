s = """AAACCCGGT"""


old_letters = "ATCG"
new_letters = "TAGC"

rule = str.maketrans(old_letters, new_letters)
complement = s.strip().translate(rule)

reverse_complement = complement[::-1]

print(reverse_complement)

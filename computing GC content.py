dataset = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

highest_id = ""
highest_gc = 0.0

lines = dataset.strip().split(">")
for line in lines:
    if line:
        parts = line.strip().split("\n")
        rosalind_id = parts
        
        dna_sequence = "".join(parts[1:])
        
        g_count = dna_sequence.count("G")
        c_count = dna_sequence.count("C")
        total_len = len(dna_sequence)
        
        gc_content = (g_count + c_count) / total_len * 100
        
        if gc_content > highest_gc:
            highest_gc = gc_content
            highest_id = rosalind_id

print(highest_id)
print(highest_gc)

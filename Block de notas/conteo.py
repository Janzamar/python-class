def count_bases(dna):
    bases = "ATGC"
    for base in bases: 
        numbases =dna.upper().count(base)
        print(f"{base} {numbases}")

count_bases("GACTGTCAGG")
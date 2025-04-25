def at_content(dna, sig_figs):

    dna = dna.upper()
    length = len(dna)
    a_count = dna.count("A")
    t_count = dna.count("T")
    at_content = (a_count + t_count)/length
    return round(at_content, sig_figs)
    
# resultado = at_content("GATGCTAGCTAGCTGATCGATGCTAGCTAGCCCTAGCAA", 1)
# print(resultado)

#resultado = at_content("AGTGTGATGATGTACACACACAGTTAGAGTGA", 2)
# print(resultado)

#resultado = at_content(sig_figs= 2, dna="AGTGTGATGATGTACACACACAGTTAGAGTGA")
# print(resultado)

#testing temporal, evalua el funcionamiento de at_content
assert at_content("ATGC", 1) == 0.5

assert at_content("ATGCNNNN", 1) == 0.5
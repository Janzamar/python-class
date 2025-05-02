def count_bases(dna, sig_figs):
   dna =dna.upper()
   conteo = {
      "A": dna.count("A")
      "C": dna.count("C")
      "T": dna.count("T")
      "G": dna.count("G")

   }
   return conteo

dna = "AGTGTCGATAACATGATACATA"
resultado = count_bases(dna)
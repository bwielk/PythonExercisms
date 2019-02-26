def to_rna(dna_strand):
    map_of_nucleotids = {"A" : "U",
                         "T" : "A",
                         "G" : "C",
                         "C" : "G"}
    transcribed_RNA = ''
    for char in dna_strand.upper():
            if map_of_nucleotids.__contains__(char):
                transcribed_RNA += map_of_nucleotids[char]
    return transcribed_RNA

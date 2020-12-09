def hamming(a,b):
    return sum([ 1 for c,d in zip(a,b) if c != d ])

print(hamming('AGCAGCGCAAGTACCTTGGCTATCTGGCACCCCCTGTATGACTTTCATTGCGGCACACGATGGGATCTTCTCGAGGACAACTTGATTTTGCCAGTATAACAGGACCCTATTATTGAGTTATAACATGCGCTGTGCGAGCCTGTCCTGCACGAGAAGTCGGCCGGGAAGCTCTTGCTAGAATTACAAGGCCACGGCTCTAGGGTTCAAGCTTGAGCGTGCGGGTACGTCTTTGAGTGTTGCGCACCACAAGTCAGCGTAGTCTTATCGCCAGTGGGCACGACCAATCACCCGCCTCCTGGAGGCGTAAGGTCTGGTGGAATTCCAGATATAGAGAAGAGCTAGACGGGGACATGATCTCAGGCTACGCTCAACACCGTTCATCTCAGACACGCTATAGATAGGTACCTGACGAACTGTAGGCGAGGGTCCCACCTTTGCCCTTTCGCCTGGGGGTGACATAAAATGCGGAAAACATAGGGTAGAGGGATTCACGGCGTCTTCTGGTTTCCGGAGTTTATCCAGCTATGTGTTCTTGTCGCTACTCTTTCTTGTTTGTCCGTCGATAGATGTTGAGACTCGAGGCCGTCACGGGGTTAATGCGCCATATTTCCTACATTGCCAAAGACTGGAACGTTGTAATTTACCTACTCGTACGTACGATAACAAAGTCAGCGCGACAAGCACCTTACACGTCTATACAGAGTGGCAGGCGACAACTAACCGTAGACACTTTATTAGGGACCCCAAGTCACGATTATACTCCACAAGTTACGCCCAAAGGAGAGTACTCGCAGCAATTAGGGCTTTACCATCGAGATACCGGTCTGGGTGAGTTTCCTGGGCACTATACGCGGCCACAATCCATAAGTTAATGGTGGTTAAAATCCGTCGGTGCTCATTGGAAC','CCGTGGCTGAGTTAAATCGTTTTCGGGTAACTCGGCGCTACGTATCATGCTTGTCCCGGCTTCTCCAGTATCGATCGCGACTCGGATCAGCAACCAGAATCCCAACCTTAAATAGTGTTATAAGATGGCCAGTGCTACCATCGCAAGCACGATCACCCCACTTCGATTCACGGGCAAGCTTACCATAAGAGTAGTTCTAGTACCGTAGTGGGCGGCTACGGGAGCGTGTGGCAGGTGTGCTAATCACATGTCGGCACTGTAGAAACGCGTCTGGGTGCCATGATGCGCTTGTGACTAGGCGTGGTAGGGAAAGGTGGACATAAAGATAAATAAGCCAGCCAGTCGGACGGAAGATAGCCCTCGACGCGGAAACCGGAGCCTCTCATAGACGATAGGGCATAGCATCTATCTAATTGCCGAAAGGCATCCCTTCAACGATCTTTTGCCGGAGGGTCATCGGGAATACAGAAAACCTGCGATACTGTTAAAGACGTCCTCTGGGCGAAGCTCCAGTTTAAGTAGCTAAGCTTTCATTAGACCTCTATTGCTGTTTAGTCAGGACGTAGGAGTTAGGCTTGACGGAAACTTTTGCTTCGGCAGTGCATATTAGCTAATTCAGGCAAGAGGGAGATATCGCTGTATACCTTGTCGTAACTAGAAGAATACTGTCTCCGCGCCGAGCACAAAGTCCCTCTTTACTGAGTGGAAGACGGGAGCTGCTCGTAATCCATTTAGTTGGTGTGGCAAGTCACGACGAACCCTTAGACGTTGGGCCCACAGGGGCTTAGTCCCCTAAATAGGGTGGGTACCGTTCAGATAATGTTGCGGGTTCGTTTGTGGGGTAGTAAAGGCTGCCATTTTCCACAGGATAACTATCTCTACCCTCCTTCGATCAACATAGGAAC'))
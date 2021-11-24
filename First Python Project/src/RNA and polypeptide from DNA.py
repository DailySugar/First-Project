dna = "GGTAATGCTAGCTTGACCTAGCCCTGACATCGATATCGACTAGCTG"

rna_translation = {'G':'C','C':'G','A':'U','T':'A'}
amino_translation = {
    'U':{
        'U':{'U':'F','C':'F','A':'L','G':'L'},
        'C':{'U':'S','C':'S','A':'S','G':'S'},
        'A':{'U':'Y','C':'Y','A':-1,'G':-1},
        'G':{'U':'C','C':'C','A':-1,'G':'W'}},
    'C':{
        'U':{'U':'L','C':'L','A':'L','G':'L'},
        'C':{'U':'P','C':'P','A':'P','G':'P'},
        'A':{'U':'H','C':'H','A':'Q','G':'Q'},
        'G':{'U':'R','C':'R','A':'R','G':'R'}},
    'A':{
        'U':{'U':'I','C':'I','A':'I','G':'M'},
        'C':{'U':'T','C':'T','A':'T','G':'T'},
        'A':{'U':'N','C':'N','A':'K','G':'K'},
        'G':{'U':'S','C':'S','A':'R','G':'R'}},
    'G':{
        'U':{'U':'V','C':'V','A':'V','G':'V'},
        'C':{'U':'A','C':'A','A':'A','G':'A'},
        'A':{'U':'D','C':'D','A':'E','G':'E'},
        'G':{'U':'G','C':'G','A':'G','G':'G'}}
    }

def decode_amino(rna):
    """Translates RNA sequence to amino acids, treating the first
    three nucleotides as the first codon."""
    polypeptide = ""
    for y in range(0, len(rna) - 2, 3):
        # print(rna[y:y + 3], amino_translation[rna[y]][rna[y + 1]][rna[y + 2]])
        amino_acid = amino_translation[rna[y]][rna[y + 1]][rna[y + 2]]
        if amino_acid == -1:
            return polypeptide
        else:
            polypeptide += amino_translation[rna[y]][rna[y + 1]][rna[y + 2]]
    return polypeptide


def translate(rna):
    """Finds the start codon and translates the RNA sequence from there."""
    try:
        for x in range(len(rna)):
                if rna[x] == 'A':
                    if rna[x + 1] == 'U':
                        if rna[x + 2] == 'G':
                            return decode_amino(rna[x:])
    except:
        return None


def transcript_antisense_strand(dna):
    """Finds the RNA transcript of a DNA sequence given the antisense strand."""
    rna = ""
    for x in range(len(dna) - 1, -1, -1):
        rna += rna_translation[dna[x]]
    return rna


def transcript_sense_strand(dna):
    """Finds the RNA transcript of a DNA sequence given the sense strand."""
    return dna.replace("T","U")


def dna_to_polypeptide(dna):
    """Finds the amino acid sequence given the sense strand of DNA without introns."""
    return translate(transcript_sense_strand(dna))

test = "atgtctt caacaaagga tatggaattttctacttctg gtcatgctta cactgataca gggaaagcat caggcaacct agaaaccaaatataaggtct gtaactatgg acttaccttc acccagaaat ggaacacaga caatactctagggacagaaa tctcttggga gaataagttg gctgaagggt tgaaactgac tcttgataccatatttgtac cgaacacagg aaagaagagt gggaaattga aggcctccta taaacgggattgttttagtg ttggcagtaa tgttgatata gatttttctg gaccaaccat ctatggctgggctgtgttgg ccttcgaagg gtggcttgct ggctatcaga tgagttttga cacagccaaatccaaactgt cacagaataa tttcgccctg ggttacaagg ctgcggactt ccagctgcacacacatgtga acgatggcac tgaatttgga ggttctatct accagaaggt gaatgagaagattgaaacat ccataaacct tgcttggaca gctgggagta acaacacccg ttttggcattgctgctaagt acatgctgga ttgtagaact tctctctctg ctaaagtaaa taatgccagcctgattggac tgggttatac tcagaccctt cgaccaggag tcaaattgac tttatcagctttaatcgatg ggaagaactt cagtgcagga ggtcacaagg ttggcttggg atttgaactggaagcttaat gtggtttgag gaaagcatca gatttgtccc tggaagtgaa gagaaatgaacccactatgt tttggcctta aaattcttct gtgaaatttc aaaagtgtga actttttattcttccaaaga attgtaatcc tccccacact gaagtctagg ggttgcgaat ccctcctgagggagatgctt gaaggcatgc ctggaagttg tcatgtttgt gccacgtttc agttcagttctgaagtgtta ttaaatgtgt tcctcagcga cagtgtagcg tcatgttaga ggagacgatctgacccacca gtttgtacat cacgtcctgc atgtcccaca ccattttttc atgaccttgtaatatactgg tctctgtgct atagtggaat ctttggtttt gcatcatagt aaaataaaataaacccatca catttggaac ataa".replace(" ", "").upper()
print(dna_to_polypeptide(test))




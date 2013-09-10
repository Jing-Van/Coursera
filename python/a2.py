def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1)>len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2)>0:
        return True
    else:
        return False

def is_valid_sequence(dnap):
    """ (str) -> bool

    The parameter is a potential DNA sequence.
    Return True if and only if the DNA sequence is valid 
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ACEGI')
    False
    """
    for char in dnap:
        if char not in 'ATCG':
            return False
    return True

def insert_sequence(s1,s2,i):
    """(str, str, int) -> str  
    The first two parameters are DNA sequences and the third parameter is an index. 
    Return the DNA sequence obtained by inserting the second DNA sequence into the 
    first DNA sequence at the given index. (You can assume that the index is valid.)

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('CCGG','AT',1) 
    'CATCGG'
    >>> insert_sequence('CCGG','AT',0)
    'ATCCGG'
    >>> insert_sequence('CCGG','AT',4)
    'CCGGAT'
    """
    l=len(s1) 
    return s1[0:i]+s2+s1[i:l]

def get_complement(c):
    """(str) -> str
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G').
    Return the nucleotide's complement.

    """
    complement=''
    if c=='A':
        complement='T'
    elif c=='T':
        complement='A'
    elif c=='C':
        complement='G'
    else:
        complement='C'
    return complement

def get_complementary_sequence(s):
    """(str) -> str
    The parameter is a DNA sequence. 
    Return the DNA sequence that is complementary to the given DNA sequence.
    >>> get_complementary_sequence('AT')
    'TA'
    
    >>> get_complement('ACGTACG')
    'TGCATGC'
    """
    complement=''
    for char in s:
        complement+=get_complement(char)
    return complement

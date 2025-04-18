#PROGRAM TO COUNT DNA SEQUENCE

#FUNCTION1 - GET INPUT FROM USER
def get_input():
    sequence = input ('Enter your sequence:')
    sequence = sequence.upper()
    return sequence

#FUNCTION 2 - CLEANED DNA
def cleaned_dna(seq):
    cleaned = ""
    for base in seq.upper():
        if base in ["A", "T", "C", "G"]:
            cleaned += base
    return cleaned

#FUNCTION2 - COUNT THE BASES
def count_bases(dna):
    count_A = 0
    count_T = 0
    count_C = 0
    count_G = 0

    for base in dna:
        if base == "A":
            count_A += 1
        elif base == "T":
            count_T += 1
        elif base == "C":
            count_C += 1
        elif base == "G":
            count_G += 1
    print("A:", count_A)
    print("T:", count_T)
    print("C:", count_C)
    print("G:", count_G)

    return count_A, count_T, count_C, count_G
#FUNCTION3 - CHECK FOR PERCENTAGE OF GC CONTENT
def gc_content(dna):
    count_C = 0
    count_G = 0
    for base in dna:
        if base == "C":
            count_C += 1
        elif base == "G":
            count_G += 1
    total_bases = len(dna)
    gc_count= count_C + count_G
    gc_percent = round((gc_count / total_bases) * 100, 2)
    return gc_percent

dna = get_input()
dna = cleaned_dna(dna)
print("\nCleaned DNA:", dna)
count_A, count_T, count_C, count_G = count_bases(dna)
gc_percent = gc_content(dna)

print("\n🔬 DNA Analysis Report:")
print("• A:", count_A)
print("• T:", count_T)
print("• C:", count_C)
print("• G:", count_G)
print("• GC Content:", gc_percent, "%")


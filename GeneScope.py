def analyze_dna(sequence):

    sequence = sequence.upper()

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    length = len(sequence)

    gc_content = ((g + c) / length) * 100

    reverse_seq = sequence[::-1]

    complement = ""

    for base in sequence:

        if base == "A":
            complement += "T"

        elif base == "T":
            complement += "A"

        elif base == "G":
            complement += "C"

        elif base == "C":
            complement += "G"

    reverse_complement = complement[::-1]

    return {
        "Length": length,
        "A Count": a,
        "T Count": t,
        "G Count": g,
        "C Count": c,
        "GC Content": round(gc_content, 2),
        "Reverse Sequence": reverse_seq,
        "Complement": complement,
        "Reverse Complement": reverse_complement
    }


dna = input("Enter DNA Sequence: ")

result = analyze_dna(dna)

for key, value in result.items():
    print(key, ":", value)

print("\nComplexity Analysis")
print("Best Case : O(n)")
print("Average Case : O(n)")
print("Worst Case : O(n)")
print("Space Complexity : O(n)")

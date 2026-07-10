"""
==========================================
BioForge - DNA Sequence Analysis Toolkit
Author: Aman Yadav
Version: 0.4
==========================================
"""

# Import functions
from validation import validate_dna

from dna import (
    get_length,
    count_bases,
    gc_content,
    at_content,
    reverse_sequence,
    reverse_complement
)


def main():

    print("=" * 60)
    print("🧬 BioForge - DNA Sequence Analysis Toolkit")
    print("=" * 60)

    # User Input
    dna_sequence = input("Enter DNA Sequence: ").strip().upper()

    # Validate Sequence
    is_valid, invalid_bases = validate_dna(dna_sequence)

    # If sequence is valid
    if is_valid:

        print("\n✅ Valid DNA Sequence\n")

        # Length
        print(f"Sequence Length : {get_length(dna_sequence)}")

        # Base Counts
        counts = count_bases(dna_sequence)

        print(f"A : {counts['A']}")
        print(f"T : {counts['T']}")
        print(f"G : {counts['G']}")
        print(f"C : {counts['C']}")

        # GC Content
        print(f"GC Content : {gc_content(dna_sequence):.2f}%")

        # AT Content
        print(f"AT Content : {at_content(dna_sequence):.2f}%")

        # Reverse Sequence
        print(f"Reverse Sequence : {reverse_sequence(dna_sequence)}")

        # Reverse Complement
        print(f"Reverse Complement : {reverse_complement(dna_sequence)}")

    # If sequence is invalid
    else:

        print("\n❌ Invalid DNA Sequence")
        print("\nInvalid Bases Found:")

        for base in invalid_bases:
            print(f"• {base}")


# Program starts here
if __name__ == "__main__":
    main()
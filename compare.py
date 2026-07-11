"""
=====================================================
BioForge Comparison Module
Author  : Suryansh Singh Yadav
Version : 1.0
=====================================================
"""

from Bio.Seq import Seq

from protein import (
    translate_dna,
    protein_length,
    has_start_codon,
    has_stop_codon
)


def compare_translation(sequence):

    sequence = sequence.upper()

    print("\n" + "=" * 60)
    print("DNA Translation Comparison")
    print("=" * 60)

    manual = translate_dna(sequence)

    bio = str(Seq(sequence).translate())

    print("\nDNA Sequence")
    print("-" * 60)
    print(sequence)

    print("\nManual Translation")
    print("-" * 60)
    print(manual)

    print("\nBiopython Translation")
    print("-" * 60)
    print(bio)

    print("\nComparison")
    print("-" * 60)

    if manual == bio:

        print("✅ Translation Matched")

    else:

        print("❌ Translation Not Matched")

    print("\nProtein Length :", protein_length(manual))

    print("Start Codon :", has_start_codon(sequence))

    print("Stop Codon :", has_stop_codon(sequence))
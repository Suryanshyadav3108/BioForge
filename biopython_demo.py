"""
==================================
BioForge Biopython Demo
==================================
"""

from Bio.Seq import Seq


dna = Seq("ATGGCTTTTGAA")

print("DNA")

print(dna)

print()

print("RNA")

print(dna.transcribe())

print()

print("Protein")

print(dna.translate())

print()

print("Reverse Complement")

print(dna.reverse_complement())
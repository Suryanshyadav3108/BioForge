from protein import translate_dna
from protein_properties import (
    analyze_protein,
    protein_status
)

dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

protein = translate_dna(dna)

result = analyze_protein(protein)

print("\nProtein Sequence:")
print(protein)

print("\nProtein Length:", result["length"])

print("Molecular Weight:",
      result["molecular_weight"])

print("Isoelectric Point:",
      result["isoelectric_point"])

print("Aromaticity:",
      result["aromaticity"])

print("Instability Index:",
      result["instability_index"])

print("GRAVY:",
      result["gravy"])

print(
    "Status:",
    protein_status(
        result["instability_index"]
    )
)
from pipeline import run_complete_analysis

sequence = input("Enter DNA Sequence:\n")

result = run_complete_analysis(sequence)

print("\n========== DNA ==========")

print("Length :", result["length"])

print("GC % :", result["gc"])

print("AT % :", result["at"])

print("\n========== RNA ==========")

print(result["rna"])

print("\n========== Protein ==========")

print(result["protein"])

print("\n========== ORF ==========")

print(result["orf"])

print("\n========== Restriction ==========")

print(result["restriction"])

print("\n========== Primer ==========")

print(result["primer"])

print("\n========== Codons ==========")

print(result["codons"])
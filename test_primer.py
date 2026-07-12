from primer import design_primers, primer_quality

sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

result = design_primers(sequence)

print("Forward Primer :", result["forward"])
print("Reverse Primer :", result["reverse"])
print("Length :", result["length"])
print("GC % :", result["gc"])
print("Tm :", result["tm"])
print("Quality :", primer_quality(result["forward"]))
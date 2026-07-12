from blast import run_blast, parse_blast

sequence = input("Enter DNA Sequence:\n").strip().upper()

if len(sequence) < 100:
    print("\n❌ Sequence too short for BLAST.")
    print("Please enter at least 100 nucleotides.")
    exit()

xml = run_blast(sequence)

results = parse_blast(xml)

if len(results) == 0:

    print("\n⚠ No BLAST hits found.")
    print("Try another DNA sequence.")

else:

    print("\nTop 5 Matches")
    print("=" * 60)

    for item in results[:5]:

        print(item["title"])
        print("Identity :", item["identity"], "%")
        print("Coverage :", item["coverage"])
        print("Score :", item["score"])
        print("E-value :", item["expect"])
        print("-" * 60)
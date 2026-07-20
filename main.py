"""
=====================================================
BioForge - Professional Bioinformatics Toolkit
By  : Suryansh Singh Yadav
Version : 1.0
=====================================================
"""

from validation import validate_dna

from dna import (
    get_length,
    count_bases,
    gc_content,
    at_content,
    reverse_sequence,
    reverse_complement
)

from fasta import read_fasta

from report import generate_report

from visualization import (
    plot_base_composition,
    plot_gc_at
)


from pdf_generator import (
    generate_pdf_report
)

from rna import (
    transcribe_dna,
    reverse_rna,
    rna_length,
    count_rna_bases
)

from protein import (
    translate_dna,
    protein_length,
    amino_acid_count,
    has_start_codon,
    has_stop_codon
)

from compare import compare_translation

from orf import (
    find_orf,
    orf_length,
    has_orf
)

from mutation import (
    find_mutations,
    mutation_percentage,
    mutation_summary,
    compare_codons,
    protein_change
)

from ncbi import (
    fetch_sequence,
    save_fasta
)

# ==========================================
# Banner
# ==========================================

def show_banner():

    print("\n")
    print("=" * 70)
    print("🧬                BioForge v3.2")
    print("Professional Bioinformatics Toolkit")
    print("=" * 70)


# ==========================================
# Menu
# ==========================================

def show_menu():

    print("\nChoose an Option\n")

    print("1. DNA Analysis")
    print("2. Read FASTA File")
    print("3. DNA → RNA")
    print("4. DNA → Protein")
    print("5. Compare Manual vs Biopython")
    print("6. ORF Finder")
    print("7. Mutation Analysis")
    print("8. NCBI Downloader")
    print("9. Exit")


# ==========================================
# DNA Analysis
# ==========================================

def analyze_dna(sequence, header="Manual DNA"):


    valid, invalid = validate_dna(sequence)


    if not valid:

        print("\n❌ Invalid DNA Sequence")

        print("\nInvalid Characters")

        for item in invalid:

            print("-", item)

        return



    length = get_length(sequence)


    counts = count_bases(sequence)


    gc = gc_content(sequence)


    at = at_content(sequence)


    reverse = reverse_sequence(sequence)


    reverse_comp = reverse_complement(sequence)



    print("\n✅ DNA Analysis Completed")


    print("\nSequence Name :", header)


    print("\nLength :", length)



    print("\nBase Count")

    print("--------------------")


    print("A :", counts["A"])

    print("T :", counts["T"])

    print("G :", counts["G"])

    print("C :", counts["C"])



    print("\nGC Content :", round(gc,2), "%")

    print("AT Content :", round(at,2), "%")



    print("\nReverse Sequence")

    print(reverse)



    print("\nReverse Complement")

    print(reverse_comp)



    # ======================================
    # Professional Report
    # ======================================


    choice = input(
        "\nGenerate Professional PDF Report (Y/N): "
    ).upper()



    if choice == "Y":


        print("\nGenerating Graphs...")


        # Base Composition Graph

        base_graph = plot_base_composition(
            counts
        )


        # GC AT Graph

        gc_graph = plot_gc_at(
            gc,
            at
        )



        # ==================================
        # ORF Analysis Data
        # ==================================


        orf_result = find_orf(
            sequence
        )


        if orf_result:


            orf_data = {

                "ORF Found":
                True,


                "ORF Length":
                orf_length(
                    orf_result
                ),


                "ORF Sequence":
                orf_result

            }


        else:


            orf_data = {

                "ORF Found":
                False

            }



        print("\nGenerating PDF...")



        generate_pdf_report(

            "BioForge_Report.pdf",


            header,


            sequence,


            counts,


            round(gc,2),


            round(at,2),


            [

                base_graph,

                gc_graph

            ],


            orf_data=orf_data

        )



        print(
            "\n✅ Professional Report Generated Successfully"
        )


        print(
            "File : BioForge_Report.pdf"
        )

# ==========================================
# Manual DNA Input
# ==========================================

def manual_input():

    sequence = input("\nEnter DNA Sequence : ").upper().strip()

    analyze_dna(sequence)


# ==========================================
# FASTA Reader
# ==========================================

def fasta_input():

    path = input("\nEnter FASTA File Path : ").strip()

    header, sequence = read_fasta(path)

    if not header or not sequence:

        return

    print("\n✅ FASTA Loaded Successfully")

    print("Header :", header)

    analyze_dna(sequence, header)


# ==========================================
# RNA Analysis
# ==========================================

def rna_analysis():

    sequence = input("\nEnter DNA Sequence : ").upper()

    valid, invalid = validate_dna(sequence)

    if not valid:

        print("\nInvalid DNA")

        return

    rna = transcribe_dna(sequence)

    print("\nRNA Sequence")

    print("---------------------")

    print(rna)

    print("\nRNA Length :", rna_length(rna))

    counts = count_rna_bases(rna)

    print("\nRNA Base Count")

    print(counts)

    print("\nReverse RNA")

    print(reverse_rna(rna))
    
# ==========================================
# Protein Analysis
# ==========================================

def protein_analysis():

    sequence = input("\nEnter DNA Sequence : ").upper().strip()

    valid, invalid = validate_dna(sequence)

    if not valid:

        print("\n❌ Invalid DNA Sequence")

        return

    protein = translate_dna(sequence)

    print("\nProtein Sequence")
    print("-" * 30)

    print(protein)

    print("\nProtein Length :", protein_length(protein))

    print("\nContains Start Codon :", has_start_codon(sequence))

    print("Contains Stop Codon :", has_stop_codon(sequence))

    print("\nAmino Acid Frequency")
    print("-" * 30)

    counts = amino_acid_count(protein)

    for aa, count in counts.items():

        print(f"{aa} : {count}")


# ==========================================
# Manual vs Biopython
# ==========================================

def compare_module():

    sequence = input("\nEnter DNA Sequence : ").upper().strip()

    valid, invalid = validate_dna(sequence)

    if not valid:

        print("\n❌ Invalid DNA Sequence")

        return

    compare_translation(sequence)




# ==========================================
# ORF Analysis
# ==========================================

def orf_analysis():

    sequence = input("\nEnter DNA Sequence : ").upper().strip()

    valid, invalid = validate_dna(sequence)

    if not valid:

        print("\n❌ Invalid DNA Sequence")

        return

    orf = find_orf(sequence)

    if orf is None:

        print("\n❌ No ORF Found")

        return

    print("\n✅ ORF Found")
    print("-" * 40)

    print(orf)

    print("\nORF Length :", orf_length(orf))

# ==========================================
# Mutation Analysis
# ==========================================

def mutation_analysis():

    reference = input(
        "\nEnter Reference DNA Sequence : "
    ).upper().strip()


    mutated = input(
        "\nEnter Mutated DNA Sequence : "
    ).upper().strip()



    # Validate Reference DNA

    valid1, invalid1 = validate_dna(reference)


    # Validate Mutated DNA

    valid2, invalid2 = validate_dna(mutated)



    if not valid1 or not valid2:

        print("\n❌ Invalid DNA Sequence")

        return



    try:


        # Basic Mutation Analysis

        result = mutation_summary(
            reference,
            mutated
        )



        print("\n🧬 Mutation Analysis Report")

        print("-" * 40)



        print(
            "Sequence Length :",
            result["Sequence Length"]
        )


        print(
            "Total Mutations :",
            result["Total Mutations"]
        )


        print(
            "Mutation Percentage :",
            result["Mutation Percentage"],
            "%"
        )



        print("\nBase Mutations")

        print("-" * 40)



        for mutation in result["Mutation Details"]:

            print(mutation)




        # ===============================
        # Codon Level Analysis
        # ===============================


        print("\nCodon Changes")

        print("-" * 40)



        codon_changes = compare_codons(
            reference,
            mutated
        )



        if codon_changes:


            for change in codon_changes:

                print(change)


        else:

            print("No Codon Change")





        # ===============================
        # Protein Level Analysis
        # ===============================


        print("\nProtein Changes")

        print("-" * 40)



        protein_changes = protein_change(
            reference,
            mutated
        )



        if protein_changes:


            for change in protein_changes:

                print(change)


        else:

            print("No Amino Acid Change")




    except ValueError as e:


        print(
            "\n❌ Error :",
            e
        )

# ==========================================
# NCBI Downloader
# ==========================================

def ncbi_analysis():

    accession = input(
        "\nEnter NCBI Accession ID : "
    ).strip()


    result = fetch_sequence(
        accession
    )


    if result is None:

        print("\n❌ Sequence Not Found")

        return



    print("\n🌍 NCBI Sequence Downloaded")

    print("-" * 40)



    print(
        "ID :",
        result["id"]
    )


    print(
        "Description :",
        result["description"]
    )


    print(
        "Sequence Length :",
        result["length"],
        "bp"
    )



    print("\nSequence Preview:")

    print(
        result["sequence"][:200],
        "..."
    )



    # ======================================
    # Save FASTA File
    # ======================================


    save_choice = input(
        "\nSave FASTA File? (Y/N): "
    ).upper()



    if save_choice == "Y":


        filename = input(
            "\nEnter FASTA File Name : "
        ).strip()



        if not filename.endswith(".fasta"):

            filename += ".fasta"



        saved = save_fasta(
            result,
            filename
        )



        if saved:

            print(
                "\n✅ FASTA Saved Successfully:",
                filename
            )


        else:

            print(
                "\n❌ FASTA Save Failed"
            )



    # ======================================
    # Analyze Downloaded Sequence
    # ======================================


    analyze_choice = input(
        "\nAnalyze This Sequence? (Y/N): "
    ).upper()



    if analyze_choice == "Y":


        analyze_dna(

            result["sequence"],

            result["id"]

        )

#=============================
# main
#=============================

def main():

    while True:

        show_banner()

        show_menu()

        choice = input("\nEnter Choice : ").strip()

        if choice == "1":

            manual_input()

        elif choice == "2":

            fasta_input()

        elif choice == "3":

            rna_analysis()

        elif choice == "4":

            protein_analysis()

        elif choice == "5":

            compare_module()

        elif choice == "6":

            orf_analysis()

        elif choice == "7":
            mutation_analysis()

        elif choice == "8":
            ncbi_analysis()

        elif choice == "9":


            print("\n==========================================")
            print("Thank You For Using BioForge ❤️")
            print("Developed By : Suryansh Singh Yadav")
            print("==========================================")

            break

        else:

            print("\n❌ Invalid Choice")

# ==========================================
# Program Starts Here
# ==========================================

if __name__ == "__main__":

    main()
"""
=====================================================
BioForge Analysis Pipeline

By Suryansh Singh Yadav
=====================================================
"""

from validation import validate_dna

from dna import (
    get_length,
    count_bases,
    gc_content,
    at_content
)

from rna import transcribe_dna

from protein import translate_dna

from orf import find_orf

from restriction import generate_restriction_report

from primer import design_primers

from codon import generate_codon_report

from mutation import mutation_analysis

from protein_properties import analyze_protein


def run_complete_analysis(sequence):

    sequence = sequence.upper().strip()

    valid, invalid = validate_dna(sequence)

    if not valid:

        raise ValueError(
            "Invalid DNA Sequence"
        )

    report = {}

    # -----------------------
    # DNA
    # -----------------------

    report["length"] = get_length(sequence)

    report["counts"] = count_bases(sequence)

    report["gc"] = gc_content(sequence)

    report["at"] = at_content(sequence)

    # -----------------------
    # RNA
    # -----------------------

    report["rna"] = transcribe_dna(sequence)

    # -----------------------
    # Protein
    # -----------------------

    protein = translate_dna(sequence)

    report["protein"] = protein

    # -----------------------
    # Protein Properties
    # -----------------------

    try:

        report["protein_properties"] = analyze_protein(
            protein
        )

    except:

        report["protein_properties"] = None

    # -----------------------
    # ORF
    # -----------------------

    report["orf"] = find_orf(sequence)

    # -----------------------
    # Restriction
    # -----------------------

    report["restriction"] = generate_restriction_report(
        sequence
    )

    # -----------------------
    # Primer
    # -----------------------

    try:

        report["primer"] = design_primers(
            sequence
        )

    except:

        report["primer"] = None

    # -----------------------
    # Codons
    # -----------------------

    report["codons"] = generate_codon_report(
        sequence
    )

    # -----------------------
    # Mutation
    # -----------------------

    try:

        report["mutation"] = mutation_analysis(
            sequence
        )

    except:

        report["mutation"] = None

    return report
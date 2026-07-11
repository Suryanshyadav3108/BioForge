"""
=====================================================
BioForge - Mutation Analysis Module

By : Suryansh Singh Yadav
Version: 1.0
=====================================================
"""


def validate_sequences(reference, mutated):

    if len(reference) != len(mutated):
        raise ValueError(
            "Sequences must have same length"
        )

    return True



def find_mutations(reference, mutated):

    validate_sequences(
        reference,
        mutated
    )

    mutations = []


    for i in range(len(reference)):

        if reference[i] != mutated[i]:

            mutations.append({

                "position": i + 1,

                "reference":
                reference[i],

                "mutated":
                mutated[i],

                "type":
                classify_mutation(
                    reference[i],
                    mutated[i]
                )

            })


    return mutations



def classify_mutation(ref, alt):


    transitions = [

        ("A","G"),
        ("G","A"),

        ("C","T"),
        ("T","C")

    ]


    if (ref,alt) in transitions:

        return "Transition"

    else:

        return "Transversion"




def mutation_count(reference, mutated):

    return len(
        find_mutations(
            reference,
            mutated
        )
    )



def mutation_percentage(reference, mutated):

    total_length = len(reference)

    total_mutations = mutation_count(
        reference,
        mutated
    )


    percentage = (
        total_mutations /
        total_length
    ) * 100


    return round(
        percentage,
        2
    )



def mutation_summary(reference, mutated):


    mutations = find_mutations(
        reference,
        mutated
    )


    return {

        "Sequence Length":
        len(reference),

        "Total Mutations":
        len(mutations),

        "Mutation Percentage":
        mutation_percentage(
            reference,
            mutated
        ),

        "Mutation Details":
        mutations
    }

# ==========================================
# Advanced Mutation Analysis
# ==========================================


def split_codons(sequence):

    codons = []

    for i in range(0, len(sequence)-2, 3):

        codons.append(
            sequence[i:i+3]
        )

    return codons



def compare_codons(reference, mutated):

    ref_codons = split_codons(reference)

    mut_codons = split_codons(mutated)


    changes = []


    for i in range(
        min(len(ref_codons), len(mut_codons))
    ):

        if ref_codons[i] != mut_codons[i]:

            changes.append({

                "codon_position": i+1,

                "reference_codon":
                ref_codons[i],

                "mutated_codon":
                mut_codons[i]

            })


    return changes

#================================
#protein change detection
#================================

from protein import translate_dna



def protein_change(reference, mutated):


    ref_protein = translate_dna(
        reference
    )


    mut_protein = translate_dna(
        mutated
    )


    changes = []


    length = min(
        len(ref_protein),
        len(mut_protein)
    )


    for i in range(length):

        if ref_protein[i] != mut_protein[i]:

            changes.append({

                "position": i+1,

                "reference_amino_acid":
                ref_protein[i],

                "mutated_amino_acid":
                mut_protein[i]

            })


    return changes
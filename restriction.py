"""
=====================================================
BioForge - Restriction Enzyme Analysis Module

By : Suryansh Singh Yadav
Version : 2.0
=====================================================
"""

from validation import validate_dna

# ==========================================
# Restriction Enzyme Database
# ==========================================

RESTRICTION_ENZYMES = {

    "EcoRI": "GAATTC",

    "BamHI": "GGATCC",

    "HindIII": "AAGCTT",

    "NotI": "GCGGCCGC",

    "XhoI": "CTCGAG",

    "PstI": "CTGCAG",

    "SmaI": "CCCGGG",

    "NcoI": "CCATGG",

    "SalI": "GTCGAC",

    "KpnI": "GGTACC"

}


# ==========================================
# Return Enzyme Database
# ==========================================

def restriction_enzymes():

    return RESTRICTION_ENZYMES


# ==========================================
# Find Restriction Sites
# ==========================================

def find_restriction_sites(sequence):

    sequence = sequence.upper().strip()

    validate_dna(sequence)

    results = []

    for enzyme, site in RESTRICTION_ENZYMES.items():

        start = 0

        while True:

            position = sequence.find(site, start)

            if position == -1:
                break

            results.append({

                "enzyme": enzyme,

                "site": site,

                "position": position + 1

            })

            start = position + 1

    results.sort(

        key=lambda x: x["position"]

    )

    return results


# ==========================================
# Count Restriction Sites
# ==========================================

def enzyme_count(sequence):

    return len(

        find_restriction_sites(sequence)

    )


# ==========================================
# Enzyme Summary
# ==========================================

def enzyme_summary(sequence):

    results = find_restriction_sites(sequence)

    summary = {}

    for enzyme in RESTRICTION_ENZYMES:

        summary[enzyme] = sum(

            1

            for item in results

            if item["enzyme"] == enzyme

        )

    return summary


# ==========================================
# Generate Report
# ==========================================

def generate_restriction_report(sequence):

    sequence = sequence.upper().strip()

    validate_dna(sequence)

    results = find_restriction_sites(sequence)

    report = []

    report.append("=" * 55)

    report.append("BioForge Restriction Enzyme Analysis")

    report.append("=" * 55)

    report.append(

        f"Sequence Length : {len(sequence)} bp"

    )

    report.append("")

    if not results:

        report.append(

            "No restriction enzyme sites found."

        )

    else:

        for item in results:

            report.append(

                f"Enzyme : {item['enzyme']}"

            )

            report.append(

                f"Recognition Site : {item['site']}"

            )

            report.append(

                f"Position : {item['position']}"

            )

            report.append("-" * 30)

    report.append("")

    report.append(

        f"Total Restriction Sites : {len(results)}"

    )

    report.append("")

    report.append("Enzyme Summary")

    report.append("-" * 30)

    summary = enzyme_summary(sequence)

    for enzyme, count in summary.items():

        report.append(

            f"{enzyme:<10} : {count}"

        )

    return "\n".join(report)


# ==========================================
# Complete Restriction Analysis
# ==========================================

def restriction_analysis(sequence):

    sequence = sequence.upper().strip()

    validate_dna(sequence)

    return {

        "sequence_length": len(sequence),

        "total_sites": enzyme_count(sequence),

        "enzyme_summary": enzyme_summary(sequence),

        "sites": find_restriction_sites(sequence),

        "report": generate_restriction_report(sequence)

    }


# ==========================================
# Module Test
# ==========================================

if __name__ == "__main__":

    dna = "ATCGAATTCGGATCCCTCGAGGAATTCAAGCTTGCGGCCGCGGTACC"

    analysis = restriction_analysis(dna)

    print(

        analysis["report"]

    )
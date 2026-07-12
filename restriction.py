"""
=====================================================
BioForge Restriction Enzyme Analysis

By Suryansh Singh Yadav
=====================================================
"""

# Dictionary of common restriction enzymes
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


def restriction_enzymes():
    """
    Return all supported restriction enzymes.
    """
    return RESTRICTION_ENZYMES


def find_restriction_sites(sequence):
    """
    Find all restriction enzyme recognition sites.
    """

    sequence = sequence.upper()

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

    results.sort(key=lambda x: x["position"])

    return results


def enzyme_count(sequence):
    """
    Count total restriction sites.
    """

    return len(find_restriction_sites(sequence))


def generate_restriction_report(sequence):
    """
    Generate formatted restriction analysis report.
    """

    results = find_restriction_sites(sequence)

    if not results:
        return "No restriction enzyme sites found."

    report = []

    report.append("=" * 45)
    report.append("BioForge Restriction Analysis")
    report.append("=" * 45)

    for item in results:

        report.append(
            f"\nEnzyme : {item['enzyme']}"
        )

        report.append(
            f"Recognition Site : {item['site']}"
        )

        report.append(
            f"Position : {item['position']}"
        )

    report.append("\nTotal Sites : " + str(len(results)))

    return "\n".join(report)
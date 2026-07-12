"""
=====================================================
BioForge BLAST Module

By Suryansh Singh Yadav
=====================================================
"""

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def run_blast(sequence, program="blastn", database="nt"):
    """
    Run an online BLAST search using NCBI.
    """

    sequence = sequence.upper().strip()

    if len(sequence) < 100:
        raise ValueError(
            "Sequence should be at least 100 nucleotides for BLAST."
        )

    print("\nSubmitting sequence to NCBI BLAST...")
    print("Please wait. This may take a few minutes.\n")

    try:

        result_handle = NCBIWWW.qblast(
            program=program,
            database=database,
            sequence=sequence
        )

        with open("blast_result.xml", "w") as file:
            file.write(result_handle.read())

        result_handle.close()

        print("BLAST completed successfully.\n")

        return "blast_result.xml"

    except Exception as e:

        print("BLAST Error :", e)

        return None


def parse_blast(xml_file):
    """
    Parse BLAST XML results.
    """

    if xml_file is None:
        return []

    try:

        with open(xml_file) as file:

            blast_record = NCBIXML.read(file)

        results = []

        if len(blast_record.alignments) == 0:
            return []

        for alignment in blast_record.alignments:

            if len(alignment.hsps) == 0:
                continue

            hsp = alignment.hsps[0]

            identity_percent = round(
                (hsp.identities / hsp.align_length) * 100,
                2
            )

            results.append({

                "title": alignment.title,

                "length": alignment.length,

                "score": hsp.score,

                "identity": identity_percent,

                "coverage": hsp.align_length,

                "expect": hsp.expect

            })

        return results

    except Exception as e:

        print("Parsing Error :", e)

        return []


def generate_blast_report(sequence):
    """
    Run BLAST and generate a formatted report.
    """

    xml = run_blast(sequence)

    results = parse_blast(xml)

    report = []

    report.append("=" * 60)
    report.append("BioForge BLAST Report")
    report.append("=" * 60)

    if len(results) == 0:

        report.append("")
        report.append("No BLAST hits found.")
        report.append("Try a longer DNA sequence.")
        report.append("Recommended length: 100+ bp")

        return "\n".join(report)

    for i, item in enumerate(results[:5], start=1):

        report.append("")
        report.append(f"Match {i}")

        report.append(f"Title : {item['title']}")

        report.append(f"Identity : {item['identity']} %")

        report.append(f"Coverage : {item['coverage']}")

        report.append(f"Score : {item['score']}")

        report.append(f"E-value : {item['expect']}")

        report.append("-" * 60)

    return "\n".join(report)
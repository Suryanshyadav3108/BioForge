"""
=====================================================
BioForge FASTA Reader
Author  : Aman Yadav
Version : 2.0
=====================================================
"""


def read_fasta(file_path):
    """
    Reads a FASTA file and returns:

    Header
    Sequence
    """

    try:

        with open(file_path, "r") as file:

            lines = file.readlines()

    except FileNotFoundError:

        print("\n❌ FASTA File Not Found")

        return "", ""

    header = ""

    sequence = ""

    for line in lines:

        line = line.strip()

        if line == "":

            continue

        if line.startswith(">"):

            header = line[1:]

        else:

            sequence += line.upper()

    return header, sequence
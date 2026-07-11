"""
=====================================================
BioForge - NCBI Downloader Module

By : Suryansh Singh Yadav
Version: 1.0
=====================================================
"""


from Bio import Entrez, SeqIO
from io import StringIO



# NCBI requires email

Entrez.email = "your_email@example.com"



def fetch_sequence(accession):


    try:

        handle = Entrez.efetch(

            db="nuccore",

            id=accession,

            rettype="fasta",

            retmode="text"

        )


        record = SeqIO.read(
            handle,
            "fasta"
        )


        handle.close()


        return {

            "id":
            record.id,


            "description":
            record.description,


            "sequence":
            str(record.seq),


            "length":
            len(record.seq)

        }


    except Exception as e:


        print(
            "NCBI Error:",
            e
        )


        return None
    
# ==========================================
# Save NCBI Sequence as FASTA
# ==========================================

def save_fasta(sequence_data, filename):


    try:

        with open(filename, "w") as file:


            file.write(
                ">" +
                sequence_data["description"]
                +
                "\n"
            )


            file.write(
                sequence_data["sequence"]
                +
                "\n"
            )


        return True


    except Exception as e:


        print(
            "Save Error:",
            e
        )


        return False
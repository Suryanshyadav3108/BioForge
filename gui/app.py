"""
=====================================================
BioForge GUI Application

By : Suryansh Singh Yadav
Version: 4.0
=====================================================
"""


import customtkinter as ctk

from tkinter import filedialog

import sys
import os



# ==========================================
# Project Path
# ==========================================

sys.path.append(

    os.path.abspath(

        os.path.join(

            os.path.dirname(__file__),

            ".."

        )

    )

)



# ==========================================
# BioForge Imports
# ==========================================

from validation import validate_dna


from dna import (

    get_length,

    count_bases,

    gc_content,

    at_content,

    reverse_complement

)



from fasta import read_fasta



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



from orf import (

    find_orf,

    orf_length

)



from mutation import (

    find_mutations,

    mutation_percentage,

    mutation_summary

)



from ncbi import (

    fetch_sequence,

    save_fasta

)



from visualization import (

    plot_base_composition,

    plot_gc_at

)



from pdf_generator import (

    generate_pdf_report

)

from pipeline import run_complete_analysis





# ==========================================
# Theme
# ==========================================

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("blue")





# ==========================================
# Window
# ==========================================

app = ctk.CTk()


app.title(
    "BioForge - Professional Bioinformatics Toolkit"
)


app.geometry(
    "800x900"
)

# ==========================================
# Scrollable Main Container
# ==========================================

main_frame = ctk.CTkScrollableFrame(

    app,

    width=760,

    height=850

)

main_frame.pack(

    fill="both",

    expand=True,

    padx=10,

    pady=10

)





# ==========================================
# Header
# ==========================================

title = ctk.CTkLabel(

    main_frame,

    text="🧬 BioForge",

    font=("Arial",32)

)

title.pack(
    pady=20
)



subtitle = ctk.CTkLabel(

    main_frame,

    text="Professional Bioinformatics Toolkit\nBy: Suryansh Singh Yadav"

)

subtitle.pack()





# ==========================================
# Input
# ==========================================

sequence_input = ctk.CTkEntry(

    main_frame,

    width=600,

    height=45,

    placeholder_text="Enter DNA Sequence / Accession ID"

)

sequence_input.pack(
    pady=15
)





# ==========================================
# Output Box
# ==========================================

result_box = ctk.CTkTextbox(

    main_frame,

    width=650,

    height=300

)

result_box.pack(
    pady=15
)





# ==========================================
# DNA Analysis
# ==========================================


def dna_analysis_gui():


    sequence = sequence_input.get().upper().strip()


    valid, invalid = validate_dna(sequence)



    result_box.delete(
        "0.0",
        "end"
    )



    if not valid:


        result_box.insert(

            "end",

            "❌ Invalid DNA Sequence"

        )

        return




    counts = count_bases(sequence)



    result = f"""

🧬 DNA Analysis


Length:

{get_length(sequence)} bp



Base Count:

{counts}



GC Content:

{round(gc_content(sequence),2)} %



AT Content:

{round(at_content(sequence),2)} %



Reverse Complement:

{reverse_complement(sequence)}

"""



    result_box.insert(

        "end",

        result

    )







# ==========================================
# FASTA Upload
# ==========================================


def fasta_upload_gui():


    file = filedialog.askopenfilename(

        filetypes=[

            ("FASTA","*.fasta"),

            ("All Files","*.*")

        ]

    )



    if not file:

        return



    header, sequence = read_fasta(file)



    sequence_input.delete(

        0,

        "end"

    )


    sequence_input.insert(

        0,

        sequence

    )


    result_box.delete(

        "0.0",

        "end"

    )


    result_box.insert(

        "end",

        f"""

✅ FASTA Loaded


Header:

{header}


Length:

{len(sequence)} bp


"""

    )





# ==========================================
# RNA Analysis
# ==========================================


def rna_analysis_gui():


    sequence = sequence_input.get().upper().strip()



    if not validate_dna(sequence)[0]:

        return



    rna = transcribe_dna(sequence)



    result_box.delete(
        "0.0",
        "end"
    )


    result_box.insert(

        "end",

        f"""

🧬 RNA Analysis


RNA:

{rna}


Length:

{rna_length(rna)}


Count:

{count_rna_bases(rna)}


Reverse RNA:

{reverse_rna(rna)}

"""

    )





# ==========================================
# Protein Analysis
# ==========================================


def protein_analysis_gui():


    sequence = sequence_input.get().upper().strip()



    if not validate_dna(sequence)[0]:

        return



    protein = translate_dna(sequence)



    result_box.delete(

        "0.0",

        "end"

    )


    result_box.insert(

        "end",

        f"""

🔬 Protein Analysis


Protein:

{protein}


Length:

{protein_length(protein)}


Start:

{has_start_codon(sequence)}


Stop:

{has_stop_codon(sequence)}


Amino Acid Count:

{amino_acid_count(protein)}

"""

    )

# ==========================================
# ORF Finder GUI
# ==========================================


def orf_analysis_gui():


    sequence = sequence_input.get().upper().strip()



    result_box.delete(
        "0.0",
        "end"
    )



    if not validate_dna(sequence)[0]:


        result_box.insert(

            "end",

            "❌ Invalid DNA Sequence"

        )

        return




    orf = find_orf(sequence)



    if orf:


        result = f"""

🔎 ORF Analysis


ORF Found:

YES ✅


ORF Sequence:

{orf}


ORF Length:

{orf_length(orf)} bp


"""



    else:


        result = """

🔎 ORF Analysis


No ORF Found ❌

"""



    result_box.insert(

        "end",

        result

    )







# ==========================================
# Mutation Analysis GUI
# ==========================================


def mutation_analysis_gui():

    window = ctk.CTkToplevel(app)

    window.title("Mutation Analysis")

    window.geometry("700x650")

    ctk.CTkLabel(
        window,
        text="Reference DNA"
    ).pack(pady=(15,5))

    ref_box = ctk.CTkTextbox(
        window,
        width=600,
        height=120
    )
    ref_box.pack()

    ctk.CTkLabel(
        window,
        text="Mutated DNA"
    ).pack(pady=(15,5))

    mut_box = ctk.CTkTextbox(
        window,
        width=600,
        height=120
    )
    mut_box.pack()

    result = ctk.CTkTextbox(
        window,
        width=600,
        height=170
    )
    result.pack(pady=15)

    def analyze():

        reference = ref_box.get("1.0", "end").strip().upper()

        mutated = mut_box.get("1.0", "end").strip().upper()

        result.delete("1.0", "end")

        try:

            mutations = find_mutations(reference, mutated)

            percent = mutation_percentage(reference, mutated)

            summary = mutation_summary(reference, mutated)

            text = ""

            text += "🧪 Mutation Analysis\n\n"

            text += f"Mutation Percentage : {percent:.2f}%\n\n"

            text += "Summary\n"

            text += str(summary)

            text += "\n\n"

            text += "Mutations\n"

            text += str(mutations)

            result.insert("end", text)

        except Exception as e:

            result.insert("end", str(e))

    ctk.CTkButton(
        window,
        text="Analyze Mutation",
        command=analyze
    ).pack(pady=10)







# ==========================================
# NCBI Downloader GUI
# ==========================================


def ncbi_download_gui():


    accession = sequence_input.get().strip()



    result_box.delete(

        "0.0",

        "end"

    )



    if not accession:


        result_box.insert(

            "end",

            "❌ Enter Accession ID"

        )

        return




    data = fetch_sequence(

        accession

    )



    if data is None:


        result_box.insert(

            "end",

            "❌ Sequence Not Found"

        )

        return




    sequence_input.delete(

        0,

        "end"

    )



    sequence_input.insert(

        0,

        data["sequence"]

    )



    result_box.insert(

        "end",

        f"""

🌍 NCBI Download


ID:

{data['id']}



Description:

{data['description']}



Length:

{data['length']} bp



Sequence Loaded ✅

"""

    )







# ==========================================
# PDF Generator GUI
# ==========================================


def generate_pdf_gui():


    sequence = sequence_input.get().upper().strip()



    result_box.delete(

        "0.0",

        "end"

    )



    if not validate_dna(sequence)[0]:


        result_box.insert(

            "end",

            "❌ Invalid DNA Sequence"

        )

        return




    counts = count_bases(sequence)


    gc = gc_content(sequence)


    at = at_content(sequence)




    base_graph = plot_base_composition(

        counts

    )



    gc_graph = plot_gc_at(

        gc,

        at

    )




    orf = find_orf(sequence)



    if orf:


        orf_data = {

            "ORF Found": True,

            "ORF Length": orf_length(orf),

            "ORF Sequence": orf

        }


    else:


        orf_data = {

            "ORF Found": False

        }




    generate_pdf_report(

        "BioForge_Report.pdf",

        "BioForge GUI Analysis",

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




    result_box.insert(

        "end",

        """

📄 PDF Generated Successfully ✅


File:

BioForge_Report.pdf


by:

Suryansh Singh Yadav

"""

    )

# ==========================================
# Complete Analysis GUI
# ==========================================

def complete_analysis_gui():

    sequence = sequence_input.get().upper().strip()

    result_box.delete("0.0", "end")

    if sequence == "":

        result_box.insert(
            "end",
            "❌ Enter DNA Sequence"
        )
        return

    try:

        report = run_complete_analysis(sequence)

    except Exception as e:

        result_box.insert(
            "end",
            str(e)
        )
        return

    text = ""

    text += "🧬 BioForge Complete Analysis\n"
    text += "=" * 55 + "\n\n"

    text += f"Length : {report['length']} bp\n"

    text += f"GC : {round(report['gc'],2)} %\n"

    text += f"AT : {round(report['at'],2)} %\n\n"

    text += "Base Count\n"

    text += str(report["counts"])

    text += "\n\n"

    text += "RNA\n"

    text += report["rna"]

    text += "\n\n"

    text += "Protein\n"

    text += report["protein"]

    text += "\n\n"

    text += "ORF\n"

    text += str(report["orf"])

    text += "\n\n"

    text += "Restriction\n"

    text += str(report["restriction"])

    text += "\n\n"

    text += "Primer\n"

    text += str(report["primer"])

    text += "\n\n"

    text += "Codons\n"

    text += str(report["codons"])

    text += "\n\n"

    text += "Mutation\n"

    text += str(report["mutation"])

    result_box.insert(
        "end",
        text
    )







# ==========================================
# GUI Buttons
# ==========================================


buttons = [

    (
        "🧬 DNA Analysis",
        dna_analysis_gui
    ),

    (
        "📂 FASTA Upload",
        fasta_upload_gui
    ),

    (
        "🧬 RNA Analysis",
        rna_analysis_gui
    ),

    (
        "🔬 Protein Translation",
        protein_analysis_gui
    ),

    (
        "🔎 ORF Finder",
        orf_analysis_gui
    ),

    (
        "🧪 Mutation Analysis",
        mutation_analysis_gui
    ),

    (
        "🌍 NCBI Downloader",
        ncbi_download_gui
    ),

    (
        "📄 Generate PDF",
        generate_pdf_gui
    ),


    (
    "🚀 Run Complete Analysis",
    complete_analysis_gui
    )

]


for text, command in buttons:


    btn = ctk.CTkButton(

        main_frame,

        text=text,

        width=350,

        height=45,

        command=command

    )


    btn.pack(

        pady=8

    )







# ==========================================
# Start Application
# ==========================================


app.mainloop()
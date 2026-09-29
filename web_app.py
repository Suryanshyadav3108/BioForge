import streamlit as st

from validation import validate_dna
from fasta import read_fasta
from dna import (
    get_length,
    count_bases,
    gc_content,
    at_content,
    reverse_sequence,
    reverse_complement,
)
from rna import (
    transcribe_dna,
    reverse_rna,
    rna_length,
    count_rna_bases,
)
from protein import (
    translate_dna,
    protein_length,
    amino_acid_count,
    has_start_codon,
    has_stop_codon,
)
from orf import (
    find_orf,
    orf_length,
    has_orf,
)
from mutation import (
    mutation_summary,
    compare_codons,
    protein_change,
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="BioForge",
    page_icon="🧬",
    layout="wide",
)


# =========================================================
# HEADER
# =========================================================

st.title("🧬 BioForge")
st.subheader("Professional Bioinformatics Toolkit")

st.markdown(
    """
    **By : Suryansh Singh Yadav**

    Analyze DNA, RNA, proteins, ORFs and mutations directly
    from your browser.
    """
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🧬 BioForge")

st.sidebar.markdown("### Modules")

module = st.sidebar.radio(
    "Select Analysis",
    [
        "DNA Analysis",
        "FASTA Analysis",
        "DNA → RNA",
        "DNA → Protein",
        "ORF Finder",
        "Mutation Analysis",
    ],
)

st.sidebar.divider()

st.sidebar.info(
    "BioForge is a bioinformatics toolkit "
    "for sequence analysis."
)


# =========================================================
# DNA VALIDATION FUNCTION
# =========================================================

def clean_dna(sequence):
    """
    Clean and validate DNA sequence.
    """

    sequence = sequence.upper().replace(" ", "").replace("\n", "")

    valid, invalid = validate_dna(sequence)

    if not valid:
        return None, invalid

    return sequence, []


# =========================================================
# DNA ANALYSIS
# =========================================================

if module == "DNA Analysis":

    st.header("🧬 DNA Analysis")

    st.write(
        "Enter a DNA sequence using A, T, G and C."
    )

    sequence = st.text_area(
        "DNA Sequence",
        placeholder="Example: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",
        height=150,
    )

    analyze_button = st.button(
        "🔬 Analyze DNA",
        type="primary",
    )

    if analyze_button:

        if not sequence.strip():

            st.warning("Please enter a DNA sequence.")

        else:

            dna, invalid = clean_dna(sequence)

            if dna is None:

                st.error(
                    "Invalid DNA sequence."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(invalid),
                )

            else:

                st.success(
                    "DNA sequence is valid."
                )

                st.subheader("📊 Sequence Statistics")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "Length",
                    get_length(dna),
                )

                col2.metric(
                    "GC %",
                    f"{gc_content(dna):.2f}%",
                )

                col3.metric(
                    "AT %",
                    f"{at_content(dna):.2f}%",
                )

                col4.metric(
                    "GC Bases",
                    dna.count("G") + dna.count("C"),
                )

                st.divider()

                st.subheader("🧪 Base Composition")

                counts = count_bases(dna)

                c1, c2, c3, c4 = st.columns(4)

                c1.metric("A", counts["A"])
                c2.metric("T", counts["T"])
                c3.metric("G", counts["G"])
                c4.metric("C", counts["C"])

                st.divider()

                st.subheader("🔄 Sequence Operations")

                col1, col2 = st.columns(2)

                with col1:

                    st.write("**Reverse Sequence**")

                    st.code(
                        reverse_sequence(dna),
                        language="text",
                    )

                with col2:

                    st.write("**Reverse Complement**")

                    st.code(
                        reverse_complement(dna),
                        language="text",
                    )

# =========================================================
# FASTA ANALYSIS
# =========================================================

elif module == "FASTA Analysis":

    st.header("📁 FASTA File Analysis")

    st.write(
        "Upload a FASTA file to read its header and DNA sequence."
    )

    uploaded_file = st.file_uploader(
        "Upload FASTA File",
        type=["fasta", "fa", "fas", "txt"],
    )

    if uploaded_file is not None:

        temp_path = "uploaded_sequence.fasta"

        with open(temp_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        header, sequence = read_fasta(temp_path)

        if not sequence:

            st.error(
                "No valid sequence found in the FASTA file."
            )

        else:

            dna, invalid = clean_dna(sequence)

            if dna is None:

                st.error(
                    "The FASTA sequence contains invalid DNA bases."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(invalid),
                )

            else:

                st.success(
                    "FASTA file successfully loaded!"
                )

                st.subheader("📌 FASTA Header")

                st.code(
                    header if header else "No header found",
                    language="text",
                )

                st.subheader("🧬 DNA Sequence")

                st.code(
                    dna,
                    language="text",
                )

                st.subheader("📊 Sequence Statistics")

                counts = count_bases(dna)

                c1, c2, c3, c4 = st.columns(4)

                c1.metric(
                    "Length",
                    get_length(dna),
                )

                c2.metric(
                    "GC %",
                    f"{gc_content(dna):.2f}%",
                )

                c3.metric(
                    "AT %",
                    f"{at_content(dna):.2f}%",
                )

                c4.metric(
                    "GC Bases",
                    counts["G"] + counts["C"],
                )

                st.subheader("🧪 Base Composition")

                b1, b2, b3, b4 = st.columns(4)

                b1.metric("A", counts["A"])
                b2.metric("T", counts["T"])
                b3.metric("G", counts["G"])
                b4.metric("C", counts["C"])

# =========================================================
# DNA → RNA
# =========================================================

elif module == "DNA → RNA":

    st.header("🧪 DNA → RNA Transcription")

    sequence = st.text_area(
        "Enter DNA Sequence",
        placeholder="Example: ATGGCCATTGTA",
        height=150,
    )

    if st.button(
        "🧬 Transcribe DNA",
        type="primary",
    ):

        if not sequence.strip():

            st.warning(
                "Please enter a DNA sequence."
            )

        else:

            dna, invalid = clean_dna(sequence)

            if dna is None:

                st.error(
                    "Invalid DNA sequence."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(invalid),
                )

            else:

                rna = transcribe_dna(dna)

                st.success(
                    "DNA successfully transcribed to RNA."
                )

                st.subheader("RNA Sequence")

                st.code(
                    rna,
                    language="text",
                )

                st.divider()

                st.subheader("📊 RNA Statistics")

                counts = count_rna_bases(rna)

                c1, c2, c3, c4 = st.columns(4)

                c1.metric("Length", rna_length(rna))
                c2.metric("A", counts["A"])
                c3.metric("U", counts["U"])
                c4.metric("G + C", counts["G"] + counts["C"])

                st.write("**Reverse RNA**")

                st.code(
                    reverse_rna(rna),
                    language="text",
                )


# =========================================================
# DNA → PROTEIN
# =========================================================

elif module == "DNA → Protein":

    st.header("🧫 DNA → Protein Translation")

    sequence = st.text_area(
        "Enter DNA Sequence",
        placeholder="Example: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG",
        height=150,
    )

    if st.button(
        "🧬 Translate DNA",
        type="primary",
    ):

        if not sequence.strip():

            st.warning(
                "Please enter a DNA sequence."
            )

        else:

            dna, invalid = clean_dna(sequence)

            if dna is None:

                st.error(
                    "Invalid DNA sequence."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(invalid),
                )

            else:

                protein = translate_dna(dna)

                st.success(
                    "DNA successfully translated."
                )

                st.subheader("Protein Sequence")

                st.code(
                    protein,
                    language="text",
                )

                st.divider()

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Protein Length",
                    protein_length(protein),
                )

                c2.metric(
                    "Start Codon",
                    "Yes" if has_start_codon(dna) else "No",
                )

                c3.metric(
                    "Stop Codon",
                    "Yes" if has_stop_codon(dna) else "No",
                )

                st.subheader(
                    "🧪 Amino Acid Composition"
                )

                aa_counts = amino_acid_count(protein)

                st.dataframe(
                    [
                        {
                            "Amino Acid": aa,
                            "Count": count,
                        }
                        for aa, count in aa_counts.items()
                    ],
                    use_container_width=True,
                )


# =========================================================
# ORF FINDER
# =========================================================

elif module == "ORF Finder":

    st.header("🔬 Open Reading Frame Finder")

    sequence = st.text_area(
        "Enter DNA Sequence",
        placeholder="Example: CCCATGGCTTTTGAATAG",
        height=150,
    )

    if st.button(
        "🔎 Find ORF",
        type="primary",
    ):

        if not sequence.strip():

            st.warning(
                "Please enter a DNA sequence."
            )

        else:

            dna, invalid = clean_dna(sequence)

            if dna is None:

                st.error(
                    "Invalid DNA sequence."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(invalid),
                )

            else:

                orf = find_orf(dna)

                if has_orf(dna):

                    st.success(
                        "ORF detected!"
                    )

                    st.subheader(
                        "ORF Sequence"
                    )

                    st.code(
                        orf,
                        language="text",
                    )

                    st.metric(
                        "ORF Length",
                        orf_length(orf),
                    )

                else:

                    st.warning(
                        "No complete ORF found."
                    )


# =========================================================
# MUTATION ANALYSIS
# =========================================================

elif module == "Mutation Analysis":

    st.header("🧬 Mutation Analysis")

    st.write(
        "Compare a reference DNA sequence with a mutated DNA sequence."
    )

    reference = st.text_area(
        "Reference DNA",
        placeholder="Enter reference sequence",
        height=130,
    )

    mutated = st.text_area(
        "Mutated DNA",
        placeholder="Enter mutated sequence",
        height=130,
    )

    if st.button(
        "🔬 Analyze Mutations",
        type="primary",
    ):

        if not reference.strip() or not mutated.strip():

            st.warning(
                "Please enter both sequences."
            )

        else:

            ref, ref_invalid = clean_dna(reference)
            mut, mut_invalid = clean_dna(mutated)

            if ref is None:

                st.error(
                    "Reference sequence is invalid."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(ref_invalid),
                )

            elif mut is None:

                st.error(
                    "Mutated sequence is invalid."
                )

                st.write(
                    "Invalid characters:",
                    ", ".join(mut_invalid),
                )

            elif len(ref) != len(mut):

                st.error(
                    "Reference and mutated sequences "
                    "must have the same length."
                )

            else:

                summary = mutation_summary(
                    ref,
                    mut,
                )

                st.success(
                    "Mutation analysis completed."
                )

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Sequence Length",
                    summary["Sequence Length"],
                )

                c2.metric(
                    "Total Mutations",
                    summary["Total Mutations"],
                )

                c3.metric(
                    "Mutation %",
                    f'{summary["Mutation Percentage"]:.2f}%',
                )

                st.divider()

                st.subheader(
                    "🧬 Mutation Details"
                )

                mutations = summary[
                    "Mutation Details"
                ]

                if mutations:

                    st.dataframe(
                        mutations,
                        use_container_width=True,
                    )

                else:

                    st.info(
                        "No mutations detected."
                    )

                st.subheader(
                    "🧪 Codon Changes"
                )

                codon_changes = compare_codons(
                    ref,
                    mut,
                )

                if codon_changes:

                    st.dataframe(
                        codon_changes,
                        use_container_width=True,
                    )

                else:

                    st.info(
                        "No codon changes detected."
                    )

                st.subheader(
                    "🧫 Protein Changes"
                )

                protein_changes = protein_change(
                    ref,
                    mut,
                )

                if protein_changes:

                    st.dataframe(
                        protein_changes,
                        use_container_width=True,
                    )

                else:

                    st.info(
                        "No protein-level changes detected."
                    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "BioForge | Professional Bioinformatics Toolkit | "
    "By : Suryansh Singh Yadav"
)
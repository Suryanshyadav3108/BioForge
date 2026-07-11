"""
=====================================================
BioForge - Professional PDF Report Generator

By : Suryansh Singh Yadav
Version: 3.4
=====================================================
"""


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime



# ==========================================
# Generate PDF Report
# ==========================================


def generate_pdf_report(

        filename,

        sequence_id,

        sequence,

        counts,

        gc,

        at,

        graphs=None,

        orf_data=None,

        mutation_data=None,

        ncbi_data=None

):


    doc = SimpleDocTemplate(
        filename
    )


    styles = getSampleStyleSheet()


    content = []



    # ======================================
    # Title
    # ======================================


    content.append(

        Paragraph(

            "BioForge Analysis Report",

            styles["Title"]

        )

    )


    content.append(
        Spacer(1,20)
    )



    # ======================================
    # Author Information
    # ======================================


    date = datetime.now().strftime(
        "%d-%m-%Y %H:%M"
    )


    author_info = f"""

    <b>Author:</b> Suryansh Singh Yadav<br/>

    <b>Software:</b> BioForge Professional Bioinformatics Toolkit<br/>

    <b>Version:</b> 3.4<br/>

    <b>Generated:</b> {date}

    """



    content.append(

        Paragraph(

            author_info,

            styles["BodyText"]

        )

    )


    content.append(
        Spacer(1,20)
    )



    # ======================================
    # Sequence Information
    # ======================================


    sequence_info = f"""


    <b>Sequence Information</b><br/><br/>


    <b>Sequence ID:</b> {sequence_id}<br/>

    <b>Sequence Length:</b> {len(sequence)} bp<br/><br/>


    <b>GC Content:</b> {gc}%<br/>

    <b>AT Content:</b> {at}%


    """



    content.append(

        Paragraph(

            sequence_info,

            styles["BodyText"]

        )

    )


    content.append(
        Spacer(1,20)
    )



    # ======================================
    # Base Composition Table
    # ======================================


    content.append(

        Paragraph(

            "Base Composition",

            styles["Heading2"]

        )

    )


    table_data = [

        ["Base","Count"],

        ["A", counts["A"]],

        ["T", counts["T"]],

        ["G", counts["G"]],

        ["C", counts["C"]]

    ]



    table = Table(
        table_data
    )



    table.setStyle(

        TableStyle(

            [

                ("GRID",(0,0),(-1,-1),0.5,None)

            ]

        )

    )


    content.append(
        table
    )


    content.append(
        Spacer(1,20)
    )



    # ======================================
    # NCBI Information
    # ======================================


    if ncbi_data:


        content.append(

            Paragraph(

                "NCBI Information",

                styles["Heading2"]

            )

        )


        content.append(

            Paragraph(

                str(ncbi_data),

                styles["BodyText"]

            )

        )



        content.append(
            Spacer(1,20)
        )



    # ======================================
    # ORF Information
    # ======================================


    if orf_data:


        content.append(

            Paragraph(

                "ORF Analysis",

                styles["Heading2"]

            )

        )


        content.append(

            Paragraph(

                str(orf_data),

                styles["BodyText"]

            )

        )



        content.append(
            Spacer(1,20)
        )



    # ======================================
    # Mutation Information
    # ======================================


    if mutation_data:


        content.append(

            Paragraph(

                "Mutation Analysis",

                styles["Heading2"]

            )

        )


        content.append(

            Paragraph(

                str(mutation_data),

                styles["BodyText"]

            )

        )


        content.append(
            Spacer(1,20)
        )



    # ======================================
    # Add Graphs
    # ======================================


    if graphs:


        content.append(

            Paragraph(

                "Visualization",

                styles["Heading2"]

            )

        )


        for graph in graphs:


            content.append(

                Image(

                    graph,

                    width=300,

                    height=200

                )

            )


            content.append(

                Spacer(1,20)

            )



    # ======================================
    # Build PDF
    # ======================================


    doc.build(
        content
    )


    return filename
from pdf_generator import generate_pdf_report


counts={

"A":25,
"T":20,
"G":30,
"C":25

}



generate_pdf_report(

"BioForge_Report.pdf",

"Test_DNA",

"ATGCGTAC",

counts,

55,

45,

[

"base_composition.png",

"gc_at_content.png"

]

)


print("PDF Generated")
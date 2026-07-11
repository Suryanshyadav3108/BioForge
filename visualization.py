"""
=====================================================
BioForge - Visualization Engine

By : Suryansh Singh Yadav
Version: 1.0
=====================================================
"""


import matplotlib.pyplot as plt



# ==========================================
# Base Composition Graph
# ==========================================

def plot_base_composition(counts, filename="base_composition.png"):


    bases = list(counts.keys())

    values = list(counts.values())


    plt.figure(figsize=(7,5))


    plt.bar(
        bases,
        values
    )


    plt.title(
        "DNA Base Composition"
    )


    plt.xlabel(
        "Bases"
    )


    plt.ylabel(
        "Count"
    )


    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()



    return filename





# ==========================================
# GC AT Content Graph
# ==========================================

def plot_gc_at(gc, at, filename="gc_at_content.png"):


    labels = [
        "GC Content",
        "AT Content"
    ]


    values = [
        gc,
        at
    ]



    plt.figure(figsize=(6,6))


    plt.pie(

        values,

        labels=labels,

        autopct="%1.1f%%"

    )


    plt.title(
        "GC vs AT Content"
    )


    plt.savefig(

        filename,

        dpi=300,

        bbox_inches="tight"

    )


    plt.close()



    return filename
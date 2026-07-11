from ncbi import fetch_sequence



accession = input(
    "Enter NCBI Accession ID : "
)


result = fetch_sequence(
    accession
)



if result:


    print("\nNCBI Result")
    print("----------------")


    print(
        "ID:",
        result["id"]
    )


    print(
        "Description:",
        result["description"]
    )


    print(
        "Length:",
        result["length"],
        "bp"
    )


    print(
        "\nSequence:"
    )


    print(
        result["sequence"][:100],
        "..."
    )
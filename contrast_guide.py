def contrast_procedure(examination):
    procedures = {
        "CT": "Check renal function before contrast administration",
        "MRI": "Screen for MRI contrast contraindications"
    }

    return procedures.get(examination,"Procedure not available")

print(contrast_procedure("CT"))
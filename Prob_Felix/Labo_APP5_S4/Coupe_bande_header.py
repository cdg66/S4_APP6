# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import getpass

def header_coupe_bande(coupe_bande_Q2_5,filename):

    # ouvrir le fichier pour l'écriture
    with open(filename, "w") as file:
        # écrire les directives de préprocesseur pour éviter une inclusion multiple du fichier header
        file.write("// IIRCoeffs : coefficients (b0, b1, b2, a0, a1, a2) for N_SOS_SECTIONS cascaded SOS sections\n")
        file.write("#define IIR_QXY_RES_NBITS 13 // Q2.13\n")
        # file.write("#ifndef filterIIRcoeffs_TEST_H\n")
        # file.write("#define filterIIRcoeffs_TEST_H\n\n")

        # écrire le tableau de coefficients
        file.write("#define N_SOS_SECTIONS {}\n".format(len(coupe_bande_Q2_5) // 6))
        file.write("int32_t IIRCoeffs[N_SOS_SECTIONS][6] = {\n")
        for i in range(len(coupe_bande_Q2_5) // 6):
            row_start = i * 6
            row_end = (i + 1) * 6
            row = coupe_bande_Q2_5[row_start:row_end]
            file.write("\t{" + ", ".join(str(int(x)) for x in row) + "},\n")
        file.write("};\n\n")

        # écrire la déclaration des tableaux IIRu et IIRv
        file.write("int32_t IIRu[N_SOS_SECTIONS] = {0}, IIRv[N_SOS_SECTIONS] = {0};\n\n")
        # # écrire les directives de préprocesseur pour fermer le fichier header
        # file.write("#endif /* COEFFICIENTS_H */\n")

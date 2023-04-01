import numpy as np

def hanning_header():
    filename = 'window_header.h'
    varname = 'WINDOW'
    length = 255
    # Generate Hanning window
    hanning = np.hanning(length)

    # Open file for writing
    with open('C:/Users/Felix/Documents/GitHub/S4_APP6/APP6_Problematique.X/' + filename, 'w') as f:
        # Write header guard and include statements
        f.write('#ifndef ' + varname.upper() + '_H\n')
        f.write('#define ' + varname.upper() + '_H\n\n')
        f.write('#include <stdint.h>\n\n')

        # Write variable declaration
        f.write('static const int32_t ' + varname + '[' + str(length) + '] = {\n')

        # Write Hanning window values
        for i in range(length):
            f.write('    ' + str(int(hanning[i] * 2**31)) + ',\n')

        # Write closing brace and header guard
        f.write('};\n\n')
        f.write('#endif // ' + varname.upper() + '_H')

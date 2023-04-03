# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import getpass
def PY2C( array, filename='header.h',PYtype=int,Ctype='int32_t',varname='Coefficient',complex=0, gard='HEADER_H',blocktitle='',includesanddef=['#include <stdint.h>'], static=1):
    return #just not to hammer my ssd
    machine = os.name
    if (machine == 'nt'):
        nl = '\n\r'
    if (machine == 'posix'):
        nl = '\r'
    if (machine == 'java'):
        print('get fucked java user')
        return
    titleblock = [
        '/*',
        'File name: ',filename,nl,
        ' *Author:', getpass.getuser(), nl,
        ' *Python script author:', 'Claude-David Gaudreault', nl,
        ' *Machine:', machine, nl,
        ' *This file was generated using the C_header.py python script',nl,
        ' *If you want to change this file please modify and rerun the code that generated it',nl,
        ' */',nl
    ]

    headder = open(filename, "w")
    #write title and info
    if (blocktitle == ''): # title block not overwrited
        headder.writelines(titleblock)
    else:
        headder.writelines(['/*', nl])
        for i in range(len(blocktitle)):
            headder.writelines([blocktitle[i],nl])
        headder.writelines(['*/', nl])
    # write start gard
    headder.writelines(['#ifndef ',gard, nl])
    headder.writelines(['#define ', gard,nl])
    #write includes
    for i in range(len(includesanddef)):
        headder.writelines([includesanddef[i], nl])
    #write type
    headder.writelines('   ')
    if(static >= 1):
        headder.writelines('static ')
    headder.writelines([Ctype, ' '])
    #write varname
    headder.writelines([varname,'[',str(len(array)),']', '= {',nl])
    #write array
    if (complex == 1):
        for i in range(len(array)-1):
            headder.writelines(['{',str(PYtype(array.real[i])),',',str(PYtype(array.imag[i])),'},',nl])
        i = i+1
        headder.writelines(['{',str(PYtype(array.real[i])),',',str(PYtype(array.imag[i])),'}};', nl])
    if (complex == 0):
        for i in range(len(array) - 1):
            headder.writelines(['       ',str(PYtype(array[i])), ',',nl])
        i = i + 1
        headder.writelines(['       ',str(PYtype(array[i])),'};', nl])
    # write end gard
    headder.writelines(['#endif ', gard])

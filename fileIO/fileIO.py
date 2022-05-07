import sys


debug = True
def open_file(inputfile):
    try:
        f = open(inputfile, "r")
        return(f)
    except FileNotFoundError:
        if debug:
            print('File Not Found')
        return(sys.stdin)
    except OSEError:
        if debug:
            print('OS Error')
        return(sys.stdin)

def open_output(outputfile):
    try:
        f = open(outputfile, "w")
        return(f)
    except FileNotFoundError:
        if debug:
            print('File Not Found')
        return(sys.stdin)
    except OSEError:
        if debug:
            print('OS Error')
        return(sys.stdin)

def safe_input(in_1 = None, in_2 = None):
    column1 = ''
    column2 = ''
    if in_1 is sys.stdin or in_1 is None:
        column1 = in_1.input()
    if in_2 is sys.stdin or in_2 is None:
        column1 = in_2.input()
    else:
        column1 = in_1.readline()
        column2 = in_2.readline()
        if column1 == column2 == '':
            return('', '', False)
    return(column1, column2, True)

if __name__ == "__main__":
    cflag = True
    infile_1 = open_file('file.input1.txt')
    infile_2 = open_file('file.input2.txt')
    outfile = open_output('file.output.txt')
    while cflag:
        out = []
        c1, c2, cflag = safe_input(infile_1, infile_2)
        if not cflag:
            break
        out.append(c1)
        out.append(c2)
        print('\t'.join(out), file=outfile)

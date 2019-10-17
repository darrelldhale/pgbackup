# This function will take two open files and transfer the contents from the outfile to the infile

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()



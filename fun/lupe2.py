from Bio import Entrez
from substring import substr_after, substr_before
from compare_genome import comparisons
import sys
import os.path
from os import path
import os

if(path.exists("email.txt")):
    with open("email.txt") as file:
        email = file.read()
else:
    emailF = open("email.txt", 'w')
    email = input("Please enter your email: ")
    emailF.write(email)
    emailF.close()

Entrez.email=email

with open('Pantoea_S_sub_S.txt') as file:
    _compare_PSsubS = file.read()
    _compare_PSsubS = _compare_PSsubS.replace("\n", "")

# input the reference from text file

outfile = input("Please enter a file to write results to --example -- [results.txt].  \n****WARNING****: This will delete contents of existing file: ")
if len(outfile) < 3:
    outfile = "results.txt"
print(outfile)
if(path.exists(outfile)):
    open(outfile,'w').close()
# Protein of interest
search_Tag = "leucine-responsive transcriptional regulator"

quit = 0
while quit == 0:
    idinput = input("Please enter a genbank # or LOCUS or press q to quit:  ") # user input for GenBank.  Pantoea_S_sub_S = CP017581.1
    # The decimal is unnecessary.
    idinput = idinput.replace("\n", "")
    idinput = idinput.replace(" ", "")
    testquit = idinput.lower()
    if testquit == "q" or testquit == "quit":
        quit = 1
    else:
        try:
            fetch = Entrez.efetch(db='nucleotide', id=idinput, rettype='gb', retmode='text')
            gb=fetch.read()
            # Check page for search tag.  Delete all characters not located in the translation
            if search_Tag in gb:
                with open('tempgenebankresults.txt', 'w') as f:
                    f.write(gb)
                temp = substr_after(gb,search_Tag)
                temp = substr_after(temp, "translation=")
                temp = substr_before(temp, "gene")
                temp = temp.replace(" ", "")
                temp = temp.replace("\n", "")
                protein_string = temp[1: len(temp)-1]
                output = open(outfile, "a+")
                output.write(idinput)
                output.write(": ")
                output.write(protein_string)
                output.write("\n")


                if _compare_PSsubS == protein_string:
                    print("Same protein string")
                    output.write("Same protein string\n\n")
                else:
                    change, x = comparisons(_compare_PSsubS, protein_string)
                    print(x)
                    print(change, ". Changes: ", len(x))
                    for i in x:
                        for item in i:
                            output.write(str(item))
                            output.write(' ')
                        output.write(', ')
                    output.write("\n")
                    output.write(change)
                    output.write(". Changes: ")
                    output.write(str(len(x)))
                    output.write("\n\n")

                output.close()
            else:
                print("No result for ", search_Tag)
        except:
            print("error fetching data from ncbi")
if path.exists("tempgenebankresults.txt"):
    os.remove("tempgenebankresults.txt")

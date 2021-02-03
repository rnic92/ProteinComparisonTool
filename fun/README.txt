          Genome comparison tool for leucine-responsive transcriptional regulator
          Version 1.01
          1/29/2021
          Nicolas Rohr
Written in Python version 3.7.4 on windows 10.0.18363
Makes use of the Biopython package 1.78 https://biopython.org/docs/1.75/api/Bio.html
All credit for Biopython to Biopython Contributors


To use this simple tool, run using ! python lupe2.py [GenBank# or LOCUS]

This will print the protein string from the search result to results2.txt
Command line output includes
- "same" if the leucine-responsive transcriptional regulator is
equivalent to Pantoea stewartii subsp. stewartii DC283's.
- A list of all differences in the form of (location, [original protein if present], [compared protein if present])

TIPs:
This comparison is easy to change.
Simply email nic.rohr@me.com with the requested reference and search tag.  These can also be modified
locally by creating a new .txt file and changing line 7 to the reference protein.  Modify line 13 with the new search tag.
Some changes may be required in lines 26-33 to ensure the correct strings are being compared.

This is meant to be a very simple and quick tool used for basic comparison in a single project.
Use at your own risk.

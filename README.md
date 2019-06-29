#asciilinesAustin
Copyright (c) 2019 Jeff Austin

This program is a `mini` practice program created for the purpose of practicing creating an open source project.
It accepts a .tvg file as input from the commmand line and, given the information in that
file, manipulates a n x m table filled with period characters ('.') according to parse commands provided
in the tvg file. The first row indicates the character to overwrite the periods with. The second and third 
the values for the row and column to start editing at. The fourth and fifth, respectively, determine whether
the values will be written horizontally or vertically and how many characters will be overwritten.

Build and Run

Nothing is required to build the program as it is written in python3 and interpreted with the standard interpreter.
To run the program (assuming you have python version 3.5 or greater), enter the directory on the command line 
containing `sol.py` and press enter after typing the following:

........................................
$ python3 sol.py yourExternalFyle.tvg
........................................

Where `yourExternalFyle.tvg` is a .tvg file provided in the `tests` directory, or a newly created one (properly formatted according to the assignment description).

Bugs

No bugs, failures, or incomplete behavior promted by testing environments is aware of at this time.
Incomplete and illformatted tvg files are known to cause bahavioral faults in the form of the program panicking.

License

This program is licensed under the "MIT License".  Please
see the file `LICENSE` in the source distribution of this
software for license terms.

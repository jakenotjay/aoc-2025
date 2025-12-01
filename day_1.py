"""Day 1 - Secret Entrance

My interpretation:
- Safe dial 0-99 (always starting at 50)
- Given a rotation sequence of the form:
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
- L indicates deprecation i.e. subtraction, R indicates addition
- HOWEVER, the password is not given by the end combination but by the number of times the dial points towards ZERO
- For the above example:
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0. __1__
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0. __2__
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0. __3__
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.
- The password is 3

Implementation method:
- Create a "safe" class with a simple pointer int that starts at 50, and a "zero_count" variable
- Add a left and right method
- Add a check_zero() method that adds 1 if we're currently at zero
- Add a parser method that iterates over the input file calling left and right.
"""

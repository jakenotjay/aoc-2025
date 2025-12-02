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
- The dial is a circle, so if the dial is turned left from zero one click its 99, similar right from 99 makes it zero
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
- Add a left and right method, if it crosses 99/0 correctly add or subtract to the right amount
- Add a check_zero() method that adds 1 if we're currently at zero
- Add a parser method that iterates over the input file calling left and right.
"""


class Safe:
    """Defines the safe dial"""

    _dial: int

    _zero_count: int

    def __init__(self):
        self._dial = 50
        self._zero_count = 0

    def check_zero(self):
        """Checks if the dial is currently at zero, if so add one to zero_count."""
        if self._dial != 0:
            return

        self._zero_count += 1

    def right(self, count: int):
        """Adds count to the dial, takes the remainder of (100) to get actual val"""
        val = self._dial + count
        self._dial = val % 100
        self.check_zero()

    def left(self, count: int):
        """Removes count from dial, taking remainder of 100 to get the val"""
        val = self._dial - count
        self._dial = val % 100
        self.check_zero()

    def test_val(self, val: int):
        """Raises an error if not the val expected."""
        if self._dial != val:
            raise ValueError(f"Dial value {self._dial} is not equal to {val}")

        print(f"{self._dial} == {val}")

    def get_password(self) -> int:
        return self._zero_count

    def parse_file(self, file: str):
        with open(file) as f:
            lines = f.readlines()

        for line in lines:
            if len(line) == 0:
                break

            direction = line[:1].lower()
            count = int(line[1:])

            if direction == "r":
                self.right(count)
            else:
                self.left(count)


def test_case(safe: Safe) -> int:
    """For a given safe instance, run the test vals and return the password"""
    safe.test_val(50)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(68)
    safe.test_val(82)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(30)
    safe.test_val(52)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.right(48)
    safe.test_val(0)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(5)
    safe.test_val(95)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.right(60)
    safe.test_val(55)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(55)
    safe.test_val(0)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(1)
    safe.test_val(99)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(99)
    safe.test_val(0)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.right(14)
    safe.test_val(14)
    print(f"Safe pass: {safe.get_password()}\n")

    safe.left(82)
    safe.test_val(32)
    print(f"Safe pass: {safe.get_password()}\n")

    return safe.get_password()


if __name__ == "__main__":
    import time

    tik = time.time()
    test_answer = test_case(Safe())
    print(f"Test answer {test_answer}")
    safe = Safe()
    safe.parse_file("day_1_input.txt")
    print(f"Password is {safe.get_password()}")

    tok = time.time()

    print(f"{tok - tik}s")

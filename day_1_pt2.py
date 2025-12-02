"""
"Due to newer security protocols,
please use password method 0x434C49434B until further notice.


Count the number of times the dial crosses zero, including if it crosses more than once.

For the same example as before:
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
- Password is 6
"""

from day_1 import Safe, test_case


class BasicSafe(Safe):
    def increment(self):
        self._dial += 1
        if self._dial == 100:
            self._dial = 0

    def decrement(self):
        self._dial -= 1

        if self._dial == -1:
            self._dial = 99

    def right(self, count: int):
        for i in range(count):
            self.increment()
            self.check_zero()

    def left(self, count: int):
        for i in range(count):
            self.decrement()
            self.check_zero()


# class Safe_0x434C49434B(Safe):
#     _rotation_count: int

#     def __init__(self):
#         super().__init__()
#         self._rotation_count = 0

#     def right(self, count: int):
#         val = self._dial + count
#         self._rotation_count += val // 100
#         self._dial = val % 100

#     def left(self, count: int):
#         val = self._dial - count

#         if val == 0:
#             self._rotation_count += 1

#         if val < 0:
#             self._rotation_count += abs(val + 1) // 100

#         self._dial = val % 100

#     def get_password(self) -> int:
#         return self._rotation_count + self._zero_count


def test_case_2(safe):
    safe.right(1000)

    print(safe.get_password())

    safe.left(1000)
    print(safe.get_password())


if __name__ == "__main__":
    import time

    tik = time.time()
    test_answer = test_case(BasicSafe())
    # test_case_2(Safe_0x434C49434B())
    print(f"Test answer {test_answer}")
    safe = BasicSafe()
    safe.parse_file("day_1_input.txt")

    safe = Safe_0x434C49434B()
    safe.parse_file("day_1_input.txt")
    print(f"Password is {safe.get_password()}")

    tok = time.time()

    print(f"{tok - tik}s")

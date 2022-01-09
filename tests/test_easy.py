"""
Test suite for easy deck

If needed, install pytest: pip install pytest

Then run the command: pytest
"""
import os
import re
import sys
from io import StringIO

PLACE_HOLDER = "⚂"


def run_card(file_name, values=range(1, 21)):
    """Returns a list of printed lines"""
    file_path = os.path.normpath(
        os.path.join(
            sys.path[0], "../projects/programming-time/decks/easy", file_name + ".py"
        )
    )

    with open(file_path, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            line = line.rstrip()
            # remove blank and comment lines
            if line != "" and not re.match(r"^\s*#", line):
                lines.append(line)
        prog_text = "\n".join(lines)

    # replace PLACE_HOLDER symbols with actual values
    value_index = 0
    while prog_text.find(PLACE_HOLDER) != -1:
        prog_text = prog_text.replace(PLACE_HOLDER, str(values[value_index]), 1)
        value_index += 1

    # capture stdout output
    old_stdout = sys.stdout
    sys.stdout = my_stdout = StringIO()

    # pylint: disable = exec-used
    exec(prog_text)

    sys.stdout = old_stdout
    return my_stdout.getvalue().strip().split("\n")


def test_01():
    """gcd"""
    output = run_card("01", [12, 16])
    assert output[-1] == "4"


def test_02():
    """Diffie–Hellman Key Exchange"""
    output = run_card("02", [15, 7])
    assert output[-1] == "Shared Secret: 15 15"
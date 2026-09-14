"""BUG 05 - Tier 2 - target time: 12 minutes

Register students for a company's drive.

The first company's list is fine. The second company somehow starts with
the first company's students already in it. Nobody wrote code to do that.

Hint: run the tests in order and watch how state leaks between calls.
"""


def register(name, drive=[]):
    drive.append(name)
    return drive

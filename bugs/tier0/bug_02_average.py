"""BUG 02 - Tier 0 - target time: 3 minutes

Average CGPA for a batch. It crashes. Read the traceback bottom-up:
the LAST line tells you what went wrong, the lines above tell you where.
"""


def average_cgpa(cgpas):
    total = 0
    for cgpa in cgpas:
        total = total + cgpa
    return total / len(cgpa)

# Placement Tracker — C++ assessment sandbox

This folder is a small C++ version of the workshop's placement-tracker task.
It is separate from the Python teaching code so students can practise in a
language available in the Capgemini assessment.

## The task

Implement <code>studentsAtRisk</code> in <code>placement_tracker.cpp</code>.

A student is at risk when:

- their CGPA is below <code>6.0</code>, or
- they have one or more backlogs.

Return the at-risk students sorted by CGPA, worst first. For equal CGPAs,
preserve their original order. Do not modify the input vector.

## Compile and run

From this folder:

~~~bash
g++ -std=c++17 -Wall -Wextra -pedantic placement_tracker.cpp -o placement_tracker
./placement_tracker
~~~

The starter program is expected to fail until <code>studentsAtRisk</code> is implemented.

## Suggested AI prompt

~~~text
I am solving a C++17 coding task. First explain the requirements,
edge cases, and implementation plan. Do not edit code yet.

Then implement the smallest change to studentsAtRisk in
placement_tracker.cpp.

Rules:
- CGPA below 6.0 OR backlogs greater than 0 means at risk
- sort by CGPA ascending
- preserve input order for equal CGPAs
- do not modify the input vector
- use only the C++ standard library

After editing, show the diff and tell me to compile with:
g++ -std=c++17 -Wall -Wextra -pedantic placement_tracker.cpp -o placement_tracker
~~~

Students must compile the result, test an edge case, and explain every
generated line before accepting it.

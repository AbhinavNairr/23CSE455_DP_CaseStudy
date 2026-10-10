# Part 3 — Evidence

Raw, real run logs for the cross-language comparison. Each `*.txt` records the
exact command, runtime/compiler version, program output, the five timing samples
and the median. These are the only source for the values in
`../../data/cross_language.csv`.

Files:

- `Strategy_javascript.txt`, `Strategy_python.txt`, `Strategy_java.txt`, `Strategy_cpp.txt`
- `State_javascript.txt`, `State_python.txt`, `State_java.txt`, `State_cpp.txt`

## Measurement rules (fixed for the whole case study)

**LOC (`source_loc`).** Physical lines of the production snippet only, excluding
blank lines, comment lines (`//`, `#`, `/* ... */`, and Python module
docstrings) and excluding the test file. Computed per file; values: Strategy —
JS 75, Python 49, Java 77, C++ 70; State — JS 94, Python 57, Java 83, C++ 97.

**Cyclomatic complexity (`max_function_cc`).** For each function/method, CC = 1 +
the number of decision points, where a decision point is each `if`, `else if`,
`for`, `while`, `case`, `catch`, each `&&` / `||` / `and` / `or`, and each
ternary/conditional expression. The reported value is the maximum over all
functions in the production snippet. A Python comprehension's `if` filter counts
as one decision; its `for` clause does not. Because the State pattern moves
transition logic into polymorphic objects, its snippets are branch-free in the
garbage-collected languages (CC 1); C++ is 2 only for its manual
memory-management guard.

**Timing (`median_process_ms`).** Compile first (where applicable); discard one
warm-up run; time five runs with a high-resolution stopwatch; report the median.
The measured quantity is whole-process wall time — runtime/VM startup plus
program execution — so interpreted/VM languages include their startup cost. All
runs are on one machine, sequentially.

No value here is estimated or copied; all come from the logs in this directory.

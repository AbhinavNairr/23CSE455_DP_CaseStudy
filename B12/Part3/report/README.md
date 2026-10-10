# Part 3 — Cross-language Comparison

Team B12. Patterns compared: **Strategy** (slot allocation) and **State** (EV
charging session). Languages: JavaScript, Python, Java, C++. All numbers are from
real runs recorded in `../evidence/` and in `../../data/cross_language.csv`.

## Results

| Pattern | Language | LOC | max CC | Test result | Median ms |
|---|---|---|---|---|---|
| Strategy | JavaScript | 75 | 5 | 5/5 | 80.866 |
| Strategy | Python | 49 | 6 | 5/5 | 112.122 |
| Strategy | Java | 77 | 7 | 5/5 | 185.646 |
| Strategy | C++ | 70 | 8 | 5/5 | 18.977 |
| State | JavaScript | 94 | 1 | 13/13 | 73.154 |
| State | Python | 57 | 1 | 13/13 | 67.420 |
| State | Java | 83 | 1 | 13/13 | 173.178 |
| State | C++ | 97 | 2 | 13/13 | 20.833 |

## Observations

- **Same behaviour, same tests.** The identical cases pass in all four languages;
  the pattern's semantics do not depend on the language.
- **LOC tracks verbosity, not difficulty.** Python is shortest in both patterns
  (duck typing / no interface boilerplate); Java is longest for Strategy; C++ is
  longest for State because of header guards and out-of-line definitions needed
  to resolve incomplete types.
- **Cyclomatic complexity is lowest for State.** Moving the transition logic
  into polymorphic state objects removes every branch from the context — max CC
  is 1 in the garbage-collected languages. Counted decisions appear only in the
  Strategy `choose()` methods.
- **Timing is dominated by process/VM startup,** not the snippet. Java's ~170-185
  ms is almost entirely JVM startup; Node ~70-80 ms; the statically linked native
  C++ binary is fastest (~19-21 ms) by roughly an order of magnitude. These
  figures measure whole-process wall time and must not be read as algorithmic
  performance of the pattern.
- **Language-specific idioms:** JavaScript and Python express the Strategy
  interface as an abstract base class; Java uses an explicit `interface`; C++
  uses a pure-virtual class with `override`. State uses default methods (Java
  `default`, JS/Python inherited methods) to share the invalid-transition
  handling; C++ adds one guard branch for manual memory management.

See `../evidence/README.md` for the exact LOC, complexity and timing rules.

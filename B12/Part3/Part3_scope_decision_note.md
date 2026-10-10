# Part 3 scope — evidence-based decision note (B12)

Date: 2026-10-10
Author: Team B12

Status: **OPEN — pending instructor clarification.** No Part 3 work was expanded
or changed on the basis of this note; the existing implementations are left as
delivered. This note records what the instructions say, what the repository
currently contains, and why the two do not fully agree.

---

## 1. What the instruction says (verbatim)

From `DP_Csestudy_INSTRUCTIONS.pdf`, page 2, section **4. cross_language.csv —
snippet comparison**:

> "One row = one representative confirmed pattern instance implemented in one
> language. **For each detected pattern type, implement its small problem in all
> four languages, using the same inputs and expected outputs.**"

From the same PDF, page 3, the required repository hierarchy:

> "Part3/ **pattern_problem_name/ repeat for each pattern type**"

From the report template (`DP_Casestudy_completed.tex`, line 81, section *Part 3
Cross-language comparison*):

> "**For each confirmed pattern type, choose one representative verified
> instance.** Implement its small problem/snippet in Java, Python, JavaScript and
> C++; preserve the same pattern and behavior."

## 2. What the repository currently contains

`data/cross_language.csv` has 8 rows = **2 pattern types × 4 languages**:

| Pattern type | Representative instance | Source | Languages |
|---|---|---|---|
| Strategy | Slot allocation strategies | Part 1 baseline (Change 1) | JS, Python, Java, C++ |
| State | EV charging session lifecycle | Part 2 (Change 2) | JS, Python, Java, C++ |

All 8 rows report real passes (Strategy 5/5, State 13/13 per language) with raw
logs in `Part3/evidence/`. Implementation folders exist as
`Part3/Strategy/<lang>` and `Part3/State/<lang>`.

## 3. The ambiguity

Confirmed pattern types in this study are **not limited to Strategy and State**:

- Part 1 baseline (`data/patterns.csv`) confirms **4 pattern types**:
  Strategy, Repository, Dependency Injection / IoC, and Layered Architecture
  (7 instances).
- Part 2 (`data/patterns_evolution.csv`) adds State and Observer.

So the phrase "each detected pattern type" admits at least three readings:

1. **Baseline confirmed types only** → Strategy, Repository, DI/IoC, Layered
   Architecture (4 types). Repository / DI / Layered are architectural or
   framework-wiring patterns that do not have a natural standalone
   cross-language "small problem" in the same way a behavioural pattern does,
   so this reading is awkward to satisfy mechanically.
2. **All confirmed types across the study** → the 4 baseline types plus State and
   Observer (6 types). This is the most literal reading of "each ... pattern
   type" and would require 4 more snippets × 4 languages (Repository, DI/IoC,
   Layered, Observer).
3. **A representative subset** → the word "representative" in "one
   representative confirmed pattern instance" can be read as allowing the team to
   pick representative behavioural types (Strategy + State), which is what was
   implemented.

The instruction does not resolve which reading is intended, and the template's
own example shows only a single illustrative pattern per row.

## 4. Decision taken (no expansion)

Per team lead instruction, **Part 3 was not expanded and was not changed.** The
delivered Strategy + State implementations (8 suites, all passing) are kept as
they are. Expanding to readings (1) or (2) would add work that may not be wanted
and cannot be reverted cheaply.

## 5. Recommendation

**Ask the instructor (Madam)** which reading of "each detected pattern type"
applies:

- If reading (3) is accepted → current Part 3 already complies; no action.
- If reading (1) or (2) is required → Part 3 must be extended so that each
  required pattern type has one representative instance implemented in all four
  languages with the same inputs and expected outputs, and
  `data/cross_language.csv` extended with one row per type per language.

Until this is confirmed, Part 3 should be treated as **complete for Strategy and
State, with scope compliance unresolved**.

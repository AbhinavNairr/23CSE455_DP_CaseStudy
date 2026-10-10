# B12 — Central LLM Research References

This is the **single central index** for the LLM-assisted research used by Team
B12. Per-part folders (`Part1/llm/`, `Part2/llm/`, `Part3/llm/`) hold the raw
prompts, inputs, outputs and verification notes for each part; this file records
the shared external sources of that research and what each one is used for.

> Nothing in this repository treats an LLM conversation or document as evidence
> for any pattern, count, metric, or test result. Those are established only by
> direct inspection of the source code and by real test runs.

---

## 1. LLM-assisted research conversation (ChatGPT, shared)

- **Exact URL (preserved verbatim — do not shorten, replace or re-invent):**
  `https://chatgpt.com/share/6aca22a9-2844-83ec-8126-e6f81ef8e85e`
- **Title shown by the share page:** `ChatGPT - Analyze Design Patterns`
- **Type:** LLM-assisted research conversation (ChatGPT).
- **Access status (checked 2026-10-10):** the share link is publicly reachable
  (HTTP 200) and the returned page embeds topic content — e.g. it contains the
  strings `SlotAllocationStrategy`, `FirstAvailableStrategy`, and the baseline
  commit `940daeeab52d5a0b101ce0e76813bcfac88e01a1`.
- **Verification note:** the content of this conversation has **not** been
  independently verified as correct. It is recorded as a research artifact only.
- **What it supports (subject to verification):**
  - Part 1 — candidate-pattern discussion prior to source inspection.
  - Part 2 — the evolution-scenario reasoning (dynamic allocation → Strategy;
    EV charging → State; occupancy monitoring → Observer).
  - Part 3 — the proposed cross-language selection (Strategy + State).

## 2. Original research document (DOCX)

- **Path (kept in place, NOT copied into the repository, NOT modified):**
  `C:\Users\eswar\Downloads\Analyze Design Patterns.docx`
- **Size / status:** 99,835 bytes; exists and was read on 2026-10-10.
- **Type:** prior research document containing LLM-assisted analysis (a design
  discussion, not source evidence about the application).
- **Contents (as read, summarised):**
  - A conceptual parking-management model with seven modules and their design
    pressures.
  - Candidate patterns, alternatives, and candidate over-engineering cases.
  - A design-pattern decision matrix.
  - The Part 3 selection of **Strategy** and **State** for cross-language
    comparison, and proposed NestJS mappings/implementation considerations.
  - A prior baseline source-code analysis prompt and its tentative results
    (Strategy marked confirmed; State/Repository/DI/Decorator marked uncertain;
    Observer/Factory/Adapter/Command/Singleton marked rejected, all "pending
    verification").
- **Relationship to the shared conversation:** the DOCX and the shared ChatGPT
  conversation cover the same topics and reference the same baseline commit.
  They are **not** claimed to be identical (identical contents were not
  verified).

## 3. Evidence tiers (keep these distinct everywhere)

1. **Evidence from source code** — verifiable `file:line` facts about the
   original application. This is the only basis for CONFIRMED pattern claims.
2. **Research findings/proposals (DOCX + LLM discussion)** — prior reasoning and
   suggestions; may be right or wrong; never auto-promoted to fact.
3. **Assumptions requiring validation** — stated as assumptions, with the check
   that would resolve them.
4. **B12 final design decisions** — the team's chosen direction after review.
5. **Executed tests and results** — only real runs; commands and raw output
   recorded. No fabricated or "expected" results.

## 4. Cross-references

- `data/llm.csv` — register of individual LLM prompt/input/output artifacts.
- `Part1/llm/README.md`, `Part2/llm/README.md`, `Part3/llm/README.md` — per-part
  raw artifacts; each should point back to this file for the shared sources.

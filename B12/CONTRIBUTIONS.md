# B12 — Team Contributions and AI (ChatGPT) Conversations

**Team:** B12 — *Design Pattern Identification and Evolution in a NestJS-Based
Parking Management Application.* All members are from batch **CSE**.

This table records each member's contribution only so far as it can be evidenced
by the artifacts in this repository and by the members' shared ChatGPT
conversations (checked 2026-10-14). It is deliberately not a balanced split and
nothing is invented: where authorship is **not** recorded — the repository has a
single Git author and the conversations cover Part 1 research — the contribution
is stated as a team declaration and flagged, never guessed.

| Team member | Roll number | Verified contribution | Supporting evidence | ChatGPT conversation |
| --- | --- | --- | --- | --- |
| Samanthula Eswar | AM.SC.U4CSE23349 (CSE) | Part 1 pattern discovery and the pattern decision matrix; the design direction adopted for Parts 2–3 — the three evolution scenarios (Strategy slot allocation, State EV charging, Observer occupancy monitoring) and the cross-language selection (Strategy + State); baseline source verification at commit `940daee`. | `Part1/report/B12_Part1_Pattern_Discovery.md`, `Part2/changes/Change1..3/`, `Part3/`, `LLM_RESEARCH_REFERENCES.md` | [Analyze Design Patterns](https://chatgpt.com/share/6aca22a9-2844-83ec-8126-e6f81ef8e85e) |
| Bantupalli Harsha Vardhan | AM.SC.U4CSE23210 (CSE) | Part 1 discovery-report drafting; the seven-module pattern inventory separating GoF patterns from architectural and NestJS-framework features; the pattern-to-source-code mapping; source-verification review of the pattern claims. | `Part1/report/B12_Part1_Pattern_Discovery.md`, `Part1/evidence/` | [Write Pattern Discovery Report](https://chatgpt.com/share/6acf4ad3-5900-83ee-bd23-a3440efaf33a) |
| Rayudu Vamsi Krishna | AM.SC.U4CSE23344 (CSE) | Independent Part 1 pattern discovery and report drafting, cross-checking candidate patterns against source `file:line` references. | `Part1/report/B12_Part1_Pattern_Discovery.md`, `Part1/evidence/pattern_evidence.md` | [Write Pattern Discovery Report](https://chatgpt.com/share/6acf4a3b-0d60-83ee-af0e-eb5a739699e1?ogimg=plain) |
| Sammeta Pavan | AM.SC.U4CSE23350 (CSE) | Preliminary Part 1 pattern-discovery draft and a review/improvement pass over the draft report. | `Part1/report/B12_Part1_Pattern_Discovery.md` | [Pattern Discovery Analysis](https://chatgpt.com/share/6acf5448-c740-83e8-b064-e5604a16fb75?ogimg=plain) |

## Evidence notes

- **Conversations are research artifacts, not evidence.** The four ChatGPT links
  above record AI-assisted research. As stated in `LLM_RESEARCH_REFERENCES.md`
  and `data/llm.csv`, no LLM conversation is used as evidence for any pattern,
  count, metric or test result; those come only from direct source inspection and
  real runs.
- **Where the evidence is strong.** The evolution scenarios and the pattern
  selection discussed in the conversations match the delivered artifacts exactly:
  Change 1 = Strategy, Change 2 = State and Change 3 = Observer
  (`Part2/changes/`, `Part2/prompts/Part2_prompt.txt`), and Part 3 is built on
  Strategy + State (`Part3/`). The baseline commit `940daee` referenced in the
  research matches `README.md` and the Part 1 report.
- **Where it is not recorded.** The Part 2 and Part 3 code, tests and metrics were
  produced by the team, but per-member authorship is **not** recorded in Git (a
  single author) or in the conversations. It is therefore a team declaration and
  is not attributed to an individual here.
- Names and roll numbers match `README.md` and `B12_Report.tex`.

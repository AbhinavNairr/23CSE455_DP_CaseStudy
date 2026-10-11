# Part 3: Python and JavaScript

I used two patterns from Part 1: Strategy and Observer. This folder has small
examples in Python and JavaScript. They show how the patterns work without
needing the full Next.js app or any online service.

## Patterns I used

| Pattern | Name in Part 1 | Where it appears in the app |
|---|---|---|
| Strategy | LLM Provider Streaming Strategy | `code/features/ai-assistant/llmService.ts:69-155` |
| Observer | Auth State Observer | `code/features/auth/context/AuthProvider.tsx:37-50` |

I used the original app at commit
`90ec6565877053ee0e93e9f09dcc7c7213aa4832`. The Strategy example reads
sample messages from three providers. The Observer example sends sample sign-in
and sign-out events to a subscriber. These examples are based on the app's
patterns, but they are not copies of its app code. The app diagrams are in
`Part1/uml_strategy.mmd` and `Part1/uml_observer.mmd`. Diagrams for these examples
are in each pattern folder as `roles.mmd`.

## How to run the tests

Open a terminal in `B14/` and run:

```powershell
python Part3/llm_provider_streaming/python/test_implementation.py
node --test Part3/llm_provider_streaming/javascript/test_implementation.mjs
python Part3/auth_state_observer/python/test_implementation.py
node --test Part3/auth_state_observer/javascript/test_implementation.mjs
python Part3/verify_cross_language.py
```

Each pattern has one `fixtures.json` file. Python and JavaScript use the same
inputs and expected results. You can also run a program with one JSON file:

```powershell
python Part3/llm_provider_streaming/python/implementation.py Part3/llm_provider_streaming/benchmark_input.json
node Part3/auth_state_observer/javascript/implementation.mjs Part3/auth_state_observer/benchmark_input.json
```

## Results

I ran the tests on Windows 11 with Python 3.12.10 and Node.js 24.15.0.

| Pattern | Language | Tests passed | Code lines | Highest function CC | Median run time |
|---|---|---:|---:|---:|---:|
| Strategy | Python | 11/11 | 53 | 8 | 96.870 ms |
| Strategy | JavaScript | 11/11 | 47 | 9 | 57.485 ms |
| Observer | Python | 15/15 | 74 | 21 | 100.344 ms |
| Observer | JavaScript | 15/15 | 62 | 20 | 57.960 ms |

Running each shared input through both programs also passed 26/26 cases. Test
logs are in `evidence/tests/`. The results table for the team report is
`../data/cross_language.csv`.

For code lines and complexity, I used Lizard 1.24.1. Code lines exclude empty
lines, comments and tests. CC means cyclomatic complexity, which counts paths
through a function. To check again, run:

```powershell
python -m pip install lizard==1.24.1
python Part3/measure_static.py
```

For run time, I did one warm-up run and then five timed runs on the same
computer. Timing includes starting the program, reading the JSON file and
printing the result. It does not include tests or compilation. All five times
are in `evidence/timings/process_timings.json`. Run `python Part3/benchmark.py`
to measure again. These examples are so small that startup time has a large
effect, so the times do not prove one language has a better design.

## What is left

Soorya still needs to add Java and C++ using the same test cases. I wrote
`SOORYA_INTEGRATION.md` for that. Nivedita's Part 2 work was still an interim
handoff when I made this folder. The final team report needs her finished
changes and datasets before the whole case study can be called complete.

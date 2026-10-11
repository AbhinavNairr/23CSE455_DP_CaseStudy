# Part 3 — Cross-Language Comparison (B14)

## Scope and relationship to Parts 1 and 2

This working submission compares **two** confirmed Part 1 patterns, as requested:
1. **Strategy — LLM Provider Streaming Strategy** (`code/features/ai-assistant/llmService.ts`)
2. **Observer — Auth State Observer** (`code/features/auth/context/AuthProvider.tsx` and `AuthContext.tsx`)

RBAC is intentionally omitted to keep the scope to two patterns. It is an architecture/security pattern rather than a GoF pattern.

The comparison examples are small, deterministic demonstrations of each pattern's intent; they are not ports of the production Next.js application or its network/Supabase dependencies.

Part 2's uploaded evidence records:
- CH01: centralize model-to-provider inference (`inferProviderFromModel()`); its implementation note explicitly says this did not refactor every provider-selection branch.
- CH02: extract publication title/content validation helpers; no new GoF pattern is claimed.
- CH03: extract `parseGeneratedPostJson()` to remove duplicated JSON parsing.

CH02 and CH03 do not change the two selected collaborations. CH01 is relevant to the Strategy context, but the uploaded `B14/code/features/ai-assistant/llmService.ts` remains the original source snapshot and does not contain the helper described in the Part 2 implementation note. Thus the Part 3 demonstration preserves the provider-selection behaviour from the confirmed Part 1 baseline, and does not claim to benchmark the post-CH01 production source. If the team later merges the Part 2 source changes into `code/`, update the source-snapshot note and evidence links.

## Common test cases

`test-cases/common_test_cases.csv` is the shared language-independent specification. Java and C++ runners implement the same cases:
- Strategy: S01–S04 (Claude, OpenAI, Gemini, unsupported provider)
- Observer: O01–O04 (sign-in, sign-out, unsubscribe, multiple observers)

## Build and run

Requires a JDK (`javac`, `java`) and a C++17 compiler (`g++`).

From this `Part3/` directory:

```sh
mkdir -p build/java/strategy build/java/observer build/cpp
javac -d build/java/strategy strategy/java/Strategy.java strategy/java/StrategyTest.java
java -cp build/java/strategy StrategyTest
javac -d build/java/observer observer/java/AuthObserver.java observer/java/ObserverTest.java
java -cp build/java/observer ObserverTest
g++ -std=c++17 -O2 -Wall -Wextra -pedantic strategy/cpp/test_strategy.cpp -o build/cpp/test_strategy
./build/cpp/test_strategy
g++ -std=c++17 -O2 -Wall -Wextra -pedantic observer/cpp/test_observer.cpp -o build/cpp/test_observer
./build/cpp/test_observer
```

## Measurements

- LOC counts include production files only (`Strategy.java`, `AuthObserver.java`, `strategy.hpp`, `observer.hpp`), excluding blank lines and comments; test runners are excluded.
- Cyclomatic complexity has been audited function-by-function using the documented McCabe rule `M = 1 + D`; decision points and calculations are in `evidence/complexity_audit.csv` and `evidence/complexity_audit.md`. This is a transparent manual source-level audit, not output from an external static-analysis package.
- Timing procedure: compile before measurement; run one warm-up, then five measured process launches on the same machine. `median_process_ms` includes process startup and the test harness, and excludes compilation.
- Raw timings are in `evidence/timing_raw.csv`; summary rows are in `cross_language.csv`.
- The numbers are machine/environment-specific and should be regenerated on the team's submission machine if required.
- Java and C++ timing results are not proof that one language is generally faster: process startup and runtime initialization materially affect these small examples.

## Important scope limitation

The supplied professor instructions specify Java, Python, JavaScript, and C++. This user-requested working scope includes Java and C++ only. Unless the professor has approved a reduced scope, this is not a complete four-language submission.

## Evidence and AI records

- `evidence/test_results.txt`: actual compile/test output from this environment.
- `evidence/environment.txt`: tool versions.
- `evidence/timing_raw.csv`: raw timing runs.
- `evidence/complexity_audit.csv` and `evidence/complexity_audit.md`: method-level complexity decisions, calculations, and rule.
- `llm/part3_prompt.txt`: reusable prompts.
- `llm/llm.csv`: header-only template. Add actual AI interaction records only; do not invent model use or outputs.

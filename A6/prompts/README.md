# LLM records

The course rules say LLM records must be real runs ("Do not submit invented LLM records"). Every output file here is
the actual answer of the model named in `data/llm.csv`, saved unchanged except for Markdown capture (see each file's header).

## How the runs were made (2026-10-11)
- **Claude record** - `Dilip_Kumar_Reddy_claude_*`: Dilip Kumar Reddy's own prompt to Claude Opus 5.5 in the Claude Code
  desktop app (paid tier, not a free tool) and the model's first reply.
- **ChatGPT records** - the 9 other prompts: team members were not available, so with Dilip's approval each prompt file
  was pasted unchanged into a new chat on **chatgpt.com (free tier, logged out)** from Dilip's computer, with the
  browser driven by Claude Code. The interface showed only "ChatGPT" (no model name). The member named in a file is
  the **owner of that topic**, not the person who typed the prompt.
- Code in the cross-language answers was extracted and actually compiled/run (`tools/run_llm_code.py`); the logs are
  `*_coderun_02.txt`. All other claims were checked against `Part1/code`, `Part2/code` and the test results.

| Topic owner | Prompt | Part | Verdict | Verification |
|---|---|---|---|---|
| Dilip Kumar Reddy | `Dilip_Kumar_Reddy_claude_prompt_01.txt` | Application study / pattern discovery (Claude) | partial | `Dilip_Kumar_Reddy_claude_verification_01.md` |
| Dilip Kumar Reddy | `Dilip_Kumar_Reddy_prompt_01.txt` | Pattern discovery | partial | `Dilip_Kumar_Reddy_verification_01.md` |
| Sai Sameer | `Sai_Sameer_prompt_01.txt` | Evolution CH01 | correct (analysis) / partial (design) | `Sai_Sameer_verification_01.md` |
| Sai Sameer | `Sai_Sameer_prompt_02.txt` | Cross-language Observer | partial | `Sai_Sameer_verification_02.md` + `Sai_Sameer_coderun_02.txt` |
| M Kumar | `M_Kumar_prompt_01.txt` | Evolution CH02 | partial | `M_Kumar_verification_01.md` |
| M Kumar | `M_Kumar_prompt_02.txt` | Cross-language State | correct | `M_Kumar_verification_02.md` + `M_Kumar_coderun_02.txt` |
| K Harish | `K_Harish_prompt_01.txt` | Evolution CH03 | partial | `K_Harish_verification_01.md` |
| K Harish | `K_Harish_prompt_02.txt` | Cross-language Strategy | partial | `K_Harish_verification_02.md` + `K_Harish_coderun_02.txt` |
| S Leela Shankar | `S_Leela_Shankar_prompt_01.txt` | Pattern discovery (dataset audit) | correct | `S_Leela_Shankar_verification_01.md` |
| S Leela Shankar | `S_Leela_Shankar_prompt_02.txt` | Cross-language metrics | correct | `S_Leela_Shankar_verification_02.md` |

Each topic owner should read their verification file and sign it (see `HUMAN_VERIFICATION.md`).

## Re-running
`python tools/make_prompt_bundles.py` regenerates the prompt files from `Part1/code`, `Part3/test-cases` and `data/`.
`python tools/run_llm_code.py prompts/<name>_output_02.md <scratch-dir>` recompiles and reruns the generated code.

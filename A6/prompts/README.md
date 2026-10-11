# LLM records - how each member creates them

The course rules say LLM records must be real runs ("Do not submit invented LLM records"). Each file below must be
pasted by the member it is assigned to, and the answer saved exactly as the model gave it.

| File | Who runs it | Part | Tool |
|---|---|---|---|
| `Dilip_Kumar_Reddy_claude_prompt_01.txt` | Dilip Kumar Reddy (already recorded) | Pattern discovery / application study | Claude Code session (paid tier, not free) |
| `Dilip_Kumar_Reddy_prompt_01.txt` | Dilip Kumar Reddy | Pattern discovery | ChatGPT and claude |
| `Sai_Sameer_prompt_01.txt` | Sai Sameer | Evolution CH01 | ChatGPT and Gemini |
| `Sai_Sameer_prompt_02.txt` | Sai Sameer | Cross-language Observer | ChatGPT and Gemini |
| `M_Kumar_prompt_01.txt` | M Kumar | Evolution CH02 |ChatGPT|
| `M_Kumar_prompt_02.txt` | M Kumar | Cross-language State | ChatGPT|
| `K_Harish_prompt_01.txt` | K Harish | Evolution CH03 |ChatGPT|
| `K_Harish_prompt_02.txt` | K Harish | Cross-language Strategy | ChatGPT|
| `S_Leela_Shankar_prompt_01.txt` | S Leela Shankar | Pattern discovery (dataset audit) |ChatGPT|
| `S_Leela_Shankar_prompt_02.txt` | S Leela Shankar | Cross-language metrics |ChatGPT|

## Steps (about 10 minutes per person)
1. Open https://chatgpt.com (or https://gemini.google.com) and start a **new chat**.
2. Open your prompt file, select **all** the text, copy it, paste it into the chat and send it. Do not edit it.
3. When the answer finishes, click the model's **Copy** button under the answer.
4. Create `<same name>_output_0N.md` in this folder (for example `Sai_Sameer_output_01.md`) and paste the answer unchanged.
5. Write down the **model name shown on screen** (for example "ChatGPT - GPT-5 mini") and the **date**, and send both
   to Dilip with the output file. They go into `data/llm.csv` column `model_and_date`.

The verification files (`*_verification_0N.md`) are written afterwards by checking every claim in the output against the
source code and test results; the result goes into `data/llm.csv` column `evaluation`
(correct / partial / incorrect / cannot confirm).

`tools/make_prompt_bundles.py` regenerates the prompt files from `Part1/code`, `Part3/test-cases` and `data/`.

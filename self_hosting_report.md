# Self-Hosting Report

## Task 1 — Benchmark two local models

| Model | Approx size / quant | Load time (s) | Tokens/sec | RAM used | Quality note |
|-------|---------------------|---------------|------------|----------|--------------|
| llama3.2:3b | 3B | 1.009435 seconds | 95.10270596918078 | 0.15 | Detailed and accurate explanation of an inference engine. |
| qwen2.5:0.5b | 0.5B | 0.629757 | 260.1735515606081 | 0.14 | Understandable answer but less precise; incorrectly describes an inference engine as a machine learning model. | 

**Trade-off you observed (2–3 sentences):**

> The larger llama3.2:3b model took longer to load and ran at roughly half the tokens/sec of qwen2.5:0.5b, but it produced a more accurate and conceptually correct definition of an inference engine. The smaller qwen2.5:0.5b was noticeably faster and used far less RAM, but its answer was less precise and conflated an inference engine with a machine learning model. Overall, smaller models trade accuracy and depth for speed and a lighter memory footprint.

## Task 3 — VLM: local vs hosted

Image used: `sample_chart.png`. Task performed: captioning + visual question answering (describing the chart contents and reading values from it).

| System | Answer (short) | Speed | Cost |
|--------|----------------|-------|------|
| Local VLM (moondream) | Correctly describes bar chart (2 blue bars, approx 12 and 8 units, total 14 people) | ~3–6s | free / local |
| Gemini (multimodal) | Correctly reads chart: 4 models compared (Qwen2.5 0.5B fastest ~98 tok/s, Llama 3.2 3B ~61, Gemma 3 4B ~44, Llama 3.1 8B slowest ~27). Clearly explains speed vs model size trade-off. | ~1–3s | free tier |

**Comparison (2–3 sentences):**

> Gemini produced a more accurate and detailed reading of the chart, correctly identifying all four model labels and their exact tokens/sec values along with the overall size-vs-speed trend, while moondream gave a much vaguer description with incorrect bar values and an unrelated "people" framing. Gemini was also slightly faster on average. However, moondream ran entirely locally at no cost and with no internet dependency, making it a reasonable free fallback even though its output quality was clearly lower for this OCR/chart-reading task. 
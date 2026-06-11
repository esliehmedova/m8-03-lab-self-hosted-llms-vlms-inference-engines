# Self-Hosting Report

Fill in the tables with real numbers from **your** machine. Honest, small
numbers beat invented impressive ones.

## Task 1 — Benchmark two local models

Same prompt for both. Get RAM from your OS activity monitor / `top`.

| Model | Approx size / quant | Load time (s) | Tokens/sec | RAM used | Quality note |
|-------|---------------------|---------------|------------|----------|--------------|
| llama3.2:3b | 3B | YOUR_VALUE | YOUR_VALUE | YOUR_VALUE | Detailed and accurate explanation of an inference engine. |
| qwen2.5:0.5b | 0.5B | YOUR_VALUE | YOUR_VALUE | YOUR_VALUE | Understandable answer but less precise; incorrectly describes an inference engine as a machine learning model. |


**Trade-off you observed (2–3 sentences):**

> TODO

## Task 3 — VLM: local vs hosted

Image used: `sample_chart.png` (provided) or your own — committed in this
repo. Task performed: TODO (caption / VQA / OCR).

| System | Answer (short) | Speed | Cost |
|--------|----------------|-------|------|
| Local VLM (moondream) | Correctly describes bar chart (2 blue bars, approx 12 and 8 units, total 14 people) | ~3–6s | free / local |
| Gemini (multimodal) | Correctly reads chart: 4 models compared (Qwen2.5 0.5B fastest ~98 tok/s, Llama 3.2 3B ~61, Gemma 3 4B ~44, Llama 3.1 8B slowest ~27). Clearly explains speed vs model size trade-off. | ~1–3s | free tier |

**Comparison (2–3 sentences):**

> TODO — quality, speed, and cost. Where did the local VLM keep up, and
> where did it visibly fall short?

Answers;

Explain what an inference engine is in 3 sentences.
An inference engine is a software component that uses logical rules and facts to deduce conclusions or make
decisions based on the input data provided to it. It takes the data as input, applies the rules of logic to arrive
at new information, and outputs the results in a structured format. Inference engines are commonly used in
artificial intelligence (AI) and expert systems to reason about complex problems and provide intelligent
decision-making capabilities.

An inference engine is a type of machine learning model that can analyze and generate predictions or outputs based on input
data. Inference engines use algorithms to process large amounts of information and extract relevant insights from it,
allowing them to make informed decisions or provide recommendations. They are often used in natural language processing (NLP)
applications such as language translation, summarization, and sentiment analysis. By enabling machine learning algorithms to
analyze text data, inference engines can improve the accuracy and speed of natural language processing tasks.

The image shows a bar graph with two bars, each representing the number of people in different age groups. The first bar is
on the left side and measures around 12 units, while the second bar is on the right side and measures around 8 units. Both
bars are colored blue, making it easy to differentiate between them. The chart displays information about the ages of
individuals, with a total of 14 people represented in the graph. 

This image is a bar chart titled "Inference Speed by Model" with the subtitle
"tokens per second (higher is faster)".

The chart compares the inference speeds of four different language models,
measured in tokens per second (tok/s). The models are listed along the
horizontal x-axis, and the speed values are shown on the vertical y-axis, which
ranges from 0 to 120.

Here is the data presented in the chart:

  - Qwen2.5 0.5B: 98 tok/s (represented by a blue bar)
  - Llama 3.2 3B: 61 tok/s (represented by an orange bar)
  - Gemma 3 4B: 44 tok/s (represented by a green bar)
  - Llama 3.1 8B: 27 tok/s (represented by a red bar)

The chart illustrates a clear trend: as the model size (the number of
parameters, indicated by "B" for billions) increases, the inference speed
decreases. Qwen2.5 0.5B is the fastest, while Llama 3.1 8B is the slowest among
the models shown.
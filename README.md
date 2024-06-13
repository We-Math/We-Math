# CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery

![Large Language Models](https://img.shields.io/badge/Task-Large%20Language%20Models-red)
![Computer Science](https://img.shields.io/badge/Field-Computer%20Science-blue)
![Dataset](https://img.shields.io/badge/Dataset-CS--Bench-green)


Code for the Paper "[CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://pris-nlp.github.io/)".

For more details, please refer to the project page with dataset exploration and key results: [https://csbench.github.io/](https://csbench.github.io/).

:bell: If you have any questions or suggestions, please don't hesitate to let us know. You can comment on the [Email](https://csbench2024@gmail.com), or post an issue on this repository.


[[Webpage](https://csbench.github.io/)] [[Paper](https://pris-nlp.github.io/)] [[Huggingface Dataset](https://huggingface.co/datasets/CS-Bench/CS-Bench)] [[Leaderboard](https://csbench.github.io/#leaderboard)] [[Result Explorer](https://csbench.github.io/#explorer)]

<p align="center">
    <img src="assets/csbench_logo_2.png" width="30%"> <br>
</p>

## Outlines

- [💥 News 💥](https://github.com/csbench/csbench/blob/main/README.md#-news-)
- [👀 About CS-Bench](https://github.com/csbench/csbench/blob/main/README.md#-about-cs-bench)
- [🏆 Leaderboard on CS-Bench (English) 🏆](https://github.com/csbench/csbench/blob/main/README.md#-leaderboard-on-cs-bench-english-)
- [🏆 Leaderboard on CS-Bench (Chinese) 🏆](https://github.com/csbench/csbench/blob/main/README.md#-leaderboard-on-cs-bench-chinese-)
- [📊 CS-Bench Dataset](https://github.com/csbench/csbench/blob/main/README.md#-cs-bench-dataset)
- [📝 Evaluation on CS-Bench](https://github.com/csbench/csbench/blob/main/README.md#-evaluation-on-cs-bench)
- [📜 License](https://github.com/csbench/csbench/blob/main/README.md#-license)
- [✅ Cite](https://github.com/csbench/csbench/blob/main/README.md#white_check_mark-cite)
- [🤝 Contributors](https://github.com/csbench/csbench/blob/main/README.md#-contributors)



## 💥 News 💥
- **[2023.6.14]** Our paper is now accessible at https://pris-nlp.github.io/.
- **[2024.6.13]** Our dataset is now accessible at [Huggingface Datasets](https://huggingface.co/datasets/CS-Bench/CS-Bench).
- **[2024.6.12]** Our project homepage can be accessed at https://csbench.github.io/.


## 👀 About CS-Bench

**Computer Science (CS)** stands as a testament to the intricacies of human intelligence, profoundly advancing the development of artificial intelligence and modern society. However, the current community of **large language models (LLMs)** overly focuses on benchmarks for analyzing specific foundational skills (e.g. mathematics and code generation), neglecting an all-round evaluation of the computer science field. To bridge this gap, **we introduce CS-Bench**, the first bilingual (Chinese-English) benchmark dedicated to evaluating the performance of LLMs in computer science. CS-Bench comprises approximately 5K meticulously curated test samples, covering 26 subfields across 4 key areas of computer science, encompassing various task forms and divisions of knowledge and reasoning. Utilizing CS-Bench, **we conduct a comprehensive evaluation of over 30 mainstream LLMs**, revealing the relationship between CS performance and model scales. We also quantitatively analyze the reasons for failures in existing LLMs and highlight directions for improvements, including knowledge supplementation and CS-specific reasoning. Further **cross-capability experiments** show a high correlation between LLMs' capabilities in computer science and their abilities in mathematics and coding. Moreover, expert LLMs specialized in mathematics and coding also demonstrate strong performances in several CS subfields. Looking ahead, we envision CS-Bench serving as a cornerstone for LLM applications in the CS field and paving new avenues in assessing LLMs' diverse reasoning capabilities.


<p align="center">
    <img src="assets/CS_Bench-main.png" width="90%"> <br>
  Overview diagram and statistics of <b>CS-Bench</b>.
</p>

For more details, you can find our project page [here](https://csbench.github.io/) and our paper [here](https://pris-nlp.github.io/).

## 🏆 Leaderboard on CS-Bench (English) 🏆

### Contributing the Leaderboard

The evaluation instructions are available at [📝 Evaluation on CS-Bench](https://github.com/csbench/csbench/blob/main/README.md#-evaluation-on-cs-bench).

To submit your results to the leaderboard, please send to  [this email](csbench2024@gmail.com) with your result json files.

### Overall

<p align="center">
    <img src="assets/web_leaderboard_en.png" width="90%"> <br>
  The leaderboard of LLMs on <b>CS-Bench (EN) </b>.
</p>

### Detailed scores


| Model               | DSA |               |               | CO |               |               | CN |               |               | OS |               |               | Overall          |               |               |
|---------------------|-------------------|---------------|---------------|-----------------------|---------------|---------------|------------------|---------------|---------------|------------------|---------------|---------------|------------------|---------------|---------------|
|                     | Klg               | Rng           | Avg           | Klg                   | Rng           | Avg           | Klg              | Rng           | Avg           | Klg              | Rng           | Avg           | Klg              | Rng           | Avg           |
| Random              | 28.04             | 24.63         | 26.65         | 26.57                 | 25.24         | 26.13         | 26.34            | 22.49         | 24.98         | 29.06            | 24.23         | 27.27         | 27.4             | 24.12         | 26.2           |
| *Open-source LLM (Scale < 10B)* |                   |               |               |                       |               |               |                  |               |               |                  |               |               |                  |               |               |
| Gemma-2B            | 56.76             | 23.44         | 43.20         | 47.69                 | 30.18         | 41.92         | 45.22            | 26.38         | 38.59         | 37.79            | 31.32         | 35.39         | 46.89            | 27.59         | 39.86          |
| Qwen1.5-4B          | 58.76             | 36.56         | 49.72         | 52.31                 | 33.88         | 46.23         | 52.70            | 33.97         | 46.11         | 40.03            | 38.52         | 39.47         | 51.18            | 35.70         | 45.54          |
| ChatGLM3-6B         | 51.10             | 34.08         | 44.17         | 48.11                 | 32.73         | 43.04         | 51.15            | 32.66         | 44.64         | 43.57            | 37.03         | 41.14         | 48.63            | 34.07         | 43.33          |
| Llama2-7B           | 51.51             | 32.61         | 43.82         | 48.89                 | 31.82         | 43.26         | 46.72            | 30.75         | 41.10         | 41.04            | 26.26         | 35.55         | 47.15            | 30.48         | 41.08          |
| DeepseekLLM-7B      | 56.42             | 28.94         | 45.23         | 52.09                 | 32.48         | 45.62         | 52.43            | 31.41         | 45.03         | 41.66            | 31.98         | 38.06         | 50.87            | 31.11         | 43.67          |
| Baichuan2-7B        | 53.11             | 34.95         | 45.72         | 45.10                 | 38.67         | 42.98         | 51.26            | 34.27         | 45.28         | 43.47            | 33.63         | 39.82         | 48.29            | 35.33         | 43.57          |
| Gemma-7B            | 59.53             | 35.18         | 49.62         | 49.97                 | 33.27         | 44.46         | 60.87            | 37.09         | 52.50         | 48.67            | 34.23         | 43.31         | 54.90            | 35.02         | 47.66          |
| Qwen1.5-7B          | 59.90             | 35.28         | 49.88         | 55.21                 | 42.73         | 51.09         | 61.56            | 43.02         | 55.04         | 52.01            | 39.78         | 47.47         | 57.34            | 40.08         | 51.05          |
| InternLm2-7B        | 59.57             | 40.92         | 51.98         | 58.83                 | 37.94         | 51.94         | 62.65            | 40.60         | 54.89         | 50.94            | 39.29         | 46.61         | 58.31            | 39.77         | 51.56          |
| Mistral-7B          | 63.24             | 34.86         | 51.69         | 57.52                 | 38.67         | 51.30         | 61.48            | 44.92         | 55.65         | 51.66            | 43.79         | 48.73         | 58.63            | 40.44         | 52.01          |
| Llama3-8B           | 66.25             | 37.29         | 54.46         | 55.38                 | 40.67         | 50.53         | 62.21            | 53.02         | 58.98         | 55.26            | 49.34         | 53.06         | 59.75            | 44.97         | 54.37          |
| *Open-source LLM (Scale > 10B)* |                   |               |               |                       |               |               |                  |               |               |                  |               |               |                  |               |               |
| Llama2-13B          | 51.74             | 35.00         | 44.93         | 51.81                 | 36.18         | 46.66         | 53.03            | 37.99         | 47.74         | 48.12            | 32.36         | 42.27         | 51.31            | 35.46         | 45.54          |
| Baichuan-13B        | 54.82             | 33.39         | 46.10         | 50.50                 | 39.52         | 46.88         | 55.87            | 42.21         | 51.06         | 48.44            | 34.73         | 43.35         | 52.53            | 37.44         | 47.03          |
| Qwen1.5-14B         | 64.95             | 46.74         | 57.54         | 60.06                 | 45.58         | 55.28         | 68.66            | 52.91         | 63.12         | 56.56            | 51.48         | 54.67         | 62.79            | 49.18         | 57.83          |
| InternLm2-20B       | 66.72             | 38.21         | 55.11         | 58.38                 | 39.82         | 52.26         | 64.13            | 50.35         | 59.28         | 53.51            | 46.43         | 50.88         | 60.81            | 43.66         | 54.56          |
| Qwen1.5-32B         | 69.70             | 51.19         | 62.17         | 67.63                 | 52.91         | 62.78         | 69.23            | 58.74         | 65.54         | 60.06            | 56.21         | 58.63         | 66.87            | 54.72         | 62.45          |
| Mistral-8×7B        | 70.94             | 40.50         | 58.55         | 66.88                 | 42.06         | 58.70         | 67.49            | 52.86         | 62.34         | 57.56            | 51.65         | 55.37         | 65.91            | 46.66         | 58.90          |
| DeepseekLLM-67B     | 69.70             | 44.17         | 59.31         | 63.59                 | 39.15         | 55.53         | 69.04            | 50.25         | 62.43         | 57.86            | 50.11         | 54.98         | 65.23            | 45.96         | 58.22          |
| Llama2-70B          | 64.28             | 41.51         | 55.01         | 56.35                 | 40.85         | 51.24         | 61.99            | 43.07         | 55.33         | 51.79            | 41.15         | 47.84         | 58.73            | 41.68         | 52.52          |
| Llama3-70B          | 75.72             | 53.03         | 66.48         | 71.45                 | 51.09         | 64.74         | 74.78            | 63.02         | 70.64         | 63.77            | 58.08         | 61.65         | 71.65            | 56.36         | 66.08          |
| Qwen1.5-72B         | 72.71             | 50.69         | 63.75         | 69.28                 | 54.12         | 64.28         | 71.97            | 66.73         | 70.13         | 63.96            | 59.62         | 62.35         | 69.63            | 57.75         | 65.31          |
| Qwen1.5-110B        | 73.11             | 53.58         | 65.16         | 73.65                 | 54.18         | 67.23         | 75.36            | 70.75         | 73.74         | 64.55            | 65.27         | 64.82         | 71.98            | 60.91         | 67.95          |
| *Closed-source LLM* |                   |               |               |                       |               |               |                  |               |               |                  |               |               |                  |               |               |
| PaLM-2              | 70.07             | 38.98         | 57.41         | 63.81                 | 41.91         | 56.59         | 65.11            | 49.43         | 59.59         | 60.41            | 45.96         | 55.22         | 64.85            | 44.01         | 57.26          |
| Claude-2.1          | 68.39             | 44.54         | 58.68         | 62.09                 | 50.24         | 58.18         | 66.58            | 52.81         | 61.74         | 53.93            | 50.55         | 52.67         | 62.97            | 49.42         | 58.04          |
| Claude-3            | 77.53             | 52.25         | 67.24         | 72.53                 | 64.12         | 69.76         | 75.08            | 68.69         | 72.83         | 64.36            | 62.80         | 63.78         | 72.57            | 61.75         | 68.63          |
| GPT-3.5             | 71.34             | 39.22         | 58.27         | 60.78                 | 42.97         | 54.91         | 65.27            | 52.16         | 60.66         | 54.42            | 39.01         | 48.69         | 63.04            | 43.45         | 55.91          |
| GPT-4               | 78.53             | 59.36         | 70.73         | 75.40                 | 59.21         | 70.06         | 77.38            | 67.64         | 73.95         | 67.21            | 64.40         | 66.16         | 74.85            | 62.66         | 70.41          |
| GPT-4o              | 81.51             | 57.80         | 71.86         | 75.60                 | 58.61         | 70.00         | 80.57            | 71.76         | 77.47         | 69.35            | 68.68         | 69.10         | 76.95            | 64.15         | 72.29          |


Some notations in the table:

- **Domains**
  -  **DSA:** **D**ata **S**tructure and **A**lgorithm
  -  **CO** **C**omputer **O**rganization
  -  **CN:** **C**omputer **N**etwork
  -  **OS:** **O**perating **S**ystem
  
- **Types:** 
  - **Klg:** **k**now**l**ed**g**e-type
  - **Rng:** **r**easo**n**in**g**-type
  - **Avg:** **Av**era**g**e

## 🏆 Leaderboard on CS-Bench (Chinese) 🏆

### Overall

<p align="center">
    <img src="assets/web_leaderboard_cn.png" width="90%"> <br>
  The leaderboard of LLMs on <b>CS-Bench (CN) </b>.
</p>


### Detailed scores

| Model | DSA |  |  | CO |  |  | CN |  |  | OS |  |  | Overall |  |  |
|-------|-------------------|--|--|-----------------------|--|--|-----------------|--|--|------------------|--|--|---------|--|--|
|       | Klg               | Rng | Avg | Klg              | Rng | Avg | Klg        | Rng | Avg | Klg           | Rng | Avg | Klg     | Rng | Avg |
| **Open-source LLM (Scale < 10B)** | | | | | | | | | | | | | | | |
| Random | 28.04 | 24.63 | 26.65 | 26.57 | 25.24 | 26.13 | 26.34 | 22.49 | 24.98 | 29.06 | 24.23 | 27.27 | 27.4 | 24.12 | 26.20 |
| ChatGLM3-6B | 41.74 | 32.48 | 37.97 | 44.07 | 34.91 | 41.05 | 49.02 | 32.31 | 43.14 | 43.02 | 32.86 | 35.98 | 44.67 | 33.09 | 40.45 |
| Baichuan2-7B | 42.04 | 31.51 | 37.75 | 44.93 | 37.88 | 42.61 | 50.74 | 31.11 | 43.83 | 42.18 | 34.07 | 39.16 | 45.27 | 33.47 | 40.97 |
| InternLm2-7B | 41.97 | 34.54 | 38.95 | 55.77 | 38.67 | 50.13 | 60.05 | 41.86 | 53.65 | 50.94 | 44.07 | 48.39 | 52.71 | 39.61 | 47.94 |
| Qwen1.5-7B | 49.13 | 37.71 | 44.48 | 60.86 | 44.48 | 55.46 | 60.90 | 45.68 | 55.54 | 58.38 | 48.24 | 54.61 | 57.62 | 43.79 | 52.59 |
| Llama3-8B | 50.47 | 29.68 | 42.01 | 50.81 | 36.30 | 46.03 | 56.09 | 42.21 | 51.21 | 52.01 | 38.85 | 47.12 | 52.46 | 36.61 | 46.69 |
| Llama3-8B-Chinese | 49.20 | 33.72 | 42.90 | 54.99 | 33.09 | 47.77 | 58.77 | 48.59 | 55.19 | 55.58 | 41.10 | 50.20 | 54.84 | 39.17 | 49.13 |
| **Open-source LLM (Scale > 10B)** | | | | | | | | | | | | | | | |
| Baichuan2-13B | 48.83 | 34.68 | 43.07 | 54.18 | 36.00 | 48.18 | 55.11 | 39.85 | 49.74 | 49.19 | 40.27 | 45.88 | 52.10 | 37.63 | 46.83 |
| Qwen1.5-14B | 51.47 | 48.81 | 50.39 | 64.43 | 46.85 | 58.63 | 68.69 | 55.18 | 63.94 | 69.58 | 56.59 | 64.76 | 63.78 | 51.81 | 59.42 |
| InternLm2-20B | 51.97 | 38.03 | 46.30 | 58.36 | 45.76 | 54.20 | 60.60 | 50.50 | 57.05 | 58.70 | 45.66 | 53.86 | 57.59 | 44.85 | 52.95 |
| Qwen1.5-32B | 55.89 | 56.70 | 56.22 | 67.74 | 60.00 | 65.19 | 70.33 | 66.83 | 69.10 | 72.40 | 62.03 | 68.55 | 66.77 | 61.35 | 64.80 |
| Llama3-70B | 53.28 | 55.41 | 54.15 | 67.97 | 49.58 | 61.91 | 71.07 | 61.81 | 67.81 | 65.29 | 57.36 | 62.35 | 64.86 | 56.18 | 61.70 |
| Qwen1.5-72B | 58.16 | 52.02 | 55.66 | 70.28 | 52.91 | 64.55 | 75.25 | 66.23 | 72.08 | 74.12 | 63.19 | 70.06 | 69.73 | 58.52 | 65.64 |
| **Closed-source LLM** | | | | | | | | | | | | | | | |
| GPT-3 | 54.15 | 39.63 | 48.24 | 60.86 | 43.27 | 55.06 | 64.29 | 48.89 | 58.87 | 56.36 | 39.84 | 50.22 | 59.27 | 42.96 | 53.33 |
| GPT-4 | 60.03 | 60.28 | 60.13 | 77.60 | 60.24 | 71.88 | 73.50 | 72.86 | 73.27 | 71.46 | 65.60 | 69.29 | 71.06 | 64.80 | 68.78 |
| GPT-4o | 61.67 | 66.45 | 63.62 | 78.86 | 55.32 | 71.10 | 78.61 | 74.17 | 77.05 | 72.66 | 69.94 | 71.67 | 73.46 | 66.69 | 71.00 |
| GLM-4 | 58.12 | 58.37 | 58.22 | 74.03 | 59.49 | 69.24 | 71.65 | 70.21 | 71.14 | 73.31 | 67.14 | 71.06 | 69.55 | 63.75 | 67.44 |
| ERNIE-3.5 | 58.16 | 55.62 | 57.13 | 74.56 | 58.73 | 69.34 | 74.68 | 65.16 | 71.33 | 72.13 | 63.37 | 68.94 | 70.28 | 60.63 | 66.77 |
| ERNIE-4 | 57.92 | 62.33 | 59.72 | 78.24 | 64.18 | 73.60 | 76.27 | 69.74 | 73.97 | 75.84 | 69.54 | 73.54 | 72.49 | 66.36 | 70.26 |


## 📊 CS-Bench Dataset

### Statistics

<p align="center">
    <img src="assets/appendix_pie.png" width="90%"> <br>
</p>

<details>
<summary>The length distribution of questions and answers on CS-Bench (EN).</summary>
<p align="center">
    <img src="assets/appendix_length_distribution_en_detail.png" width="90%"> <br>
</p>
</details>

<details>
<summary>The length distribution of questions and answers on CS-Bench (CN).</summary>
<p align="center">
    <img src="assets/appendix_length_distribution_cn_detail.png" width="90%"> <br>
</p>
</details>

<details>
<summary>Summary of 26 fine-grained subfields on CS-Bench.</summary>
<p align="center">
    <img src="assets/table_5.png" width="90%"> <br>
</p>
</details>


### Exmaples
<details>
<summary>🔍Examples of samples in different domains.</summary>
<p align="center">
    <img src="assets/table_6.png" width="90%"> <br>
</p>
</details>


<details>
<summary>🔍Examples of different task formats.</summary>
<p align="center">
    <img src="assets/table_7.png" width="90%"> <br>
</p>
</details>


<details>
<summary>🔍Examples of knowledge-type and reasoning-type.</summary>
<p align="center">
    <img src="assets/table_8.png" width="90%"> <br>
</p>
</details>


<details>
<summary>🔍Examples of different languages.</summary>
<p align="center">
    <img src="assets/table_9.png" width="90%"> <br>
</p>
</details>


## 📝 Evaluation on CS-Bench

### Option
Option 1: Use Step 1 to construct the reasoning prompt, replace Step 2.1 with your own reasoning method to obtain the model's output, and use Steps 3 and 4 to get the model's scores.

Option 2: Use Step 1 to construct the reasoning prompt, use the vllm reasoning we provide in Step 2.1 (requires environment setup) to obtain the model's output, and use Steps 3 and 4 to get the model's scores.

### Install Dependencies
```
git clone https://github.com/csbench/csbench
```

### Evaluate a new model on CS-Bench:

#### Step 1. Create your input prompt

Fill in your file path in `create_input.py` and create English(default) or Chinese prompt by running the functions create_en_prompt and create_cn_prompt.


#### Step 2. Generate Model Answers

You may use inference engine such as [vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html) or [SGLang](https://github.com/sgl-project/sglang?tab=readme-ov-file#using-local-models) to generate your model answers. We will provide our inference code in the near future.

Please ensure that your answer is saved in JSONL format and retains all keys from the original dataset.

#### Step 2.1 Generate Model Answers with vLLM(optional)

vLLM is a fast and easy-to-use library for LLM inference and serving.

##### Getting Started(vLLM)

Visit our [documentation](https://vllm.readthedocs.io/en/latest/) to get started.
- [Installation](https://vllm.readthedocs.io/en/latest/getting_started/installation.html)
- [Quickstart](https://vllm.readthedocs.io/en/latest/getting_started/quickstart.html)
- [Supported Models](https://vllm.readthedocs.io/en/latest/models/supported_models.html)

##### You can install vLLM using pip:
```
# (Recommended) Create a new conda environment.
conda create -n myenv python=3.9 -y
conda activate myenv
# Install vLLM with CUDA 12.1.
pip install vllm
```
##### Generate Model Answers:
Fill in your model path, data save path and other parameters in `run_csbench.sh` and run this script.
```
bash run_csbensh.sh
```


#### Step 3. Generate Judgments

If you want to evaluate questions in all formats.Fill in your API in `test_call_llm.py`
Run the command to generate judgments with GPT:
```
python gen_judgment.py --judge_with_gpt 1 your_file_path
```

If you only want to evaluate questions in 'Multiple-choice' and 'Assertion'.
Run the command to generate judgments without GPT:
```
python gen_judgment.py --judge_with_gpt 0 your_file_path
```

#### Step 4. Show result
Output model win scores. Run the command to generate judgments without GPT:
```
python show_result.py your_file_path
```

## 📜 License

Our dataset are distributed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.


## :white_check_mark: Cite

If you find **CS-Bench** useful for your your research and applications, please kindly cite using this BibTeX:

```latex
TODO
```


## 🤝 Contributors

Here are the key contributors to this project:

Xiaoshuai Song, Muxi Diao, Guanting Dong, Zhengyang Wang, Yujia Fu, Runqi Qiao, Zhexu Wang, Dayuan Fu, Huangxuan Wu, Bin Liang, Weihao Zeng, Yejie Wang, Zhuoma GongQue, Jianing Yu, Qiuna Tan, Weiran Xu

[PRIS-NLP Research Group](https://pris-nlp.github.io/) , Beijing University of Posts and Telecommunications

# [We-Math: Does Your Large Multimodal Model Achieve Human-like Mathematical Reasoning?](https://arxiv.org/pdf/2407.01284)

![Dataset](https://img.shields.io/badge/Dataset-We--Math-green)
![Multi-Modal](https://img.shields.io/badge/Task-Multi--Modal-red)
![Mathematical Reasoning](https://img.shields.io/badge/Task-Mathematical_Reasoning-red) 

<p align="center">
    <img src="./assets/logo-another.png" width="35%"> <br>
</p>

## Outlines
- [💥 News 💥](https://github.com/We-Math/We-Math/blob/main/README.md#-news-)
- [👀 About We-Math](https://github.com/We-Math/We-Math/blob/main/README.md#-about-we-math)
- [🏆 Leaderboard on We-Math 🏆](https://github.com/We-Math/We-Math/blob/main/README.md#-leaderboard-on-we-math-)
- [📝 Evaluation Piplines on We-Math](https://github.com/We-Math/We-Math/blob/main/README.md#-evaluation-piplines-on-we-math)
- [📊 We-Math Dataset](https://github.com/We-Math/We-Math/blob/main/README.md#-we-math-dataset)
- [📜 License](https://github.com/We-Math/We-Math/blob/main/README.md#-license)
- [🤝 Contributors](https://github.com/We-Math/We-Math/blob/main/README.md#-contributors)

## 💥 News 💥
  **[2025.5.16]** 🎉 We-Math is accepted by ACL 2025 🎉
  **[2024.7.2]** Our paper is now accessible at https://arxiv.org/abs/2407.01284.
  
  **[2024.7.2]** Our dataset is now accessible at [Huggingface Datasets](https://huggingface.co/datasets/We-Math/We-Math/).
  
  **[2024.7.2]** Our project homepage can be accessed at https://we-math.github.io/.

## 👀 About We-Math
Inspired by human-like mathematical reasoning, we introduce We-Math, the first benchmark specifically designed to <b>explore the problem-solving principles beyond the end-to-end performance.</b> We meticulously collect and categorize 6.5K visual math problems, spanning 67 hierarchical knowledge concepts and 5 layers of knowledge granularity.

<p align="center">
    <img src="assets/fig_lun.png" alt="Overview diagram and the statistics of WE-MATH" style="width: 85%;" /> <br>
    Overview diagram and the statistics of <b>We-Math</b>.
</p>

We firstly <b>decompose composite problems into sub-problems</b> according to the required knowledge concepts and introduce a novel four-dimensional metric, namely <b>Insufficient Knowledge (IK)</b>, <b>Inadequate Generalization (IG)</b>, <b>Complete Mastery (CM)</b>, and <b>Rote Memorization (RM)</b> to hierarchically assess inherent issues in LMMs’ reasoning process.

<p align="center">
    <img src="assets/3-example.png" alt="The pipeline of knowledge-based data decomposition (an example of a three-step problem in We-Math)." style="width: 65%;" /> <br>
    The pipeline of knowledge-based data decomposition (an example of a three-step problem in We-Math).
</p>

<p align="center">
    <img src="assets/metric_2.png" alt="The pipeline of knowledge-based data decomposition (left) and an example of the four-dimensional metrics for evaluating a two-step problem (right), using both loose and strict settings." style="width: 95%;" /> <br>
    An example of the four-dimensional metrics for evaluating a two-step problem, using both loose and strict settings.
</p>


With We-Math, we conduct a thorough evaluation of existing LMMs in visual mathematical reasoning and reveal a negative correlation between solving step and problem-specific performance. We confirm the IK issue of LMMs can be effectively improved via knowledge augmentation strategy. More notably, <b>the primary challenge of GPT-4o has significantly transitioned from IK to IG, establishing it as the first LMM advancing towards the knowledge generalization stage.</b> In contrast, other LMMs exhibit a marked inclination towards Rote Memorization they correctly solve composite problems involving multiple knowledge concepts, yet fail in answering sub-problems. We anticipate that We-Math will open new pathways for advancements in visual mathematical reasoning for LMMs.

<p align="center">
    <img src="assets/fig1_result.png" alt="pipeline of decomposition" style="width: 95%;" /> <br>
    Overview of LMMs' performances on We-Math. Figures from left to right illustrates the (1) accuracy of different LMMs on various problem-solving steps, (2) the performance in different visual mathematics categories and (3) the result in knowledge based reasoning evaluation.
</p>




## 🏆 Leaderboard on We-Math 🏆
🚨🚨 The [Leaderboard](https://we-math.github.io/#leaderboard) is continuously being updated. We welcome the results of your model!
To submit your results to the leaderboard on the **testmini** subset, please send to [this email](mailto:qrq@bupt.edu.cn) with your result JSON file and score CSV file.

## 📝 Evaluation Piplines on We-Math

### Response Generation 
The models generate responses based on the given questions and images. Examples for generating responses from some LMMs are provided in the [evaluation](./evaluation). Our prompt specifies the format of answer generation to facilitate subsequent extraction of the answer using string matching. Please refer to the following template to prepare your result JSON files for subsequent evaluation.
```json
{
    "ID": "3steps_165",
    "split": "testmini",
    "knowledge concept": "Area of Circles",
    "question": "As shown in the figure, there is a circular flower bed. Mary walked from the northernmost point of the flower bed along the edge to the easternmost point, taking a total of 80 steps. It is known that Mary's average step length is 0.628 cm, what is the area of the flower bed (  ) m²?(π = 3.14)",
    "option": "A. 200.96;B. 3215.36;C. 6280;D. 32; E. No correct answer",
    "answer": "B",
    "image_path": "3steps/image/165-3.png",
    "key": "3steps_3",
    "question number": 1575,
    "knowledge concept description": "Area of ...",
    "response": "<Thought process>: ... <Answer>: ..."
}
```
### Score Calculation
Due to the multiple-choice question format of our dataset and the specific answer generation prompt, we use string matching to directly extract answers, which eliminates the high cost of using additional models for further answer extraction.  The extracted answer is normalized to an option letter and calculate scores on our proposed four-dimensional metrics in [four_dimensional_metrics.py](https://github.com/We-Math/We-Math/blob/main/evaluation/four_dimensional_metrics.py).
```sh
cd evaluation

python four_dimensional_metrics_refine.py \
--model_name GPT-4o \
--output_json ../output/GPT-4o.json  \
--main_results_csv_path ../result/four_dimensional_metrics.csv
```

Performences on One-Step / Two-Step / Three-Step problems and different problem domains are obtained from [accuracy.py](https://github.com/We-Math/We-Math/blob/main/evaluation/accuracy.py).

```sh
cd evaluation

python accuracy.py \
--model_name GPT-4o \
--output_json ../output/GPT-4o.json  \
--knowledge_structure_nodes_path /data/knowledge_structure_nodes.json \
```


## 📊 We-Math Dataset

### Metric for Reasoning Evaluation
Based on the decomposed multi-step problems, we further reveal the inherent issues of LMMs in problem-solving process. We feed both the M one-step sub-problems and the original problem into LMMs, and classifying the responses into four categories
1. Insufficient Knowledge (IK): Part of one-step problems contain errors, and the multi-step problem is wrong. It is reasonable because model's insufficient grasp of single knowledge concept may lead to errors in multi-step problem.
2. Inadequate Generalization (IG): One-Step problems are all correct, but the multi-step problem is incorrect. This is also considered reasonable. While LMMs are capable of understanding individual knowledge concepts, they may struggle to generalize that knowledge to solve composite problems.
3. Complete Mastery (CM): One-Step problems are all correct, and multi-step problem is also answered correctly. This result demonstrates that the model's results are both reliable and accurate.
4. Rote Memorization (RM): One-Step problems contain errors, but the multi-step problem is answered correctly, which contradicts human logical thinking. If a model can solve composite multi-step problems but fails to answer the one-step problems needed in the process, it raises doubts about the model's reliability.

### Exmaples
<details>
<summary>🔍Examples of samples.</summary>
<p align="center">
    <img src="assets/example-2.png" width="90%"> <br>
</p>
</details>

### Knowledge cards
<details>
<summary>🔍Examples of Knowledge cards.</summary>
<p align="center">
    <img src="assets/example-card.png" width="90%"> <br>
</p>
</details>


## 📜 License

Our dataset are distributed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.


## :white_check_mark: Cite

If you find **We-Math** useful for your your research and applications, please kindly cite using this BibTeX:

```bibtex
@article{qiao2024we,
  author       = {Runqi Qiao and
                  Qiuna Tan and
                  Guanting Dong and
                  Minhui Wu and
                  Chong Sun and
                  Xiaoshuai Song and
                  Zhuoma Gongque and
                  Shanglin Lei and
                  Zhe Wei and
                  Miaoxuan Zhang and
                  Runfeng Qiao and
                  Yifan Zhang and
                  Xiao Zong and
                  Yida Xu and
                  Muxi Diao and
                  Zhimin Bao and
                  Chen Li and
                  Honggang Zhang},
  title        = {We-Math: Does Your Large Multimodal Model Achieve Human-like Mathematical
                  Reasoning?},
  journal      = {CoRR},
  volume       = {abs/2407.01284},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2407.01284},
  doi          = {10.48550/ARXIV.2407.01284},
  eprinttype    = {arXiv},
  eprint       = {2407.01284},
  timestamp    = {Tue, 13 Aug 2024 12:02:59 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2407-01284.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```


## 🤝 Contributors
Here are the key contributors to this project:

Runqi Qiao, Qiuna Tan, Guanting Dong, Minhui Wu, Chong Sun, Xiaoshuai Song, Zhuoma GongQue, Shanglin Lei, Zhe Wei, Miaoxuan Zhang, Runfeng Qiao, Yifan Zhang, Xiao Zong, Yida Xu, Muxi Diao, Zhimin Bao, Chen Li, Honggang Zhang.

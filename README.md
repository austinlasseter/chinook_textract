# Machine Learning Engineer Nanodegree
## Capstone Proposal
Austin Lasseter  
October 27, 2020

## Proposal

### Domain Background

The US Army must submit the President's Budget to Congress on the first Monday in February each year. The program in the Budget must be both "authorized" and "appropriated" before any dollars can be obligated. The Budget is accompanied by Justification Books, known as "J-Books", which are the documents an agency submits to the appropriations committees in support of its budget request. The Office of Management and Budget (OMB) prescribes justification materials, which typically explain changes between the current appropriation and the amounts requested for the next fiscal year.

While the J-Books are informative and publicly available, they are not designed for easy analysis. Text and numeric data are presented in PDF format, making it difficult to summarize by topic, or drill down into particular data trends. Following a tradition going back decades, the J-Books were designed to be printed and distributed in book format. While technology has evolved, the presentation of the J-Books has not. They are available in PDF format through the website of the US Army Office of Financial Management and Comptroller: https://www.asafm.army.mil/Budget-Materials/

### Problem Statement

When data is locked up in PDFs and associated with text, this is a classic problem for Natural Language Processing (NLP) combined with text extraction methods. The project will extract numeric and text data from the J-books, organize them into a dataset, and then carry out topic modeling followed by some exploratory analysis and time-series analysis. The project will answer the following questions:

* What are the primary topic clusters in the US Army budget, as a whole and by funding strata?
* How have topic clusters changed over time?
* Choose a few key words (like "artificial intelligence", "cloud computing", or "anti-terrorism") and track how their funding levels have changed over time.

### Datasets and Inputs
_(approx. 2-3 paragraphs)_

In this section, the dataset(s) and/or input(s) being considered for the project should be thoroughly described, such as how they relate to the problem and why they should be used. Information such as how the dataset or input is (was) obtained, and the characteristics of the dataset or input, should be included with relevant references and citations as necessary It should be clear how the dataset(s) or input(s) will be used in the project and whether their use is appropriate given the context of the problem.

| Description | TOA Prior Years | FY 2019 | FY 2020 | FY 2021 | FY 2022 | FY 2023 | FY 2024 | FY 2025 |
| - | - | - | - | - | - | - | - | - |
| Text | $$ | $$ | $$ | $$ | $$ | $$ | $$ | $$ | $$ |
| Text | $$ | $$ | $$ | $$ | $$ | $$ | $$ | $$ | $$ |
| Text | $$ | $$ | $$ | $$ | $$ | $$ | $$ | $$ | $$ |


### Solution Statement
_(approx. 1 paragraph)_

In this section, clearly describe a solution to the problem. The solution should be applicable to the project domain and appropriate for the dataset(s) or input(s) given. Additionally, describe the solution thoroughly such that it is clear that the solution is quantifiable (the solution can be expressed in mathematical or logical terms) , measurable (the solution can be measured by some metric and clearly observed), and replicable (the solution can be reproduced and occurs more than once).

### Benchmark Model
_(approximately 1-2 paragraphs)_

In this section, provide the details for a benchmark model or result that relates to the domain, problem statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods or known information in the domain and problem given, which could then be objectively compared to the solution. Describe how the benchmark model or result is measurable (can be measured by some metric and clearly observed) with thorough detail.

### Evaluation Metrics
_(approx. 1-2 paragraphs)_

In this section, propose at least one evaluation metric that can be used to quantify the performance of both the benchmark model and the solution model. The evaluation metric(s) you propose should be appropriate given the context of the data, the problem statement, and the intended solution. Describe how the evaluation metric(s) are derived and provide an example of their mathematical representations (if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed in mathematical or logical terms).

### Project Design
_(approx. 1 page)_

In this final section, summarize a theoretical workflow for approaching a solution given the problem. Provide thorough discussion for what strategies you may consider employing, what analysis of the data might be required before being used, or which algorithms will be considered for your implementation. The workflow and discussion that you provide should align with the qualities of the previous sections. Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in describing the project design, but it is not required. The discussion should clearly outline your intended workflow of the capstone project.

![](chinookflow.png)


-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?

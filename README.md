From Correlation to Causation: Identifying True Drivers of Customer Churn

## Abstract

Most customer churn studies rely on predictive models and feature importance scores, which capture correlations but do not establish causal relationships. This project applies causal inference methods to identify factors that causally influence customer churn. By explicitly modeling causal assumptions using a Directed Acyclic Graph (DAG) and estimating treatment effects, the project demonstrates how causal analysis leads to more reliable and interpretable conclusions than standard machine learning approaches.


---

## Research Objective

The primary objective of this project is to distinguish true causal drivers of customer churn from spurious correlations and to estimate the effect of potential interventions.

Specifically, the project addresses the question:

> Does changing customer contract characteristics causally reduce the probability of churn?




---

## Dataset

-Name: Telco Customer Churn (IBM)

-Source: Kaggle

-Observations: ~7,000 customers

-Outcome Variable: Churn

-Key Covariates:

Contract type

Tenure

Monthly charges

Internet service

Payment method




---

## Methodology

1. Data Preprocessing

Removal of missing and inconsistent values

Encoding of categorical variables

Prevention of data leakage

Standardization of numerical features



---

2. Exploratory Analysis

Exploratory Data Analysis (EDA) was conducted to understand feature distributions and correlations. This step is used only for descriptive analysis and not for causal interpretation.


---

3. Correlation-Based Analysis

Correlation matrices and feature–outcome relationships were analyzed to highlight potential misleading associations that arise when causality is not explicitly modeled.


---

4. Causal Problem Formulation

Treatment: Contract type

Outcome: Customer churn

Confounders: Tenure, monthly charges, internet service


The causal question is formulated under the potential outcomes framework, explicitly stating assumptions about confounding and causal pathways.


---

5. Causal Graph Construction

A Directed Acyclic Graph (DAG) is constructed to encode domain assumptions and to identify valid backdoor adjustment sets. This step ensures transparency and interpretability of the causal model.


---

6. Causal Effect Estimation

Causal effects are estimated using the DoWhy framework:

Identification of causal estimands

Estimation of Average Treatment Effect (ATE)

Comparison with correlation-based findings



---

7. Robustness and Refutation

The stability of causal estimates is evaluated using:

Placebo treatment refutation

Random common cause tests


These tests strengthen confidence in the estimated causal effects.


---

## Key Findings

Long-term contracts exhibit a significant causal effect in reducing churn

Monthly charges, while correlated with churn, show limited causal influence

Customer tenure acts as a major confounding variable

Causal estimates differ meaningfully from correlation-based conclusions



---

## Reproducibility and Artifacts

The causal DAG is exported as a DOT file and converted to PNG for portability

All analyses are reproducible using the provided notebooks


---

## Limitations

The analysis assumes no unobserved confounders

Results depend on the correctness of the causal graph

Findings are based on observational data rather than randomized experiments



---

## Future Work

Estimation of heterogeneous treatment effects using EconML

Extension to instrumental variable approaches

Validation through randomized A/B experiments



---

## Relevance to Research Internships

This project demonstrates:

Ability to reason beyond predictive accuracy

Understanding of causal inference principles

Research-oriented problem formulation and evaluation

Strong alignment with machine learning and data science research labs



---

## Conclusion

By moving from correlation to causation, this project illustrates how causal reasoning provides
deeper insight into real-world decision-making problems and supports more reliable interventions
than standard predictive models.
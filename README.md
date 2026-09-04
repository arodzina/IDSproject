# 🥦 Food Product Market Acceptance Prediction — Data Science Project (CRISP-DM)

**IDSproject (Food Product Acceptance Analysis)** is an end-to-end **Data Science & Machine Learning** project implemented in **Python**. The goal of the project is to predict the market launch success (*success* and *overall_appreciation*) of new food products based on 42 attributes spanning sensory evaluation, nutritional values, marketing metrics, and brand perceptions.

The entire analytical workflow adheres strictly to the industry-standard **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology.

---

## 🌟 Project Phases (CRISP-DM Framework)

### 1. 🎯 Business Understanding
* Formulated the business problem: optimizing new food product commercialization and mitigating financial risks of failed product launches.
* Defined quantitative evaluation criteria and evaluation setups for both **balanced** and **imbalanced** versions of the target dataset.

### 2. 📊 Data Understanding (Exploratory Data Analysis — EDA)
* **Analyzed 2,000 products across 42 variables**:
  * *Nutritional Metrics*: calories, fat, sugar, protein, fiber, sodium.
  * *Sensory Attributes*: aroma/color intensity, sweetness, sourness, spiciness, umami, crispness, softness, aftertaste length.
  * *Market & Brand Indicators*: price, brand trust, packaging appeal, eco score, prelaunch review count, marketing spend ($k), shelf life, allergen warning count.
* **Data Diagnostics**: Performed univariate/bivariate profiling, identified missing data patterns, detected outliers, and analyzed feature correlation matrices.

### 3. 🧹 Data Preparation
* **Missing Value Imputation**: Imputed missing entries in key features (*protein_g*, *fiber_g*, *umami*, *aroma_intensity*).
* **Feature Encoding & Scaling**: Encoded categorical/boolean variables and standardized numerical features.
* **Class Imbalance Handling**: Conducted separate experimental pipelines for **balanced** vs. **imbalanced** target distributions.

### 4. 🤖 Modeling
Trained, cross-validated, and fine-tuned hyperparameters across 6 distinct Machine Learning model families:
1. **k-Nearest Neighbors (k-NN)** — Distance metric tuning and neighbor count optimization.
2. **Bayesian Classifier (Naive Bayes / Gaussian Bayes)**.
3. **Decision Trees** — Tree depth and splitting criteria analysis.
4. **Tree Ensembles** — Random Forest, Gradient Boosting, and XGBoost.
5. **Support Vector Machines (SVM)** — Linear and RBF kernel parameter tuning.
6. **Artificial Neural Networks (MLP Classifier)** — Multi-Layer Perceptron architecture optimization.

### 5. 📈 Evaluation & Main Conclusions
* **Performance Metrics**: Evaluated models using Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Confusion Matrices.
* **Business Recommendations**: Identified key drivers of product success (e.g., *brand_trust*, *packaging_appeal*, balanced sweetness/umami profiles) and provided actionable insights for food product launches.

---

## 🛠️ Tech Stack & Dependencies

* **Language**: Python 3.8+ (Jupyter Notebook)
* **Data Manipulation**: `pandas`, `numpy`
* **Machine Learning**: `scikit-learn` (k-NN, Naive Bayes, Decision Trees, Random Forest, SVM, MLPClassifier, metrics, pipelines), `xgboost`
* **Visualization**: `matplotlib`, `seaborn`

---

## 📁 Repository Structure

```text
IDSproject/
├── project.ipynb                        # Primary Jupyter notebook containing full CRISP-DM analysis & models
├── food_product_acceptance_dataset.xlsx # Dataset (2,000 records, 42 features)
├── Assignment_food_acceptance_2526.pdf   # Assignment prompt and business context
├── LICENSE                              # Project license
└── README.md                            # Project documentation

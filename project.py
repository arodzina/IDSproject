#%% raw
# classi#%% md
# ##### 1. Business understanding
# • Give your view of the business problem following the CRISP-DM list of outputs when adequate.
# 
# #### 2. Data Understanding
# • Looking at the raw data, describe variables according to their types: interval-scaled, binary, nominal, ordinal, ratio-scaled. Be aware that there are specific methods suitable to each type of variable.  
# • Perform a preliminary analysis (summaries, spread measures, histograms, boxplots, density). These are interesting to be applied to the raw data to “uncover’’ inconsistencies, outliers, duplicates etc.  
# • Perform bivariate analysis (correlations, regression)  
# • Provide any insights about the data and the problem that you may have found.
# 
# #### 3. Data Preparation
# • List of main changes that can need to be performed to the raw data, including feature selection.  
# • Describe the potentially useful ones and their results in terms of data.
# 
# #### 4. Modeling 
# (consider the balanced and the non-balanced versions of the dataset as 2 separate problems)
# First work with the balanced data and then with the non-balanced data. Try each of the methods
# below, select hyper parameters using default values and empirical analysis. Separate a test set and use cross-validation on the rest of the examples. Visualize models when possible, visualize results, produce aggregating tables with good insightful summaries of the results, and whatever other tools you may find useful.  
# • Nearest neighbor  
# • Bayesian Classifier  
# • Decision Trees  
# • Tree ensembles  
# • Support Vector Machines  
# • Neural Network Classifier  
# • Comparison  
# #### 5. Evaluation and Main Conclusions
# • What is the best model and the recommended data science procedure for each business problem?  
# • What do you think that the business can gain from your data science effort?  
# • What are the lessons learnt?  
# • What is your summary of the achieved results?  
#%%
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np
data=pd.read_excel("food_product_acceptance_dataset.xlsx")
print(data.info())

#print(data.head())
data
#%% md
# ### Business problem 
# We want to create a new product that would be successful in the market taking into consideration its type, price, characteristics. In detail:
# 1. Drastically reduce the rate of expensive product market failures by implementing a data-driven system capable of predicting a product's eventual success or failure before committing to large-scale production and distribution.
# 2. Reduce reliance on costly, time-consuming sensory panel testing by validating a predictive model that can reliably estimate a product’s Overall Appreciation Score based on easily measurable and controllable features (like ingredients, price, and basic marketing metrics).
# 3. Identify and quantify the causal link between product features (sensory scores, nutritional data, price) and market success, creating a set of evidence-based guidelines for the Research, Development and Marketing teams.
#%% md
# There are 41 variables: <br>
# 
# - **Nominal variables**:
# Variables used for identification or grouping. They have distinct categories but no inherent order. They describe a product.
#   1. product_id
#   2. name
#   3. category (there are 9 categories so it might be useful to try it with One-Hot encoding)
#   4. subcategory
#   5. description
#   6. country_origin
# 
# - **Binary variables (0,1)**: 
#   Indicate popular product features
#   1. organic
#   2. gluten_free
#   3. contains_nuts
#   4. contains_meat
#   5. contains_dairy
#   6. seasonal
#   7. success (target)
# 
# - **Ordinal (0-5)**: Variables with a clear, ranked order, but the difference between levels doesn't have to be uniform or measurable.
#   1. spicy_level (but this is categorical so it might be useful to try it with One-Hot encoding)
# 
# - **Interval_scaled numeric(0-10)**: The difference between scores is consistent, ratios are not meaningful. Mostly show subjective experience from tasting a product.
#   1. color_intensity
#   2. aroma_intensity
#   3. sweetness
#   4. saltiness
#   5. bitterness
#   6. umami
#   7. sourness
#   8. texture_crispness
#   9. texture_softness
#   10. aftertaste_length
#   11. familiarity_score
#   12. novelty_score
#   13. brand_trust
#   14. packaging_appeal
#   15. overall_appreciation (Target)
# 
# 
# - **Ratio-scaled numerical variables**: The nutritional values and some distribution charasteristics:
#   1. calories
#   2. fat_g
#   3. sugar_g
#   4. protein_g
#   5. fiber_g
#   6. sodium_mg
#   7. price
#   8. eco_score
#   9. shelf_life_days
#   10. distribution_channels_count (but this is categorical so it might be useful to try it with One-Hot encoding)
#   11. review_count_prelaunch
#   12. allergy_warnings_count (but this is categorical so it might be useful to try it with One-Hot encoding)
#   13. marketing_spend_k
# 
#%% md
# column	type	description <br>
# product_id	string	Unique product code.<br>
# name	string	Marketing name; flavor + category/subcategory.<br>
# category	categorical	Top-level product category.<br>
# subcategory	categorical	Subcategory within category.<br>
# description	string	Short product descriptor.<br>
# country_origin	categorical	Country of origin.<br>
# calories	numeric	Per serving calories (kcal).<br>
# fat_g	numeric	Fat per serving (g).<br>
# sugar_g	numeric	Sugar per serving (g).<br>
# protein_g	numeric	Protein per serving (g).<br>
# fiber_g	numeric	Fiber per serving (g).<br>
# sodium_mg	numeric	Sodium per serving (mg).<br>
# organic	binary	Organic certification (True/False).<br>
# gluten_free	binary	Gluten-free claim (True/False).<br>
# contains_nuts	binary	Contains nuts (True/False).<br>
# contains_meat	binary	Contains meat (True/False).<br>
# contains_dairy	binary	Contains dairy (True/False).<br>
# seasonal	binary	Seasonal/limited edition (True/False).<br>
# spicy_level	ordinal 0-5	Subjective spiciness from panel.<br>
# color_intensity	numeric 0-10	Visual color intensity rating.<br>
# aroma_intensity	numeric 0-10	Aroma intensity rating.<br>
# sweetness	numeric 0-10	Sweetness rating.<br>
# saltiness	numeric 0-10	Saltiness rating.<br>
# bitterness	numeric 0-10	Bitterness rating.<br>
# umami	numeric 0-10	Umami rating.<br>
# sourness	numeric 0-10	Sourness rating.<br>
# texture_crispness	numeric 0-10	Crispness rating.<br>
# texture_softness	numeric 0-10	Softness rating.<br>
# aftertaste_length	numeric 0-10	Aftertaste length rating.<br>
# price	numeric	Suggested retail price (Euro).<br>
# familiarity_score	numeric 0-10	Consumer familiarity.<br>
# novelty_score	numeric 0-10	Perceived novelty.<br>
# brand_trust	numeric 0-10	Trust in brand.<br>
# packaging_appeal	numeric 0-10	Packaging visual appeal.<br>
# eco_score	numeric 0-100	Environmental friendliness score.<br>
# shelf_life_days	integer	Shelf life in days.<br>
# distribution_channels_count	integer	Count of planned channels.<br>
# review_count_prelaunch	integer	Pre-launch review mentions.<br>
# allergy_warnings_count	integer	Count of allergy warnings present.<br>
# marketing_spend_k	numeric	Marketing spend allocated (€ thousands).<br>
# overall_appreciation	target (0-10)	Overall appreciation from taster<br>
# success	target (0/1)	Expected market success
#%% md
# ## Analysis of nominal variables
#%%
NOMINAL_COLS = ['category', 'subcategory', 'country_origin']
# Exclude text columns for printing unique counts
EXCLUDE_TEXT_COLS = ['product_id', 'name', 'description']
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 6)
plt.rcParams['figure.dpi'] = 100

top_n = 10

for col in NOMINAL_COLS:
    # 1. Calculate and Print Descriptive Statistics
    counts = data[col].value_counts()
    proportions = data[col].value_counts(normalize=True) * 100
    # Calculate the number of null rows
    null_count = data[col].isnull().sum()
    summary_df = pd.DataFrame({
        'Count': counts,
        'Proportion (%)': proportions.round(2)
    })

    num_unique = data[col].nunique()
    print(f"Variable: {col}")
    print(f"Total Unique Categories: {num_unique}")
    # Display the null count
    print(f"Missing Rows: {null_count}")
    print(f"Top categories ({min(num_unique, top_n)} out of {num_unique}):")
    print(summary_df.head(top_n).to_markdown())

    # 2. Generate Bar Plot
    plt.figure()
    ax = sns.barplot(x=counts.index, y=counts.values, order=counts.index, color=sns.color_palette("viridis")[0])
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=3)

    plt.title(f'Distribution of Products by {col}', fontsize=14)
    plt.xlabel(col.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# 3. Print analysis for excluded text columns
print("Text Variable Check")
for col in EXCLUDE_TEXT_COLS:
    if col in data.columns:
        print(f"Variable '{col}': Total Unique Values = {data[col].nunique()}")
        null_count = data[col].isnull().sum()
        if     null_count >0:
            print(f"Missing Rows: {null_count}")


#%% md
# There are just 9 categories so it may be useful to encode them. The number of subcategories is bigger and there are some of them containing only one otem so it may not be useful to use them in the model. The country of origin has 20 values and all of them have more than 60 observations so it may be worth considering it in a model.
# There are no missing values.
#%% md
# Looking at the plots for subcategory, we can see that there are some typos that need to be fixed and we can also merge some similar subcategories to reduce dimensionality
#%%
reduction_map = {
    # 1. SWEET TREATS
    'Cookies': 'Dessert', 'Cakes': 'Dessert', 'Ice Cream': 'Dessert',
    'Sweet': 'Dessert', 'Dessert': 'Dessert',
    # 2. MAIN MEALS (Savory & heavy)
    'Soup': 'Meal', 'Curry': 'Meal', 'Pasta': 'Meal', 'Rice Bowl': 'Meal',
    'Pizza': 'Meal', 'Seafood': 'Meal', 'Savory': 'Meal',
    # 3. BAKERY
    'Bread': 'Bakery', 'Baked': 'Bakery',
    # 4. VEGETABLES
    'Veg Mix': 'Vegetable', 'Vegetable': 'Vegetable',
    # 5. PROTEIN & FITNESS
    'High-protein': 'Protein', 'Protein': 'Protein', 'Recovery Shake': 'Protein',
    # 6. BEVERAGES (General)
    'Coffee RTD': 'Beverage', 'Herbal Tea': 'Beverage', 'Juice': 'Beverage',
    'Sparkling': 'Beverage', 'Electrolyte Drink': 'Beverage',
    # 7. FUNCTIONAL / FERMENTED
    'Kombucha': 'Fermented', 'Fermented': 'Fermented', 'Yogurt': 'Fermented',
    # 8. CONDIMENTS
    'Sauce': 'Condiment', 'Dressing': 'Condiment', 'Spread': 'Condiment',
    # 9. SPECIAL DIET CLAIMS (Group vague health claims)
    'Gluten-free': 'Wellness', 'Healthy': 'Wellness',
    # 10. DAIRY (Solid)
    'Cheese': 'Dairy',
    # LEAVE THESE AS IS
    'Plant-based': 'Plant-based',
    'Experimental': 'Experimental'
}

data['subcategory'] = data['subcategory'].map(reduction_map).fillna(data['subcategory'])

print(f"New Subcategory Counts:\n{data['subcategory'].value_counts()}")
#%% md
# ## Binary variables
#%%
BINARY_COLS = ['organic', 'gluten_free', 'contains_nuts', 'contains_meat', 'contains_dairy', 'seasonal', 'success']

def safe_autopct(values):
    """Formats pie chart text to show both percentage and count."""
    def inner(pct):
        total = sum(values)
        if pct == 0 or total == 0:
            return "0%\n(0)"
        count = int(round(pct * total / 100))
        return f"{pct:.1f}%\n({count})"
    return inner

# Create a figure with one subplot for each binary column
fig, axes = plt.subplots(1, len(BINARY_COLS), figsize=(18, 5))

for i, col in enumerate(BINARY_COLS):
    ax = axes[i]
    counts = data[col].value_counts().sort_index()
    sizes = counts.reindex([0, 1], fill_value=0)
    wedges, label_texts, autopct_texts = ax.pie(
        sizes,
        autopct=safe_autopct(sizes),
        startangle=90,
        colors=['#8b0000', 'green'],
        counterclock=False,
    )

    for text_list in [label_texts, autopct_texts]:
        for txt in text_list:
            txt.set_color('white')
            txt.set_fontsize(9)

    ax.set_title(col.replace("_", " ").title(), fontsize=10, color='black')

plt.tight_layout()
plt.show()
for col in BINARY_COLS:
    null_count = data[col].isnull().sum()
    print(f"Variable: {col}, Null Rows: {null_count}")

#%% md
# Most of the variables are imbalanced - they have more 0 values than 1. The target binary variable shows a strong imbalance ratio for success and failure so we need to address it because the model which predicts success for every observation will have 93.8 % accuracy but no usefulness. There are no missing values.
#%% md
# ## Ordinal variable
#%%
plt.rcParams['figure.figsize'] = (7, 4)
plt.rcParams['figure.dpi'] = 100

print("Ordinal Variable: spicy_level ")
counts = data['spicy_level'].value_counts().sort_index()
proportions = data['spicy_level'].value_counts(normalize=True).sort_index() * 100
summary_df = pd.DataFrame({
    'Count': counts,
    'Proportion (%)': proportions.round(2)
})
null_count = data['spicy_level'].isnull().sum()
print(f"Null Rows: {null_count}")
print(f"Unique Levels: {data['spicy_level'].nunique()}")
print("Distribution:")
print(summary_df.to_markdown())
median_val = data['spicy_level'].median()
mode_val = data['spicy_level'].mode().iloc[0] if not data['spicy_level'].mode().empty else 'N/A'

print(f"\nMode: {mode_val}, Median: {median_val}\n")
plt.figure()
order = sorted(data['spicy_level'].unique())

ax = sns.countplot(
    x='spicy_level',
    data=data,
    order=order,
    hue='spicy_level',
    palette='magma',
    legend=False
)

for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=3)

plt.title('Product Distribution by Spicy Level (0-5)', fontsize=12)
plt.xlabel('Spicy Level', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.tight_layout()
plt.show()
#%% md
# Most of the products aren't spicy at all.
#%% md
# ## Interval scaled numerical variables
#%%
def plot_numeric_descriptive_analysis(data, cols_list, title, hist_color_1, hist_color_2, box_color_1, box_color_2, median_color):
    """
    Generates descriptive statistics and customized 4-plot visualizations for numeric columns.
    """
    print(f"\n--- {title} ---\n")
    # 1. Summary Statistics Table
    print("Descriptive Statistics:")
    desc_df = data[cols_list].describe().T
    summary_df = desc_df.rename(columns={'50%': 'median'})
    summary_df['null count'] = data[cols_list].isnull().sum()
    print(summary_df.to_markdown(floatfmt=".2f"))

    # 2. Histograms and Box Plots
    num_vars = len(cols_list)
    for i in range(0, num_vars, 2):
        col1 = cols_list[i]
        col2 = cols_list[i+1] if i + 1 < num_vars else None
        # Custom width ratios: [3 (Hist), 1 (Box), 3 (Hist), 1 (Box)]
        fig = plt.figure(figsize=(18, 5))
        gs = fig.add_gridspec(1, 4, width_ratios=[3, 1, 3, 1])
        # Variable 1
        ax0 = fig.add_subplot(gs[0, 0])
        sns.histplot(data[col1], kde=True, ax=ax0, color=hist_color_1, bins=15)
        ax0.axvline(data[col1].mean(), color='red', linestyle='--', label=f'Mean: {data[col1].mean():.2f}')
        ax0.axvline(data[col1].median(), color=median_color, linestyle='-', label=f'Median: {data[col1].median():.2f}')
        ax0.set_title(f'{col1.replace("_", " ").title()}', fontsize=10)
        ax0.set_xlabel('')

        print("mean: ", data[col1].mean())
        print("median: ", data[col1].median())

        ax1 = fig.add_subplot(gs[0, 1])
        sns.boxplot(y=data[col1], ax=ax1, color=box_color_1)
        ax1.set_title(f'{col1.replace("_", " ").title()}', fontsize=10)
        ax1.set_ylabel(col1.replace("_", " ").title())
        ax1.set_xlabel('')

        #Variable 2 (if exists)
        if col2:
            ax2 = fig.add_subplot(gs[0, 2])
            sns.histplot(data[col2], kde=True, ax=ax2, color=hist_color_2, bins=15)
            ax2.axvline(data[col2].mean(), color='red', linestyle='--', label=f'Mean: {data[col2].mean():.2f}')
            ax2.axvline(data[col2].median(), color=median_color, linestyle='-', label=f'Median: {data[col2].median():.2f}')
            ax2.set_title(f'{col2.replace("_", " ").title()}', fontsize=10)
            ax2.set_xlabel('')

            ax3 = fig.add_subplot(gs[0, 3])
            sns.boxplot(y=data[col2], ax=ax3, color=box_color_2)
            ax3.set_title(f'{col2.replace("_", " ").title()}', fontsize=10)
            ax3.set_ylabel(col2.replace("_", " ").title())
            ax3.set_xlabel('')
        else:
            fig.delaxes(fig.add_subplot(gs[0, 2]))
            fig.delaxes(fig.add_subplot(gs[0, 3]))

        plt.tight_layout()
        plt.show()

#%%
INTERVAL_COLS = ['color_intensity', 'aroma_intensity', 'sweetness', 'saltiness','bitterness', 'umami', 'sourness', 'texture_crispness','texture_softness', 'aftertaste_length', 'familiarity_score','novelty_score', 'brand_trust', 'packaging_appeal', 'overall_appreciation']

plot_numeric_descriptive_analysis(
    data=data,
    cols_list=INTERVAL_COLS,
    title="Interval-Scaled Numeric Variable Descriptive Analysis (0-10)",
    hist_color_1='dodgerblue',
    hist_color_2='olive',
    box_color_1='lightcoral',
    box_color_2='grey',
    median_color='orange'
)
#%% md
# The majority of the interval-scaled variables, such as color_intensity, sweetness, aroma_intensity, and overall_appreciation, exhibit a symmetric distribution. This is evidenced by the mean and median values being closely aligned in the descriptive statistics, suggesting that these variables are not strongly skewed and are close to a normal distribution.
# 
# Outliers, however, are present in several variables, as clearly visible in the box plots. Specifically, bitterness, sourness, brand_trust, and packaging_appeal contain extreme values that lie outside the interquartile range (IQR).
# 
# The range of all variables is between 0 and 10.
# 
# Two columns have missing values: aroma_intensity: 70 and umami: 65. It's not a big problem because the missing values are less than 4% of the number of data so they can be imputed without risking significant changes in the data.
#%% md
# ## Ratio-scaled variables
#%%
RATIO_COLS = ['calories', 'fat_g', 'sugar_g', 'protein_g', 'fiber_g','sodium_mg', 'price', 'eco_score', 'shelf_life_days','distribution_channels_count', 'review_count_prelaunch','allergy_warnings_count', 'marketing_spend_k']

plot_numeric_descriptive_analysis(
    data=data,
    cols_list=RATIO_COLS,
    title="Ratio-Scaled Numerical Variable Descriptive Analysis",
    hist_color_1='forestgreen',
    hist_color_2='darkorange',
    box_color_1='gold',
    box_color_2='darkred',
    median_color='darkblue',
)
#%% md
# Based on the plots of the ratio-scaled variables, most distributions deviate significantly from normality, often showing strong positive skewness and a high number of outliers in key metrics such as Price, Sodium (mg), and Review count prelaunch. This non-normal behavior indicates that data transformations—such as log or square root—may be necessary before applying linear models. Additionally, the visualizations reveal that Allergy warnings count and Distribution channels count are actually discrete, categorical variables, which should be properly encoded (e.g., via One-Hot Encoding) rather than treated as continuous in predictive models.
# 
# The range of the variables spans from 0 to 5520. Similar to the interval-scaled variables, there are two columns with missing values: protein_g (71) and fiber_g (63). Since these missing values represent less than 4% of the observations, imputing them is the most appropriate approach.
#%% md
# What's done:
# 1. description of the data considering their type: the analysis of proportions, frequencies, distribution, range, missing values.
#%% md
# # Filling missing values
#%% md
# The goal is to apply group-based imputation using categories, as there is a sufficient number of distinct categories and we expect them to meaningfully differ in their nutritional characteristics.
#%%
cols = ['protein_g', 'fiber_g', 'aroma_intensity', 'umami']
plt.figure(figsize=(14, 10))
for i, col in enumerate(cols, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(data=data, x='category', y=col)
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
#%% md
# As expected, there are clear differences in fiber and protein levels across categories, so we will use category-based group medians to impute the missing values in these variables. However, there is no significant difference for aroma_intensity and umami across categories, so we will examine their correlations with other variables to identify suitable candidates for imputation.
#%%
target_cols = ['aroma_intensity', 'umami']
numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
corr_matrix = data[numeric_cols].corr(method='pearson')
for col in target_cols:
    correlations = corr_matrix[col].drop(col)
    top5 = correlations.abs().sort_values(ascending=False).head(5)
    print(f"\nTop 5 correlations for {col}:")
    print(top5)
#%% md
# Since there are no strongly correlated variables for aroma_intensity and umami, we will impute their missing values using the global median.
#%%
group_impute = ['protein_g', 'fiber_g']
global_impute = ['aroma_intensity', 'umami']
GROUP_COL = 'category'
df = data.copy()

for col in group_impute:
    df[col] = df.groupby(GROUP_COL)[col].transform(
        lambda x: x.fillna(x.median())
    )
    df[col] = df[col].fillna(df[col].median())

for col in global_impute:
    df[col] = df[col].fillna(df[col].median())


print("Missing values after imputation:")
print(df[['protein_g', 'fiber_g', 'aroma_intensity', 'umami']].isnull().sum())
print(df.isna().sum())

#%% md
# # Categorical variables transformations
#%% md
# First, we look at the bar plots for the potential categorical variables to see how the values of each category are distributed.
#%%
CAT_COLS = ['category', 'country_origin', 'allergy_warnings_count', 'distribution_channels_count']
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
for ax, col in zip(axes.flatten(), CAT_COLS):
    counts = data[col].value_counts().sort_index()
    bars = ax.bar(counts.index.astype(str), counts.values, color='skyblue')
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, str(int(height)), ha='center', va='bottom')

    ax.set_title(f'Distribution of "{col}"')
    ax.set_xlabel(col)
    ax.set_ylabel('Number of samples')
    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels(counts.index.astype(str), rotation=45, ha='right')
plt.tight_layout()
plt.show()
#%% md
# 'category' has a few rare values, while 'country_origin' has a sufficient number of observations per country. 'allergy_warnings_count' and 'distribution_channels_count' also contain some rare categories. Next, we will look at the number of observations and their percentage share for each category.
#%%
summary_list = []

for col in CAT_COLS:
    counts = data[col].value_counts().reset_index()
    counts.columns = ['category', 'count']
    counts['variable'] = col
    counts['percent'] = counts['count'] / counts['count'].sum() * 100
    summary_list.append(counts)

summary_df = pd.concat(summary_list, axis=0, ignore_index=True)
summary_df = summary_df[['variable', 'category', 'count', 'percent']]
summary_df = summary_df.sort_values(by=['variable', 'count'], ascending=[True, False]).reset_index(drop=True)

print(summary_df)

#%% md
# Before converting the variables to dummy variables, we will transform the original categorical variables to handle very rare values that may not be useful for modeling.
# 
# - allergy_warnings_count will be grouped into four categories: 0, 1, 2, >2.
# - country_origin will remain unchanged.
# - category: RTD Meal and Supplements will be combined into a single category called 'Other'.
# - distribution_channels_count will be grouped into six categories: 1, 2, 3, 4, 5, >5.
#%%
# df = data.copy()

# 1. Transform allergy_warnings_count into 0,1,2,>2
def transform_allergy(x):
    if x > 2:
        return '>2'
    else:
        return str(int(x))

df['allergy_warnings_count'] = df['allergy_warnings_count'].fillna(0).apply(transform_allergy)

# 2. Transform distribution_channels_count into 1,2,3,4,5,>5
def transform_distribution(x):
    if x > 5:
        return '>5'
    else:
        return str(int(x))

df['distribution_channels_count'] = df['distribution_channels_count'].fillna(0).apply(transform_distribution)

# 3. Remove rare categories ('RTD Meal' & 'Supplements') by treating them as a single category 'Other'.
rare_categories = ['RTD Meal', 'Supplements']
df['category'] = df['category'].replace(rare_categories, 'other')

# 4. Create dummy variables for categories, country_origin, allergy_warnings_count, distribution_channels_count
CAT_COLS = ['category', 'country_origin', 'subcategory','allergy_warnings_count', 'distribution_channels_count']
df_dummies = pd.get_dummies(df, columns=CAT_COLS, drop_first=True)

print("List of new columns after dummy encoding:")
print(df_dummies.columns)

#%% md
# # Handling nearly constant variables
# Because features with extremely low variance add noise and do not help any model — especially a classifier like success.
#%%
# Separate numeric columns
from sklearn.feature_selection import VarianceThreshold

binary_cols = [col for col in df_dummies.columns if df_dummies[col].nunique() == 2]
continuous_cols = [col for col in df_dummies.select_dtypes(include=np.number).columns if col not in binary_cols]

# Variance threshold for binary columns
binary_selector = VarianceThreshold(threshold=0.01*(1-0.01))
binary_selector.fit(df_dummies[binary_cols])
binary_removed = df_dummies[binary_cols].columns[~binary_selector.get_support()]

continuous_selector = VarianceThreshold(threshold=0.1)
continuous_selector.fit(df_dummies[continuous_cols])
continuous_removed = df_dummies[continuous_cols].columns[~continuous_selector.get_support()]

print("Nearly constant binary columns:")
print(binary_removed)
print("\nNearly constant continuous columns:")
print(continuous_removed)

#%% md
# After creating dummy variables, we checked their variance to ensure they are informative.
# We also adjusted the coding of rare categories, and removed any nearly constant variables
# that would not contribute meaningfully to the model.
# 
#%% md
# # Bivariate analysis
#%%
# Remove the first 5 columns which are non-numericcolumns
cols_to_remove = df_dummies.columns[:5]
df_dummies = df_dummies.drop(columns=cols_to_remove)

print("Columns after removal:")
print(df_dummies.columns)

#%%
corr_with_target_s = df_dummies.corr()['success'].sort_values(ascending=False).drop(['success','overall_appreciation'])
corr_with_target_s

#%%
corr_with_target_a = df_dummies.corr()['overall_appreciation'].sort_values(ascending=False).drop(['overall_appreciation','success'])
corr_with_target_a
#%%
important_vars = corr_with_target_a[abs(corr_with_target_a) > 0.2].index

df_dummies[important_vars].corr()
#%%
corr_matrix = df_dummies.corr()

corr_pairs = (
    corr_matrix.where(~corr_matrix.isna())
    .abs()
    .unstack()
    .reset_index()
)

corr_pairs.columns = ['var1', 'var2', 'corr']

corr_pairs = corr_pairs[corr_pairs['var1'] != corr_pairs['var2']]
corr_pairs = corr_pairs.drop_duplicates(subset=['corr'])

top_corr = corr_pairs.sort_values(by='corr', ascending=False)

top_corr.head(30)

#%%

targets = ["overall_appreciation", "success"]

corr_matrix =df_dummies.corr(method="pearson")

for target in targets:
    print(f"\n=== Correlation with {target} ===")
    corr_target = (
        corr_matrix[target]
        .drop(['success','overall_appreciation'])
        .sort_values(ascending=False)
    )
    print(corr_target.to_markdown(floatfmt=".3f"))
#%%
corr_pairs = (
    corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    .stack()
    .reset_index()
)
corr_pairs.columns = ['Feature1', 'Feature2', 'Correlation']

strong_corr = corr_pairs[abs(corr_pairs['Correlation']) >= 0.5] \
                    .sort_values(by='Correlation', ascending=False)

print("\n=== Strong correlations between features (|r| ≥ 0.5) ===")
print(strong_corr.to_markdown(floatfmt=".3f"))

#%%
important_vars = (
    corr_matrix["overall_appreciation"]
    .abs()
    .sort_values(ascending=False)
)
important_vars = important_vars[important_vars >= 0.20].index.tolist()

print("\n=== Variables with |correlation| ≥ 0.20 to overall_appreciation ===")
print(important_vars)

corr_subset = corr_matrix.loc[important_vars, important_vars]

plt.figure(figsize=(10, 8))
sns.heatmap(corr_subset, cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap (reduced to important variables)")
plt.tight_layout()
plt.show()
#%% md
# Now we focus on visualizing the relationships between the variables with scatterplots.
#%%
# top 6 correlated variables
print(important_vars)
top_vars = important_vars[1:7] 

fig, axes = plt.subplots(3, 3, figsize=(16, 18)) 
axes = axes.flatten() 

for i, var in enumerate(top_vars):
    sns.regplot(x=var, y='overall_appreciation', data=df_dummies,
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=axes[i])
    axes[i].set_title(f"Relationship: {var} vs Overall Appreciation")

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()



#%% md
# ### Now we test numerical vs categorical
# We divide overal_appreciation into 3 bins with equal width:
# 
# Pandas splits the data so that:
# 
# 1/3 of the observations go into the first bin
# 
# 1/3 into the second bin
# 
# 1/3 into the third bin
# 
# The division is based on the percentiles of the data.
#%%
colors = ['green', 'red', 'blue']
features_to_plot = important_vars[2:7]
num_features = len(features_to_plot)
ncols = 3 # Number of subplots per row
# Calculate number of rows needed, accounting for the additional binary feature plot
nrows = ((num_features + 1) + ncols - 1) // ncols
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 6, nrows * 4))
axes = axes.flatten() # Flatten the 2D array of axes for easier iteration

df['OA_bins'] = pd.qcut(df['overall_appreciation'], q=3, labels=['Low', 'Medium', 'High'])
df_dummies['OA_bins'] = df['OA_bins']

for i, feature in enumerate(features_to_plot):
    ax = axes[i]
    for j, group in enumerate(['Low', 'Medium', 'High']):
        subset = df_dummies[df_dummies['OA_bins'] == group]
        if df_dummies[feature].nunique() <= 2:
            sns.histplot(subset[feature], label=group, color=colors[j], ax=ax, kde=False, stat="density", common_norm=False, alpha=0.3)
        else:
            sns.kdeplot(subset[feature], label=group, fill=True, alpha=0.3, color=colors[j], ax=ax)

        ax.set_title(f'Distribution of {feature} by OA group')
        ax.legend()
binary_feature = important_vars[1]

# Compute the mean (proportion) of 1's per OA bin
bin_values = df_dummies.groupby('OA_bins', observed=True)[binary_feature].mean()

# Add the binary feature plot to the next available subplot slot
ax_binary = axes[num_features]
sns.barplot(x=bin_values.index, y=bin_values.values, ax=ax_binary)
ax_binary.set_ylabel(f"Proportion of {binary_feature} = 1")
ax_binary.set_title(f"{binary_feature}: proportion by OA group")
ax_binary.set_ylim(0, 1)


# Hide any unused subplots, starting from the slot after the binary feature plot
for k in range(num_features + 1, nrows * ncols):
    fig.delaxes(axes[k])


plt.tight_layout()
plt.show()
#%% md
# # Regression Problem
# Business Goal: Reduce reliance on costly sensory panel testing by
# predicting overall_appreciation score based on measurable features
#%% md
# ##### Imports
#%%
# Data manipulation
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, KFold

# Models (we'll use these as we progress)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB  # For Bayesian (we'll adapt for regression)
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

from sklearn.model_selection import GridSearchCV
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_squared_error
from scipy import stats



# Metrics
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    mean_absolute_percentage_error
)

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['figure.dpi'] = 100

print("All libraries imported successfully")
#%% md
# ##### Loading data
#%%
print("Current columns in df_dummies:")
print(df_dummies.columns.tolist())
print(f"\nDataset shape: {df_dummies.shape}")


# Define target for regression
target_col = 'overall_appreciation'

# Define columns to exclude from features
cols_to_exclude = [
    'overall_appreciation',  # Target for regression
    'success',  # Target for classification
    'OA_bins'  # Binned version
]

# Create feature matrix X
X = df_dummies.drop(columns=cols_to_exclude, errors='ignore')

# Create target vector y
y = df_dummies[target_col]

print(f"\nFeatures prepared: {X.shape[1]} features")
print(f"Target prepared: {y.shape[0]} samples")
print(f"\nTarget statistics:")
print(f"  Mean: {y.mean():.2f}")
print(f"  Std:  {y.std():.2f}")
print(f"  Min:  {y.min():.2f}")
print(f"  Max:  {y.max():.2f}")
#%% md
# ##### Splitting
#%%
# Assignment requirement:
# - First 1600 rows: Training (for model fitting and cross-validation)
# - Next 200 rows: Validation (for model selection and hyperparameter tuning)
# - Last 200 rows: Test (for final evaluation )

# Training set (rows 0-1599)
X_train = X.iloc[:1600].copy()
y_train = y.iloc[:1600].copy()

# Validation set (rows 1600-1799)
X_val = X.iloc[1600:1800].copy()
y_val = y.iloc[1600:1800].copy()

# Test set (rows 1800-1999)
X_test = X.iloc[1800:].copy()
y_test = y.iloc[1800:].copy()

print("DATA SPLIT SUMMARY")
print(f"Training set:   {X_train.shape[0]} samples ({X_train.shape[0] / len(X) * 100:.1f}%)")
print(f"Validation set: {X_val.shape[0]} samples ({X_val.shape[0] / len(X) * 100:.1f}%)")
print(f"Test set:       {X_test.shape[0]} samples ({X_test.shape[0] / len(X) * 100:.1f}%)")

#%% md
# ##### Scaling for distance based models
#%%
# Only needed for: KNN, SVM, Neural Networks
# NOT needed for: Decision Trees, Random Forest, Gradient Boosting

# We'll create scaled versions but keep originals as primary
# Use scaled versions ONLY when training KNN, SVM, or Neural Networks

scaler = StandardScaler()

# Fit on training data only
scaler.fit(X_train)

# Transform all sets - we'll use these selectively
X_train_scaled = pd.DataFrame(
    scaler.transform(X_train),
    columns=X_train.columns,
    index=X_train.index
)

X_val_scaled = pd.DataFrame(
    scaler.transform(X_val),
    columns=X_val.columns,
    index=X_val.index
)

X_test_scaled = pd.DataFrame(
    scaler.transform(X_test),
    columns=X_test.columns,
    index=X_test.index
)

print("\nScaled versions created (use only for KNN, SVM, Neural Networks)")
print(f"  Original data preserved: X_train, X_val, X_test")
print(f"  Scaled data available: X_train_scaled, X_val_scaled, X_test_scaled")

#%% md
# ##### Evaluation functions
#%%
def evaluate_regression_model(y_true, y_pred, set_name="Validation"):
    """
    Comprehensive evaluation metrics for regression models
    """
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    # Avoid division by zero in MAPE
    mask = y_true != 0
    if mask.sum() > 0:
        mape = mean_absolute_percentage_error(y_true[mask], y_pred[mask])
    else:
        mape = np.nan

    print(f"\n{set_name} Set Performance:")
    print(f"  RMSE:  {rmse:.4f}")
    print(f"  MAE:   {mae:.4f}")
    print(f"  R²:    {r2:.4f}")
    print(f"  MAPE:  {mape:.2%}" if not np.isnan(mape) else "  MAPE:  N/A")

    return {
        'RMSE': rmse,
        'MAE': mae,
        'R2': r2,
        'MAPE': mape
    }


def plot_predictions(y_true, y_pred, model_name="Model", set_name="Validation"):
    """
    Visualize predictions vs actual values
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Scatter plot: Predicted vs Actual
    axes[0].scatter(y_true, y_pred, alpha=0.5, edgecolors='k', linewidths=0.5)
    axes[0].plot([y_true.min(), y_true.max()],
                 [y_true.min(), y_true.max()],
                 'r--', lw=2, label='Perfect Prediction')
    axes[0].set_xlabel('Actual Overall Appreciation')
    axes[0].set_ylabel('Predicted Overall Appreciation')
    axes[0].set_title(f'{model_name}: Predicted vs Actual ({set_name})')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Residual plot
    residuals = y_true - y_pred
    axes[1].scatter(y_pred, residuals, alpha=0.5, edgecolors='k', linewidths=0.5)
    axes[1].axhline(y=0, color='r', linestyle='--', lw=2)
    axes[1].set_xlabel('Predicted Overall Appreciation')
    axes[1].set_ylabel('Residuals (Actual - Predicted)')
    axes[1].set_title(f'{model_name}: Residual Plot ({set_name})')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def cross_validate_model(model, X, y, cv=5, scoring='neg_mean_squared_error'):
    """
    Perform k-fold cross-validation and return metrics
    """
    scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
    rmse_scores = np.sqrt(-scores)  # Convert negative MSE to RMSE

    print(f"\nCross-Validation Results (CV={cv}):")
    print(f"  RMSE: {rmse_scores.mean():.4f} (+/- {rmse_scores.std():.4f})")
    print(f"  Individual folds: {rmse_scores}")

    return rmse_scores

#%% md
# ##### Baseline model for comparison
#%%
# Simple baseline: always predict the training mean
baseline_pred_val = np.full(len(y_val), y_train.mean())
baseline_metrics = evaluate_regression_model(y_val, baseline_pred_val, "Baseline (Mean)")
#%% md
# ## Model 1 - KNN
#%% md
# We have to many features for knnn, we need to reduce them
#%%
# STEP 1: Hyperparameter Grid Definition

param_grid = {
    'n_neighbors': [3, 5, 7, 10, 15, 20, 30, 50,60,70],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan', 'minkowski'],
    'p': [1, 2]
}

print("KNN Hyperparameter Grid:")
print(f"  n_neighbors: {param_grid['n_neighbors']}")
print(f"  weights: {param_grid['weights']}")
print(f"  metric: {param_grid['metric']}")
print(
    f"  Total combinations: {len(param_grid['n_neighbors']) * len(param_grid['weights']) * len(param_grid['metric']) * len(param_grid['p'])}")

# STEP 2: Grid Search with Cross-Validation
knn = KNeighborsRegressor()
grid_search = GridSearchCV(
    estimator=knn,
    param_grid=param_grid,
    cv=5,
    scoring='neg_root_mean_squared_error',
    n_jobs=-1,
    verbose=1,
    return_train_score=True
)
grid_search.fit(X_train_scaled, y_train)

# STEP 3: Best Model and Results

best_knn = grid_search.best_estimator_
cv_results_df = pd.DataFrame(grid_search.cv_results_)

print("\nBest Parameters:")
for param, value in grid_search.best_params_.items():
    print(f"  {param}: {value}")
print(f"Best CV RMSE: {-grid_search.best_score_:.4f}")

# STEP 4: Impact of n_neighbors
k_values = sorted(cv_results_df['param_n_neighbors'].unique())
k_analysis = []

for k in k_values:
    k_subset = cv_results_df[cv_results_df['param_n_neighbors'] == k]
    best_idx = k_subset['mean_test_score'].idxmax()
    k_analysis.append({
        'k': k,
        'CV_RMSE': -k_subset.loc[best_idx, 'mean_test_score'],
        'Std': k_subset.loc[best_idx, 'std_test_score']
    })

k_df = pd.DataFrame(k_analysis)
print("\nCV RMSE by k:")
print(k_df.to_string(index=False))

plt.figure(figsize=(10, 5))
plt.errorbar(k_df['k'], k_df['CV_RMSE'], yerr=k_df['Std'],
             marker='o', capsize=5, linewidth=2)
plt.scatter([grid_search.best_params_['n_neighbors']],
            [-grid_search.best_score_],
            color='red', s=200, marker='*', zorder=5)
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Cross-Validation RMSE')
plt.title('Impact of k on Model Performance')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# STEP 5: Impact of Other Hyperparameters
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Weighting scheme
weights_df = cv_results_df.groupby('param_weights')['mean_test_score'].agg(['mean', 'std']).reset_index()
weights_df['mean'] *= -1
ax1 = axes[0, 0]
ax1.bar(range(len(weights_df)), weights_df['mean'], yerr=weights_df['std'],
        capsize=5, alpha=0.7, edgecolor='black')
ax1.set_xticks(range(len(weights_df)))
ax1.set_xticklabels(weights_df['param_weights'])
ax1.set_ylabel('Average CV RMSE')
ax1.set_title('Impact of Weighting Scheme')
ax1.grid(alpha=0.3, axis='y')

# Distance metric
metric_df = cv_results_df.groupby('param_metric')['mean_test_score'].agg(['mean', 'std']).reset_index()
metric_df['mean'] *= -1
metric_df = metric_df.sort_values('mean')
ax2 = axes[0, 1]
ax2.bar(range(len(metric_df)), metric_df['mean'], yerr=metric_df['std'],
        capsize=5, alpha=0.7, edgecolor='black')
ax2.set_xticks(range(len(metric_df)))
ax2.set_xticklabels(metric_df['param_metric'])
ax2.set_ylabel('Average CV RMSE')
ax2.set_title('Impact of Distance Metric')
ax2.grid(alpha=0.3, axis='y')

# Interaction: weights × metric
interaction = cv_results_df.groupby(['param_weights', 'param_metric'])['mean_test_score'].mean().reset_index()
interaction['mean_test_score'] *= -1
pivot = interaction.pivot(index='param_metric', columns='param_weights', values='mean_test_score')
ax3 = axes[1, 0]
sns.heatmap(pivot, annot=True, fmt='.4f', cmap='RdYlGn_r', ax=ax3,
            linewidths=1, cbar_kws={'label': 'CV RMSE'})
ax3.set_title('Interaction: Weights × Metric')

# Interaction: k × weights
k_weights = cv_results_df.groupby(['param_n_neighbors', 'param_weights'])['mean_test_score'].mean().reset_index()
k_weights['mean_test_score'] *= -1
ax4 = axes[1, 1]
for weight in k_weights['param_weights'].unique():
    data = k_weights[k_weights['param_weights'] == weight]
    ax4.plot(data['param_n_neighbors'], data['mean_test_score'],
             marker='o', linewidth=2, label=weight)
ax4.set_xlabel('Number of Neighbors (k)')
ax4.set_ylabel('CV RMSE')
ax4.set_title('Interaction: k × Weights')
ax4.legend(title='Weights')
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# STEP 6: Validation Performance

y_val_pred = best_knn.predict(X_val_scaled)
val_metrics = evaluate_regression_model(y_val, y_val_pred, "Validation")

plot_predictions(y_val, y_val_pred,
                 f"KNN (k={grid_search.best_params_['n_neighbors']})",
                 "Validation")

# STEP 7: Residual Analysis

residuals = y_val - y_val_pred
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(residuals, bins=20, edgecolor='black', alpha=0.7)
axes[0, 0].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Residuals')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Distribution of Residuals')

stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot')

axes[1, 0].scatter(y_val_pred, residuals, alpha=0.5)
axes[1, 0].axhline(y=0, color='red', linestyle='--')
axes[1, 0].set_xlabel('Predicted Values')
axes[1, 0].set_ylabel('Residuals')
axes[1, 0].set_title('Residuals vs Predicted')

axes[1, 1].scatter(y_val, np.abs(residuals), alpha=0.5)
axes[1, 1].set_xlabel('Actual Values')
axes[1, 1].set_ylabel('Absolute Error')
axes[1, 1].set_title('Absolute Error vs Actual')

plt.tight_layout()
plt.show()

print("\nResidual Statistics:")
print(f"  Mean: {residuals.mean():.4f}")
print(f"  Median: {residuals.median():.4f}")
print(f"  Std Dev: {residuals.std():.4f}")

# STEP 8: Feature Importance
perm_importance = permutation_importance(
    best_knn,
    X_val_scaled,
    y_val,
    n_repeats=10,
    random_state=42,
    scoring='neg_root_mean_squared_error'
)

importance_df = pd.DataFrame({
    'feature': X_train.columns,
    'importance': perm_importance.importances_mean,
    'std': perm_importance.importances_std
}).sort_values('importance', ascending=False)

print("\nTop 10 Important Features:")
print(importance_df.head(10).to_string(index=False))

plt.figure(figsize=(10, 6))
top_features = importance_df.head(15)
plt.barh(range(len(top_features)), top_features['importance'],
         xerr=top_features['std'], alpha=0.7)
plt.yticks(range(len(top_features)), top_features['feature'])
plt.xlabel('Permutation Importance')
plt.title('KNN: Top 15 Important Features')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# STEP 9: Model Comparison

comparison = pd.DataFrame({
    'Model': ['Baseline (Mean)', 'KNN'],
    'RMSE': [baseline_metrics['RMSE'], val_metrics['RMSE']],
    'MAE': [baseline_metrics['MAE'], val_metrics['MAE']],
    'R²': [baseline_metrics['R2'], val_metrics['R2']]
})

print("\nModel Comparison:")
print(comparison.to_string(index=False))

improvement = (baseline_metrics['RMSE'] - val_metrics['RMSE']) / baseline_metrics['RMSE'] * 100
print(f"\nRMSE improvement over baseline: {improvement:.2f}%")

# STEP 10: Store Results

knn_results = {
    'model_name': 'K-Nearest Neighbors',
    'best_params': grid_search.best_params_,
    'cv_rmse': -grid_search.best_score_,
    'cv_std': cv_results_df.loc[grid_search.best_index_, 'std_test_score'],
    'val_rmse': val_metrics['RMSE'],
    'val_mae': val_metrics['MAE'],
    'val_r2': val_metrics['R2'],
    'model': best_knn
}

print("\nKNN Results Summary:")
for key, value in knn_results.items():
    if key != 'model':
        print(f"  {key}: {value}")
#%% md
# # Classification Problem
#%% md
# ## Decision Tree
#%% md
# ## Random Forrest
#%% md
# ## SVM
#%% md
# ## KNN
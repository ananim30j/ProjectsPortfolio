# Exploratory Data Analysis on Consumer price index (CPI)
## Introduction
This project explores the impact of key economic factors such as the unemployment rate, GDP, and income inequality on the cost of living in various countries. Our initial findings highlight the highest cost of living in European countries and the lowest in Asian countries. Therefore, the further research primarily focuses on Europe, Asia, and North America (where we reside). We base our analysis on the Consumer Price Index (CPI), a crucial indicator often linked with the cost of living as defined by the [United States Bureau of Labor Statistics](https://www.bls.gov/cpi/questions-and-answers.htm). Spanning from 2000 to 2022, our study aims to analyze CPI as an independent variable and its relationships with unemployment rates, income inequality, and national GDP.

## Team Members

- [Ziji Tang](https://github.com/Tangzj10032)
- [Ananya Nimbalkar](https://github.com/ananim30j)
- [Hexuan Fan](https://github.com/Hillbert-F)
- [Xiaohan Kuang](https://github.com/kuangxh9)


## Research Question
How do key economic factors such as economic growth, inflation, and income inequality collectively influence a nation's CPI, and what can be inferred from these interactions regarding the broader economic landscape?

## Installation Requirements
To run the notebooks effectively, please install all required packages listed in `requirements.txt` by:
```bash
pip install -r requirements.txt
```

## Repository Description
- `data`: This directory consists of `raw` and `cleaned` data folders. The `raw` folder contains the datasets used in each individual notebook, while `cleaned` includes processed datasets such as `CPI_cleaned.xlsx`, which is the source of CPI data for all subsequent notebooks.

- `plots`: This director contains all the visualizations and charts created by the various notebooks. It includes both the key plots featured in the final report and additional ones. For a comprehensive view of all plots, including those not showcased in the `Final_Report.pdf`, please refer to this directory.

## Notebook Description
The Jupyter notebooks should be read sequentially for a comprehensive understanding:

- `Global_Cost_Living.ipynb`: The starting point of our analysis, examining the cost of living in different countries.

- `Unemployment_vs_CPI_Analysis.ipynb`: Explores the correlation between the unemployment rate and CPI.

- `GDP_vs_CPI_Analysis.ipynb`: Analyzes the correlation between GDP and CPI.

- `Gini_vs_CPI_Analysis.ipynb`: Investigates the correlation between the Gini index and CPI.


## Final Report
`Final_Report.pdf` integrates all analyses to comprehensively answer the research question.

## Appendix
Data Reference: 
- [WorldBank](https://databank.worldbank.org/home)
- [Kaggle](https://www.kaggle.com/)

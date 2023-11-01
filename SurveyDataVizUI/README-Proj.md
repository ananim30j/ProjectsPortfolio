# Analyzing and Visualizing Creative Community Survey Data for Non-Profit Initiatives

## Project Submission - Tianhao, Ananya, Susheel, Yuhao

### Overview

This project is a comprehensive analysis and visualization of a survey conducted by a non-profit organization in Nashville. The survey targets various roles within the creative community, aiming to gain insights to enhance the welfare and happiness of the individuals in this sector. Our team, composed of four dedicated members, have meticulously cleaned, analyzed, and visualized the survey data to provide actionable insights and a user-friendly interface for public engagement.

### Contents

1. **User Interface (UI)** - A locally runnable application developed in Streamlit, offering interactive visual insights and conclusions from the survey data.
2. **Jupyter Notebooks** - A set of five notebooks with detailed analyses and visualizations, accompanied by literate programming for comprehensive insights to help determine what activities to invest in to meet the needs of the artistic community.
3. **Requirements.txt** - A file containing all the necessary packages to run the UI and notebooks.
4. **.devcontainer** - To ensure a seamless, containerized environment setup for reproducibility.

### User Interface

Our UI is designed with the general public in mind, ensuring that the visualizations and insights are easily understandable and engaging. Developed in Streamlit, the UI is divided into several sections, each offering unique insights into the survey data.

**Pages In app.py (streamlit file):**

1. **Title and Home Page:**
    - Detailed overview of the survey.
    - Interactive demographic breakdown.
    - Visualization of responses from different roles.

2. **Creative Entrepreneurs:**
    - Types and years of creative practice.
    - Income source breakdown as a percentage.
    - Pre/post COVID annual income insights.

3. **Barriers:**
    - Visual insights into barriers faced by different roles.
    - Comparative analysis of top barriers.

4. **Space Needs:**
    - Visualizations of space needs identified by various roles.
    - Comparative analysis of top space needs.

*Additional insights and features to be added based on further analysis and team collaboration.*

### Jupyter Notebooks

Our notebooks are detailed, offering both visual and textual insights to aid the non-profit in decision-making. Each notebook is tailored to address specific questions and provide comprehensive analyses.

0. **Demographics:**
    - Data cleaning and preparation steps.
    - Detailed demographic analysis of survey respondents.

1. **Entrepreneurs and Teaching Artists:**
    - Distribution of years in creative practice vs age for various roles.
    - Rate of business closure analysis.

2. **Creative Workers, Funders:**
    - Primary arts focus of different organizations
    - Layoffs and economic situation analysis of different organizations.

3. **Arts Participation - Business Professionals and Social Workers:**
    - Pre/post COVID arts event attendance
    - Art discpline distribution
    - Size of company distribution
    - VLPA Program interest

4. **Future Directions:**
    - Analysis of non-profit organization membership.
    - Insights into potential areas of investment for the non-profit.

### How to Run

1. Clone the GitHub repository.
2. Navigate to the project directory.
3. Install the required packages using `pip install -r requirements.txt` in the terminal. Or if you are using vscode, select "reopen using container". Make sure Docker is open and running before trying to open in container.
4. Run the Streamlit app using `streamlit run app.py` in the terminal. If you cannot run due to "ModuleNotFoundError: No module named 'altair.vegalite.v4'", please run "pip install --upgrade streamlit".
5. Open other Jupyter notebooks and run the cells to view the analyses.

### Team Members

1. **Susheel**: Responsible for Notebook 2 and documentation for Notebook 0, along with the second page of the UI (Creative Entrepreneurs). Also worked on the README-Proj.
2. **Ananya**: Responsible for Notebook 1 and and code for Notebook 0, along with the third page of the UI (Barriers). Also worked on the README-Proj.
3. **Tianhao**: Responsible for Notebook 3 and first page of the UI (Home).
4. **Yuhao**: Responsible for Notebook 4 and the fourth page of the UI (Space Needs).

*All team members contributed collaboratively to all aspects of the project, having good usage of GitHub flow, commit, and branching strategies.*

### Additional Notes

- Ensure to have Python installed and preferably use a virtual environment to install the dependencies.
- The code is designed to be reproducible; ensure to follow the steps in the "How to Run" section for accurate results.
- The .devcontainer folder ensures that graders can recreate our environment without hassle.

### Unanswered Questions
Some questions could not be answered due to missing data. Here is a list of them:

**User Interface**
-Barriers Page: Figure for Barriers for Teaching Artists

**Jupyter Notebooks**
-Notebook 2: Creative Workers, Arts Administrators: What is the primary arts focus of the organizations and at what distribution? What about funders?
-Notebook 3: What areas of expertise are represented in these two roles?

*For any additional information or clarification, feel free to contact any of the team members.*

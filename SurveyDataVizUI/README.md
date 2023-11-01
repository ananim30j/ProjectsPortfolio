[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/HI2dhF09)
# Analyzing and Visualizing Creative Community Survey Data for Non-Profit Initiatives
> Providing business analyses and creating user interfaces

**Due Monday, October 16th, 11:59pm**

# Overview:
You have been approached by a non-profit company in Nashville focusing on the welfare and happiness of the creative community. They have conducted a survey targeting various roles in the creative industry and are interested in gaining insights from this data to better support the community.

Your task is to:
- Analyze and clean the survey data.
- Develop a public-facing graphical user interface to display the results.
- Create and answer insightful questions in Jupyter notebooks to help the non-profit make informed decisions.

At the end of the project, you will submit:
1. A user interface (likely developed in Streamlit or Gradio) via a Python file. You don't need to have this hosted anywhere, and only needs to be able to run locally.
2. A set of 5 Jupyter notebooks with literate programming practices - targeted towards the collaborator for review and decision-making.

## Data:
The survey includes standard demographic information and specific questions related to the roles and interactions of participants in the creative industry in Nashville. The roles include:
- Creative Entrepreneurs
- Creative Workers
- Arts Administrators
- Arts Educators or Teaching Artists
- Arts Funders
- Business Professionals
- Civic and/or Social Service Workers

The survey is organized into blocks, and each role takes one or more blocks of the survey. For example, all roles take the initial 7 demographics questions, and then only Creative Entrepreneurs answer questions 8-36 (based on column numbers). You will be able to discern which questions are answered by whom based on the data.

# Logistical Details
## Teams
You will be working in teams of 4. Each member is fully responsible for all of the work done on the project. The expectation is that each member will be primarily responsible for one page of the user interface and one page of the Jupyter notebook analysis. The remaining tasks should be divided among members.

## Usage of Generative AI
You can use generative AI to the desired extent that you wish. Upload data to OpenAI Advanced Data Analytics, download Jupyter notebook analyses, use Bing Chat to help with new APIs. However, it is your responsibility to review and assess the output of the generative AI platforms that you use; the work is expected to reflect the beliefs, activity, and ideas of your team. You own the work.


# Requirements and Grading (Out of 200 points)
Your project should be submitted as a GitHub repository with 5 notebooks, an `app.py` file (or file representing the user interface), and a `requirements.txt` file (or file with additional package installation requirements). You should also include a `.devcontainer` folder and `ReadMe.md` files. The `.devcontainer` directory should allow the graders to create containers with your specified environment without needing to install any packages on their own. The Readme should provide an overview of the files of the repository and any additional information needed to run the app if you choose not to use gradio or streamlit.

## User Interface (80 points)
The user interface should be a deployable `app.py` file with a `requirements.txt` file or similar with additional required packages. The expectation is that the user interface will be created using streamlit or gradio, and these two platforms will be the only ones supported by your instructional team; however, feel free to try other packages like Flask if desired. **Remember that the purpose of this user interface is to convey information in a visual format - remember this as you're creating the figures below.**

The UI is public-facing, meaning it's meant for the outside word of non-data scientists to understand the survey and the results in an aesthetically pleasing way. For this reason, you should have plots and brief descriptions accompanying any plots. The app should minimally have the following 4 pages:
1. **Title and Home Page (20 points):** Provides details about the survey (similar to ReadMe information), and must include:
    * 1 figure with interactive selection that allows users to see the breakdown of 4 different demographics based on the selection
    * A figure representing how many of the individual of the different roles responded to the survey
2. **Creative Entrepreneurs (20 points)**:
    * Figure for types of creative practice
    * Figure for years of creative practice existence
    * Percentage of income from various sources
    * Pre/post COVID annual income, typical annual income from creative practice
3. **Barriers (20 points)**
    * Figure for Barriers faced by Creative Entrepreneurs
    * Figure for Barriers faced by Arts Administrators and Creative Workers
    * Figure for Barriers for Teaching Artists
    * Figure comparing magnitude of top 3 barriers for each of the above sets of roles
4. **Space Needs (20 points)**
    * Figure for Space Needs Identified by Creative Entrepreneurs and Teaching Artists/Educators
    * Figure for Space Needs for Arts Admiinstrators and Creative Workers
    * Figure for Future Spaces for Arts Administrators, Creative Workers, Creative Entrepreneurs, and Teaching Artists
    * Figure comparing/ displaying top 3 needs for each of the above sets of roles

The user interface will be additionally evaluated on presentation, chart choices and ease of visual understanding, and concise helpful explanation.

## Jupyter Notebooks (90 points)
The Jupyter notebooks are organization facing and are meant to allow the collaborators to both read and view the results of the analysis. Their objective in this analysis is to determine what activities to invest in in order to meet the needs of the artistic community. In these notebooks, you'll create this analysis. Minimally, the following notebooks are required. These questions are more free-form, and you should use your analytical skills with pandas functionality to deliver the answers.

0. **Demographics (10 points)**
    * Any necessary data cleaning to prepare the data. Make sure to indicate steps of cleaning, effects, and justification. If desired, you can put this in a separate notebook.
    * Who has taken the survey? (with figures)
    * Which questions are answered by which roles, and how many respondents are there to each question (with figure)
    * In looking at the percentage of respondents based on demographics, how representative of each population do you think the results will be? In other words, by what decomposition does it seem that the data is actionable? (i.e., If the survey has 2 Funders, do you think the business should make conclusions based on the results from the findings of funders in the surveys?)

1. **Entrepreneurs and Teaching Artists (10 points)**
    * Creative Entrepreneurs: What is the distribution of the years in creative practice vs the age of the demographic?
    * Creative Entrepreneurs: What is the rate of business closure out of the participants?
    * Arts Educators: What is the distribution of years as an arts educator relative to the age of the demographic?
    * Arts educator: What types of creative disciplines are taught and at what distribution?
    * Arts educators: What are the primary roles as arts educators and at what distribution?


2. **Creative Workers, Funders (10 points)**
    * Creative Workers, Arts Administrators: What is the primary arts focus of the organizations and at what distribution? What about funders?
    * Creative Workers, Arts Administrators: Provide figures and commentary regarding layoffs and the economic situation for the organization in terms of a) operating budget, and b) layoffs relative to the number of staff members.
   
   
    
3. **Arts Participation: Business Professionals and Social Workers (30 points)**
In this section, you will benefit from inspecting the text of the questions, as some questions in the two sections are similar, but slightly differently phrased. If you align the question texts, you may be better able to combine these questions for study. If you find that the distributions for the roles separately is uninteresting/uninformative, you can combine them together into a single distribution/figure, but justify your answer.

    * For these two roles, what is the difference between how many arts events they visited in a single month on average pre- and post- COVID? Use figures to justify and demonstrte the reasoning for your answer.
    * What arts disciplines are generally pursued/experienced by respondents in these roles and at what distribution?
    * What areas of expertise are represented in these two roles?
    * What are the distributions of sizes for companies/organizations for these two roles?
    * To what extent are individuals of these roles interested in volunteering their skills for the VLPA program?
    * What is the distribution of yearly financial or in-kind distributions to arts organizations for these two roles?
    * What, if any, relationship is there between friends/family members working in the arts, participation in the arts (i.e., current average arts attendance), and yearly financial/in-kind contributions?

    
3. **Future Directions (30 points)**
    * Of all of the respondents who answered the question, what proportion of respondents are currently members of the non-profit organization? Does this differ by role?
    * Based on Creative Workers and Arts Administrators, what would be beneficial for the non-profit organization to invest its time and energy into? Justify your answers.
    * Based on Business Professionals and Social Workers, what would be beneficial for the non-profit organization to invest its time and energy into? Are there certain topics or outcomes that seem more interesting than others and more worth the expense? Justify your answers.
    * What is the distribution of respondents that are planning on leaving Nashville in the next year? Does this differ by role?
    * Based on the final 20 questions of the survey, what is the distribution of respondents who know about the events mentioned in these questions? Does this differ by role?
    * Show the distribution of words which come to mind for respondents when they think of the non-profit organization. You can do this using a package to assist in creating word clouds or also you can create a general bar plot.


The notebooks will be additionally evaluated on correctness, literacy, code simplicity, and presentation.

## Other submission components (30 points)
* **ReadMe (5 points)**: General overview of the project (brief) and any required instructions for running your code. If this is overly complex, additional points above the 5 points noted here may be deducted based on the difficulty required in order to evaluate the submission.
* **devcontainer and requirements.txt (5 points)**: These define the environment that your code needs to run, and we will use these to create the appropriate environment.
* **Good usage of GH flow, commit, and branching strategies(20 points)**: Since this is a group project for data science, it is expected that best practices will be used when committing code to the repository and building the deliverables. There is an expectation of seeing different branches for different components (e.g., we would expect a different branch for a different notebook, different UI page, etc.), with pull requests, commentary/approval, and merging. It is expected that there should be a minimum of 1-2 commits on each branch to finish the task. It is additionally expected that branches will be merged into the main branch, and at any time, the main branch will represent a final version of the current state of the work. Do not delete your branches after merging.

### Additional Notes:
- Your code will need to be reproducible. We reserve the right to re-run all the notebooks and follow any reasonable instructions provided in the ReadMe to re-generate any code.
- Keep in mind that the data cleaning that you do in the Jupyter notebook as well as some of the plots will be replicated on the user interface. If you use a package like nbdev, this can reduce the amount of cleaning you'll need to do.
- Code which does not run may be subject to larger penalties than those described by the rubric depending on the magnitude of challenge faced when trying to evaluate the submissions.
- Ensure that your analysis in the Jupyter notebooks is comprehensible to non-technical stakeholders.
- Your user interface should be public-friendly and focus on information relevant to the general public, while the Jupyter notebooks should be more detailed and aimed at helping the non-profit make informed decisions.

Good luck!

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# How to run this:  streamlit run final_app.py


# Load the data
@st.cache_data
def load_data():
    return pd.read_excel("2023-cleaned-survey.xlsx")

df = load_data()

# Function to safely plot count plots
def safe_countplot(data, y_col, title, ax):
    if data.empty:
        st.write(f"No data available for {title}")
        return
    sns.countplot(data=data, y=y_col, ax=ax)
    plt.title(title)

# Title and Home Page
st.title("Creative Sector Survey 2023")


# Dropdown menu for pages
page = st.sidebar.selectbox("Select a Page:", ["Home", "Creative Entrepreneurs", "Barriers", "Space Needs"])

if page == "Home":
    st.write("""
    # Survey Overview
    This survey aims to understand the landscape of the creative sector in 2023.
    The data provides insights into various roles, demographics, and challenges faced by creative professionals.
    Please check below for demographics information regarding the survey.
    """)
    # Dropdown for selecting demographic
    demographic_option = st.selectbox("Select a demographic for breakdown:", ["Age", "Identified Gender", "Describe Your Location", "Select Your Race/Ethnicity"])
    fig, ax = plt.subplots()
    safe_countplot(df, demographic_option, f"Breakdown by {demographic_option}", ax)
    st.pyplot(fig)

    # Roles
    fig, ax = plt.subplots()
    safe_countplot(df, "Describe Your Primary Role in Creative Sector", "Roles in Creative Sector", ax)
    st.pyplot(fig)

elif page == "Creative Entrepreneurs":
    st.write("## Creative Entrepreneurs")
    
    # Dropdown to choose between the two plots
    plot_choice = st.selectbox("Choose a Visualization:", ["Types of Creative Practice", "Years of Professional Creative Practice","Income Sources Distribution","Income Analysis (Pre/Post COVID)"])
    
    if plot_choice == "Types of Creative Practice":
        # Description
        st.write("""
        The visualization showcases the diverse range of creative practices among Creative Entrepreneurs. The vertical bars represent the count of respondents for each specific creative practice.
        """)
        
        # Types of creative practice plot
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.countplot(data=df, y="Primary Creative Activity", order=df["Primary Creative Activity"].value_counts().index, palette="viridis", ax=ax)
        ax.set_title("Types of Creative Practice among Creative Entrepreneurs", fontsize=16)
        ax.set_xlabel("Number of Respondents", fontsize=14)
        ax.set_ylabel("Type of Creative Practice", fontsize=14)
        st.pyplot(fig)
    
    elif plot_choice == "Years of Professional Creative Practice":
        # Description
        st.write("""
        The chart illustrates the distribution of "Years of Professional Creative Practice" among Creative Entrepreneurs. It provides insights into how experienced the respondents are in their creative fields. From newcomers with "0-5 years" of practice to seasoned professionals with "21+ years", the data captures a broad spectrum of expertise within the community.
        """)
        
        # Years of Professional Creative Practice plot
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.countplot(data=df, y="Years of Professional Creative Practice", order=df["Years of Professional Creative Practice"].value_counts().index, palette="viridis", ax=ax)
        ax.set_title("Years of Professional Creative Practice among Creative Entrepreneurs", fontsize=16)
        ax.set_xlabel("Number of Respondents", fontsize=14)
        ax.set_ylabel("Years of Practice", fontsize=14)
        st.pyplot(fig)

    elif plot_choice == "Income Sources Distribution":
        st.write("""
        The bar chart reveals the distribution of average income percentages across different sources. It becomes evident that the majority of Creative Entrepreneurs derive a significant portion of their income from "Non-artistic freelance/contract work," followed by sources like "Freelance/contract artistic work" and "Full-time artistic employment."
        """)
        
        # Computing the average income percentage within the Streamlit code
        income_columns = [
            "Income Sources (in %) Full-time artistic employement",
            "Income Sources (in %) Part-time artistic employment",
            "Income Sources (in %) Freelance/contract artistic work",
            "Income Sources (in %) Full-time non-artistic employment",
            "Income Sources (in %) Part-time non-artistic employment",
            "Income Sources (in %) Non-artistic freelance/contract work"
        ]
        average_income_percentage = df[income_columns].mean()
        
        # Displaying the numerical summary in a table
        st.table(average_income_percentage.reset_index().rename(columns={'index': 'Income Source', 0: 'Average Percentage (%)'}))
        
        # Income Sources Distribution plot
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(x=average_income_percentage.values, y=average_income_percentage.index, palette="viridis", ax=ax)
        ax.set_title("Average Percentage of Income from Various Sources", fontsize=16)
        ax.set_xlabel("Average Percentage (%)", fontsize=14)
        ax.set_ylabel("Income Source", fontsize=14)
        st.pyplot(fig)

    elif plot_choice == "Income Analysis (Pre/Post COVID)":
        income_analysis_choice = st.selectbox("Select Income Analysis:", [
            "Pre-COVID Typical Total Annual Household Income",
            "Pre-COVID Typical Annual Income from Artistic/Creative Practice",
            "Post-COVID Annual Household Income",
            "Post-COVID Annual Income from Artistic/Creative Practice",
            "Comparison of Annual Household Incomes (Pre vs. Post COVID)",
            "Comparison of Annual Incomes from Artistic/Creative Practice (Pre vs. Post COVID)"
        ])
        
        # Filter dataframe for Creative Entrepreneurs
        df_ce = df[df["Describe Your Primary Role in Creative Sector"] == "Creative Entrepreneurs (Artists, performers, makers, creatives of all disciplines, self-employed)"]
        # Define custom order for income brackets
        income_order = ['$0-$10,000',
                        '$10,001-$25,000',
                        '$25,001-$50,000',
                        '$50,001-$75,000',
                        '$75,001 or above',
                        'Prefer not to answer']

        
        if income_analysis_choice == "Pre-COVID Typical Total Annual Household Income":
            st.write("### Pre-COVID Typical Total Annual Household Income among Creative Entrepreneurs")
            st.write(df_ce["Income Details BEFORE COVID-19 Typical total annual household income"].describe())
    
            # Sorting the data based on the defined order
            sorted_data = df_ce["Income Details BEFORE COVID-19 Typical total annual household income"].astype(pd.CategoricalDtype(categories=income_order, ordered=True))
    
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.histplot(sorted_data, bins=30, kde=True, ax=ax)
            ax.set_title("Distribution of Pre-COVID Typical Total Annual Household Income")
            ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility
    
            st.pyplot(fig)
            
        elif income_analysis_choice == "Pre-COVID Typical Annual Income from Artistic/Creative Practice":
            st.write("### Pre-COVID Typical Annual Income from Artistic/Creative Practice among Creative Entrepreneurs")
            st.write(df_ce["Income Details BEFORE COVID-19 Typical annual income from artistic/creative practice"].describe())
            sorted_data = df_ce["Income Details BEFORE COVID-19 Typical annual income from artistic/creative practice"].astype(pd.CategoricalDtype(categories=income_order, ordered=True))
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.histplot(sorted_data, bins=30, kde=True, ax=ax)
            ax.tick_params(axis='x', rotation=45)
            ax.set_title("Distribution of Pre-COVID Typical Annual Income from Artistic/Creative Practice")
            st.pyplot(fig)

        elif income_analysis_choice == "Post-COVID Annual Household Income":
            st.write("### Post-COVID Annual Household Income among Creative Entrepreneurs")
            st.write(df_ce["Income Details POST COVID-19 RESTRICTIONS (2022) Annual household income"].describe())
            sorted_data = df_ce["Income Details POST COVID-19 RESTRICTIONS (2022) Annual household income"].astype(pd.CategoricalDtype(categories=income_order, ordered=True))
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.histplot(sorted_data, bins=30, kde=True, ax=ax)
            ax.tick_params(axis='x', rotation=45)
            ax.set_title("Distribution of Post-COVID Annual Household Income")
            st.pyplot(fig)


        elif income_analysis_choice == "Post-COVID Annual Income from Artistic/Creative Practice":
            st.write("### Post-COVID Annual Income from Artistic/Creative Practice among Creative Entrepreneurs")
            st.write(df_ce["Income Details POST COVID-19 RESTRICTIONS (2022) Annual income from artistic/creative practice"].describe())
            sorted_data = df_ce["Income Details POST COVID-19 RESTRICTIONS (2022) Annual income from artistic/creative practice"].astype(pd.CategoricalDtype(categories=income_order, ordered=True))
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.histplot(sorted_data, bins=30, kde=True, ax=ax)
            ax.tick_params(axis='x', rotation=45)
            ax.set_title("Distribution of Post-COVID Annual Income from Artistic/Creative Practice")
            st.pyplot(fig)

        elif income_analysis_choice == "Comparison of Annual Household Incomes (Pre vs. Post COVID)":
            st.write("### Comparison of Annual Household Incomes (Pre vs. Post COVID) among Creative Entrepreneurs")
    
            # Extracting and counting data for Pre-COVID
            pre_covid_counts = df_ce["Income Details BEFORE COVID-19 Typical total annual household income"].value_counts().to_dict()
    
            # Extracting and counting data for Post-COVID
            post_covid_counts = df_ce["Income Details POST COVID-19 RESTRICTIONS (2022) Annual household income"].value_counts().to_dict()
    
            # Identifying unique income brackets
            income_brackets = list(set(list(pre_covid_counts.keys()) + list(post_covid_counts.keys())))
            income_brackets.sort()
    
            pre_covid_values = [pre_covid_counts.get(bracket, 0) for bracket in income_brackets]
            post_covid_values = [post_covid_counts.get(bracket, 0) for bracket in income_brackets]
    
            # Plotting
            fig, ax = plt.subplots(figsize=(15, 8))
            bar_width = 0.35
            bar_positions_1 = np.arange(len(income_brackets))
            bar_positions_2 = [pos + bar_width for pos in bar_positions_1]
    
            ax.barh(bar_positions_1, pre_covid_values, bar_width, label="Pre-COVID", color='blue')
            ax.barh(bar_positions_2, post_covid_values, bar_width, label="Post-COVID", color='red')
    
            ax.set_title("Comparison of Annual Household Incomes (Pre vs. Post COVID)")
            ax.set_yticks([pos + bar_width for pos in bar_positions_1])
            ax.set_yticklabels(income_brackets)
            ax.legend(title="Time Period")
    
            st.pyplot(fig)


        elif income_analysis_choice == "Comparison of Annual Incomes from Artistic/Creative Practice (Pre vs. Post COVID)":
            st.write("### Comparison of Annual Incomes from Artistic/Creative Practice (Pre vs. Post COVID) among Creative Entrepreneurs")
    
            # Extracting and counting data for Pre-COVID
            pre_covid_practice_counts = df_ce["Income Details BEFORE COVID-19 Typical annual income from artistic/creative practice"].value_counts().to_dict()
    
            # Extracting and counting data for Post-COVID
            post_covid_practice_counts = df_ce["Income Details POST COVID-19 RESTRICTIONS (2022) Annual income from artistic/creative practice"].value_counts().to_dict()
    
            # Identifying unique income brackets
            practice_income_brackets = list(set(list(pre_covid_practice_counts.keys()) + list(post_covid_practice_counts.keys())))
            practice_income_brackets.sort()
    
            pre_covid_practice_values = [pre_covid_practice_counts.get(bracket, 0) for bracket in practice_income_brackets]
            post_covid_practice_values = [post_covid_practice_counts.get(bracket, 0) for bracket in practice_income_brackets]

            # Plotting
            fig, ax = plt.subplots(figsize=(15, 8))
            bar_width = 0.35
            bar_positions_1 = np.arange(len(practice_income_brackets))
            bar_positions_2 = [pos + bar_width for pos in bar_positions_1]
    
            ax.barh(bar_positions_1, pre_covid_practice_values, bar_width, label="Pre-COVID", color='blue')
            ax.barh(bar_positions_2, post_covid_practice_values, bar_width, label="Post-COVID", color='red')
    
            ax.set_title("Comparison of Annual Incomes from Artistic/Creative Practice (Pre vs. Post COVID)")
            ax.set_yticks([pos + bar_width for pos in bar_positions_1])
            ax.set_yticklabels(practice_income_brackets)
            ax.legend(title="Time Period")
    
            st.pyplot(fig)


elif page == "Barriers":
    st.write("## Barriers")

    #Figure 1

    # Filter the dataset for Creative Entrepreneurs using the correct category name
    creative_entrepreneurs_df = df[df['Describe Your Primary Role in Creative Sector'] == 'Creative Entrepreneurs (Artists, performers, makers, creatives of all disciplines, self-employed)']

    # Identify potential columns related to barriers by scanning column names for relevant keywords
    barrier_keywords = ['barrier', 'challenge', 'difficulty', 'obstacle']
    potential_barrier_columns = [col for col in creative_entrepreneurs_df.columns if any(keyword in col.lower() for keyword in barrier_keywords)]

    # Count the frequency distribution of ratings for each barrier column
    barrier_ratings_counts = {}
    for col in potential_barrier_columns:
        if "Rate Barriers to Success in Creative Practice" in col:
            barrier_ratings_counts[col] = creative_entrepreneurs_df[col].value_counts()

    # Extracting barrier labels and formatting them for better readability
    formatted_barrier_labels = [label.split("Rate Barriers to Success in Creative Practice ")[1] for label in barrier_ratings_counts.keys()]

    # Generating the stacked bar chart with rotated axes and moving the legend outside of the plot
    fig1, ax = plt.subplots(figsize=(12, 15))

    # Define ratings categories for ordering in the stacked bar
    ratings_order = ['1 - No Impact', '2 - Little Impact', '3 - Some Impact', '4 - Significant impact', '5 - Most impactful']

    # Stacking bars for each rating category
    left_values = [0] * len(barrier_ratings_counts)
    for rating in ratings_order:
        current_values = [barrier_ratings_counts[barrier].get(rating, 0) for barrier in barrier_ratings_counts.keys()]
        ax.barh(formatted_barrier_labels, current_values, left=left_values, label=rating)
        left_values = [left + current for left, current in zip(left_values, current_values)]

    ax.set_title("Barriers Faced by Creative Entrepreneurs")
    ax.set_xlabel("Count of Responses")
    ax.set_ylabel("Barriers")
    ax.legend(title="Impact Rating", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    plt.show()

    #Figure 2
    # Filter the dataset for Arts Administrators and Creative Workers
    arts_admin_and_workers_df = df[df['Describe Your Primary Role in Creative Sector'].isin([
        'Arts Administrator (Theater managers, development staff, executive directors, program coordinators at an arts-based business usually a non-profit, e.g., at a museum, symphony, theater, etc.)',
        'Creative Worker (In-house graphic designers, copywriters, art directors employed at a business working in the creative industries)'
    ])]

    # Identify potential columns related to barriers by scanning column names for relevant keywords
    barrier_keywords = ['barrier', 'challenge', 'difficulty', 'obstacle']
    potential_barrier_columns_2 = [col for col in arts_admin_and_workers_df.columns if any(keyword in col.lower() for keyword in barrier_keywords)]

    # Count the frequency distribution of ratings for each barrier column
    barrier_ratings_counts_2 = {}
    for col in potential_barrier_columns_2:
        if "Rate Barriers to Success" in col:
            barrier_ratings_counts_2[col] = arts_admin_and_workers_df[col].value_counts()

    # Extracting barrier labels specific to Arts Administrators and Creative Workers and formatting them for better readability
    formatted_barrier_labels_2 = [label.split("Rate Barriers to Success in Your Organization ")[1] for label in barrier_ratings_counts_2.keys() if "Rate Barriers to Success in Your Organization" in label]

    # Generating the stacked bar chart with rotated axes for Arts Administrators and Creative Workers
    fig2, ax = plt.subplots(figsize=(12, 15))

    # Define ratings categories for ordering in the stacked bar
    ratings_order = ['1 - No Impact', '2 - Little Impact', '3 - Some Impact', '4 - Significant impact', '5 - Most impactful']

    # Stacking bars for each rating category
    left_values = [0] * len(formatted_barrier_labels_2)
    for rating in ratings_order:
        current_values = [barrier_ratings_counts_2[barrier].get(rating, 0) if barrier in barrier_ratings_counts_2 else 0 for barrier in barrier_ratings_counts_2.keys() if "Rate Barriers to Success in Your Organization" in barrier]
        ax.barh(formatted_barrier_labels_2, current_values, left=left_values, label=rating)
        left_values = [left + current for left, current in zip(left_values, current_values)]

    ax.set_title("Barriers Faced by Arts Administrators and Creative Workers")
    ax.set_xlabel("Count of Responses")
    ax.set_ylabel("Barriers")
    ax.legend(title="Impact Rating", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    plt.show()

    #Figure 3
    print("Insufficent Data")

    #Figure 4
    # Define a function to compute total impact for each barrier using the updated impact scores
    def compute_total_impact_updated(barrier_counts):
        impact_scores_updated = {
            '1 - No Impact': 1,
            '1 - No impact': 1,
            '2 - Little Impact': 2,
            '2 - Little impact': 2,
            '3 - Some Impact': 3,
            '3 - Some impact': 3,
            '4 - Significant impact': 4,
            '5 - Most impactful': 5,
            '5 - Highly impactful': 5
        }
        total_impact = {}
        for barrier, counts in barrier_counts.items():
            impact = sum(impact_scores_updated[rating] * count for rating, count in counts.items())
            total_impact[barrier] = impact
        return total_impact

    # Filter dataset for specific roles and compute the top 3 barriers based on total impact
    arts_admin_and_workers_df = df[df['Describe Your Primary Role in Creative Sector'].isin([
        'Arts Administrator (Theater managers, development staff, executive directors, program coordinators at an arts-based business usually a non-profit, e.g., at a museum, symphony, theater, etc.)',
        'Creative Worker (In-house graphic designers, copywriters, art directors employed at a business working in the creative industries)'
    ])]

    # Identify columns related to barriers and count the frequency distribution of ratings for each barrier column
    barrier_keywords = ['barrier', 'challenge', 'difficulty', 'obstacle']
    potential_barrier_columns_2 = [col for col in arts_admin_and_workers_df.columns if any(keyword in col.lower() for keyword in barrier_keywords)]
    barrier_ratings_counts_2 = {col: arts_admin_and_workers_df[col].value_counts() for col in potential_barrier_columns_2 if "Rate Barriers to Success" in col}

    # Compute total impact and extract top 3 barriers for each role set
    total_impact_entrepreneurs = compute_total_impact_updated(barrier_ratings_counts)
    top_3_entrepreneurs = sorted(total_impact_entrepreneurs.items(), key=lambda x: x[1], reverse=True)[:3]

    total_impact_admin_and_workers = compute_total_impact_updated(barrier_ratings_counts_2)
    top_3_admin_and_workers = sorted(total_impact_admin_and_workers.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract data for visualization and generate the comparison chart
    roles = ["Creative Entrepreneurs", "Arts Administrators & Creative Workers"]
    barriers_data = {
        "Creative Entrepreneurs": {barrier[0].split(" ")[-1]: barrier[1] for barrier in top_3_entrepreneurs},
        "Arts Administrators & Creative Workers": {barrier[0].split(" ")[-1]: barrier[1] for barrier in top_3_admin_and_workers}
    }

    fig4, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    for ax, role in zip(axs, roles):
        barriers = list(barriers_data[role].keys())
        values = list(barriers_data[role].values())
        ax.barh(barriers, values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        ax.set_title(role)
        ax.set_xlabel("Total Impact")

    plt.tight_layout()
    plt.show()

    # Displaying Figure 1
    st.write("### Barriers Faced by Creative Entrepreneurs")
    st.write("This figure depicts several barriers faced by Creative Entrepreneurs and its impact according to the respondents. As seen, 'Transportation' is the most impactful barrier, whereas 'Ongoing restrictions due to the COVID-19 pandemic' has the least impact. Overall, most of the barriers have a diverse impact rating, showcasing Creative Entreprenerus face many barriers, ranging from minimal to high impact levels.")
    st.pyplot(fig1)
    
    # Displaying Figure 2
    st.write("### Barriers Faced by Arts Administrators and Creative Workers")
    st.write("This figure shows the barriers faced by Arts Administrators and Creative Workers, as well as how much it impacted them. For these roles, time, expected audience habits, and lack of support from the private sector/business community have the highest count of responses. This indicates these are the most frequent barriers. Also, each and every barrier had a significant impact, as depicted by red bars.")
    st.pyplot(fig2)

    # Displaying message for Figure 3
    st.write("### Barriers Faced by Teaching Artists")
    st.write("Unfortunately, there is no data that shows any barriers faced by Teaching Artists. Although they may be struggling, right now it is not possible to come to a conclusion for this specific role.")

    # Displaying Figure 4
    #Since Teaching Artists Data is empty, cannot show top 3 barriers for that
    st.write("### Top 3 Barriers Comparison")
    st.write("This figure shows the top 3 barriers for roles Creative Entrepreneurs, Arts Adminstrators, and Creative Workers. For Creative Entrepreneurs, the top 3 barriers are events, transportation, and technology. Transportation and technology have the greatest impact amongst the role. However, development, time, and hire are the top 3 barriers for Arts Administrators and Creative Workers, with hire having the greatest impact.")
    st.pyplot(fig4)

elif page == "Space Needs":
    st.write("## Space Needs")
    
    
    # Additional selection for professional groups
    group = st.sidebar.radio("Select Group", ["Entrepreneurs & Teaching Artists", "Arts Administrators & Creative Workers", "Future Spaces - Various Roles", "Compare Top Needs"])
    # Q1
    
    if group == "Entrepreneurs & Teaching Artists":
        st.write("## Space Needs for Creative Entrepreneurs and Teaching Artists/Educators")
        st.write("""
        # Survey Overview
        These data come from "How important are the following space types/amenities to your creative practice or business?" 
        I choose to calculate counts of "Critically Important" responses for each space and amenity and then draw the image.
        """)
        # This is the data I have analyzed
        data_entrepreneurs_artists = {
            "Photography studio/dark room": 25,
            "Music practice room": 21,
            "Music recording studio": 21,
            "Computer lab": 24,
            "Individual artist studio": 24,
            "Shared artist studio (any discipline)": 25,
            "Mirrored dance/rehearsal studio": 28,
            "Podcasting studio": 21,
            "Projector/screening equipment": 23,
            "Industrial arts workshops (wood, metal)": 18,
            "Textile/fashion lab": 22,
            "Writing room or quiet area": 26,
            "General co-working space": 27,
            "Theater/auditorium (<100 seats)": 21,
            "Theater/auditorium (100+ seats)": 29,
            "Gallery/exhibition space": 19,
            "Retail opportunities": 33,
            "Secure storage/lockers": 19,
            "Business services, such as mailboxes, copy/fax, printing": 28,
            "Collaboration/networking events": 22
        }
        df1 = pd.Series(data_entrepreneurs_artists).reset_index()
        df1.columns = ['Amenity', 'Count']
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.barh(df1['Amenity'], df1['Count'], color='skyblue')
        ax1.set_xlabel('Count')
        ax1.set_title('Critically Important Space Needs for Creative Entrepreneurs and Teaching Artists/Educators')
        plt.tight_layout()
        st.pyplot(fig1)
        
    elif group == "Arts Administrators & Creative Workers":
        st.write("### Space Needs for Arts Administrators and Creative Workers")
        st.write("""
        # Survey Overview
        These data come from "How important are the following space types/amenities to your creative practice or business?" 
        I choose to calculate counts of "Critically Important" responses for each space and amenity and then draw the image.
        """)
        # This is the data I have analyzed
        data_admin_creative_workers = {
            "Photography studio/dark room": 21,
            "Music practice room": 26,
            "Music recording studio": 24,
            "Computer lab": 33,
            "Individual artist studio (any discipline)": 25,
            "Shared artist studio (any discipline)": 28,
            "Mirrored dance/rehearsal studio": 24,
            "Podcasting studio": 26,
            "Projector/screening equipment": 30,
            "Industrial arts workshops (wood, metal)": 25,
            "Textile/fashion lab": 26,
            "Writing room or quiet area": 27,
            "General co-working space": 24,
            "Theater/auditorium (<100 seats)": 30,
            "Theater/auditorium (100+ seats)": 31,
            "Gallery/exhibition space": 23,
            "Retail opportunities": 25,
            "Secure storage/lockers": 25,
            "Business services, such as mailboxes, copy/fax, printing": 31,
            "Collaboration/networking events": 19
        }
        df2 = pd.Series(data_admin_creative_workers).reset_index()
        df2.columns = ['Amenity', 'Count']
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.barh(df2['Amenity'], df2['Count'], color='salmon')
        ax2.set_xlabel('Count')
        ax2.set_title('Critically Important Space Needs for Arts Administrators and Creative Workers')
        plt.tight_layout()
        st.pyplot(fig2)

    elif group == "Future Spaces - Various Roles":
        st.write("### Future Spaces for Arts Administrators, Creative Workers, Creative Entrepreneurs, and Teaching Artists")
        st.write("""
        # Survey Overview
        These data come from "Rate the importance of each aspect when considering a move to a new creative space Storage" 
        I choose to calculate counts of "Critically Important" responses for each space and amenity and then draw the image.
        """)
        data_future_spaces = {
            "Dedicated workspaces/workstations": 26,
            "Parking and accessibility": 24,
            "Smaller conference rooms/ meeting": 25,
            "Storage": 26,
            "Green space": 23,
            "Large event space": 24,
            "Retail space": 28,
            "Shared workspaces/workstations": 29,
            "Restaurant": 15,
            "Shared back office services": 29,
            "Photography studio": 28,
            "Music practice room": 21,
            "Music recording studio": 20,
            "Computer lab": 23,
            "Individual artist studio (any discipline)": 27,
            "Shared artist studio (any discipline)": 28,
            "Mirrored dance/rehearsal studio": 18,
            "Podcasting studio": 22,
            "Projector/screening equipment": 26,
            "Writing room or quiet area": 25,
            "General co-working space": 26,
            "Theater/auditorium (<100 seats)": 23,
            "Theater/auditorium (100+ seats)": 16,
            "Gallery/exhibition space": 26,
            "Retail opportunities": 23,
            "Secure storage/lockers": 20,
            "Business services, such as mailboxes, copy/fax, printing": 24,
            "Collaboration/networking events": 26
        }

        df3 = pd.Series(data_future_spaces).reset_index()
        df3.columns = ['Aspect/Amenity', 'Count']
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        ax3.barh(df3['Aspect/Amenity'], df3['Count'], color='lightgreen')
        ax3.set_xlabel('Count')
        ax3.set_title('Critically Important Aspects and Amenities for Future Spaces')
        plt.tight_layout()
        st.pyplot(fig3)
    
    elif group == "Compare Top Needs":
        st.write("### Comparing Top Space Needs Across Different Roles")
        
        # Data
        top_needs_data = {
            'Entrepreneurs and Artists': {'Retail opportunities': 33, 'Theater/auditorium (100+ seats)': 29, 'Mirrored dance/rehearsal studio': 28},
            'Administrators and Workers': {'Computer lab': 33, 'Theater/auditorium (100+ seats)': 31, 'Business services': 31},
            'Future Spaces': {'Shared workspaces/workstations': 29, 'Shared back office services': 29, 'Retail space': 28}
        }
        
        # Visualization
        fig, ax = plt.subplots(figsize=(10, 6))
        
        colors = ['blue', 'orange', 'green']
        for i, (role, needs) in enumerate(top_needs_data.items()):
            ax.barh([f"{key} ({role})" for key in needs.keys()], list(needs.values()), color=colors[i], label=role)
        
        ax.set_xlabel("Count")
        ax.set_title("Top 3 Critically Important Space Needs Across Different Roles")
        plt.legend(loc='upper right')  # Place the legend in the upper right corner
        plt.tight_layout()
        st.pyplot(fig)

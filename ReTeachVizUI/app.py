import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from ai_assisted_coding_v2 import In_Loop_AI_Assist_Labeling, AI_Assist_Labeling, Ask_your_dataset

# Custom styling for aesthetics
def set_page_style():
    st.markdown("""
        <style>
            .main h1 { color: #0b5d8e; font-family: 'Helvetica'; }
            .main h2, .sidebar h2 { color: #ff6347; font-family: 'Arial'; }
            .main .block-container { padding-top: 2rem; }
            .stButton>button { background-color: #0b5d8e; color: white; }
            .stFileUploader { border-color: #ff6347; }
            .stTextInput>div>div>input { color: #0b5d8e; }
            .css-2trqyj:focus:not(:active) { border-color: #ff6347; }
        </style>
    """, unsafe_allow_html=True)

set_page_style()



# Custom styling for aesthetics
def set_page_style():
    st.markdown('''
        <style>
            .main h1 { color: #0b5d8e; font-family: 'Helvetica'; }
            .main h2, .sidebar h2 { color: #ff6347; font-family: 'Arial'; }
            .main .block-container { padding-top: 2rem; }
            .stButton>button { background-color: #0b5d8e; color: white; }
            .stFileUploader { border-color: #ff6347; }
            .stTextInput>div>div>input { color: #0b5d8e; }
            .css-2trqyj:focus:not(:active) { border-color: #ff6347; }
        </style>
    ''', unsafe_allow_html=True)

set_page_style()

# Initialize the session state variables at the start to ensure they exist before use

if 'accuracy_log' not in st.session_state:
    st.session_state.accuracy_log = []  # Log for tracking st.session_state.model accuracy over time
if 'batch_sizes' not in st.session_state:
    st.session_state.batch_sizes = []  # Initial batch size for labeling
if 'current_line_index' not in st.session_state:
    st.session_state.current_line_index = 0  # Index to keep track of the current line to be labeled
if 'start_line' not in st.session_state:
    st.session_state.start_line = 0
if 'model' not in st.session_state:
    # Initialize the st.session_state.model from the AI_Assist_Labeling package
    st.session_state.model = In_Loop_AI_Assist_Labeling.BertLabeler()
if 'num_lines' not in st.session_state:
    st.session_state.num_lines = 10
if 'data' not in st.session_state:
    st.session_state.data = None
if 'datalog' not in st.session_state:
    st.session_state.datalog = []

# Define a function to calculate accuracy
def calculate_accuracy(user_labels, predicted_labels):
    correct_predictions = sum(1 for true, pred in zip(user_labels, predicted_labels) if true == pred)
    accuracy = correct_predictions / len(user_labels)
    return accuracy

# Define a function to plot and save the model accuracy and batch size logs

def plot_and_save_logs():
    plt.style.use('ggplot')  # Enhanced visual style
    # ... [rest of the existing plot_and_save_logs function code]

    # Ensure that accuracy log and batch sizes have the same length
    if len(st.session_state.accuracy_log) > len(st.session_state.batch_sizes):
        # Append the last known batch size to match the length of accuracy_log
        # st.session_state.batch_sizes += [st.session_state.batch_sizes[-1]] * (len(st.session_state.accuracy_log) - len(st.session_state.batch_sizes))
        st.session_state.batch_sizes += st.session_state.num_lines

    if st.session_state.accuracy_log:
        fig, ax1 = plt.subplots()
        color = 'tab:blue'
        ax1.set_xlabel('Batch Number')
        ax1.set_ylabel('Accuracy', color=color)
        ax1.plot(range(1, len(st.session_state.accuracy_log) + 1), st.session_state.accuracy_log, 'o-', color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'tab:red'
        ax2.set_ylabel('Batch Size', color=color)
        ax2.plot(range(1, len(st.session_state.batch_sizes) + 1), st.session_state.batch_sizes, 's-', color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        ax1.grid(True)
        plt.title('BERT Model Accuracy and Batch Size Over Time')
        fig.tight_layout()  # adjust subplot params so that the subplot(s) fits in to the figure area
        

        # Save the logs to a CSV file
        logs_df = pd.DataFrame({
            'Batch Number': range(1, len(st.session_state.accuracy_log) + 1),
            'Accuracy': st.session_state.accuracy_log,
            'Batch Size': st.session_state.batch_sizes
        })


        csv = logs_df.to_csv(index=False).encode('utf-8')
        st.pyplot(fig)  # display the plot
        st.download_button("Download accuracy log as CSV", csv, "accuracy_log.csv", "text/csv")


# Create a sidebar for navigation
st.sidebar.title("Navigation")
# The sidebar allows the user to select which page to view
page = st.sidebar.radio("Go to", ["Home", "AI-Assisted Labeling Page", "Ask the Dataset Page", "AI-Assisted Analysis Page"])

# Home Page
if page == "Home":
    st.title("ReTeach: Automated Teacher Feedback System")  # Project title
    st.write("""
    Welcome to ReTeach, our innovative solution designed to transform how educational feedback is delivered. ReTeach is an automated platform that not only listens to classroom interactions but also intelligently analyzes them to provide constructive feedback.
    """)
    st.write("Project Developed by: Ananya Nimbalkar, Susheel Srikanth, Tianhao Qu, Yuhao Zhang")
    st.write("""
    Purpose of ReTeach: To offer an interactive labeling platform that adapts and evolves. As you label data, ReTeach learns and improves, offering increasingly accurate predictions and insights.
    """)
    st.write("""
    How to Use ReTeach: Navigate through each section, following the instructions provided. For optimal performance and to avoid errors, it's essential to adhere to these guidelines.
    """)
    st.write("""
    Key Features:
    - **AI-Assisted Labeling**: Streamline the labeling process with AI-generated suggestions. Review and adjust labels with ease, saving time and enhancing accuracy.
    - **Ask the Dataset**: Interact directly with your data. Pose questions and receive answers, enabling deeper understanding and exploration of the content.
    - **AI-Assisted Analysis**: Utilize advanced algorithms for comprehensive analysis of teaching methods and classroom interactions.
    """)
    st.markdown("""
    ## User Experience Focus
    Each page of ReTeach has been meticulously crafted to prioritize ease of use and clarity. Our goal is to deliver a user-friendly interface that not only looks good but makes your workflow efficient and enjoyable.
    """)
    st.markdown("""
    ## Getting Started
    To begin, choose a feature from the menu and upload your classroom session transcript. Follow the on-screen prompts to label, query, or analyze your data. If you're new, we recommend starting with the AI-Assisted Labeling feature for a quick and effective introduction to ReTeach.
    """)

# AI-Assisted Labeling Page
elif page == "AI-Assisted Labeling Page":
    st.header("AI-Assisted Labeling Page")
    
    # Description and usage instructions for the AI-Assisted Labeling page
    st.write("On this page, users can upload a CSV file of the current Text table, whether labeled or unlabeled.")
    st.markdown("""
    ### How to Use
    1. Upload your CSV file using the uploader below.
    2. The AI model will automatically label the text data and calculate confidence scores.
    3. The labeled data, along with confidence scores, will be displayed.
    4. You can then download the AI-assisted labeled data.
    """)

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        # Read the uploaded file
        data = pd.read_csv(uploaded_file)

        # Initialize CsvLabeler and process the data
        csv_labeler = AI_Assist_Labeling.CsvLabeler()  # Adjust if necessary

        # Save the uploaded file to a temporary location
        temp_file_path = 'temp_uploaded_file.csv'
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getvalue())

        # Define the output path
        output_dir = 'labeled_data'
        output_filename = os.path.join(output_dir, 'labeled_classroom_transcripts.csv')

        # Label the data and read the labeled data
        labeled_data_path = csv_labeler.label_csv(temp_file_path, output_filename)
        labeled_data = pd.read_csv(labeled_data_path)

        # Displaying the labeled data with color coding
        styled_data = csv_labeler.colorize_confidence(labeled_data)
        st.dataframe(styled_data)

        # Download link for the new CSV file
        st.download_button(
            label="Download AI-Assisted Labeled Data",
            data=labeled_data.to_csv(index=False).encode('utf-8'),
            file_name="ai_labeled_data.csv",
            mime="text/csv",
        )

# Ask the Dataset Page
elif page == "Ask the Dataset Page":
    st.header("Ask the Dataset Page")
    
    # Description and usage instructions for the Ask the Dataset page
    st.write("Welcome to the Ask the Dataset page! Here, you can upload one or more CSV files, "
             "ask questions about the data, and receive insights directly from an AI assistant. "
             "This tool is perfect for quick data analysis, extracting key information, "
             "or answering specific queries about your datasets.")

    st.markdown("""
    ### How to Use
    1. **Upload CSV Files**: Use the file uploader to select one or more CSV files. 
       The system will concatenate these files into a single dataset.
    2. **Enter Your OpenAI API Key**: Input your OpenAI API key in the provided text box. 
       This key is essential for the AI assistant to process your questions.
    3. **Ask Your Question**: Type in your question about the data in the text input box. 
       You can ask for summaries, specific data points, comparisons, or any other analysis.
    4. **Submit and View Responses**: Press the 'Ask' button to submit your question. 
       The AI assistant's response will be displayed below. You can ask multiple questions; 
       each new response will appear after the previous one.
    5. **Conversation History** : The page also keeps track of your conversation history, 
       allowing the AI to utilize previous context for better responses.
    """)

    # Streamlit app title for the CSV Data Analysis Chatbot
    st.title("CSV Data Analysis Chatbot")

    # API Key input
    api_key = st.text_input("Enter your OpenAI API Key", type="password")

    # File uploader
    uploaded_files = st.file_uploader("Upload CSV files", accept_multiple_files=True, type="csv")

    # Chat history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # Chat input
    user_question = st.text_input("Your question about the data")

    # Process files and questions
    if st.button("Ask"):
        if api_key and uploaded_files and user_question:
            # Read and process CSV data
            reader = Ask_your_dataset.CSVDataReader()
            csv_data = reader.read_data(uploaded_files)

            # Create OpenAI Chat Client
            chat_client = Ask_your_dataset.OpenAIChatClient(api_key)

            # Get the answer
            answer = chat_client.query_gpt(csv_data, user_question)

            # Update chat history
            st.session_state['history'].append({"question": user_question, "answer": answer})

            # Display the conversation
            for chat in st.session_state['history']:
                st.text_area("Question", chat["question"], height=75)
                st.text_area("Answer", chat["answer"], height=150)
        else:
            st.error("Please provide all required inputs.")


# AI-Assisted Analysis Page
elif page == "AI-Assisted Analysis Page":
    st.header("AI-Assisted Analysis Page")
    st.write("""
    The AI-Assisted Analysis Page is a robust tool designed to facilitate the efficient labeling and analysis of classroom session texts. It combines user input with AI technology to progressively improve label accuracy and deepen insights into educational interactions.
    """)
    st.markdown("""
    ### How to Use
    1. **Upload CSV Files**: Start by uploading one or more CSV files containing classroom session transcripts. These can be files with or without existing labels.
    2. **Select Lines to Label**: Choose a number of lines you wish to label initially. This can be a predefined number or a number of your choosing.
    3. **Label and Train**: Manually apply labels to these lines. Labels include categories like OTR (Opportunity to Respond), PRS (Praise), REP (Reprimand), and NEU (Neutral). After labeling, these inputs are used to train the st.session_state.model.
    4. **Model Predictions and Corrections**: The st.session_state.model will then predict labels for the next batch of statements. Review these predictions and correct any inaccuracies.
    5. **Iterative Learning**: With each round of corrections, the model learns and improves its prediction accuracy. Continue this process of prediction and correction to enhance model performance.
    6. **Download Labeled Data**: At any point, you can download the updated CSV file with your verified labels. This file can be used for further analysis or record-keeping.
    7. **Continuous Labeling Option**: If you choose to continue labeling after a download, you can do so seamlessly. The system will maintain the state of your work.
    8. **Accuracy Tracking**: The platform keeps a log of the model's prediction accuracy, updating it with each batch. This log, along with batch sizes, is visualized in a graph for easy tracking. You can also download this accuracy log.
    """)

    # File uploader widget modified to accept multiple files
    uploaded_files = st.file_uploader("Choose one or more CSV files", accept_multiple_files=True, type="csv")

    if uploaded_files:
        # Concatenate all uploaded files into a single dataframe
        st.session_state.data = pd.concat([pd.read_csv(file) for file in uploaded_files], ignore_index=True)
        st.session_state.model.set_df(st.session_state.data)
        #data['Label'] = data['Label'].fillna('NEU')  # Default label for unlabeled data
        
        remaining_lines = len(st.session_state.data) - st.session_state.current_line_index

        # Check if there are no more lines to label and disable widgets accordingly
        if remaining_lines <= 0:
            st.write("All lines have been labeled. Thank you!")
        else:
            # Widgets for labeling logic
            max_line_index = max(0, len(st.session_state.data) - 1)
            if st.session_state.current_line_index > max_line_index:
                st.session_state.current_line_index = max_line_index
                st.session_state.num_lines = max_line_index - st.session_state.current_line_index

            # start_line = st.number_input("Start line", value=st.session_state.current_line_index, min_value=0, max_value=max_line_index)
            num_lines = st.session_state.num_lines


            st.session_state.end_line = st.session_state.start_line + num_lines

            
            lines_to_label = st.session_state.data.iloc[st.session_state.start_line:st.session_state.end_line]


            if 'selectbox_value' not in st.session_state:
                predicted_labels = st.session_state.model.label_list_sentences(lines_to_label['Text'].tolist())
                st.session_state.selectbox_value = [label[0] for label in predicted_labels]
            
            predicted_labels = st.session_state.selectbox_value
            print('start and end lines are: ', st.session_state.start_line, st.session_state.end_line, len(lines_to_label), len(st.session_state.selectbox_value))

            for i, (row, default_value) in enumerate(zip(lines_to_label.itertuples(), st.session_state.selectbox_value), start=st.session_state.start_line):
                label = st.selectbox(f"Line {i}: {row.Text}", options=['OTR', 'PRS', 'REP', 'NEU'], 
                                    index=['OTR', 'PRS', 'REP', 'NEU'].index(default_value), 
                                    key=f"label_{i}")
                st.session_state.data.at[row.Index, 'Label'] = label



            if st.button('Save Labels and Retrain BERT Model'):
                st.session_state.data = st.session_state.data
                # Extract sentences and user labels from the labeled data
                user_labels = [st.session_state.data.at[row.Index, 'Label'] for row in lines_to_label.itertuples()]
                sentences_to_train = lines_to_label['Text'].tolist()
                print('user_labels are: ', user_labels)
                # Train the st.session_state.model
                st.session_state.model.train_with_sentences(sentences_to_train, user_labels)

                if len(st.session_state.data) - st.session_state.current_line_index < st.session_state.num_lines:
                    st.session_state.num_lines = len(st.session_state.data) - st.session_state.current_line_index
                st.session_state.batch_sizes.append(st.session_state.num_lines)
                zp = list(zip(sentences_to_train, user_labels))
                st.session_state.datalog.extend(zp)

                # Calculate accuracy
                accuracy, st.session_state.num_lines = st.session_state.model.accuracy_batch_calculation(predicted_labels, user_labels, num_lines)
                st.session_state.accuracy_log.append(accuracy)  # Store the calculated accuracy
                
                # Now we want to show predictions for the next set of lines
                next_start_line = st.session_state.current_line_index + num_lines
                next_end_line = next_start_line + st.session_state.num_lines
                next_lines_to_label = st.session_state.data.iloc[next_start_line:next_end_line]

                # Make predictions for the next set of lines
                next_sentences_to_predict = next_lines_to_label['Text'].tolist()
                predicted_labels = st.session_state.model.label_list_sentences(next_sentences_to_predict)
                predicted_labels = [label[0] for label in predicted_labels]  # Assuming the output is a list of lists
                st.session_state.selectbox_value = predicted_labels
                print('after prediction, length of selectbox_value is: ', len(st.session_state.selectbox_value))
                
                # Display next batch of sentences and their predicted labels
                st.session_state.current_line_index = next_start_line
                st.session_state.start_line = next_start_line
                st.session_state.end_line = next_end_line
                # Show the accuracy to the user
                st.write(f"model accuracy: {accuracy:.2f}")
                st.rerun()

        plot_and_save_logs()  # Call the plotting function to display the graphs
        # Button to download the updated CSV with labels

        updated_csv = pd.DataFrame(st.session_state.datalog, columns=["Texts", "Label"]).to_csv(index=False).encode('utf-8')
        st.download_button("Download data as CSV", updated_csv, "updated_data.csv", "text/csv", key='download_csv')

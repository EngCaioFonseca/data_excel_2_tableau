import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

def process_file(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            
            # Select the rows to be pivoted
            dataset = df[28:]  # Rows starting from row 28
            
            # Read the first 25 rows of the Excel file (for the Run ID)
            df1 = pd.read_excel(uploaded_file, sheet_name=0, header=None, nrows=25)

            # Select the second column of the first 25 rows
            run_id_column = df1[1].tolist()
            run_id_column = run_id_column[1:]  # Remove the first element of the list

            # Rename the columns of the dataset
            dataset.columns = ['Time Stamp'] + run_id_column

            # Pivot the dataset
            dataset_melted = pd.melt(dataset, id_vars=["Time Stamp"], var_name="Probes", value_name="Temperature")

            return dataset_melted
        except Exception as e:
            st.error(f"An error occurred: {e}")
    return None

def visualize_data(dataset_melted):
    if dataset_melted is not None:
        try:
            # Convert "Time Stamp" to datetime for plotting
            dataset_melted["Time Stamp"] = pd.to_datetime(dataset_melted["Time Stamp"])

            # Create a plot
            fig, ax = plt.subplots(figsize=(10, 6))
            for probe in dataset_melted["Probes"].unique():
                probe_data = dataset_melted[dataset_melted["Probes"] == probe]
                ax.plot(probe_data["Time Stamp"], probe_data["Temperature"], label=probe)

            # Set plot title and labels
            ax.set_title("Temperature Probes vs Time Stamp")
            ax.set_xlabel("Time Stamp")
            ax.set_ylabel("Temperature")
            ax.legend(loc="upper right", bbox_to_anchor=(1.15, 1), title="Probes")
            plt.xticks(rotation=45)
            plt.grid()
            plt.tight_layout()

            st.pyplot(fig)

        except Exception as e:
            st.error(f"An error occurred during visualization: {e}")

st.title("Pivot Data Processor")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    dataset_melted = process_file(uploaded_file)
    if dataset_melted is not None:
        st.success("The dataset has been successfully pivoted and is ready to use in Tableau.")
        
        if st.button("Visualize the Data"):
            visualize_data(dataset_melted)
        
        csv = dataset_melted.to_csv(index=False)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name="pivoted_data.csv",
            mime="text/csv",
        )
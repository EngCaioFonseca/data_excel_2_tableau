# Pivot Data Processor
deployed: https://dataexcel2tableau.streamlit.app/
## Overview

The Pivot Data Processor is a Streamlit web application designed to process and visualize Excel data, particularly for temperature probe measurements. It allows users to upload Excel files, pivot the data, visualize temperature trends, and download the processed data as a CSV file.

## Features

- Excel file upload
- Automated data pivoting
- Interactive data visualization
- CSV file download of processed data

## Installation

To run this app locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pivot-data-processor.git
   cd pivot-data-processor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run gui_data_2_tableau.py
   ```

2. Open a web browser and go to `http://localhost:8501` (or the URL provided in the terminal).

3. Use the file uploader to select an Excel file for processing.

4. Once the file is processed, you can:
   - Visualize the data by clicking the "Visualize the Data" button
   - Download the processed data as a CSV file

## Input File Format

The app expects Excel files with a specific structure:
- The first 25 rows are reserved for metadata
- The actual data starts from row 28
- The second column of the first 25 rows contains the Run ID information

## Dependencies

- streamlit
- pandas
- matplotlib
- openpyxl

For a complete list of dependencies, see `requirements.txt`.

## Deployment

This app is designed to be easily deployed on Streamlit Cloud:

1. Fork this repository to your GitHub account.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with your GitHub account.
3. Create a new app, selecting this repository and the `gui_data_2_tableau.py` file.
4. Deploy the app.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

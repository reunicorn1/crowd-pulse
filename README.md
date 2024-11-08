# crowd-pulse

## Action Plan

For detailed information about the action plan, please refer to the [Action Plan Document](https://basalt-wineberry-274.notion.site/Action-Plan-12d42ba08c328089be49c7321914a9e9).

## Requirements

- Python 3.10

## Virtual Environment Setup

### Windows

To create a virtual environment and install the required dependencies on Windows, follow these steps:

1. Open Command Prompt.
2. Navigate to your project directory:
   ```bash
   cd /crowd-pulse
   ```
3. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
4. Activate the virtual environment:
   ```bash
   .\myenv\Scripts\activate
   ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### macOS

To create a virtual environment and install the required dependencies on macOS, follow these steps:

1. Open Terminal.
2. Navigate to your project directory:
   ```bash
   cd /crowd-pulse
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv myenv
   ```
4. Activate the virtual environment:
   ```bash
   source myenv/bin/activate
   ```
5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Data Preprocessing

The `data_cleaning.py` script is used to preprocess text data in a CSV file. It performs various text preprocessing steps such as expanding contractions, converting emojis to text, converting text to lowercase, removing special characters, removing stopwords, and lemmatizing text.

### Usage

To preprocess a CSV file using the `data_cleaning.py` script:

Run the `data_cleaning.py` script with the input and output file paths as arguments:

```bash
python data_cleaning.py {input_file} {output_file}
```

This command will read the data from `input_file`, preprocess the text data, and save the cleaned data to `output_file`.

#!/usr/bin/python3
"""
Merging all csv files created together
"""

import pandas as pd
from tqdm import tqdm
import glob

csv_files = glob.glob("data/bert/*.csv")

data_frames = []

for file in tqdm(csv_files, desc="Merging CSV files"):
    df = pd.read_csv(file)  # Read each CSV file
    data_frames.append(df)   # Append the data frame to the list

merged_df = pd.concat(data_frames, ignore_index=True)

merged_df.to_csv('merged_file.csv', index=False)

print("Merging complete. Saved to 'merged_file.csv'")

import kagglehub
import shutil 
from pathlib import Path 
import pandas as pd

#### LOAD DATASET #####

#path from kaggle
# path = kagglehub.dataset_download("nalisha/smartphone-usage-and-addiction-analysis-dataset")

# print("Path to dataset files:", path)

#####
project = Path("Phone_Usage_and_Addiction")
data_folder = project / "data"
# output_folder = project / "outputs"

input_csv = data_folder / "Smartphone_Usage_And_Addiction_Analysis_7500_Rows (1).csv"

# convert to a dataframe 
smartphone_df = pd.read_csv(input_csv)
# print(smartphone_df)

###### MAKING A VERSION OF THE DF W/O MISSING VALUES(CLEAN DF) ####

#check for missing values 
# print(smartphone_df.isna().sum()) # 819 missing values in addiction_level column

#dropping all missing values and trasnferring clean df to a new csv file 
smartphone_df_clean = smartphone_df.dropna()

# output_file_path = output_folder / "clean_csv_output.csv"
# smartphone_df_clean.to_csv(output_file_path, index=False)

#### CALCULATIONS FOR CLEAN DF ####
df_desc = smartphone_df_clean.describe()
print(df_desc)
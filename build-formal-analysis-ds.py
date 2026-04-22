from pathlib import Path
import pandas as pd
import json
from pathlib import Path

def list_files(directory_path):
    """
    List all files in a given directory.

    Parameters
    ----------
    directory_path : str
        Path to the directory.

    Returns
    -------
    list
        List of file names contained in the directory.
    """
    directory = Path(directory_path)

    if not directory.exists() or not directory.is_dir():
        raise ValueError(f"{directory_path} is not a valid directory")

    return [f.name for f in directory.iterdir() if f.is_file()]
def list_dataset_files(dataset_path="./dataset"):
    """
    Reads the dataset directory and returns the files contained in each
    policy folder under ./dataset/XX/

    Returns:
        dict: {folder_name: [file1, file2, ...]}
    """
    dataset_dir = Path(dataset_path)
    result = {}

    if not dataset_dir.exists():
        raise FileNotFoundError(f"Dataset directory not found: {dataset_dir}")

    for folder in sorted(dataset_dir.iterdir()):
        if folder.is_dir():
            files = [str(f)+"/"+f.name for f in folder.iterdir() if f.is_file()]
            result[folder.name] = files

    return result

def create_empty_dataframe(*columns):
    """
    Create an empty pandas DataFrame with the given column names.

    Parameters
    ----------
    *columns : str
        Column names to include in the dataframe.

    Returns
    -------
    pandas.DataFrame
    """
    return pd.DataFrame(columns=list(columns))

import pandas as pd

def add_row(df, row_values):
    """
    Add a new row to the dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to modify.
    row_values : list or tuple
        Values of the new row. Length must match the number of columns.

    Returns
    -------
    pandas.DataFrame
        The dataframe with the new row added.
    """
    df.loc[len(df)] = row_values
    return df

def read_file_to_string(file_path):
    """
    Reads the contents of a file and returns it as a string.

    Parameters
    ----------
    file_path : str
        Path to the file.

    Returns
    -------
    str
        The contents of the file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def get_uid_from_json_string(json_string):
    """
    Parse a JSON string and return the value of the 'uid' key.

    Parameters
    ----------
    json_string : str
        A string containing JSON data.

    Returns
    -------
    str
        The value associated with the 'uid' key.

    Raises
    ------
    KeyError
        If 'uid' is not present in the JSON.
    json.JSONDecodeError
        If the string is not valid JSON.
    """
    data = json.loads(json_string)
    return data["uid"]

def export_dataframe(df, csv_path, xls_path):
    """
    Export a pandas DataFrame to CSV and Excel formats.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame to export
    csv_path : str
        Path to the CSV output file
    xls_path : str
        Path to the Excel output file
    """
    # Export CSV
    df.to_csv(csv_path, index=False, encoding="utf-8")

    # Export Excel
    df.to_excel(xls_path, index=False)

    print(f"CSV written to: {csv_path}")
    print(f"Excel written to: {xls_path}")

'''
    MAIN 
'''
base_dir = "./dataset"
files = list_dataset_files(base_dir)
formal_analysis_df = create_empty_dataframe("Folder", "GlobalID","SoW","EvRequest","ODRL", "Output")
for folder, file_list in files.items():
    print(folder)
    odrl = read_file_to_string(base_dir+"/"+folder+"/odrl.jsonld")
    global_id = get_uid_from_json_string(odrl)
    
    new_dir = base_dir+"/"+folder+"/evaluation_requests"
    ev_requests = list_files(new_dir)
    ev_request_json = None
    sow_json = None
    out_json = None
    for ev_request in ev_requests:
        ev_request_dir = new_dir+"/"+ev_request
        ev_request_json = read_file_to_string(ev_request_dir)
        # SoW
        try:
            sow_die = base_dir+"/"+folder+"/sow/state"+ev_request[:len(ev_request)-2]
            sow_json = read_file_to_string(sow_die)
        except:
            print("No sow for: ", folder)
        # Output
        try:
            out_dir = base_dir+"/"+folder+"/expected_outcomes/"+ev_request[:len(ev_request)-2]+"ld"
            out_json = read_file_to_string(out_dir)
            print("done: ", out_dir, " size: ", len(out_json))
        except:
            print("No output for: ", folder)

        add_row(formal_analysis_df, [folder, global_id, sow_json, ev_request_json, odrl, out_json])
   

print(formal_analysis_df)

export_dataframe(formal_analysis_df,csv_path="evaluation-analysis.csv", xls_path="evaluation-analysis.xlsx")
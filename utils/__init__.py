import pandas as pd
import requests
from io import BytesIO


def get_id_and_title(metadata_title: str) -> tuple:
    """takes a metadata_title and returns meaningful ID and a better title

    Args:
        metadata_title (str): the metadata_title e.g. B_20_Zwischenspiel

    Returns:
        tuple: e.g. ("B_20", "Zwischenspiel" )
    """
    title = " ".join(metadata_title.split()[1:])
    doc_id = metadata_title.split()[0]
    return doc_id, title


def gsheet_to_df(sheet_id: str) -> pd.DataFrame:
    """downloads a gsheet and returns a pandas Dataframe

    Args:
        sheet_id (str): the gsheet id

    Returns:
        pd.DataFrame: the gsheet as Dataframe
    """
    GDRIVE_BASE_URL = "https://docs.google.com/spreadsheet/ccc?key="
    url = f"{GDRIVE_BASE_URL}{sheet_id}&output=csv"
    r = requests.get(url)
    print(r.status_code)
    data = r.content
    df = pd.read_csv(BytesIO(data))
    return df

from src.types.table_types import Fields
from src.config import SUBSET_FILENAME, WHOLE_TABLE_FILENAME

def save(df):
    df.to_csv(WHOLE_TABLE_FILENAME, ';', index=False)

def save_subset(df):
    copied = df.copy()
    copied = copied.drop(list(filter(lambda x: x not in [v.value for v in Fields], copied.columns)), axis=1)
    copied.to_csv(SUBSET_FILENAME, ';', index=False)

def save_both(df):
    save(df)
    save_subset(df)
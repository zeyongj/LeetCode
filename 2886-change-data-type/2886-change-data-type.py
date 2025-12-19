import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students)
    df['grade'] = df[['grade']].astype(int) # changing datatype to int.
    return df
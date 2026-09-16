from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


INPUT_PATH = Path("data/raw/california_housing.csv")
OUTPUT_DIR = Path("data/processed")


def remove_outliers(df):
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        df = df[(df[column] >= lower) & (df[column] <= upper)]

    return df


def main():
    df = pd.read_csv(INPUT_PATH)

    print(f"Original rows: {len(df)}")

    df = df.dropna()
    df = remove_outliers(df)

    train, test = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    train.to_csv(OUTPUT_DIR / "train.csv", index=False)
    test.to_csv(OUTPUT_DIR / "test.csv", index=False)

    print(f"Processed rows: {len(df)}")
    print(f"Train rows: {len(train)}")
    print(f"Test rows: {len(test)}")


if __name__ == "__main__":
    main()

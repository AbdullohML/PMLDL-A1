from pathlib import Path

from sklearn.datasets import fetch_california_housing

output_path = Path("data/raw/california_housing.csv")

data = fetch_california_housing(as_frame=True)
data.frame.to_csv(output_path, index=False)

print(f"Saved {len(data.frame)} rows to {output_path}")

import pandas as pd
from sklearn.datasets import make_classification

# Generate synthetic dataset
X, y = make_classification(n_samples=200, n_features=2, n_classes=2, 
                          n_informative=2, n_redundant=0, random_state=42)
df = pd.DataFrame(X, columns=["water_depth", "temp"])
df["target"] = y
df.to_csv("data.csv", index=False)
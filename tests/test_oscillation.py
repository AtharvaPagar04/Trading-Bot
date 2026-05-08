from src.validation.data_loader import load_csv_data
from src.validation.oscillation import (
    measure_oscillation_frequency,
)

df = load_csv_data(
    "data/raw/sample_sol.csv"
)

thresholds = [0.3, 0.5, 1.0]

for threshold in thresholds:
    result = measure_oscillation_frequency(
        df=df,
        threshold_pct=threshold,
    )

    print(result)
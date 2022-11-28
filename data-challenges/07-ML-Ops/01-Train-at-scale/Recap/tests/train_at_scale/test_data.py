from taxifare.ml_logic.data import clean_data


def test_clean_data(train_1k, train_1k_cleaned):
    df_cleaned = clean_data(train_1k)
    assert df_cleaned.shape == train_1k_cleaned.shape
    diff_means = df_cleaned['fare_amount'].mean() - train_1k_cleaned['fare_amount'].mean()
    assert round(diff_means, 3) == 0

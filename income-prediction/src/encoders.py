# encoders.py
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted
import pandas as pd

class FrequencyEncoder(BaseEstimator, TransformerMixin):
    """
    Encodes categorical columns by their frequency in the training data.
    Unseen categories during transform() are encoded as 0.
    """

    def __init__(self):
        self.freq_maps = None
        self.columns_ = None  # store fitted column names

    def fit(self, X, y=None):
        # Ensure X is DataFrame for consistent column handling
        X_df = pd.DataFrame(X) if not hasattr(X, "columns") else X
        self.columns_ = list(X_df.columns)

        # Create frequency maps for each column
        self.freq_maps = {
            col: X_df[col].value_counts(normalize=True).to_dict()
            for col in self.columns_
        }
        return self

    def transform(self, X):
        # Check if fitted before transforming
        check_is_fitted(self, ["freq_maps", "columns_"])

        # Ensure X is DataFrame
        X_df = pd.DataFrame(X, columns=self.columns_) if not hasattr(X, "columns") else X.copy()

        # Map categories to frequencies, unseen -> 0
        for col in self.columns_:
            X_df[col] = X_df[col].map(self.freq_maps[col]).fillna(0)

        return X_df if hasattr(X, "columns") else X_df.values
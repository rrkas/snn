from .base_transformer import BaseTransformer


class MinMaxScalar(BaseTransformer):
    """
    feature_range=(0, 1)
    Transform features by scaling each feature to a given range.

    The transformation is given by:
        X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
        X_scaled = X_std * (max - min) + min
    """

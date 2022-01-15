from .base_transformer import BaseTransformer


class StandardScalar(BaseTransformer):
    """
    Transforms data
    - mean = 0
    - standard deviation = 1
    """

class BaseTransformer:
    """
    Base of all transformers
    Defines the methods to be implemented
    All transformers MUST extend BaseTransformer
    """

    def fit(self):
        """
        just computes the parameters of transformer, like mean and standard deviation
        :return: None
        """
        raise NotImplementedError

    def transform(self):
        """
        apply the transformer like:
        - fill missing data/ remove columns
        - feature transformation
        :return: None
        """
        raise NotImplementedError

    def fit_transform(self):
        """
        fits
        transforms
        = fit() and then transform()
        :return: None
        """
        raise NotImplementedError

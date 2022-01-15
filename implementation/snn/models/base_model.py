class BaseModel:
    """
    Base model
    All models MUST extend BaseModel
    """

    def fit(self):
        """
        learns from the input data
        sets parameters and weights
        :return: None
        """
        raise NotImplementedError

    def predict(self):
        """

        :return: None
        """
        raise NotImplementedError

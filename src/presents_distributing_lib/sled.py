class Sled(object):
    """
    The sled to be filled with presents.
    """
    def __init__(self, max_capacity: int = 12):
        self.MAX_CAPACITY = max_capacity
        self.status = 'filling'
        self.presents_weights = []

    def get_remaining_capacity(self):
        """
        Return the weight that the sled can still handle
        :return: int, remaining capacity
        """
        return self.MAX_CAPACITY - sum(self.presents_weights)

    def can_add_present(self, present_weight: int):
        """
        Check if it's possible to add the present (while not exceeding the threshold)
        :param present_weight: int: the weight of the present to be added
        :return: bool, True if it's possible to add the present
        """
        return present_weight <= self.get_remaining_capacity()

    def add_present(self, present_weight: int):
        """
        Add a present to the sled
        :param present_weight: weight of the present to be added
        :return: None
        """
        self.presents_weights.append(present_weight)

    def is_empty(self):
        """
        Check whether the sled is empty
        :return: bool, True if the sled is empty
        """
        return len(self.presents_weights) == 0

    def remove_present(self):
        """
        Remove the first present from the sled
        :return: None
        """
        del self.presents_weights[0]

    def get_presents_weights(self):
        """
        Get the presents in the sled
        :return: List, list of the presents weights
        """
        return self.presents_weights

    def set_status(self, status):
        """
        Status setter
        :return: None
        """

        self.status = status

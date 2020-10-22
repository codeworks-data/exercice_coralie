class Sled(object):
    """
    Le traineau
    """
    def __init__(self, max_capacity=12):
        self.MAX_CAPACITY = max_capacity
        self.presents_weights = []

    def get_remaining_capacity(self):
        return self.MAX_CAPACITY-sum(self.presents_weights)

    def can_add_present(self, present_weight):
        return present_weight <= self.get_remaining_capacity()

    def add_present(self, present_weight):
        self.presents_weights.append(present_weight)

    def is_empty(self):
        return len(self.presents_weights) == 0

    def remove_present(self):
        del self.presents_weights[0]

    def get_presents_weights(self):
        return self.presents_weights

    def set_presents_weights(self, present_weights):
        self.presents_weights = present_weights

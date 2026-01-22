# Utility functions
"""
Utility functions for data handling and evaluation.
"""

def calculate_mae(predictions, targets):
    return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)


def calculate_mape(predictions, targets):
    return sum(abs((p - t) / t) for p, t in zip(predictions, targets)) / len(predictions)

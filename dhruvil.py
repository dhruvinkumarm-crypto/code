import numpy as np


def calculate(numbers):
    # Check if list contains exactly 9 elements
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # Reshape list into 3x3 Numpy array
    matrix = np.array(numbers).reshape(3, 3)

    # Build dictionary with required metrics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations
if __name__ == "__main__":
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))


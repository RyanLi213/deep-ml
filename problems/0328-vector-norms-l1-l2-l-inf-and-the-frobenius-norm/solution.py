import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    '''
    assumptions
    - input cannot be empty

    '''
    sum_int= 0
    arr_shape = arr.shape

    if norm_type == "l1":
        arr = arr.flatten()
        for i in range(len(arr)):
            sum_int += abs(arr[i])
        sum_int = float(sum_int)
    if norm_type == "l2":
        arr = arr.flatten()
        for i in range(len(arr)):
            sum_int += (arr[i])**2
        sum_int = np.sqrt(sum_int)
    if norm_type == "linf":
        arr = arr.flatten()
        for i in range(len(arr)):
            result = [np.abs(var) for var in arr]
            sum_int = np.max(result)
            sum_int = float(sum_int)
    if norm_type == "frobenius":
        for i in range(len(arr)):
            if arr.ndim == 2:
                sum_int = np.linalg.norm(arr, "fro")
            else:
                raise ValueError("need to be 1D")
                break
    return sum_int

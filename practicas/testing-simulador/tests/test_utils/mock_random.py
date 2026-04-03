"""
Mock random module for testing ESP-LEGO-SPIKE-Simulator.
Provides deterministic random number generation for reproducible tests.
"""

import math as _math

# Random state for reproducibility
_state = 1  # Initial seed


def seed(seed_value):
    """Initialize random number generator.

    Args:
        seed_value: Seed value for random generator
    """
    global _state
    _state = seed_value


def random():
    """Generate random float in range [0, 1).

    Returns:
        Random float between 0 and 1
    """
    global _state
    # Linear congruential generator
    _state = (_state * 1103515245 + 12345) & 0x7FFFFFFF
    return _state / 0x80000000


def randint(a, b):
    """Generate random integer in range [a, b].

    Args:
        a: Minimum value
        b: Maximum value

    Returns:
        Random integer
    """
    return a + int(random() * (b - a + 1))


def randrange(start, stop=None, step=1):
    """Generate random integer from range.

    Args:
        start: Start value (or stop if stop is None)
        stop: Stop value
        step: Step value

    Returns:
        Random integer
    """
    if stop is None:
        stop = start
        start = 0
    return start + step * int(random() * ((stop - start + step - 1) // step))


def choice(seq):
    """Choose random element from sequence.

    Args:
        seq: Sequence to choose from

    Returns:
        Random element
    """
    return seq[randint(0, len(seq) - 1)]


def shuffle(seq):
    """Shuffle sequence in place.

    Args:
        seq: Sequence to shuffle
    """
    for i in range(len(seq) - 1, 0, -1):
        j = randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]


def uniform(a, b):
    """Generate random float in range [a, b).

    Args:
        a: Minimum value
        b: Maximum value

    Returns:
        Random float
    """
    return a + random() * (b - a)


def sample(population, k):
    """Sample k unique elements from population.

    Args:
        population: Population to sample from
        k: Number of samples

    Returns:
        List of samples
    """
    result = list(population)
    shuffle(result)
    return result[:k]


def gauss(mu=0.0, sigma=1.0):
    """Generate random float from Gaussian distribution.

    Args:
        mu: Mean
        sigma: Standard deviation

    Returns:
        Random float from Gaussian distribution
    """
    # Box-Muller transform
    u1 = random()
    while u1 == 0:
        u1 = random()
    u2 = random()
    z = _math.sqrt(-2.0 * _math.log(u1)) * _math.cos(2.0 * _math.pi * u2)
    return mu + sigma * z


def expovariate(lambd):
    """Generate random float from exponential distribution.

    Args:
        lambd: Rate parameter

    Returns:
        Random float from exponential distribution
    """
    return -_math.log(random()) / lambd


def getstate():
    """Get random generator state.

    Returns:
        State tuple
    """
    return (_state,)


def setstate(state):
    """Set random generator state.

    Args:
        state: State tuple
    """
    global _state
    _state = state[0]


def triangular(low=0.0, high=1.0, mode=None):
    """Generate random float from triangular distribution.

    Args:
        low: Minimum value
        high: Maximum value
        mode: Mode (median)

    Returns:
        Random float from triangular distribution
    """
    if mode is None:
        mode = (low + high) / 2.0
    u = random()
    c = (mode - low) / (high - low)
    if u < c:
        return low + _math.sqrt(u * (high - low) * (mode - low))
    else:
        return high - _math.sqrt((1 - u) * (high - low) * (high - mode))

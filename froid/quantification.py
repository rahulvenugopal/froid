"""
Functions to quantify dreams based on established and novel measures (e.g., Hall and Van de Castle)
"""

__all__ = [
    "dreaminess",
]

def hvdc(report, category=None):
    """Automated Hall and Van de Castle scores.
    """
    raise NotImplementedError

def lucidity(report):
    """Return a continuous confidence value for lucidity.

    Based on model we will have to develop.
    """
    raise NotImplementedError

def common_themes(report):
    """Return a continuous confidence value for presence of common dream themes.
    Based on model we will have to develop.
    """
    raise NotImplementedError

def meaning_extraction(report):
    """Return dream-based meaning.

    Based on a model (semantic space) we will have to develop, based on dream reports (SDDb).
    """
    raise NotImplementedError

def speechgraph(report):
    """Return a variety of graph metrics.
    
    Validate against Java program.
    Reference the value of speech graphs in dream studies.
    """
    raise NotImplementedError

def dreaminess(text, **kwargs):
    """Return confidence that ``text`` is a dream report.

    Parameters
    ----------
    text : str
        Any text.

    Returns
    -------
    conf : float
        Confidence level (0, 1) that ``text`` is a dream.

    Examples
    --------
    >>> print(froid.is_dream("I went to the store."))
    0.0
    >>> print(froid.is_dream("I dreamt I went to the store."))
    1.0
    >>> print(froid.is_dream("I went to the store while I was sleeping."))
    0.2

    >>> # Increasingly bizarre events.
    >>> print(froid.is_dream("I'm playing scrabble while drinking coffee."))
    >>> print(froid.is_dream("I'm playing scrabble while drinking a lamp."))
    0.0
    0.2

    >>> # Increasingly rare animals.
    >>> animals = ["squirrel", "snake", "unicorn"]
    >>> for anim in animals:
    >>>     dream = f"I saw a {anim}"
    >>>     dreaminess = froid.is_dream(dream)
    >>>     print(dream, dreaminess)
    I saw a squirrel - 0.0
    I saw a snake - 0.2
    I saw a unicorn - 0.5
    """
    prompt = (
        "How confident (0-1) are you that text includes a dream?"
        f"\n\nText: {text}"
        "Confidence:"
    )
    response = openai_completion(prompt, **kwargs)
    text = response.choices[0].text.strip()
    return float(text)

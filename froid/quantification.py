"""
Functions to quantify dreams based on established and novel measures (e.g., Hall and Van de Castle)
"""

__all__ = [
    "dreaminess",
    "speechgraph",
]

def hvdc(report, category=None):
    """Automated Hall and Van de Castle scores."""
    raise NotImplementedError

def lucidity(report):
    """Return a continuous confidence value for lucidity."""
    raise NotImplementedError

def common_themes(report):
    """Return a continuous confidence value for presence of common dream themes."""
    raise NotImplementedError

def meaning_extraction(report):
    """Return dream-based meaning."""
    raise NotImplementedError

def dreaminess(text, **kwargs):
    """Return confidence that ``text`` is a dream report.

    Parameters
    ----------
    text : str
        Any text.
    kwargs : key, value pairs
        Additional keyword arguments are passed to :py:class:`froid.utils.openai_completion`.

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
    assert isinstance(text, str), "`text` must be a string"
    prompt = (
        "How confident (0-1) are you that text includes a dream?"
        f"\n\nText: {text}"
        "Confidence:"
    )
    response = openai_completion(prompt, **kwargs)
    text = response.choices[0].text.strip()
    return float(text)


def speechgraph(report):
    """Return a variety of graph metrics.

    Graph measures of speech are thought to be especially meaningful when applied to dream
    reports [Martin2020]_ [Mota2014]_.

    Parameters
    ----------
    report : str
        A dream report.

    Returns
    -------

    References
    ----------
    .. [Martin2020] Martin, J. M., Andriano, D. W., Mota, N. B., Mota-Rolim, S. A., Araújo, J. F.,
                    Solms, M., & Ribeiro, S. (2020). Structural differences between REM and non-REM
                    dream reports assessed by graph analysis. PloS one, 15(7), e0228903.
                    https://doi.org/10.1371/journal.pone.0228903
    .. [Mota2014] Mota, N. B., Furtado, R., Maia, P. P., Copelli, M., & Ribeiro, S. (2014).
                  Graph analysis of dream reports is especially informative about psychosis.
                  Scientific reports, 4(1), 3691. https://doi.org/10.1038/srep03691

    Examples
    --------

    """
    assert isinstance(report, str), "`report` must be a string"
    raise NotImplementedError

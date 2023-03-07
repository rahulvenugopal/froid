"""Functions to provide historical dream interpretations."""
from .utils import openai_completion


__all__ = [
    "interpret",
]


def interpret(report, context="freud", **kwargs):
    """Interpret a dream.

    Parameters
    ----------
    report : str
        A dream report.
    context : str
        The dream interpretation context.

        .. note:: Only `freud` is currently implemented.

    Returns
    -------
    interpretation : str
        The interpretation of a dream.

    Examples
    --------
    >>> interpretation = froid.interpret(dream)
    >>> print(interpretation)
    If a person dreamed of being chased by a giant, Freud would interpret this dream as a
    manifestation of the person's fear of being overwhelmed by their own emotions. The giant in the
    dream could represent the person's own inner turmoil, which they are trying to escape from.
    Freud would suggest that the dreamer needs to confront their own emotions and learn to accept
    them in order to move forward in life.


    Notes
    -----
    Dream interpretations are generated for academic purposes only.
    """
    valid_contexts = ["freud"]
    assert isinstance(report, str), "`report` must be a string"
    assert isinstance(context, str), "`context` must be a string"
    assert context in valid_contexts, f"`context` must be one of {valid_contexts}"
    if context == "freud":
        context = "Sigmund Freud"
    prompt = (
        f"Interpret a Dream the way that {context} would.\n\n",
        "Dream: {report}\n",
        "Interpretation:",
    )
    response = openai_completion(prompt=prompt, **kwargs)
    return response.choices[0].text.strip()

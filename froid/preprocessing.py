"""Functions to preprocess dream reports (e.g., transcribing and isolating dream content)."""
import pathlib
import os

from .utils import is_installed, openai_audio, openai_completion, openai_edit


__all__ = [
    "anonymize",
    "extract",
    "transcribe",
    "translate",
]


def anonymize(report, known_entities=None):
    """Anonymize a dream report using Named Entity Recognition.

    Parameters
    ----------
    report : str
        A dream report.
    known_entities : list or None        
        An optional sequence of strings that will be included as names.

    Returns
    -------
    anon_report : str
        The same ``report`` but with all names replaced.

    Examples
    --------
    >>> froid.anonymize("I was dreaming about my dad, Jim Jones, and all his friends.")
    I was dreaming about my dad, PERSON, and all his friends.
    """
    assert isinstance(report, str), "`report` must be a string"
    assert isinstance(known_entities, (type(None), list, tuple, set)), "`known_entities` must be None or a sequence"
    if known_entities is not None:
        assert all(isinstance(e, str) for e in known_entities)
    raise NotImplementedError

def extract(report, method="openai", **kwargs):
    """Extract the essential dream content of a dream report.

    .. warning::
        The only current implementation of this model requires an OpenAI API key and involves
        cloud processing.

    Parameters
    ----------
    report : str
        A dream report.

        .. important:: This will NOT work well on random text. It must be a dream report.

    method : str
        Name of the method used to extract dream content.
    kwargs : dict
        Additional key, value pairs are passed to the model (itself dependent on ``method``).

        .. important::
            If `method='openai'`, results will be non-deterministic.
            See the `'temperature'` keyword argument to influence determinism.

    Returns
    -------
    dream : str
        The dream content from a dream report, reported in present tense.

    Examples
    --------
    >>> import froid
    >>>
    >>> dream_report = (
    >>>     "Actually forgot to journal and the day was chaotic, also went to sleep at 3.40am and "
    >>>     "woke up 2 hours later, so only remember now being lucid and eating something, "
    >>>     "scrambled eggs if memory serves before flying towards a mountain."
    >>> )
    >>>
    >>> dream = froid.extract(dream_report)
    >>> print(dream)
    Lucid dreaming, eating scrambled eggs, flying towards a mountain.
    """
    valid_methods = ["openai"]
    assert isinstance(report, str), "`report` must be a string"
    assert isinstance(method, str), "`method` must be a string"
    assert method in valid_methods, f"`method` must be one of {valid_methods}"
    if method == "openai":
        # Generate the full text completion prompt for OpenAI and run the model.
        # https://platform.openai.com/docs/guides/completion/prompt-design
        prompt = f"Extract the content from a Dream.\n\nDream: {report}\nContent:"
        # Extract and return the generated text.
        # assert model_kwargs.get("n") == 1, "Only the first text is indexed."
        response = openai_completion(prompt, **kwargs)
        text = response.choices[0].text
        return text.strip()  # Remove the inevitable leading space

def transcribe(filepath, method="openai", translate=False, **kwargs):
    """Transcribe a recorded dream report to text.

    Use OpenAI or Google Cloud services.
    OpenAI can convert non-english

    Parameters
    ----------
    audio : path
        Filepath to an audio file.
    method : str
        Method used to transcribe (and possible translate) audio.
    translate : bool
        Only valid if ``method='openai'``. If True, non-english audio is converted to english text.

    Returns
    -------
    report : str
        A dream report.

    Examples
    --------
    >>> import froid
    >>> report = froid.transcribe("./Desktop/sub-005.wav")
    >>> print(report)
    I remember, uh, um, it's hard to remember. I was driving in the wrong lane when...

    Notes
    -----
    Requires authorization.
    """
    valid_methods = ["openai"]
    assert isinstance(filepath, (str, pathlib.Path)), "`filepath` must be a string or Path"
    assert isinstance(method, str), "`method` must be a string"
    assert method in valid_methods, f"`method` must be one of {valid_methods}"
    if method == "openai":
        response = openai_audio(filepath, translate, **kwargs)
        text = response.text
        return text

def translate(report, method="openai", **kwargs):
    """Return a dream report in a new language.

    Parameters
    ----------
    report : str
        A dream report.
    input_lang : str
        The language (ISO code) of the input ``report``.
    output_lang : str
        The desired language (ISO code) of the output.
    method : str
        Method used to translate the text.

    Returns
    -------
    trans_report : str
        A translated dream report.
    """
    valid_methods = ["openai"]
    assert isinstance(report, str), "`report` must be a string"
    assert isinstance(method, str), "`method` must be a string"
    assert method in valid_methods, f"`method` must be one of {valid_methods}"
    if method == "openai":
        instruction = f"Translate from {input_lang} to {output_lang}."
        response = openai_edit(report, instruction, **kwargs)
        text = response.choices[0].text
        return text.strip()  # Remove the inevitable leading space
    return NotImplementedError

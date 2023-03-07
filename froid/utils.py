"""Helper functions."""
import importlib.util
import pathlib

def is_installed(package):
    """Check whether a package is installed or not.

    Parameters
    ----------
    package : str
        Name of Python package.

    Returns
    -------
    installed : bool
        True if package is installed, otherwise False.
    """
    assert isinstance(package, str), "`package` must be a string"
    return importlib.util.find_spec(package) is not None

def openai_audio(filepath, translate=False, **kwargs):
    """Transcribe (and optionally translate) audio using OpenAI.

    Parameters
    ----------
    filepath : str or :py:class:`pathlib.Path`
        A filepath to an audio file.
    translate : bool
        If True, a non-english input file is translated to english.

        .. note::
            This is separate from the valid ``language`` keyword argument, which should be included
            (a valid ISO 639-1 country code) if the original file should stay non-english.

    Returns
    -------
    response : :py:class:`openai.openai_object.OpenAIObject`
        Specific format depends on ``"response_format"``, a valid ``kwarg``.
    """
    assert isinstance(filepath, (str, pathlib.Path)), "`filepath` must be a string or Path"
    assert isinstance(translate, bool), "`translate` must be True or False"
    assert is_installed("openai"), "openai must be installed to use OpenAI Transcription service"
    import openai
    model_kwargs = {
        "model": "whisper-1",
        "response_format": "json",
        "temperature": 0,
    } | kwargs
    # TODO: Add "prompting" to transcriptions.
    with open(filepath, "rb") as audio_file:
        if translate:
            response = openai.Audio.translate(file=audio_file, **model_kwargs)
        else:
            response = openai.Audio.transcribe(file=audio_file, **model_kwargs)
    return response

def openai_completion(prompt, **kwargs):
    """Get a text response from OpenAI.

    Parameters
    ----------
    prompt : str
        Text prompt.
    kwargs : dict
        Additional key, value pairs are passed to the model (itself dependent on ``method``).

    Returns
    -------
    response : OpenAIType
    """
    assert is_installed("openai"), "openai must be installed to use OpenAI Completion service"
    import openai
    model_kwargs = {
        "model": "text-davinci-003",
        "n": 1,
        "temperature": 0.2,
        "max_tokens": 256,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    } | kwargs
    response = openai.Completion.create(prompt=prompt, **model_kwargs)
    return response

def openai_edit(text, instruction, **kwargs):
    """Edit text with OpenAI.

    Parameters
    ----------
    text : str
        Text input.
    instruction : str
        Tell the model what kind of edits to make to ``text``.
    **kwargs : dict
        Additional key, value pairs are passed to the model (itself dependent on ``method``).

    Returns
    -------
    response : OpenAIType
    """
    assert is_installed("openai"), "openai must be installed to use OpenAI Completion service"
    import openai
    model_kwargs = {
        "model": "text-davinci-edit-001",
        "n": 1,
        "temperature": 1,
        "top_p": 1,
    } | kwargs
    response = openai.Edit.create(input=text, instruction=instruction, **model_kwargs)
    return response

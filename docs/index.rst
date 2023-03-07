
.. currentmodule:: froid

froid: dream analysis in Python
===============================

``froid`` is a Python library for analyzing dream reports. It's main modules include:


.. autosummary::
   :toctree: _autosummary

   preprocessing
   quantification
   interpretation

.. * Preprocessing dream reports (e.g., transcribing and extracting)
.. * Interpreting dreams based on various contexts
.. * Transcribing dream reports
.. * Quantifying dreams based on established and novel measures (e.g., Hall and Van de Castle)
.. * Visualizing results from dream analysis


Installation
------------

To install ``froid``, simply open a terminal or Anaconda command prompt and enter:

.. code-block:: shell

    pip install --upgrade froid


Getting started
---------------

.. code-block:: python

    import froid

    # Generate a short dream report to play with.
    dream_report = (
        "Actually forgot to journal and the day was chaotic, also went to sleep at 3.40am and "
        "woke up 2 hours later, so only remember now being lucid and eating something, "
        "scrambled eggs if memory serves before flying towards a mountain."
    )

    # Extract/isolate the actual dream content from the full dream.
    dream = froid.extract(dream_report)
    print(dream)
    # Lucid dreaming, eating scrambled eggs, flying towards a mountain.

    # Interpret the dream.
    interpretation = froid.interpret(dream)
    print(interpretation)
    # If a person dreamed of being chased by a giant, Freud would interpret this dream as a
    # manifestation of the person's fear of being overwhelmed by their own emotions. The giant in the
    # dream could represent the person's own inner turmoil, which they are trying to escape from.
    # Freud would suggest that the dreamer needs to confront their own emotions and learn to accept
    # them in order to move forward in life.

import logging

from .interpretation import *
from .preprocessing import *
from .quantification import *
from .visualization import *

# Define froid logging style.
logging.basicConfig(format="%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%b-%d %H:%M:%S")

__author__  = "Remington Mallett <mallett.remy@gmail.com>"
__version__ = "0.0.0"

def preach():
    """Preach
    """
    # import openai
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     max_tokens=256,
    #     prompt="Give me an excerpt from Sigmund Freud's book, The Interpretation of Dreams.",
    # )
    from .utils import openai_completion
    prompt = "Give me an excerpt from Sigmund Freud's book, The Interpretation of Dreams."
    print(openai_completion(prompt).choices[0].text.strip())

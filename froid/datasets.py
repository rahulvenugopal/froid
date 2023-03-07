"""
Access publicly available dream report datasets.
"""

__all__ = [
    "fetch_hvdc",
    "fetch_sddb",
    "fetch_reddit",
]

def filter_rdreams(post):
    """Filter out non-dream r/Dreams posts based on flair.

    .. seealso:: froid.scrape_reddit
    """
    raise NotImplementedError

def fetch_hvdc():
    raise NotImplementedError

def fetch_sddb():
    raise NotImplementedError

def fetch_reddit():
    raise NotImplementedError

def scrape_rdreams():
    raise NotImplementedError

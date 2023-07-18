import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desription = f.read()

__version__ = '0.0.0'
REPO_NAME = "NLP-Text-Summarizer"
AUTHOR = "Wael"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "alqaini32@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author= AUTHOR,
    author_email=AUTHOR_EMAIL,
    description= "a small python package for nlp app",
    long_description=long_desription,
    long_desription_content = "text/markdown",
    url="https://github.com/alqaini/NLP-Text-Summarizer",
    project_url = "https://github.com/alqaini?tab=repositories"
)

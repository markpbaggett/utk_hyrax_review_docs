from setuptools import setup, find_packages

with open("README.md", "r") as read_me:
    long_description = read_me.read()


setup(
    name="UT Libraries Hyrax Investigation Documentation",
    description="a documentation generator for describing UT Libraries' investigation of Hyrax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    author="Mark Baggett",
    author_email="mbagget1@utk.edu",
    maintainer_email="mbagget1@utk.edu",
    url="https://github.com/markpbaggett/utk_hyrax_review_docs",
    packages=find_packages(),
    extras_require={
        "docs": [
            "sphinx >= 3.0.1",
            "sphinxcontrib-napoleon >= 0.7",
            "sphinx-markdown-tables >= 0.0.9",
            "recommonmark >=0.5.0",
            "sphinx-bootstrap-theme >= 0.6.5",
            "sphinxemoji >= 0.1.6",
            "sphinx-bernard-theme >= 0.1.12",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords=["libraries", "metadata", "digital repositories"],
)
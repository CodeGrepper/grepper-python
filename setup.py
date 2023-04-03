import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "grepper-python",
    "version": "0.0.1a",
    "author": "CodedGrepper",
    "author_email": "support@grepper.com",
    "description": "An API wrapper for the Grepper API.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/CodeGrepper/grepper-python",
    "packages": setuptools.find_packages(),
    "install_requires": ["requests", "urllib3"],
    "classifiers": [
        "Programming Language :: Python :: 3",
    ],
    "python_requires": '>=3.7'
}


setuptools.setup(**setup_info)
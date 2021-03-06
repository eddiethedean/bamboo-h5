import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bamboo-h5",
    version="0.0.1",
    description="Persistent Pandas api package with hdf5 DataFrame storage.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/eddiethedean/bamboo-h5",
    author="Odos Matthews",
    author_email="odosmatthews@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["bamboo-h5"],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "bamboo-h5=bamboo-h5.__main__:main",
        ]
    },
)
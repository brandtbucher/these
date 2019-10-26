import setuptools


with open("README.md") as readme:
    long_description = readme.read()


setuptools.setup(
    author="Brandt Bucher",
    author_email="brandtbucher@gmail.com",
    description="The Markov Zenerator.",
    keywords="Markov Zen this",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="these",
    py_modules=['these'],
    url="https://github.com/brandtbucher/these",
    version=1,
)

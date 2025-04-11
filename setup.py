import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="real_dataclasses",
    version="0.2",
    description="Real Dataclasses for the a-real OSINT toolset",
    long_description=long_description,
    install_requires=[],
    long_description_content_type="text/markdown",
    url="https://github.com/a-real-osint/real_dataclassses",
    packages=["real_dataclasses"])

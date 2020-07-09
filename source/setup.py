import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="panpy", # Replace with your own username
    version="0.0.1",
    author="Duchao Lv",
    author_email="duchaolv@gmail.com",
    description="a SDK for Pandat applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewlyu/panpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

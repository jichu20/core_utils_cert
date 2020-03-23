import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="core_utils_cert-jichu20",
    version="0.1.1",
    author="Borja Sánchez",
    author_email="jichu20@gmail.com",
    description="manager jks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jichu20/core_utils_cert",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

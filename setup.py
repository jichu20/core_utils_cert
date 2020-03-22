from setuptools import setup

setup(
    name="core_utils_cert",
    version="0.1.0",
    author="Borja Sánchez Yuste",
    author_email="jichu20@gmail.com",
    packages=["core", "core.crypto"],
    description="Proeycto core de utilidades para la gestión de certificados.",
    long_description=open("README.md").read(),
    install_requires=["six >= 1.10.0"],
)

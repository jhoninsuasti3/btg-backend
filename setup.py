from setuptools import setup

"""
This is a shared_package setup.py script to be used by all modules/functions.
"""
setup(
    name="shared_package",
    packages=[
        "shared_package",
        "shared_package.domain",
        "shared_package.domain.funds",
        "shared_package.domain.transactions",
        "shared_package.domain.users",
    ],
    description="Shared package",
    version="1.0.0",
    author="BTG",
    author_email="jhoninsua-03@hotmail.com",
    keywords=["pip", "shared_package"],
)

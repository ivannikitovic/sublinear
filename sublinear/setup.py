from setuptools import setup, find_packages

setup(
    name="Sublinear",
    version="0.1.0",
    description="Implementation of Count-Min Sketch using Pyhon.",
    author="Ivan Nikitovic",
    author_email="ivan.bnikitovic@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        # Add your project's dependencies here
    ],
)

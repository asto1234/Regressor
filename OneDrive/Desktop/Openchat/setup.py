#!/usr/bin/env python
"""Setup configuration for OpenChat package."""

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="openchat",
    version="1.0.0",
    author="OpenChat Team",
    author_email="test@gmail.com",
    description="End-to-end encrypted chat application with NLP summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openchat/openchat",
    project_urls={
        "Documentation": "https://openchat.readthedocs.io",
        "Source Code": "https://github.com/openchat/openchat",
        "Bug Reports": "https://github.com/openchat/openchat/issues",
    },
    packages=find_packages(exclude=["tests", "benchmarks", "docs", "examples"]),
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.4.0",
            "ruff>=0.0.280",
        ],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.2.0",
            "sphinx-autodoc-typehints>=1.23.0",
        ],
        "kubernetes": [
            "kubernetes>=27.2.0",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Chat",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="chat encryption e2e nlp kubernetes cryptography",
    entry_points={
        "console_scripts": [
            "openchat=openchat.app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

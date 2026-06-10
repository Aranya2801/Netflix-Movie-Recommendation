from setuptools import setup, find_packages

setup(
    name="netflix-movie-recommendation",
    version="2.0.0",
    author="Aranya2801",
    description="Advanced Hybrid Netflix Movie Recommendation System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aranya2801/Netflix-Movie-Recommendation",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.26",
        "pandas>=2.2",
        "scikit-learn>=1.4",
        "scipy>=1.13",
        "fastapi>=0.111",
        "uvicorn[standard]>=0.30",
        "streamlit>=1.35",
        "plotly>=5.22",
        "joblib>=1.4",
        "loguru>=0.7",
        "pydantic>=2.7",
        "requests>=2.32",
        "python-dotenv>=1.0",
    ],
    extras_require={
        "deep": ["torch>=2.3", "sentence-transformers>=3.0"],
        "dev": ["pytest>=8.2", "pytest-cov>=5.0", "black", "isort", "flake8"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

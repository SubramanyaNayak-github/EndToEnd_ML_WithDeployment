import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.1"

REPO_NAME = "EndToEnd_ML_WithDeployment"
AUTHOR_USER_NAME = "SubramanyaNayak-githiub"
SRC_REPO = "ml"
AUTHOR_EMAIL = "subramanayanayak3@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=("Consignment Pricing Prediction"),
    long_description=long_description,
    #long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: MIT License",
    ]
    )


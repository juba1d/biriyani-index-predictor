from setuptools import setup, find_packages

setup(
    name="biryani_index",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # kacchi requirements
    install_requires=[
        "skforecast",
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib"
    ],
    author="Sharif Jubaid Redwan Rusho", # user info
    description="biryani price prediction tool", # geeky stuff
)
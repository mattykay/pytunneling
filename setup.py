import pytunneling
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = ['sshtunnel>=0.1.5', 'docopt>=0.6.2']
test_requirements = [
    'pytest-mock', 'pytest>=5.0.1'
]

setup(
    name="pytunneling",
    version=pytunneling.__version__,
    author=pytunneling.__author__,
    author_email=pytunneling.__email__,
    description="Python module that allows multi-hop SSH tunneling/port-forwarding",
    License="MIT",
    keywords=["ssh", "tunneling", "networking"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattykay/pytunneling",
    packages=["pytunneling"],
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    tests_require=test_requirements,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: System :: Networking",
    ],
)

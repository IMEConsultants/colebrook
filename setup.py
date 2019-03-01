import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colebrook",
    version="0.0.5",
    author="Rob Markoski",
    author_email="software@imeconsultants.com.au",
    description="A small module that calculate colebrook-white approximations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IMEConsultants/colebrook/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
)
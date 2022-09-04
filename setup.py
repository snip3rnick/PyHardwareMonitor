import os
from setuptools import setup, find_packages

os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name="PyHardwareMonitor",
    version="1.0.1",
    author="Nicholas Feix",
    author_email="nf@fconsoft.com",
    description="Python import layer for the LibreHardwareMonitorLib assembly.",
    url='git@github.com:snip3rnick/PyHardwareMonitor.git',
    license="BSD",
    classifiers=[
        "License :: Other/Proprietary License",
    ],

    install_requires=["pythonnet"],
    packages=find_packages(),

    include_package_data=True,
    package_data={"": [
        "lib/*.dll",
        "**/*.pyi",
    ]},
)

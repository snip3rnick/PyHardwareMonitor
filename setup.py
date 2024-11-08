import os
from setuptools import setup, find_packages

os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name="HardwareMonitor",
    version="1.0.0",
    author="Nicholas Feix",
    author_email="nf@fconsoft.com",
    description="Python import layer for the LibreHardwareMonitorLib assembly.",
    url='git@github.com:snip3rnick/PyHardwareMonitor.git',
    license="BSD",
    classifiers=[
        "License :: Other/Proprietary License",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows",
    ],

    install_requires=["pythonnet"],
    packages=find_packages(),

    include_package_data=True,
    package_data={"": [
        "lib/*.dll",
        "lib/LICENSE",
        "**/*.pyi",
    ]},
)

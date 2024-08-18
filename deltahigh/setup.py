from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="deltahigh",
    version="0.18.08",
    author="João Pedro de Araújo Duarte",
    description="Funções, módulos e outras dependências utilizdaas pela equipe @dronedeltahigh ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["deltahigh"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=["matplotlib>=3.8.4",
                    "MAVProxy>=1.8.70",
                    "mediapipe>=0.10.14",
                    "numpy>=1.26.4",
                    "opencv-contrib-python>=4.9.0.80",
                    "opencv-python>=4.10.0.84",
                    "pymavlink>=2.4.41",
                    "pyzbar>=0.1.9",
                    "tensorflow>=2.16.1",
                    ],
    dependency_links=['https://github.com/Delta-High-Team/cbr-2024']
)
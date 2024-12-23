from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess
import os

class CustomBuildCommand(build_py):
    def run(self):
        # Call the build script to compile the shared library
        build_script = os.path.abspath("build.py")
        print(f"Running build script: {build_script}")
        subprocess.check_call(["python", build_script])
        super().run()

setup(
    name="Sudoku",
    version="1.0.0",
    description="A comprehensive Sudoku application with puzzle generation, validation, solving (via C++), and an interactive GUI built with Pygame.",
    author="Arghya Ranjan Das",
    url="https://github.com/ArghyaDas112358/Sudoku",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    cmdclass={
        "build_py": CustomBuildCommand,
    },
    install_requires=[
        "pygame",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

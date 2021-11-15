from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='FETracker',
    version='1.0.0',
    description='Automatically tracks progress in Final Fantasy 4 Free Enterprise',
    author='Edward Parry',
    author_email='edward@eparry.uk',
    url='https://github.com/EchoDel/FETracker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['emulator_interaction', 'tracker'],
    install_requires=['bizhook'],
    tests_require=['pytest', 'pytest-runner', 'flake8<4', 'pytest-flake8', 'pytest-html', 'pytest-cov'],
    license='GNU General Public License v3.0',
    platforms='any',
)

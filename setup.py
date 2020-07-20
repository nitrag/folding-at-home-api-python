import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

setup(
    name='folding_at_home',
    version='1.2.0',
    description='API and console tool which wraps Folding@Home Client API for Pause/Restart/Power commands',
    long_description=README,
    long_description_content_type='text/markdown',
    keywords='folding folding@home foldingathome',
    url='https://github.com/nitrag/folding-at-home-api-python',
    author='Ryan Gartin',
    author_email='ryan@eagledevelopers.net',
    license='MIT',
    install_requires=[
      'argparse',
      'requests'
    ],
    entry_points={
      'console_scripts': [
          'folding-at-home = folding_at_home.main:main'
      ]
    },
    python_requires='>=3.6')

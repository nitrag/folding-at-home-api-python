from setuptools import setup

setup(name='folding_at_home',
      version='1.0.0',
      description='Console application (python) to which wraps Folding@Home API for Pause/Restart/Power commands',
      keywords='folding folding@home foldingathome api',
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
      zip_safe=False)

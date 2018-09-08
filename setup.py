
import sys

from setuptools import setup, find_packages
from os.path import join, dirname

if not sys.version_info[0] == 3 and sys.version_info[0] == 6:
    sys.exit("Sorry, need Python >= 3.6")

setup(
    name='IZORM',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://github.com/Avderevo/IZORM',
    description='Simple SQLite orm for Python',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='orm sqlite',
    author='Yury Avdeev',
    author_email='avdevman@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    zip_safe=False
)
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='IZORM',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Avderevo/IZORM',
    description='Simple SQLite orm for Python',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5.2',
    ],
    keywords='orm sqlite',
    author='Yury Avdeev',
    author_email='avdevman@gmail.com',
    license='MIT',
    python_requires='>=3.5.2',
    zip_safe=False
)

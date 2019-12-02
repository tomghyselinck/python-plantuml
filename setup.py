from setuptools import setup

with open('README.md', 'r') as fh:
    long_desc = fh.read()

from plantuml import __author__, __version_string__, __email__

requirements=[
    'httplib2',
    'six',
]

setup(
    name='plantuml',
    version=__version_string__,
    description='',
    long_description=long_desc,
    url='https://github.com/dougn/python-plantuml/',
    author=__author__,
    author_email=__email__,
    license='BSD',
    py_modules=['plantuml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    setup_requires=requirements,
    install_requires=requirements,
    keywords=[
        'plantuml',
        'uml',
    ],
)

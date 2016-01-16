from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pdfbooktool',
    version='0.1',
    description='Tool for formatting A6 PDFs into A4 ready for printing A6 books.',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Printing',
        'Topic :: Utilities'
    ],
    url='https://github.com/morngrar/pdfbooktool',
    author='Svein-Kåre Bjørnsen',
    author_email='sveinkare@gmail.com',
    license='GPL',
    packages=['pdfbooktool'],
    install_requires=[
        'PyPDF2',
    ],
    scripts=[
        'bin/booktool'
    ],
    zip_safe=False
)

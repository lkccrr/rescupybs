from setuptools import setup, find_packages
from rescupybs import __version__

setup(
    name='rescupybs',
    version=__version__,
    author='kan',
    author_email='luo_kan+pypi@outlook.com',
    python_requires='>=3.8',
    license='MIT',
    license_files=('LICENSE'),
    platforms=['Unix', 'Windows'],
    keywords='DFT rescuplus band plot wavefunction',
    description='Band structure plot and wavefunction export from rescuplus *.json and *.h5 file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lkccrr/rescupybs',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    install_requires=[
        'numpy>=1.22.0',
        'matplotlib>=3.4.0',
        'pint>=0.10'
    ],
    entry_points={
        'console_scripts': ['rescubs=rescupybs.wrapper:main',
                            'rescuiso=rescupybs.wrapper:surface']
    },
    packages=find_packages(),
    include_package_data=True
)


"""
┌┬┐┌─┐┌┬┐┌─┐┌─┐┬─┐┌─┐┬    ┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─┌─┐  ╔═╗╔╦╗╔═╗
 │ ├┤ │││├─┘│ │├┬┘├─┤│    │││├┤  │ ││││ │├┬┘├┴┐└─┐  ║ ║ ║║║╣
 ┴ └─┘┴ ┴┴  └─┘┴└─┴ ┴┴─┘  ┘└┘└─┘ ┴ └┴┘└─┘┴└─┴ ┴└─┘  ╚═╝═╩╝╚═╝

Integration of ordinary differential equations on temporally changing networks.
"""


from setuptools import setup, find_packages
import versioneer
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
    print(__doc__)

    setup(
        name='temporal_networks_ode',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        description='Integration of ODEs on temporally changing networks',
        long_description=long_description,
        url='https://github.com/Thomasillo/temporal_networks_ode',
        author='Thomas Isele',
        author_email='t.m.isele@posteo.de',
        license='GPLv3',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering'
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3.5',
        ],
        keywords='numerics integration ode',
        packages=find_packages(exclude=['doc', 'tests']),
        install_requires=[],
        extras_require={
            'dev': ['autopep8'],
            'test': ['pytest', 'pytest-cov', 'pytest-flake8'],
            'doc': ['sphinx']
        },
        # If there are data files included in your packages that need to be
        # installed, specify them here.  If using Python 2.6 or less, then these
        # have to be included in MANIFEST.in as well.
        package_data={
            'temporal_networks_ode': ['sample_networks/*'],
        },

        # Although 'package_data' is the preferred approach, in some case you may
        # need to place data files outside of your packages. See:
        # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
        # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
        #data_files=[('my_data', ['data/data_file'])],

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
#        entry_points={
#            'console_scripts': [
#                'sample=sample:main',
#            ],
#        },
    )

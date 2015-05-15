#!/usr/bin/python

from setuptools import setup, find_packages

import openaps
def readme():
    with open("README.md") as f:
        return f.read()

setup(name='openaps',
    version=openaps.__version__, # http://semver.org/
    description='DIY Open Source Artificial Pancreas System.',
    long_description=readme(),
    author="OpenAPS",
    author_email="bewest+openaps@gmail.com",
    # url="https://github.com/openaps/openaps",
    url="https://openaps.org/",
    packages=find_packages( ),
    include_package_data = True,
    install_requires = [
      'pyserial', 'python-dateutil', 'argcomplete',
      'gitpython',
      'decocare', 'dexcom_reader'
    ],
    dependency_links = [
      'http://github.com/compbrain/dexcom_reader/tarball/master#egg=dexcom_reader-master',
      'https://github.com/bewest/dexcom_reader/tarball/master#egg=dexcom_reader-0.0.6-dev-0',
      'https://github.com/bewest/decoding-carelink/tarball/master#egg=decocare-master',
      'https://github.com/bewest/decoding-carelink/tarball/bewest/dev#egg=decocare-0.0.14-dev-0',
    ],
    scripts = [
      'bin/openaps',
      'bin/openaps-device',
      'bin/openaps-enact',
      'bin/openaps-suggest',
      'bin/openaps-get',
      'bin/openaps-use',
      'bin/openaps-report',
      'bin/openaps-vendor',
      'bin/git-openaps-init',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=False,
)

#####
# EOF

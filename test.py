import sys
import platform
import subprocess

from pkg_resources import get_distribution, DistributionNotFound, Requirement


PYTHON_VERSION = platform.python_version()[:3]
IPYTHON_LATEST = '>=7.3.0'   # as of 2019-03-02
PTPYTHON_LATEST = '>=2.0.4'   # as of 2019-03-02
VERSIONS = {
    'ipython': {
        '2.7': '==5.8.0',
        '3.4': '==6.5.0',
        '3.5': IPYTHON_LATEST,
        '3.6': IPYTHON_LATEST,
        '3.7': IPYTHON_LATEST,
    },
    'ptpython': {
        '2.7': '==0.41',
        '3.4': '==0.41',
        '3.5': PTPYTHON_LATEST,
        '3.6': PTPYTHON_LATEST,
        '3.7': PTPYTHON_LATEST,
    },
}


def check_broken_requirements():
    returncode = subprocess.call([sys.executable, '-m', 'pip', 'check'])
    assert returncode == 0, 'Broken requirements found.'


def check_installed_version(package):
    try:
        version = get_distribution(package).version
    except DistributionNotFound:
        raise AssertionError('{} package not installed.'.format(package))
    specifier = VERSIONS[package][PYTHON_VERSION]
    requirement = Requirement.parse(package + specifier)
    assert version in requirement, '{}: expected{}, actual=={}.'.format(
        package, specifier, version)
    print('{}: version check passed.'.format(package))


def test():
    check_broken_requirements()
    check_installed_version('ipython')
    check_installed_version('ptpython')
    print('\nOK. All checks passed.\n')


if __name__ == '__main__':
    test()

from setuptools import find_packages, setup
setup(
    name='read_file_exec',
    packages=find_packages(include=['read_file_exec']),
    version='0.1.0',
    description='FrameWork para execução de scripts',
    author='Otavio',
    license='Apache-2.0',
    install_requires=[],
    setup_requires=['pytest-runner','pandas','numpy','openpyxl'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
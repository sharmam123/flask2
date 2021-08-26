from setuptools import setup

setup(
    name='myapp2',
    version='0.1',
    py_modules=['myapp2'],
    entry_points={
        'console_scripts': ['myapp2 = myapp2:run']
    },
)

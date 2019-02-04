
from setuptools import setup

setup(
    name='test_click_exe',
    version='0.1',
    py_modules=['test_click_exe'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        test_click_exe=test_click_exe:main
    ''',
)

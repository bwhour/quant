import os
from setuptools import setup

with open(os.path.join('README.md')) as desc:
    LONG_DESCRIPTION = desc.read()

with open(os.path.join('requirements.txt')) as reqs:
    REQUIREMENTS = reqs.readlines()

setup(
    name='bt.binance',
    version='1.0.0',
    description='Binance API integration with backtrader',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/bwhour/quant/bt.binance',
    author='willbewhour',
    author_email='juvemeen.xio@gmail.com',
    license='MIT',
    packages=['bt.binance'],
    python_requires='>=3.7',
    keywords='backtrader,binance,bitcoin,bot,crypto,trading',
    install_requires=REQUIREMENTS
)

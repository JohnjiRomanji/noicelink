from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='noicepy',
    url='https://github.com/JohnjiRomanji/noicelink.py',
    author='JohnjiRomanji',
    # Needed to actually package something
    packages=['noicepy'],
    # Needed for dependencies
    install_requires=['requests'],
    # *strongly* suggested for sharing
    version='1.0',
    # The license can be anything you like
    license='MIT',
    description='A simple and easy to use Python wrapper for the noice.link API',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

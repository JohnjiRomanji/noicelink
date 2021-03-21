from setuptools import setup

setup(
    name='noicepy',
    url='https://github.com/JohnjiRomanji/noicelink.py',
    author='JohnjiRomanji',
    packages=['noicepy'],
    install_requires=['requests'],
    # *strongly* suggested for sharing
    version='1.0',
    project_urls=
        docs="https://johnjiromanji.github.io/noicepy"
    # The license can be anything you like
    license='MIT',
    description='A simple and easy to use Python wrapper for the noice.link API',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

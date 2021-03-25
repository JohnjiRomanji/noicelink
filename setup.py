from setuptools import setup

setup(
    name='noice.py',
    url='https://github.com/JohnjiRomanji/noice.py',
    author='JohnjiRomanji',
    packages=['noice.py'],
    install_requires=['requests'],
    # *strongly* suggested for sharing
    version='1.0',
    docs="https://johnjiromanji.github.io/noice.py",
    # The license can be anything you like
    license='MIT',
    description='A simple and easy to use Python wrapper for the noice.link API',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

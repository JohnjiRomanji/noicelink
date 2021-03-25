from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='noicelink',
    url='https://github.com/JohnjiRomanji/noicelink',
    author='JohnjiRomanji',
    packages=['noicelink'],
    install_requires=['requests'],
    # *strongly* suggested for sharing
    version='1.0',
		project_urls={
			'Documentation': 'https://JohnjiRomanji.github.io/noicelink',
			'Source': 'https://github.com/JohnjiRomanji/nocielink',
			'Tracker': 'https://github.com/JohnjiRomanji/noicelink/issues',
		},
    docs="https://johnjiromanji.github.io/noicelink",
    # The license can be anything you like
    license='MIT',
    description='A simple and easy to use Python wrapper for the noice.link API',
    long_description=long_description,
    long_description_content_type="text/markdown",
		classifiers=[
			'Development Status :: 4 - Beta',
			'Intended Audience :: Developers',
			'Topic :: Software Development :: Build Tools',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.6',
			'Programming Language :: Python :: 3.7',
			'Programming Language :: Python :: 3.8',
			'Programming Language :: Python :: 3.9',
		],
		keywords='noice.link noicelink noice py link',
		python_requires='>=3'
)

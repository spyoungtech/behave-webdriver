from setuptools import setup

with open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='behave-webdriver',
    version='0.1.0',
    url='https://github.com/spyoungtech/behave-webdriver/',
    license='MIT',
    author='Spencer Young',
    author_email='spencer.young@spyoung.com',
    description='Selenium webdriver step library for behave BDD testing',
    long_description=readme,
    packages=['behave_webdriver', 'behave_webdriver.steps'],
    platforms='any',
    install_requires=[
        'selenium',
        'behave'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

from setuptools import setup, find_packages

setup(
    name='heroku-flask',
    packages=find_packages(),
    version='0.1',
    description='A Python GitHub repository for practicing Heroku.',
    author='Alexander DeJesus',
    author_email='alexander.dejesus.1985@gmail.com',
    url='https://github.com/libraryman85/Herokju',
    keywords=['libraryman85', 'python', 'Flask', 'Heroku'],
    install_requires=[
        'pytest',
        'flask',
        'flask-runner',
        'flask-script',
        'gunicorn',
        'bandit',
        'coverage',
        'coveralls',
        'flask-wtf'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
from setuptools import find_packages, setup

setup(
    name='FitPartners',
    description='Redes colaborativas Fitness',
    version='0.1',
    url='https://github.com/IvanBrasilico/fit_partners',
    license='GPL',
    author='Ivan Brasilico',
    author_email='brasilico.ivan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-Admin',
        'Flask-BootStrap',
        'Flask-Login',
        'Flask-cors',
        'Flask-nav',
        'Flask-session',
        'Flask-wtf',
        'Flask-Migrate',
        'Flask-SQLAlchemy',
        'mysql-connector',
        'sqlalchemy',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite="tests",
    package_data={
    },
    extras_require={
        'dev': [
            'alembic',
            'bandit',
            'coverage',
            'flake8',
            'flake8-docstrings',
            'flake8-todo',
            'flake8-quotes',
            'flask-webtest',
            'isort',
            'pylint',
            'pytest',
            'pytest-cov',
            'pytest-mock',
            'sphinx',
            'sphinx_rtd_theme',
            'testfixtures',
            'radon',
            'tox'
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.6',
    ],
)

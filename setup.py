from setuptools import setup, find_packages

##use readme for long description
with open('README.rst', encoding='UTF') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to aws s3',
    long_description=readme,
    author='Ray',
    author_email='ray@email.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
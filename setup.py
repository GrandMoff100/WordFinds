from setuptools import setup


with open('README.md', 'r') as f:
    read = f.read()

setup(
    name='Wordfinds',
    description='Generate and solve wordfinds in python',
    version='0.0.0',
    url='https://github.com/GrandMoff100/WordFinds',
    packages=['wordfinds'],
    install_requires=['english_words'],
    long_description=read,
    long_description_content_type='text/markdown'
)

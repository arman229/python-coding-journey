from setuptools import setup

# Read the contents of README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyQSolver',
    version='1.0.3',
    py_modules=['PyQSolver'],
    author='Arman',
    author_email='armanashraf015@gmail.com',
    description="Automatically find solutions to Python exercise questions by providing the question number or text as input.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/arman229/python-coding-journey.git',
    license='MIT',
)

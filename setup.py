from setuptools import setup, find_packages

def get_version():
    """Get the version number from the main module."""
    with open('src/main.py', 'r') as f:
        for line in f:
            if line.startswith('VERSION'):
                return line.split('=')[1].strip().strip('"')
    return '1.0.0'

setup(
    name='astar-pathfinder',
    version=get_version(),
    description='A Python implementation of the A* pathfinding algorithm for data science applications',
    url='https://github.com/samy-alderson/astar-pathfinder',
    author='Samy Alderson',
    author_email='samy.alderson@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['numpy'],
    python_requires='>=3.7',
    include_package_data=True,
    license='MIT',
    zip_safe=False
)
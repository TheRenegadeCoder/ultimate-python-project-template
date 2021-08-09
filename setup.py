import setuptools

cmdclass = {}

try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_sphinx'] = BuildDoc
except ImportError:
    print("WARNING: sphinx not available")

with open("README.md", "r") as fh:
    long_description = fh.read()

# TODO: set version of project (e.g., 0.1.0)
MAJOR = 0
MINOR = 1
PATCH = 0

name = "ultimate-python-project-template"  # TODO: set name of project (e.g. subete)
version = f"{MAJOR}.{MINOR}"
release = f"{MAJOR}.{MINOR}.{PATCH}"
setuptools.setup(
    name=name,
    version=release,
    author="The Renegade Coder",  # TODO: set author
    author_email="jeremy.grifski@therenegadecoder.com",  # TODO: set author email
    description="The ultimate Python project template",  # TODO: set project description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRenegadeCoder/ultimate-python-project-template",  # TODO: set repo url
    packages=setuptools.find_packages(),
    python_requires=">=3.6",  # TODO: specify a range of supported python versions
    install_requires=[
        # TODO: include necessary dependencies here
    ],
    classifiers=[  # TODO: check out classifiers: https://pypi.org/classifiers/
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Documentation :: Sphinx"
    ],
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs'),
            'build_dir': ('setup.py', 'docs'),
            'builder': ("setup.py", "dirhtml")
        }
    }
)

"Setup script for the code_snapshot package"

from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    "Executes setup when this script is the top-level"
    import code_snapshot as app

    classifiers = [
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ]
    setup(
        name="code-snapshot",
        author="Ainomic Technology",
        author_email="contact@ainomic.in",
        url="https://github.com/ainomic/code-snapshot",
        version=app.__version__,
        description=app.__doc__,
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        classifiers=classifiers,
        license=[
            c.rsplit('::', 1)[1].strip()
            for c in classifiers
            if c.startswith('License ::')
        ][0],
        keywords=["snapshot", "screenshot",
                  "code-snapshot", "code-screenshot"],
        packages=find_packages(),
        include_package_data=True,
        platforms="ALL",
        install_requires=[
            "requests >= 2.31.0, < 2.32",
            "certifi",
        ],
        extras_require={},
    )


if __name__ == '__main__':
    main()

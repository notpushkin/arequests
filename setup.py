from distutils.core import setup

__version__ = "0.1.1"

setup(
    name="arequests",
    version=__version__,
    author="Alexander Pushkov",
    author_email="hi@ale.rocks",
    url="https://github.com/iamale/arequests",
    description="Agnostic API classes for Requests.",
    py_modules=["arequests"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Programming Language :: Python",
    ],
)

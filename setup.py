from distutils.core import setup

setup(
    name='arequests',
    version='0.1.0',
    author='Ale',
    author_email='ale@songbee.net',
    url='https://github.com/iamale/arequests',
    description="Agnostic API classes for Requests.",
    py_modules=['arequests'],
    install_requires=[
        'requests',
    ],
    license='Apache 2.0',
    keywords=['github', 'api']
)

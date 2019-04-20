from distutils.core import setup

from arequests import __version__

setup(
    name='arequests',
    version=__version__,
    description="Async wrapper for requests library",
    author="Alexey Khit",
    install_requires=['aiohttp'],
    packages=['arequests']
)

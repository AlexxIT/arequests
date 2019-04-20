from distutils.core import setup

setup(
    name='arequests',
    version='0.1.2',
    description="Async wrapper for requests library",
    author="Alexey Khit",
    install_requires=['aiohttp'],
    packages=['arequests']
)

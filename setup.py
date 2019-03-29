from distutils.core import setup

setup(
    name='arequests',
    version='0.2.0',
    description="Async wrapper for requests library",
    author="Alexey Khit",
    install_requires=['requests', 'aiohttp'],
    packages=['arequests']
)

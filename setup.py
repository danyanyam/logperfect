from setuptools import setup

setup(
   name='foo',
   version='1.0',
   description='logging module',
   author='danyanyam',
   author_email='dvbuchko@gmail.com',
   install_requires=['colored-traceback', 'colorama'],
   packages=['logging']
)
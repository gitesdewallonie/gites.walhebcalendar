from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='gites.walhebcalendar',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python"],
      keywords='',
      author='Gites',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['gites'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
            test=['zope.testing', 'plone.testing', 'mockito']),
      install_requires=[
          'ZSI',
          'Zope2',
          'affinitic.pwmanager',
          'collective.monkeypatcher',
          'grokcore.component',
          'five.grok',
          'five.dbevent',
          'z3c.soap',
          'setuptools',
          'z3c.autoinclude',
          'walhebcalendar.db'])

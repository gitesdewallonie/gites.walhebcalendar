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
      author='Gites de Wallonie',
      author_email='jfroche@affinitic.be',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['gites'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
            test=['zope.testing', 'plone.testing', 'mockito'],
            docs=['z3c.recipe.sphinxdoc',
                  'docutils',
                  'repoze.sphinx.autointerface',
                  'collective.sphinx.includechangelog',
                  'sphinxcontrib-sdedit',
                  'Pillow',
                  'Sphinx',
                  'collective.sphinx.includedoc']),
      install_requires=[
          'ZSI',
          'Zope2',
          'affinitic.pwmanager',
          'affinitic.zamqp',
          'collective.monkeypatcher',
          'collective.autopermission',
          'grokcore.component',
          'five.grok',
          'z3c.soap',
          'dateutil',
          'plone.memoize',
          'setuptools',
          'z3c.autoinclude',
          'Products.GenericSetup',
          'Products.PluginRegistry',
          'Products.PluggableAuthService',
          'walhebcalendar.db'])

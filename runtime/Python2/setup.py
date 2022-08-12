from setuptools import setup

v = '4.10.1'
setup(
    name='antlr4-python2-runtime-thieman',
    version=v,
    url='http://www.antlr.org',
    license='BSD',
    packages=['antlr4', 'antlr4.atn', 'antlr4.dfa', 'antlr4.tree', 'antlr4.error', 'antlr4.xpath'],
    package_dir={'': 'src'},
    author='Eric Vergnaud, Terence Parr, Sam Harwell',
    author_email='eric.vergnaud@wanadoo.fr',
    description='ANTLR %s runtime for Python 2.7.12' % v
)

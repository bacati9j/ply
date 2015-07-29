try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name = "ply",
            description="Python Lex & Yacc",
            long_description = """
PLY is yet another implementation of lex and yacc for Python. Some notable
features include the fact that its implemented entirely in Python and it
uses LALR(1) parsing which is efficient and well suited for larger grammars.

PLY provides most of the standard lex/yacc features including support for empty 
productions, precedence rules, error recovery, and support for ambiguous grammars. 

PLY is extremely easy to use and provides very extensive error checking. 
It is compatible with both Python 2 and Python 3.
""",
            license="""BSD""",
            version = "3.7",
            author = "David Beazley",
            author_email = "dave@dabeaz.com",
            maintainer = "David Beazley",
            maintainer_email = "dave@dabeaz.com",
            url = "http://www.dabeaz.com/ply/",
            packages = ['ply'],
            classifiers = [
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 2',
              ]
            )

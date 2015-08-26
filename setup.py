from setuptools import setup

setup(
        name="python-mwapi",
        version="0.2.0", # Change in mwapi/__init__.py
        author="Yuvi Panda",
        author_email="yuvipanda@gmail.com",
        url="http://github.com/yuvipanda/python-mwapi",
        packages=["mwapi"],
        license=open("LICENSE").read(),
        description = "Simple wrapper for the Mediawiki API",
        long_description = open("README").read(),
        install_requires = ["requests"]
)

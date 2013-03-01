from setuptools import setup

setup(name="PySolarized",
      version="1.0.3",
      description="A simple library for accessing Apache Solr full-text search engine. Allows updating and queryies over"
                  "multiple cores.",
      author="Jernej Virag",
      author_email="jernej@virag.si",
      packages=["pysolarized"],
      license="BSD",
      install_requires=["requests"],
      classifiers=[
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries",
          "Topic :: Internet :: WWW/HTTP :: Indexing/Search"
])

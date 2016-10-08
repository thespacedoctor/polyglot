from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/polyglot/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.rst') as f:
        return f.read()

install_requires = [
    'pyyaml',
    'pypolyglot',
    'fundamentals',
    'readability-api',
    'requests'
]

# READ THE DOCS SERVERS
exists = os.path.exists("/home/docs/")
if exists:
    c_exclude_list = ['healpy', 'astropy',
                      'numpy', 'sherlock', 'wcsaxes', 'HMpTy', 'ligo-gracedb']
    for e in c_exclude_list:
        try:
            install_requires.remove(e)
        except:
            pass

setup(name="pypolyglot",
      version=__version__,
      description="Translate documents and webpages to various markup languages and document formats (html, epub, mobi ..)",
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords=['pdf, html, parser'],
      url='https://github.com/thespacedoctor/polyglot',
      download_url='https://github.com/thespacedoctor/polyglot/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['polyglot=polyglot.cl_utils:main'],
      },
      zip_safe=False)

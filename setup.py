from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='simpdf',
      version='0.1',
      description='',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords='utilities dryx',
      # url='https://github.com/thespacedoctor/simpdf',
      author='thespacedoctor',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=['simpdf'],
      include_package_data=True,
      install_requires=[
          'pyyaml',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['simpdf=simpdf.cl_utils:main']
      },
      zip_safe=False)

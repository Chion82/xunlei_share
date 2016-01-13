from setuptools import setup
setup(
  name = 'xunleishare',
  packages = ['xunleishare'],
  entry_points={
      'console_scripts': [
          'xunleishare = xunleishare.xunleishare:main',
      ],
  },
  install_requires=['requests' ,'six'],
  version = '0.1.3',
  description = 'Based on the idea of sharing, XunleiShare is a command-line interface tool to directly get download links on Xunlei Lixian servers with the help of the maintainer\'s Xunlei VIP account. You do not have to acquire a VIP.',
  author = 'Chion82',
  license='MIT',
  author_email = 'sdspeedonion@gmail.com',
  url = 'https://github.com/Chion82/xunlei_share',
  keywords = ['xunlei', 'xunleishare', 'thunder'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
  ]
)

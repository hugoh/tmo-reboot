from setuptools import setup

setup(
  name='tmo_reboot',
  version='0.1',
  description='A script to reboot the T-Mobile Home Internet 5G Gateways',
  long_description='A lightweight, cross-platform Python 3 script that can reboot the T-Mobile Home Internet Arcadyan and Nokia 5G Gateways for 4G/5G bands, cellular site (tower), and internet connectivity and reboots as needed or on-demand.',
  url='https://github.com/hugoh/tmo-monitor',
  author='hugoh',
  license='MIT',
  packages=[
    'tmo_monitor',
    'tmo_monitor.gateway'
  ],
  scripts=['bin/tmo-reboot.py'],
  install_requires=[
    'requests',
  ]
)

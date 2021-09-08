from setuptools import find_packages, setup


install_requires = [
    'python-openstackclient==5.2.0',
    'flask==1.1.2',
    'flask-restx==0.5.1',
    'pytest==5.4.2',
    'pytest-cov==2.8.1',
    'pytest-flask==1.0.0',
    'Werkzeug==0.16',
]


setup(
    name='devstack_client',
    version='0.0.1',
    description='Devstack client to control vms',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False
)
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_custome/__init__.py
from erpnext_custome import __version__ as version

setup(
	name="erpnext_custome",
	version=version,
	description="erpnext_custome",
	author="malek",
	author_email="malek.hossam.209@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

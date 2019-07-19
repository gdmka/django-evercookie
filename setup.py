from setuptools import setup, find_packages

requirements = [l.strip() for l in open('requirements.txt').readlines()]

setup(
     name='django_evercookie',
     version='0.2',
     install_requires = requirements,
     packages = find_packages(),
     include_package_data = True, 
     author = 'Alexey Haidamaka',
     author_email = 'ahaidamaka@gmail.com',
     description = 'Evercookie for Django',
     license = 'MIT License', 
     keywords = 'django evercookie',
     url='https://github.com/gdmka/django_evercookie',
     )


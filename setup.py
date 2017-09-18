from setuptools import setup, find_packages

dependency_links = [
    'http://github.com/rain0r/django-dont-vary-on/tarball/master#egg=django_dont_vary_on-1.0',

]
requirements = ['Django',
                'Pillow >= 2.0.0']

setup(
    name='django_evercookie',
    version='0.1',
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    author='Alexey Haidamaka',
    author_email='ahaidamaka@gmail.com',
    description='Evercookie for Django',
    license='MIT License',
    keywords='django evercookie',
    url='https://github.com/gdmka/django_evercookie',
)

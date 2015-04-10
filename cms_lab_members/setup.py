import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "Django==1.7.7",
    "Pillow==2.8.1",
    "Unidecode==0.04.17",
    "django-filer==0.9.9",
    "django-mptt==0.6.1",
    "django-polymorphic==0.6.1",
    "easy-thumbnails==2.2",
    "django-lab-members>=0.2.0"
]

setup(
    name='djangocms-lab-members',
    version='0.0.0',
    packages=['cms_lab_members'],
    include_package_data=True,
    license='BSD License',
    description='A Django app to display lab personnel and information about them.  It extends the default with django CMS-specific features',
    long_description=README,
    # url='http://www.example.com/',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=install_requires,
)

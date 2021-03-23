from distutils.core import setup

setup(
    name='aruodas_scraper',
    version='1.0',
    packages=['aruodas-scraper'],
    url='https://github.com/virbickt/aruodas-scraper',
    license='MIT License',
    author='Teofilius Virbickas',
    author_email='tvirbickas@gmail.com',
    description='Webscraper designed to scrape rent listings on aruodas.lt',
    install_requires=[
        'requests',
        'bs4',
        'pandas',
        'fake_useragent'
    ]
)
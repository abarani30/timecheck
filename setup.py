from distutils.core import setup
setup(
    # How you named your package folder (timecheck)
    name='time_check_validity',
    # Chose the same as "name"
    packages=['timecheck'],
    # Start with a small number and increase it with every change you make
    version='0.1',
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='A package to check the time validity',
    # Type in your name
    author='Ali Sattar Barani',
    # Type in your E-Mail
    author_email='alisattarbarani@gmail.com',
    # Provide either the link to your github or to your website
    url='https://github.com/abarani30',
    # I explain this later on
    download_url='https://github.com/abarani30/timecheck/archive/refs/tags/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['TIME', 'TIME VALIDITY', 'VALID TIME', 'TIME_VALID',
              'VALID_TIME', 'time'],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - Production/Stable',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3',
    ],
)

from setuptools import setup, find_packages

setup(name='recurring content detector',
      version='0.1',
      description='Can be used to programmatically detect credits, recaps and previews in tv shows',
      url='https://github.com/nielstenboom/recurring-content-detector',
      author='Niels ten Boom',
      author_email='nielstenboom@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data = True,
      install_requires=[
          'Pillow==6.*',
          'ffmpeg_python==0.*',
          'matplotlib==3.*',
          'opencv_python==4.*',
          'pandas==0.*',
          'scipy==1.*',
          'tqdm==4.*',
          'natsort==6.*',
          'numpy==1.*',
          'pytest==6.*'
      ],
      zip_safe=False)
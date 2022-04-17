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
          'Pillow==6.1.0',
          'ffmpeg_python==0.2.0',
          'matplotlib==3.1.1',
          'opencv_python==4.1.1.26',
          'pandas==0.25.0',
          'scipy==1.3.1',
          'tqdm==4.40.2',
          'natsort==6.2.0',
          'numpy==1.21.0',
          'pytest==6.0.2'
      ],
      zip_safe=False)
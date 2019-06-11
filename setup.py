from setuptools import setup, find_packages

setup(name='recurring content detector',
      version='0.1',
      description='Can be used to programmatically detect credits, recaps and previews in tv shows',
      url='https://github.com/nielstenboom/recurring-content-detector',
      author='Niels ten Boom',
      author_email='nielstenboom@gmail.com',
      license='MIT',
      packages=find_packages('.'),
      package_dir={'':'.'},
      include_package_data = True,
      install_requires=[
          'Keras',
          'Pillow',
          'ffmpeg_python',
          'matplotlib',
          'opencv_python',
          'pandas',
          'scipy',
          'tqdm'
      ],
      zip_safe=False)
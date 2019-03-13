from setuptools import setup

setup(name='pyoptim',
      version='0.1',
      description='optimizerTool',
      url='https://github.com/schaul/py-optim',
      author='schaul',
      packages=['PyOptim',
				'PyOptim.algorithms',
				'PyOptim.benchmarks',
				'PyOptim.core',
				'PyOptim.external_libs',
				'PyOptim.tools',
				'PyOptim.tests'])
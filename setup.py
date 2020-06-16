from setuptools import find_packages, setup

setup(name='docker_compose_env',
      version='0.1.2',
      description=
      'Solve the problem that environment variables are not interpolated by docker-compose',
      url='https://github.com/mnieber/docker_compose_env',
      download_url='https://github.com/mnieber/docker_compose_env/tarball/0.1.2',
      author='Maarten Nieber',
      author_email='hallomaarten@yahoo.com',
      license='MIT',
      packages=find_packages(),
      package_data={
          'docker_compose_env': [
              'bin/*.sh',
              'bin/*.fish',
          ]
      },
      entry_points={'console_scripts': [
          'compile-env=docker_compose_env.compile_env:main',
      ]},
      data_files=[],
      install_requires=["PyYAML"],
      zip_safe=False)

import setuptools

setuptools.setup(
  name="jupyter-nextflow-proxy",
  version='0.1.0',
  url="https://github.com/phue/jupyter-nextflow-proxy",
  description="Jupyter extension to proxy nextflow",  
  author="Patrick Hüther",
  keywords=['Jupyter', 'Nextflow'],
  classifiers=['Framework :: Jupyter'],
  entry_points={
    'jupyter_serverproxy_servers': [
        'nextflow = jupyter_nextflow_proxy:setup_nextflow'
    ]
  },
  package_data={
      'jupyter_nextflow_proxy': ['icons/nextflow.svg']
  },
  install_requires=['jupyter-server-proxy'],
)

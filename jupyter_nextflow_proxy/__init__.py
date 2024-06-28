import os
from pathlib import Path

def setup_nextflow():
  return {
    'command': ['nextflow', 'run', os.environ['NXF_USER_WORKFLOW'], '-r', os.environ['NXF_USER_REVISION'], '--PORT={port}', '-resume', '-params-file', os.environ['NXF_USER_PARAMS']],
    'timeout': 120,
    'launcher_entry': {
        'title': 'Nextflow',
        'icon_path': Path(__file__).parent / 'icons' / 'nextflow.svg'
    }
  }

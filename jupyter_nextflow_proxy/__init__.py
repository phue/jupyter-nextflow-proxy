import os
from pathlib import Path

def setup_nextflow():
  return {
    'command': _get_nextflow_cmd,
    'timeout': 120,
    'launcher_entry': {
        'title': 'Nextflow',
        'icon_path': Path(__file__).parent / 'icons' / 'nextflow.svg'
    }
  }

def _get_nextflow_cmd(port):
  cmd = ['nextflow', 'main.nf', '-resume', '--COMMS.enabled=true', '--COMMS.port={port}']
  if 'NXF_MAIL' in os.environ:
    cmd.append(f'--EMAIL={os.environ["NXF_MAIL"]}')
  return cmd
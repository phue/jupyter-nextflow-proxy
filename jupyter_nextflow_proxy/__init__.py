from pathlib import Path

def setup_nextflow():
  return {
    'command': ['nextflow', 'main.nf', '-resume', '--COMMS.enabled=true', '--COMMS.port={port}'],
    'timeout': 120,
    'environment' : {},
    'launcher_entry': {
        'title': 'Nextflow',
        'icon_path': Path(__file__).parent / 'icons' / 'nextflow.svg'
    }
  }

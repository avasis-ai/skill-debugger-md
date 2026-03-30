import click
import yaml
from pathlib import Path
import sys
import os

current_dir = Path(__file__).parent
sys.path.append(str(current_dir.parent))

from skill_debugger_md.debugger import Debugger

def main():
    """Start the skill debugger."""
    
    # Find the nearest skill-debugger-md.toml configuration file
    config_path = Path.cwd()
    while config_path != config_path.parent:
        if (config_path / "skill-debugger-md.toml").exists():
            break
        config_path = config_path.parent
    
    if not (config_path / "skill-debugger-md.toml").exists():
        click.echo("Error: Could not find skill-debugger-md.toml configuration file")
        return

    # Load configuration
    with open(config_path / "skill-debugger-md.toml", "r") as f:
        config = yaml.safe_load(f)

    # Start debugger
    debugger = Debugger(config)
    debugger.start()

if __name__ == "__main__":
    main()
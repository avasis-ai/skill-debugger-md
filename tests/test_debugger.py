import pytest
from skill_debugger_md.debugger import Debugger

def test_debugger():
    config = {
        "skill_path": "/opt/oss-factory/projects/skill-debugger-md/skills/example_skill.md"
    }
    debugger = Debugger(config)
    
    # Test breakpoint setting
    debugger.set_breakpoint("example_skill.md", 10)
    assert ("example_skill.md", 10) in debugger.breakpoints
    
    # Test breakpoint clearing
    debugger.clear_breakpoint("example_skill.md", 10)
    assert ("example_skill.md", 10) not in debugger.breakpoints
import subprocess

def test_cli_runs():
    result = subprocess.run(["python3", "certnode_cli.py", "--help"], capture_output=True)
    assert result.returncode == 0
    assert b"usage" in result.stdout

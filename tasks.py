from invoke import task
import pathlib


@task
def build(c, docs="build a exe file base on ./record.py which can record key in put to ~/KeyboardInputRecord.json"):
    current_path = pathlib.Path.cwd() / "record.py"
    c.run(f"pyinstaller -F {current_path}")


@task
def run(c, docs="simply run in terminal"):
    current_path = pathlib.Path.cwd() / "record.py"
    c.run(f"python {current_path}")


@task
def analyze(c, docs="generate a table which show your touch potential"):
    current_path = pathlib.Path.cwd() / "parser.py"
    c.run(f"python {current_path}")

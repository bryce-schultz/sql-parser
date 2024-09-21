import pytest
import subprocess
import os

def runCmd(cmd):
    print(f'Running command: {cmd}')
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

class Parser:
    def __init__(self, parser_executable):
        self.parser_executable = parser_executable

    def parse(self, sql):
        result = runCmd(f'echo {sql}| "{self.parser_executable}"')
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

@pytest.fixture(scope='session')
def parser():
    # get this directory
    directory = os.path.dirname(os.path.realpath(__file__))

    # get the parser executable
    parser_executable = os.path.abspath(os.path.join(directory, '../src/x64/Debug/sql-parser.exe'))

    assert os.path.exists(parser_executable)

    parser = Parser(parser_executable)
    yield parser

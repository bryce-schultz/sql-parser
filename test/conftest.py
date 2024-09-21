import pytest
import subprocess
import os
import re

def runCmd(cmd):
    print(f'Running command: {cmd}')
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

class Parser:
    def __init__(self, parser_executable):
        directory = os.path.dirname(os.path.realpath(__file__))
        src_directory = os.path.abspath(os.path.join(directory, '../src/'))
        assert os.path.exists(src_directory)

        result = runCmd(f'MSBuild.exe "{src_directory}/sql-parser.sln" /t:Rebuild /p:Configuration=Debug /p:Platform=x64')
        
        print(result.stdout.decode('utf-8'))
        print(result.stderr.decode('utf-8'))

        assert result.returncode == 0

        self.ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
        self.parser_executable = parser_executable

    def parse(self, sql):
        result = runCmd(f'echo {sql}| "{self.parser_executable}"')
        return self._remove_color(result.stdout.decode('utf-8')), self._remove_color(result.stderr.decode('utf-8'))
    
    def _remove_color(self, text):
        return self.ansi_escape.sub('', text)

@pytest.fixture(scope='session')
def parser():
    # get this directory
    directory = os.path.dirname(os.path.realpath(__file__))

    # get the parser executable
    parser_executable = os.path.abspath(os.path.join(directory, '../src/x64/Debug/sql-parser.exe'))

    parser = Parser(parser_executable)

    assert os.path.exists(parser_executable)
    
    yield parser

import pytest
import subprocess
from pgbackup import pgdump

url = "postgres://bob@example.com:5432/db_one"

def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen()') #popen instead of run so it happens in the background    
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen()', side_effect=OSError('no such fi;e'))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
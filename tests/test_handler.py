import pytest

from src.handler import run

def test_run_success_without_event():
    assert run(None, None) == 'Done'

def test_run_success_with_event():
    assert run({ 'should_fail': False }, None) == 'Done'

def test_run_failure():
    with pytest.raises(Exception, match='Failed on purpose'):
      run({ 'should_fail': True }, None)

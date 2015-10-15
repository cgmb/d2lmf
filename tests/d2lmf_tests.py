from nose.tools import *
from d2lmf.d2lmf import parse_submission_dirname

def test_parse_submission_dirname():
    student_id, student_name, submission_date = parse_submission_dirname(
            '840137-90210 - Johnny Cache - Sep 12, 2015 6:31 PM')
    assert student_id == '840137-90210'
    assert student_name == 'Johnny Cache'
    assert submission_date == 'Sep 12, 2015 6:31 PM'

def test_parse_submission_dirname_with_hyphen_in_name():
    student_id, student_name, submission_date = parse_submission_dirname(
            '928421-33831 - Mary-Kate Olsen - Oct 2, 2015 12:22 AM')
    assert student_id == '928421-33831'
    assert student_name == 'Mary-Kate Olsen'
    assert submission_date == 'Oct 2, 2015 12:22 AM'

def test_parse_submission_dirname_on_windows():
    student_id, student_name, submission_date = parse_submission_dirname(
            '942724-37311 - John Jacob Jingleheimer Schmidt - Jan 9, 2012 11_55 AM')
    assert student_id == '942724-37311'
    assert student_name == 'John Jacob Jingleheimer Schmidt'
    assert submission_date == 'Jan 9, 2012 11:55 AM'

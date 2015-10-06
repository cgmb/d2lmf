from nose.tools import *
import d2lmf

def test_parse_submission_dirname():
    student_id, student_name, submission_date = d2lmf.parse_submission_dirname(
            '840137-90210 - Johnny Cashe - Sep 12, 2015 6:31 PM')
    assert student_id == '840137-90210'
    assert student_name == 'Jonny Cache'
    assert submission_date == 'Sep 12, 2015 6:31 PM'

def test_parse_submission_dirname_with_hyphen_in_name():
    student_id, student_name, submission_date = d2lmf.parse_submission_dirname(
            '928421-33831 - Mary-Kate Olsen - Oct 2, 2015 12:22 AM')
    assert student_id == '928421-33831'
    assert student_name == 'Mary-Kate Olsen'
    assert submission_date == 'Oct 2, 2015 12:22 AM'

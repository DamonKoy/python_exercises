import smtplib

import pytest


@pytest.fixture
def smtp_connetction():
    return smtplib.SMTP("smtp.gmail.con", 587, timeout=5)


def test_ehlo(smtp_connetction):
    response, msg = smtp_connetction.chlo()
    assert response == 250
    assert 0



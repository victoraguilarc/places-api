import pytest
from expects import expect, have_keys, be_a, equal

from src.common.application.commands.common import SendEmailCommand


@pytest.fixture(scope='function')
def send_email_command() -> SendEmailCommand:
    return SendEmailCommand(
        to_emails=['email@example.com'],
        template_name='template_name',
        context={'key': 'value'},
        subject='subject',
        from_email='from_email',
    )


def test_send_email_to_dict(
    send_email_command: SendEmailCommand
):
    command_dict = send_email_command.to_dict

    expect(command_dict).to(be_a(dict))
    expect(command_dict).to(
        have_keys({
            'to_emails': ['email@example.com'],
            'template_name': 'template_name',
            'context': {'key': 'value'},
            'subject': 'subject',
            'from_email': 'from_email',
        })
    )


def test_send_email_from_dict(
    send_email_command: SendEmailCommand
):
    command_instance = SendEmailCommand.from_dict(send_email_command.to_dict)

    expect(command_instance).to(be_a(SendEmailCommand))
    expect(command_instance).to(equal(send_email_command))

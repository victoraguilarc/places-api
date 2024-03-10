from typing import List

from expects.matchers import Matcher


class _HasErrorCode(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, response_json: dict):
        errors = response_json.get('errors', [])
        error_codes = {error.get('code') for error in errors}
        if self._expected in error_codes:
            return True, ['error found']
        return False, [f'error {self._expected} not found']


class _HasValidationErrors(Matcher):
    def __init__(self, expected: List[str]):
        self._expected = expected

    def _match(self, response_json: dict):
        validation = response_json.get('validation', {})
        validation_keys = [key for key, value in validation.items()]
        if set(self._expected).issubset(set(validation_keys)):
            return True, ['error found']
        return False, [f'error {self._expected} not found']


class _ResponseFormat(Matcher):
    def _match(self, subject: dict):
        return ('data' in subject and 'datetime' in subject), []


class _ErrorResponseFormat(Matcher):
    def _match(self, subject: dict):
        return ('errors' in subject and 'validation' in subject), []


be_valid_response = _ResponseFormat()
be_valid_error_response = _ErrorResponseFormat()
has_error_code = _HasErrorCode
has_validation_errors = _HasValidationErrors

# -*- coding: utf-8 -*-
from spinrewriter import Api
from spinrewriter import exceptions as ex
import unittest2 as unittest


class TestErrors(unittest.TestCase):

    def setUp(self):
        """Utility code shared among all tests."""
        self.api = Api('foo@bar.com', 'test_api_key')

    def test_parsing_error_messages(self):
        """Go through all possible error messages and see that they are parsed
        correctly.
        """

        with self.assertRaises(ex.AuthenticationError):
            self.api._raise_error(
                {'response': 'Authentication failed. Unique API key is not valid for this user.'})

        with self.assertRaises(ex.AuthenticationError):
            self.api._raise_error(
                {'response': 'Authentication failed. No user with this email address found.'})

        with self.assertRaises(ex.AuthenticationError):
            self.api._raise_error(
                {'response': 'This user does not have a valid Spin Rewriter subscription.'})

        with self.assertRaises(ex.QuotaLimitError):
            self.api._raise_error(
                {'response': 'API quota exceeded. You can make 50 requests per day.'})

        with self.assertRaises(ex.UsageFrequencyError):
            self.api._raise_error(
                {'response': 'You can only submit entirely new text for analysis once every 5 seconds.'})

        with self.assertRaises(ex.UnknownActionError):
            self.api._raise_error(
                {'response': 'Requested action does not exist. Please refer to the Spin Rewriter API documentation.'})

        with self.assertRaises(ex.MissingParameterError):
            self.api._raise_error(
                {'response': 'Email address and unique API key are both required. At least one is missing.'})

        with self.assertRaises(ex.ParamValueError):
            self.api._raise_error(
                {'response': 'Original text too short.'})

        with self.assertRaises(ex.ParamValueError):
            self.api._raise_error(
                {'response': 'Original text too long. Text can have up to 4,000 words.'})

        with self.assertRaises(ex.ParamValueError):
            self.api._raise_error(
                {'response': 'Original text after analysis too long. Text can have up to 4,000 words.'})

        with self.assertRaises(ex.ParamValueError):
            self.api._raise_error(
                {'response': 'Spinning syntax invalid. With this action you should provide text with existing valid {first option|second option} spintax.'})

        with self.assertRaises(ex.ParamValueError):
            self.api._raise_error(
                {'response': 'The {first|second} spinning syntax invalid. Re-check the syntax, i.e. curly brackets and pipes.'})

        with self.assertRaises(ex.ParamValueError):
            self.api._raise_error(
                {'response': 'Spinning syntax invalid.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'Analysis of your text failed. Please inform us about this.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'Synonyms for your text could not be loaded. Please inform us about this.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'Unable to load your new analyzed project.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'Unable to load your existing analyzed project.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'Unable to find your project in the database.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'Unable to load your analyzed project.'})

        with self.assertRaises(ex.InternalApiError):
            self.api._raise_error(
                {'response': 'One-Click Rewrite failed.'})

        with self.assertRaises(ex.UnknownApiError):
            self.api._raise_error(
                {'response': 'foo'})

    def _raise_error(self, msg):
        try:
            self.api._raise_error({'response': msg})
        except ex.SpinRewriterApiError as e:
            if isinstance(e, ex.UnknownApiError):
                self.fail("UnknownApiError")

        self.assertIn("{{'response': '{0}'}}".format(msg), self.test_errors_file)

    def test_parsing_error_messages_v2(self):
        with open(__file__, 'r') as f:
            self.test_errors_file = f.read()

            self._raise_error("Email address and unique API key are both required. At least one is missing.")

            self._raise_error("Requested action does not exist. Please refer to the Spin Rewriter API documentation.")

            self._raise_error("Authentication failed. No user with this email address found.")

            self._raise_error("Authentication failed. Unique API key is not valid for this user.")

            self._raise_error("This user does not have a valid Spin Rewriter subscription.")

            self._raise_error("API quota exceeded. You can make 50 requests per day.")

            self._raise_error("Original text too short.")

            self._raise_error("Original text too long. Text can have up to 4,000 words.")

            self._raise_error("Spinning syntax invalid. With this action you should provide text with existing valid {first option|second option} spintax.")

            self._raise_error("You can only submit entirely new text for analysis once every 5 seconds.")

            self._raise_error("The {first|second} spinning syntax invalid. Re-check the syntax, i.e. curly brackets and pipes.")

            self._raise_error("Original text after analysis too long. Text can have up to 4,000 words.")

            self._raise_error("Analysis of your text failed. Please inform us about this.")

            self._raise_error("Synonyms for your text could not be loaded. Please inform us about this.")

            self._raise_error("Unable to load your new analyzed project.")

            self._raise_error("Unable to load your existing analyzed project.")

            self._raise_error("Unable to find your project in the database.")

            self._raise_error("Unable to load your analyzed project.")

            self._raise_error("One-Click Rewrite failed.")

            self._raise_error("Spinning syntax invalid.")

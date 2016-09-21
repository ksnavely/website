"""
_accounts_tests_

Unit tests coverage for website.accounts.
"""
import mock
import unittest

from website import accounts


class AccountTests(unittest.TestCase):
    """
    Test the create/get/update/delete account functionality.
    """
    @mock.patch("website.accounts.MongoClient")
    def client_singleton_test(self, m_mc):
        """
        Make sure we can fetch the mongo client, and that it's a singleton.
        """
        m_mc.return_value = mock.Mock()

        client1 = accounts._client()
        client2 = accounts._client()
        self.assertEqual(client1, client2)

    def bcrypt_test(self):
        """
        Test the account hashing/checking functionality. Verify both the success
        and failure case.
        """
        password = 'I love dachsunds#$$@#24!!'
        bad_password = 'not my password'

        hashed = accounts._get_hashed_password(password)

        self.assertTrue(accounts._check_password(password, hashed))
        self.assertFalse(accounts._check_password(bad_password, hashed))

    @mock.patch("website.accounts._get_account")
    def authenticate_test(self, m_get_account):
        user = 'someuser'
        password = 'I love dachsunds#$$@#24!!'
        hashed = accounts._get_hashed_password(password)
        m_get_account.return_value = {"hashed_password": hashed}

        self.assertTrue(accounts.authenticate(user, password))

        m_get_account.assert_called_once_with(user)

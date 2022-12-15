import unittest
from unittest import mock

from configuration import *


class ConfigurationTests(unittest.TestCase):
    @mock.patch("configuration.getenv")
    def test_set_from_env(self, mock_getenv):
        want = "My Env Value"
        mock_getenv.return_value = want
        my_config = Configuration({
            "my_setting": "Unused Default"
        })
        self.assertEqual(want, my_config["my_setting"])

    @mock.patch("configuration.getenv")
    def test_set_using_default(self, mock_getenv):
        want = "My Default"
        mock_getenv.return_value = None
        my_config = Configuration({
            "my_setting": want
        })
        self.assertEqual(want, my_config["my_setting"])

    @mock.patch("configuration.getenv")
    def test_set_bool_from_env_true(self, mock_getenv):
        mock_getenv.return_value = "true"
        my_config = Configuration({
            "my_setting": False
        })
        self.assertTrue(my_config["my_setting"])

    @mock.patch("configuration.getenv")
    def test_set_bool_from_env_false(self, mock_getenv):
        mock_getenv.return_value = "false"
        my_config = Configuration({
            "my_setting": True
        })
        self.assertFalse(my_config["my_setting"])

    @mock.patch("configuration.getenv")
    def test_set_list_from_env(self, mock_getenv):
        mock_getenv.return_value = '["my group"]'
        my_config = Configuration({
            "my_setting": '[]'
        })
        self.assertTrue(isinstance(my_config["my_setting"], list))

    @mock.patch("configuration.getenv")
    def test_is_bool(self, mock_getenv):
        mock_getenv.return_value = None
        my_config = Configuration({
            "my_setting": False
        })
        self.assertFalse(my_config["my_setting"])
        self.assertIsInstance(my_config["my_setting"], bool)

    @mock.patch("configuration.getenv")
    def test_repr(self, mock_getenv):
        mock_getenv.return_value = None
        sample = {
            "my_setting": "Test",
            "my_secret": "super secret"
        }
        want = json.dumps(sample).replace(sample["my_secret"], "********")
        my_config = Configuration(sample)
        got = str(my_config)
        self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#-*-coding:utf-8-*-

import unittest
import app


class ConfigTest(unittest.TestCase):

    def testOne(self):
        config = app.get_config()
        self.assertEqual(config.get('modules/test/version'), '0.1')

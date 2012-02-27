#-*-coding:utf-8-*-

import unittest
import app


class ConfigTest(unittest.TestCase):

    def testGet(self):
        config = app.get_config()
        self.assertEqual(config.get('modules/test/version'), '0.1')
        self.assertEqual(config.get('modules/t2/version'), '0.2')
        self.assertEqual(config.get('t2/abc'), 'rrr')

    def testGetRouters(self):
        routers = app.get_config().get('routers');
        self.assertTrue(len(routers) > 1)

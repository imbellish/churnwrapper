"""
Unit tests for churnover 

"""

import unittest
import requests
import settings
import json
from churnwrapper import ChurnOver

class TestChurnOver(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_successful_pass_to_json(self):
        query = {
            "agentfirstname":'Ian', 
            "agentlastname": 'Bellamy'
	    }
        churn = ChurnOver(**query)
        #self.assertTrue(churn.is_valid())
        observed = json.loads(churn.call())
        expected = query
        self.assertEqual(observed, expected)

    def test_invalid_key(self):
        query = {
            'foo': 'bar'
        }
        with self.assertRaises(KeyError):
            ChurnOver(**query)

    def test_invalid_entity_status(self):
        query = {
            'entitystatus': 'foo'
        }
        with self.assertRaises(AttributeError):
            ChurnOver(**query)

    def test_successful_response(self):
        """
        ChurnOver should assign a response attribute 
        which is the json response from churn.rocks
        """
        query = {
            "agentfirstname":"Ian",
            "agentlastname": "Bellamy" 
        }
        churn = ChurnOver(**query)
        churn.call()
        self.assertTrue(hasattr(churn, "response"), "ChurnOver did not assign response attr")
        print(churn.response)


if __name__ == "__main__":
    unittest.main()
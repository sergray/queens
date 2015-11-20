import json
import unittest

import queens


class QueensTestCase(unittest.TestCase):

    def setUp(self):
        queens.app.config['TESTING'] = True
        self.app = queens.app.test_client()

    def _post(self, data):
        return self.app.post('/max_queens',
                             data=json.dumps(data),
                             content_type='application/json')

    def _assert(self, response, json_data):
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), json_data)

    def test_spec(self):
        rv = self._post(dict(
            rows=8,
            columns=8,
            max_queens_on_sight=0,
            initial_queens=[{'x': 0, 'y': 0}, {'x': 1, 'y': 2}]
        ))
        self._assert(rv, {u'added_queens': [{u'x': 3, u'y': 1}, {u'x': 2, u'y': 4}, {u'x': 4, u'y': 3}]})


if __name__ == '__main__':
    unittest.main()
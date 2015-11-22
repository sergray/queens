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
        if json_data is not None:
            self.assertDictEqual(json.loads(response.data), json_data)

    def test_spec(self):
        rv = self._post(dict(
            rows=8,
            columns=8,
            max_queens_on_sight=0,
            initial_queens=[{'x': 0, 'y': 0}, {'x': 1, 'y': 2}]
        ))
        self._assert(rv, None)

    def test_boards(self):
        boards = [
            {"initial_queens": [{"y": 0, "x": 0}], "rows": 4, "max_queens_on_sight": 0, "columns": 4},
            {"initial_queens": [{"y": 0, "x": 9}, {"y": 3, "x": 0}], "rows": 10, "max_queens_on_sight": 1, "columns": 4},
            {"initial_queens": [{"y": 0, "x": 0}], "rows": 6, "max_queens_on_sight": 0, "columns": 1},
            {"initial_queens": [{"y": 0, "x": 0}, {"y": 3, "x": 2}], "rows": 5, "max_queens_on_sight": 0, "columns": 5},
            {"initial_queens": [], "rows": 20, "max_queens_on_sight": 0, "columns": 20},
            {"initial_queens": [{"y": 0, "x": 0}, {"y": 1, "x": 0}, {"y": 2, "x": 1}, {"y": 2, "x": 4}, {"y": 0, "x": 4}, {"y": 19, "x": 15}, {"y": 7, "x": 5}], "rows": 20, "max_queens_on_sight": 2, "columns": 20},
            {"initial_queens": [{"y": 0, "x": 0}, {"y": 3, "x": 2}, {"y": 2, "x": 1}, {"y": 6, "x": 0}, {"y": 0, "x": 6}, {"y": 10, "x": 9}], "rows": 10, "max_queens_on_sight": 2, "columns": 15},
        ]
        for board in boards:
            rv = self._post(board)
            self._assert(rv, None)


if __name__ == '__main__':
    unittest.main()
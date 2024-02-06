import unittest
from utils.DBUtil import DBUtil


class TestDBUtil(unittest.TestCase):
    def test_database_connection(self):
        db_connection = DBUtil.getDBConn()

        self.assertIsNotNone(db_connection)
        db_connection.close()


if __name__ == '__main__':
    unittest.main()

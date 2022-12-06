from books.requests.status import *


class TestStatus:
    def test_status_code(self):
        assert get_status().status_code == 200, 'status code not ok'

    def test_status_msg(self):
        assert get_status().json()['status'] == 'OK', 'status message not ok'

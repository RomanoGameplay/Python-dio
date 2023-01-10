from src.services import _get_trends
from unittest import mock

def test_get_trends_with_sucess():
    mock_api = mock.Mock()
    trends = _get_trends(woe_id=1000, api=mock_api)
    

def test_get_trends_without_return_with_sucess():
    mock_api = mock.Mock()
    trends = _get_trends(woe_id=1000, api=mock_api)
    assert trends == []

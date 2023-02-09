import pytest
from fletrelaygui.main import get_list_of_com_ports

__author__ = "Ananda Utama"
__copyright__ = "Ananda Utama"
__license__ = "MIT"


def test_get_list_of_com_ports():
    """API Tests"""
    com_ports = get_list_of_com_ports()
    assert len(com_ports) == 2

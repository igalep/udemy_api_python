import pytest

pytestmark = pytest.mark.all

class TestCheckout(object):
    @pytest.mark.smoke
    def test_checkout_as_guest(self):
        print('Check out test')

    @pytest.mark.regression
    def test_check_out_as_existing(self):
        print('Check out with existing')
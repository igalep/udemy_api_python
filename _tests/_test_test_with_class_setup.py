import pytest

pytestmark = pytest.mark.all

@pytest.fixture(scope='module')
def my_setup():
    print('\nMy_setup')
    return {'id' : 1, 'name' : "Igal"}


class TestCheckout(object):
    @pytest.mark.smoke
    def test_checkout_as_guest(self,my_setup):
        print('Check out test')
        print(my_setup)

    @pytest.mark.regression
    def test_check_out_as_existing(self,my_setup):
        print('Check out with existing')
        print(my_setup)
        assert  1 == 3

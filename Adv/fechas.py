import unittest

from datetime import datetime

from freezegun import freeze_time

def fin_pandemia():
    hoy = datetime.today()
    if hoy.year > 2022:
        return True
    return False

class Test(unittest.TestCase):

    @freeze_time("2023-01-01")
    def test_finalizar_pandemia_true(self):
        print(datetime.today())
        self.assertTrue(fin_pandemia())

    def test_finalizar_pandemia_false(self):
        self.assertFalse(fin_pandemia())

if __name__ == 'main':
    unittest.main()

#ERROR
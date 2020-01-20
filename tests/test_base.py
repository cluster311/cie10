from cie.cie10 import CIECodes


class TestBase:

    def test_codes(self):
        cie = CIECodes()
        x511 = cie.info(code='X511')

        assert x511['code'] == 'X511'
        assert x511['source'] == 'deis.cl'

        c020 = cie.info(code='C02.0')

        assert c020['code'] == 'C020'
        assert c020['source'] == 'icdcode.info'

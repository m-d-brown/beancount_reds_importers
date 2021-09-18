"""
Regression testing is described by
https://beancount.github.io/docs/17_importing_external_data.html#regression-testing-your-importers.

Golden files are produced with:
  pytest --generate
"""

import unittest
from os import path

from beancount.ingest import regression_pytest
from beancount_reds_importers import vanguard

# Note this is the same importer instance across all files in this
IMPORTER = vanguard.Importer({
        'main_account'   : 'Assets:Vanguard:401k',
        'account_number' : '123456',
        'transfer'       : 'Assets:Zero-Sum-Accounts:Transfers:Bank-Account',
        'dividends'      : 'Income:Dividends:401k',
        'interest'       : 'Income:Interest:401k',
        'cg'             : 'Income:Capital-Gains:401k',
        'capgains_lt'    : 'Income:Capital-Gains-Distributions:Long:401k',
        'capgains_st'    : 'Income:Capital-Gains-Distributions:Short:401k',
        'fees'           : 'Expenses:Brokerage-Fees:401k',
        'rounding_error' : 'Equity:Rounding-Errors:Imports',
        'fund_info'      : {
            'fund_data':  [
                ('VFIFX', 'VGI007743', 'Vanguard Target Retirement 2050 Fund'),
            ],
            'money_market': ['VMFXX'],
        },
    })

@regression_pytest.with_importer(IMPORTER)
@regression_pytest.with_testdir(path.dirname(__file__))
class TestImporter(regression_pytest.ImporterTestBase):
    pass

if __name__ == '__main__':
    unittest.main()

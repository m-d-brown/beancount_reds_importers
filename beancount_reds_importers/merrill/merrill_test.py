"""
Regression testing is described by
https://beancount.github.io/docs/17_importing_external_data.html#regression-testing-your-importers.

Golden files are produced with:
  pytest --generate
"""

import unittest
from os import path

from beancount.ingest import regression_pytest
from beancount_reds_importers import merrill

IMPORTER = merrill.Importer({
        'main_account'   : 'Assets:MerrillEdge',
        'account_number' : '987654321',
        'transfer'       : 'Assets:Zero-Sum-Accounts:Transfers:Bank-Account',
        'dividends'      : 'Income:Dividends:MerrillEdge',
        'interest'       : 'Income:Interest:MerrillEdge',
        'cg'             : 'Income:Capital-Gains:MerrillEdge',
        'capgains_lt'    : 'Income:Capital-Gains-Distributions:Long:MerrillEdge',
        'capgains_st'    : 'Income:Capital-Gains-Distributions:Short:MerrillEdge',
        'fees'           : 'Expenses:Brokerage-Fees:MerrillEdge',
        'rounding_error' : 'Equity:Rounding-Errors:Imports',
        'fund_info'      : {
            'fund_data':  [
                ('VFIAX', '922908710', 'Vanguard 500 Index Fund Admiral Shares'),
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

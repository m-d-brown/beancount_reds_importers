"""Merrill Lynch and Edge OFX importer."""

import ntpath
from beancount_reds_importers.libreader import ofxreader
from beancount_reds_importers.libtransactionbuilder import investments

# TODO: Fix reinvestment. For example,
#
# 2020-06-30 * "Reinvestment Share(s): VANGUARD 500 INDEX FUND ADMIRAL CL AGENT" "[VFIAX] Vanguard 500 Index Fund Admiral Shares"
#   Assets:BofA:MerrillEdge:VFIAX   1.00 VFIAX
#   Assets:Transfers:MerrillEdge   -1.00 VFIAX
#
# should instead be
#
# 2020-06-30 * "Reinvestment Share(s): VANGUARD 500 INDEX FUND ADMIRAL CL AGENT" "[VFIAX] Vanguard 500 Index Fund Admiral Shares"
#   Assets:BofA:MerrillEdge:VFIAX   1.00 VFIAX {}
#   Assets:Transfers:MerrillEdge  -327.00 USD


class Importer(investments.Importer, ofxreader.Importer):
    def custom_init(self):
        self.max_rounding_error = 0.11
        self.filename_identifier_substring = 'Quicken'
        self.get_ticker_info = self.get_ticker_info_from_id

    def file_name(self, file):
        return 'merrill-all-{}'.format(ntpath.basename(file.name))

    def get_target_acct_custom(self, transaction):
        return self.target_account_map.get(transaction.type, None)

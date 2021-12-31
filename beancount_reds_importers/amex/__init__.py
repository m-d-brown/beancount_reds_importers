"""Amex credit card ofx importer for beancount."""

from beancount_reds_importers.libreader import ofxreader
from beancount_reds_importers.libtransactionbuilder import banking


class Importer(banking.Importer, ofxreader.Importer):
    IMPORTER_NAME = 'American Express'
    def custom_init(self):
        if not self.custom_init_run:
            self.max_rounding_error = 0.04
            self.filename_identifier_substring = 'amex'
            self.custom_init_run = True

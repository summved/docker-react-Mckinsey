#detect-secrets scan --custom-plugins testing/custom_plugins_dir/ --custom-plugins testing/hippo_plugin.py

import re

from detect_secrets.plugins.base import RegexBasedDetector


class PluginKeyDetector(RegexBasedDetector):
    """
    Scans for private keys.
    This checks for private keys by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Summved Key'

    denylist = [
        
        #re.compile(r'(?:\s|=|:|"|^)PWD[a-zA-Z0-9]{10,}'),  
        
        #re.compile(r'(?:\s|=|:|"|^)SUMM[\dABCDEF][a-zA-Z0-9]{8,}'),  # SUMM Password

        re.compile(r'pass|pwd|password|token|key|access_key|', re.IGNORECASE),

        #re.compile(r'pass|pwd|password|token|key|'),

    ]
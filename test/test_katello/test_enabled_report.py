import os
import sys
import unittest
from mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), '../../src/'))
from katello import enabled_report

class TestEnabledReport(unittest.TestCase):

    @patch('katello.enabled_report.ZYPPER', True)
    def test_zypper_valid(self):
        rh_repo = os.path.join(os.path.dirname(__file__), 'data/repos/redhat.repo.suse')
        report = enabled_report.EnabledReport(rh_repo)
        expected = {'enabled_repos': {'repos': [{'baseurl': ['https://katello.example.com/pulp/repos/Dev/Library/Suse_15_SP1_v2/custom/Python_2_Module_15_SP1_x86_64/Python_2_Module_15_SP1_x86_64_SLE-Module-Python2-15-SP1-Pool_for_sle-15-x86_64'],
                                                 'repositoryid': 'Dev_Python_2_Module_15_SP1_x86_64_Python_2_Module_15_SP1_x86_64_SLE-Module-Python2-15-SP1-Pool_for_sle-15-x86_64'}]}}

        self.assertEqual(expected, report.content)

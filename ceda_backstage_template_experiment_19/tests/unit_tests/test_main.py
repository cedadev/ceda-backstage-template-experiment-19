"""
Unit tests for the main package
"""

import unittest

from ceda_backstage_template_experiment_19.main import main


class TestMain(unittest.TestCase):
    """
    Test the functionality of the main package.
    """

    def test_main(self) -> None:
        """
        Test the functionality of the :py:func:`ceda_backstage_template_experiment_19.main` function
        """

        main()

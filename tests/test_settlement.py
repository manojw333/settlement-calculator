import pytest
from settlement_calculator import calculate_fee, calculate_net_settlement


class TestCalculateFee:
    def test_card_fee(self):
        # 2.5% of SGD 1000 should be SGD 25.00
        assert calculate_fee(1000.00, "card") == 25.00

    def test_paynow_fee(self):
        # 0.5% of SGD 500 should be SGD 2.50
        assert calculate_fee(500.00, "paynow") == 2.50

    def test_paypal_fee(self):
        # 3.0% of SGD 200 should be SGD 6.00
        assert calculate_fee(200.00, "paypal") == 6.00

    def test_unknown_method_raises(self):
        with pytest.raises(ValueError):
            calculate_fee(100.00, "crypto")


class TestCalculateNetSettlement:
    def test_single_card_transaction(self):
        # SGD 1000 card payment: fee = 25.00, net = 975.00
        txns = [{"amount": 1000.00, "method": "card"}]
        assert calculate_net_settlement(txns) == 975.00

    def test_mixed_methods(self):
        # card: 1000 - 25.00 = 975
        # paynow: 500 - 2.50 = 497.50
        # total net = 1472.50
        txns = [
            {"amount": 1000.00, "method": "card"},
            {"amount": 500.00, "method": "paynow"},
        ]
        assert calculate_net_settlement(txns) == 1472.50

    def test_empty_transactions(self):
        assert calculate_net_settlement([]) == 0.0

    def test_small_amount_precision(self):
        # 2.5% of SGD 10 = SGD 0.25, net = SGD 9.75
        txns = [{"amount": 10.00, "method": "card"}]
        assert calculate_net_settlement(txns) == 9.75

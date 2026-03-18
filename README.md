# Settlement Calculator

A Python utility to calculate merchant net settlement amounts after deducting payment processing fees (MDR).

## What it does

- Accepts a list of transactions with gross amounts and payment methods
- Applies the correct MDR (Merchant Discount Rate) per payment method
- Returns net settlement amount per merchant

## Usage

```python
from settlement_calculator import calculate_net_settlement

transactions = [
    {"amount": 1000.00, "method": "card"},
    {"amount": 500.00, "method": "paynow"},
]

net = calculate_net_settlement(transactions)
print(f"Net settlement: SGD {net}")
```

## MDR Rates

| Payment Method | MDR (%) |
|---|---|
| Card | 2.5% |
| PayNow | 0.5% |
| PayPal | 3.0% |

## Running Tests

```bash
python -m pytest tests/
```

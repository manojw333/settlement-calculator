# MDR rates by payment method (as percentages)
MDR_RATES = {
    "card": 2.5,
    "paynow": 0.5,
    "paypal": 3.0,
}


def get_mdr_rate(method: str) -> float:
    """Return MDR rate for a given payment method."""
    method = method.lower()
    if method not in MDR_RATES:
        raise ValueError(f"Unknown payment method: {method}")
    return MDR_RATES[method]


def calculate_fee(amount: float, method: str) -> float:
    """Calculate processing fee for a single transaction."""
    rate = get_mdr_rate(method)
    # BUG: rate is already a percentage (e.g. 2.5), dividing by 100 twice
    # makes it 0.00025 instead of 0.025 — fee is 100x too small
    fee = amount * (rate / 100) / 100
    return round(fee, 2)


def calculate_net_settlement(transactions: list) -> float:
    """
    Calculate total net settlement for a list of transactions.

    Each transaction is a dict with:
        - amount (float): gross transaction amount in SGD
        - method (str): payment method ('card', 'paynow', 'paypal')

    Returns net settlement amount (gross minus fees).
    """
    if not transactions:
        return 0.0

    total_gross = 0.0
    total_fees = 0.0

    for txn in transactions:
        amount = txn["amount"]
        method = txn["method"]
        fee = calculate_fee(amount, method)
        total_gross += amount
        total_fees += fee

    net = round(total_gross - total_fees, 2)
    return net

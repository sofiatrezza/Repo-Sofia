def max_wealth(bank_accounts):
    max = 0
    for account in bank_accounts:
        if sum(account) > max:
            max = sum(account)
    return sum(account)

accounts = [
    [1,10,3],
    [3, 2, 1, 1623, 29834, 29384, 6462]
    ]
print(f'The max wealth is: {max_wealth(accounts)}')

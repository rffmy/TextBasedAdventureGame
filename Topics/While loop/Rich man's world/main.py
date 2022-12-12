def min_years_to_accumulate_max_insured_deposit(initial_deposit):
    end_deposit = initial_deposit
    max_insured_deposit = 700000
    apr = 0.071
    years = 0
    while end_deposit < max_insured_deposit:
        end_deposit = end_deposit * (1 + apr)
        years += 1

    return years


print(min_years_to_accumulate_max_insured_deposit(float(input())))

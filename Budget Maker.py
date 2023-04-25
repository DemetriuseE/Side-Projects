Name_of_user = "With whom do I have pleasure of trying to be of assistance to today?"
print(Name_of_user)
name = input()
appreciation_to_user = f"Thank you {name}"
print(appreciation_to_user)

Net_income_statement_m = "What is your net monthly income?"
print(Net_income_statement_m)
Net_income = int(input())
#Net Income has to be converted into an integer in order to create a proper response.#
starting_from_the_bottom = f" So I see you have a net income of ${Net_income}."
managing_finances_1 = "In order to break this down we need to understand if this is a monthly income or biweekly."
managing_finances_2 = "Naturally it is easier to work with a biweekly function so we will take the value given from you and divide it by 2."
managing_finances_3 = "What we will have as a finished product is our budget friendly income in terms of dealing with expenses for weeks to come."
print(managing_finances_1)
print(managing_finances_2)
print(managing_finances_3)
print(starting_from_the_bottom)
#Each statement produced earlier allows us to get into the part of program that's helpful knowing when to apply our 50/30/20 rule.#
Biweekly_net_income = int(Net_income)/2
Biweekly_income_response = f" So we have a biweekly income of ${Biweekly_net_income}"
print(Biweekly_income_response)
fifty_thirty_twenty_rule = "We will be utilizing something called the 50/30/20 rule in order to manage our finances better today."
fifty_thirty_twenty_rule_subtext_1 = "50% of our income goes towards bills."
fifty_thirty_twenty_rule_subtext_2 = "30% of our income goes towards expenses."
fifty_thirty_twenty_rule_subtext_3 = "20% of our income goes towards savings."
print(fifty_thirty_twenty_rule)
print(fifty_thirty_twenty_rule_subtext_1)
print(fifty_thirty_twenty_rule_subtext_2)
print(fifty_thirty_twenty_rule_subtext_3)
half_of_paycheck_towards_bills_calculator = Net_income * 0.5
three_tenths_of_paycheck_towards_expenses_calculator = Net_income * 0.3
a_fifth_of_paycheck_towards_savings_calculator = Net_income * 0.2
#Calculations for using your budget in order to keep a solid grip on what can be afforded.#
half_of_paycheck_towards_bills_text = f"You have ${half_of_paycheck_towards_bills_calculator} to use for bills."
three_tenths_of_paycheck_towards_expenses_text = f" You have ${three_tenths_of_paycheck_towards_expenses_calculator} to use for expenses."
a_fifth_of_paycheck_towards_savings_text = f" You have $ {a_fifth_of_paycheck_towards_savings_calculator} to use for savings."
#These provide printed statements with the values for each process of the budget. Use them properly and edit them for 40/40/20 or 60/30/10#
print(half_of_paycheck_towards_bills_text)
print(three_tenths_of_paycheck_towards_expenses_text)
print(a_fifth_of_paycheck_towards_savings_text)
thankfulness = f"Thank you for using the Budget Maker today {name}."
print(thankfulness)

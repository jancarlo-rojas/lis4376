print("Paycheck Calculator")
print("Program calculates net pay based upon hours worked, hourly rate, and taxes paid.\n")

print("Program Requirements:")
print("Developer: Jancarlo Rojas")
print("1. Must use float data type for user input.")
print("2. Must round calculations to two decimal places.")
print("3. Must format currency with dollar sign, and two decimal places.\n")

print("User Input: ")

# Get user input
hours = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: $"))
tax_rate = float(input("Tax Rate (percent): "))

# Calculate
gross_pay = hours * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_amount

# Display results
print("\nProgram Output:")
print("Gross Pay:\t", "${0:,.2f}".format(gross_pay))
print("Tax Rate:\t", "{:.2f}%".format(tax_rate))
print("Tax Amount:\t", "${0:,.2f}".format(tax_amount))
print("Net Pay:\t", "${0:,.2f}".format(net_pay))
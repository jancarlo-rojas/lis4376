def get_requirements():
	print("Payroll Calculator")
	print(
		"\nProgram Requirements:\n"
		"1. Must use float data type for user input.\n"
		"2. Overtime rate: 1.5 times hourly rate (hours over 40).\n"
		"3. Holiday rate: 2.0 times hourly rate (all holiday hours).\n"
		"4. Must format currency with dollar sign, and round to two decimal places.\n"
		"5. Create at least three functions that are called by the program:\n"
		"\ta. main(): calls at least two other functions.\n"
		"\tb. get_requirements(): displays the program requirements.\n"
		"\tc. calculate_payroll(): calculates an individual's one-week paycheck.\n"
	)


def calculate_payroll():
	BASE_HOURS = 40.0
	OT_RATE = 1.5
	HOLIDAY_RATE = 2.0

	print("Input:")
	hours = float(input("Enter hours worked: "))
	holiday_hours = float(input("Enter holiday hours: "))
	pay_rate = float(input("Enter hourly pay rate: "))

	regular_hours = min(hours, BASE_HOURS)
	overtime_hours = max(0.0, hours - BASE_HOURS)

	base_pay = regular_hours * pay_rate
	overtime_pay = overtime_hours * pay_rate * OT_RATE
	holiday_pay = holiday_hours * pay_rate * HOLIDAY_RATE
	gross_pay = base_pay + overtime_pay + holiday_pay

	print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)


def print_pay(base_pay, overtime_pay, holiday_pay, gross_pay):
	print("\nOutput:")
	print("{0:<10} ${1:,.2f}".format("Base:", base_pay))
	print("{0:<10} ${1:,.2f}".format("Overtime:", overtime_pay))
	print("{0:<10} ${1:,.2f}".format("Holiday:", holiday_pay))
	print("{0:<10} ${1:,.2f}".format("Gross:", gross_pay))
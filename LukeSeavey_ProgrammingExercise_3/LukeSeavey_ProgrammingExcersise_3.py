from functools import reduce

# Function to add expenses gathered from user

def add_expenses(total, expense):
    
    return total + expense[1]

# Function to find the higher expense out of the ones gathered

def higher_expense(current, expense):
    
    if current[1] > expense[1]:
        
        return current
    
    else:
        
        return expense

# Function to find the lower expense of the ones gathered

def lower_expense(current, expense):
    
    if current[1] < expense[1]:
        
        return current
    
    else:
        
        return expense

def main():
    
    expenses = []

    print("Enter your monthly expenses. Type 'done' when finished.")
    
    while True:
        
        expense_type = input("Enter expense type (or 'done'): ").strip()
        
        if expense_type.lower() == 'done':
            
            break

        try:
            
            amount = float(input(f"Enter amount for {expense_type}: "))
            
            expenses.append((expense_type, amount))
        
        except ValueError:
            
            print("Invalid amount. Please enter a number.")

    if not expenses:
        
        print("No expenses entered.")
        
        return

    # Total expenses using reduce
    
    total_expenses = reduce(add_expenses, expenses, 0)

    # Highest expense using reduce
    
    highest_expense = reduce(higher_expense, expenses)

    # Lowest expense using reduce
    
    lowest_expense = reduce(lower_expense, expenses)

    print(f"Total expenses: ${total_expenses:.2f}")
    
    print(f"Highest expense: {highest_expense[0]} (${highest_expense[1]:.2f})")
    
    print(f"Lowest expense: {lowest_expense[0]} (${lowest_expense[1]:.2f})")

if __name__ == "__main__":
    
    main()
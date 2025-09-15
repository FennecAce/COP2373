# Luke Seavey Programming Exercise 1
# This program manages ticket sales for presale cinema tickets up to a max 40 with only 4 per person.

total_tix = 10

max_per_person = 4

sales = 0

# Function to handle ticket selling process.

def selling_tickets(num_tix):
   
    global total_tix
   
    global sales

# Telling the user the constraints of the ticket sales.

    if num_tix > max_per_person:
    
        return "You can only buy up to 4 tickets."

# Checking if there are enough tickets available.
   
    elif num_tix > total_tix:
   
        return "Not enough tickets available."

# Processing the ticket sale and giving confirmation of purchase.
   
    else:
    
        total_tix -= num_tix
    
        sales += 1
      
        return f"You have successfully purchased {num_tix} tickets."

# Main function to run the ticket selling loop to keep track of sales and remaining tickets.

def main():

# Main while loop to keep selling tickets until they are sold out.
  
    while total_tix > 0:

# basic error handling for non-supported inputs.
    
        try:

# Asking user for number of tickets they want to buy and displaying remaining tickets.
        
            num_tix = int(input(f"There are {total_tix} tickets available. How many would you like to buy? "))
          
            message = selling_tickets(num_tix)
          
            print(message)
          
            print(f"{total_tix} tickets remaining.")
      
        except ValueError:
           
            print("Please enter a valid number.")

# Final message when all tickets are sold out and how many buyers there were.
   
    print(f"All tickets sold out! Total buyers: {sales}")

if __name__ == "__main__":
  

    main()

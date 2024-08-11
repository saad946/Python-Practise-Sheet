def main(): 
  try:
      a = int(input("Enter a number: "))
      print(f"You entered: {a}")
      
  except Exception as e:
      print("An unexpected error occurred:", e)
      print("Please try again later.")
  finally: # It will always be executed, regardless of whether an exception occurred or not in the try block.
      print("I am inside the finally.")
  
  print("Thanks for using our service!")


main()
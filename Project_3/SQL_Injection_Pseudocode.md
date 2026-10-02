START

GET username
GET payment amount 

VALIDATE username
VALIDATE payment amount

PREPARE SQL query:
  SELECT account FROM customers
  WHERE username = ?

EXECUTE query using username as a parameter

IF customer exists 
  GET payment amount 
  VALIDATE payment amount
  PROCESS payment
  DISPLAY "You have completed your payment successfully"
  
ELSE 
  DISPLAY "We couldn't find your account"
  ASK "Would you like to create an account with us?"

  ID answer is YES
    CREATE new account
    RETURN TO START
  ELSE 
    DISPLAY "You payment has been cancelled" 
    END IF
  END IF
  
END

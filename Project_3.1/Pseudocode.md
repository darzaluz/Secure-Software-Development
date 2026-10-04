START

LOGIN: 
    GET username
    VALIDATE username

    PREPARE SQL query:
      SELECT account FROM customers
      WHERE username = ?

    EXECUTE query using username as a parameter

    IF customer exists
      GET payment amount 
      GET payment note 

      VALIDATE payment amount
      VALIDATE payment note 

      ENCODE payment note 

      PROCESS payment 

      DISPLAY " You have completed your payment successful"
      DISPLAY payment note as text 

    ELSE
      DISPLAY "Customer account not found"
      ASK "Would you like to create an account with us?"

      IF answer is YES
        Create new aacount 
        RETURN TO LOGIN
      ELSE 
        DISPLAY "You payment has been cancelled" 
        END IF
    END IF
END

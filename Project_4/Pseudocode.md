```text
START SECURE COMMUNICATION SYSTEM 

START SERVER 
  Load server certificate 
  Load server private key
  Create secure TLS server socket 
  Wait for client connection 

START CLIENT
  Load trusted certificate 
  Create secure TLS client connection

  Connect to server

  Verify server certificate 
  Verify certificate matches expected hostname 

  IF certificate is not valid 
    Reject connection 
    Display security warning
    STOP
  END IF

  Establish TLS encrypted connection 

  Send message to server through encrypted connection 

SERVER
  Receive encrypted message 
  Read message 
  Send encrypted response back to client 

CLIENT
  Receive encrypted response
  Display response

  Close secure connection 

END SYSTEM

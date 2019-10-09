# Caesar Cipher		
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'		
max_size = len(SYMBOLS)
encryption_option = input("Would you like to Encode or Decode? ")		
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()	

def getMode():		
  while True:		
      # print('Do you wish to encrypt or decrypt a message?')		
      encryption_option = input("Would you like to Encode or Decode? ").lower()
      
      if encryption_option in ['encode', 'e', 'decode', 'd']:		
          return encryption_option		
      else:		
          print('Enter either "encrypt" or "e" or "decrypt" or "d".')		
	
def getMessage():		
  print('What is your message?')		
  return input()		
    
def getKey():		
  key = 0		
  while True:		
      print('What is your cipher number? (1-%s)' % (max_size))		
      key = int(input())		
      if (key >= 1 and key <= max_size):		
          return key		
    
def getCipherMessage(encryption_option, message, key):		
  if encryption_option[0] == 'd':		
      key = -key		
  translated = ''		
  
  for symbol in message:		
      symbolIndex = SYMBOLS.find(symbol)		
      if symbolIndex == -1: # Symbol not found in SYMBOLS.		
          # Just add this symbol without any change.		
          translated += symbol		
      else:		
          # Encrypt or decrypt		
          symbolIndex += key		
  
          if symbolIndex >= len(SYMBOLS):		
              symbolIndex -= len(SYMBOLS)		
          elif symbolIndex < 0:		
              symbolIndex += len(SYMBOLS)		
  
          translated += SYMBOLS[symbolIndex]		
  return translated		
    
# Ask the user for their message and cipher number.
if should_encode:
  # Your code here!
  encryption_option = getMode()		
  message = getMessage()		
  key = getKey()		
  print(getCipherMessage(encryption_option, message, key))
  pass
elif should_decode:
    # Your code here for extra credit
    # Focus on getting the code above to work first.
    pass
else:
    # Print a nice notice that we only support encrypt/decrypt
    # Your code here!
    pass

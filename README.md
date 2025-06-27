# Day 8 - Caesar Cipher 🔐

This project is a simple encryption/decryption tool based on the classic **Caesar Cipher**. The user can choose to encode or decode a message by shifting the alphabet by a specified number of steps.

## Description

The Caesar Cipher works by shifting each letter in the input message by a given amount along the alphabet. For example, with a shift of 3:

abc → def


If the end of the alphabet is reached, it wraps around to the beginning.

The program asks the user:
- Whether they want to **encode** or **decode** a message
- The **message** itself
- The **shift amount**

It then returns the transformed text accordingly.

The cipher supports looping to allow multiple encodings/decodings in one session.

## Example Output
```
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Hello user
Type the shift number:
3
Here is the encoded result: khoor xvhu
```

## Skills Learned

- Working with **functions** and parameters
- Handling **user input** and sanitization
- Understanding **modulo** arithmetic for letter shifting
- String manipulation using **loops**
- **Positional** vs **keyword** arguments
- Creative problem solving for wrapping the alphabet
- Optional: using ASCII art for a better UI experience

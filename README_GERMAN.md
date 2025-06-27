# Tag 8 - Caesar-Verschlüsselung 🔐

Dieses Projekt ist ein einfaches Ver-/Entschlüsselungstool auf Basis der **Caesar-Verschlüsselung**. Der Benutzer kann eine Nachricht mit einem bestimmten Buchstaben-Shift codieren oder decodieren lassen.

## Beschreibung

Die Caesar-Chiffre verschiebt jeden Buchstaben der Eingabe um eine bestimmte Anzahl im Alphabet. Beispiel bei einer Verschiebung von 3:

abc → def

Wird das Ende des Alphabets erreicht, springt es an den Anfang zurück.

Das Programm fragt:
- Ob eine **Codierung** oder **Decodierung** durchgeführt werden soll
- Die **Nachricht**
- Die **Verschiebungszahl**

Anschließend wird die verschlüsselte oder entschlüsselte Nachricht ausgegeben.

Mehrere Durchläufe sind in einer Sitzung möglich.

## Beispielausgabe
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


## Gelernt

- Arbeiten mit **Funktionen** und Parametern
- Umgang mit **Benutzereingaben**
- Einsatz von **Modulo-Rechnung** zur Buchstabenverschiebung
- **String-Manipulation** mit Schleifen
- **Positional** vs **Keyword Arguments**
- Kreative Problemlösung für das Umspringen im Alphabet
- Optional: Einsatz von ASCII-Art zur besseren Darstellung

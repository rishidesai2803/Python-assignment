text = "Hello$World" 
enc = base64.b64encode(text.encode()) 
print("Base64:", enc.decode()) 

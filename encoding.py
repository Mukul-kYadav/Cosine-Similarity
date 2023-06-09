import chardet

# Open the file in binary mode and read a portion of its contents
with open('movies.dat', 'rb') as f:
    data = f.read(10000)  # Read the first 10,000 bytes of the file

# Detect the encoding of the file
result = chardet.detect(data)
encoding = result['encoding']
confidence = result['confidence']

print(f"Detected Encoding: {encoding} with confidence: {confidence}")

text = "X-DSPAM-Confidence:    0.8475"

begpos = text.find(' ')
extract = text[begpos:]
extract.strip()
extract = float(extract)

print(extract)
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
slice = float(text[pos:pos+6])
print(slice)
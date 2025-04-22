lines = [
    'X-DSPAM-Confidence:      0.8475',
    'X-DSPAM-Confidence:      0.765',
    'X-DSPAM-Confidence:      0.998',
    'X-DSPAM-Confidence:      0.650',
    'X-Some-Other-Header:     0.123'
]

data = []

for line in lines:
    if line.startswith('X-DSPAM-Confidence:'):
        colon_index = line.find(':')
        number_part = line[colon_index+1:].strip() # removing spaces
        try: 
            value = float(number_part)
            data.append(value)
        except ValueError:
            print(f"Could not convert: {number_part}")

# Lets show cleaned results
print("Cleaned confidence values:", data)  

# WHAT
# .startswith : filters only lines you care about
# .find() : locates where the number starts 
# .rstrip : removes extrea whitespace
# float : converts the string to a usable number 
# and try/except : catches bad data safely

# WHY
# The script mirrors what would happen when
# - extracting confidence scores from email spam logs
# - pulling sensor readings from raw device output
# - cleaning CSV data where numbers are mixed with text
# - and when preparing numeric features for machine learning


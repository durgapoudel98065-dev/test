# 1. Get input from the user
original_url = input("Paste a URL:")
 
# 2. Clean the URL (convert to lowercase)
clean_url = original_url.strip().lower()
 
# 3. Extract the domain
# Splitting the clean URL by "/" gives us: ['https:', '', 'example.com', 'path']
domain = clean_url.split("/")[-1]
 
# 4. Check if it ends with .com
if domain.endswith(".com"):
    print(f"{domain} is a .com site")
else:
    print(f"{domain} is not a .com site")
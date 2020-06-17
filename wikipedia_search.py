# ===== load_thecode =====#
import wikipedia
# pip install wikipedia in command prompt
query = input("What do you want to search for?")
n = int(input("Enter no of lines"))
query = query.replace("wikipedia", "")
text = (wikipedia.summary(query, sentences=n))
print('According to wikipedia')
print(text)


import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

# Example usage
if __name__ == "__main__":
    long_url = input("Enter the long URL: ")
    short_url = shorten_url(long_url)
    print("Shortened URL:", short_url)
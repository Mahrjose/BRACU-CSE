book_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68821),
    ("Best Horror", "The Institute", 75717),
    ("Best History & Biography", "The five", 31783),
    ("Best Fiction", "The Testaments", 98291),
)

for item in book_info:
    award, book_name, votes = item
    print(f"{book_name} won the '{award}' category with {votes} votes")

import json

from mongoengine import connect

from models import Author, Quote


connect(db='web14', host="mongodb+srv://boridka:654123@cluster0.8nz8els.mongodb.net/?retryWrites=true&w=majority")

authors_dict = dict()

with open("authors.json", "r", encoding='utf-8') as fh:
    authors_json_list = json.loads(fh.read())

with open("quotes.json", "r", encoding='utf-8') as fh:
    quotes_json_list = json.loads(fh.read())

for authors_json_dict in authors_json_list:
    author = Author(
        fullname=authors_json_dict["fullname"], 
        born_date=authors_json_dict["born_date"], 
        born_location=authors_json_dict["born_location"], 
        description=authors_json_dict["description"]
        )
    authors_dict.update({author.fullname: author})
    author.save()

for quotes_json_dict in quotes_json_list:
    quote = Quote(
        tags=quotes_json_dict["tags"], 
        author=authors_dict[quotes_json_dict["author"]],
        quote=quotes_json_dict["quote"]
        )
    quote.save()
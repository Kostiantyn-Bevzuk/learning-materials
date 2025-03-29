import json

with open('src/fluent_python_book/metaprogramming/osconfeed.json', "r") as fp:
    feed = json.load(fp)

print(feed['Schedule']['speakers'][-1]['name'])
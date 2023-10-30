import wikipedia
# query = self.nlp_int.identify_search_command_and_query(self.cmd)
# query = self.nlp_int.identify_search_topic(self.query)
query = "search about pikachu".split()
print(query)
if 'search' in query:
    query.remove('search')
if 'about' in query:
    query.remove('about')
result = wikipedia.summary(query, sentences=1)
print(result)
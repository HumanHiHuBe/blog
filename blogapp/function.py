def function_to_render_correct_word_meaning(s):
    import re
    s = s.strip()
    l = s.split("\n")
    new_l = []
    #loop to remove extra new line characters in between two entries
    for i in range(len(l)):
        if not l[i]  == '':
            new_l.append(l[i])

    #Loop to split word and their meaning
    for i in range(len(new_l)):
        new_l[i] = new_l[i].split(':')

    #Loop to strip off extra spaces
    word = []
    meaning_of_the_word = []
    for i in range(len(new_l)):
        if len(new_l[i]) > 1:
            word.append(new_l[i][0].strip())
            meaning_of_the_word.append(new_l[i][1].strip())
    d=[]
    for i in range(len(word)):
        d.append({'word':word[i], 'meaning':meaning_of_the_word[i]})
    return [d,word]

def word_dictionary(word):
    import requests

    app_id  = "ab9b06e2"
    app_key  = "f49915ad409aa5421f0d41bc4cc4636b"

    language = 'en-us'
    word_id = word
    fields = 'definitions%2Cpronunciations%2Cexamples'
    strictMatch = 'false'
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    ans = r.json()
    # print("code {}\n".format(r.status_code))
    # print("text \n" + r.text)
    # print("json \n" + json.dumps(r.json()))
    return [r,ans]

# y = word_dictionary('game')
# print(type(y))
# print(y.text)

# word_dictionary('new')

# input()

# s = {"id": "new", "metadata": {"operation": "retrieve", "provider": "Oxford University Press", "schema": "RetrieveEntry"}, "results": [{"id": "new", "language": "en-us", "lexicalEntries": [{"entries": [{"pronunciations": [{"dialects": ["American English"], "phoneticNotation": "respell", "phoneticSpelling": "no\u035eo"}, {"audioFile": "https://audio.oxforddictionaries.com/en/mp3/pneu__us_1.mp3", "dialects": ["American English"], "phoneticNotation": "IPA", "phoneticSpelling": "nu"}], "senses": [{"definitions": ["not existing before; made, introduced, or discovered recently or now for the first time"], "examples": [{"text": "new crop varieties"}, {"text": "this tendency is not new"}, {"notes": [{"text": "as noun \"the new\"", "type": "wordFormNote"}], "text": "a fascinating mix of the old and the new"}], "id": "m_en_gbus0687710.006", "subsenses": [{"definitions": ["not previously used or owned"], "examples": [{"text": "a secondhand bus cost a fraction of a new one"}], "id": "m_en_gbus0687710.011"}, {"definitions": ["of recent origin or arrival"], "examples": [{"text": "a new baby"}], "id": "m_en_gbus0687710.012"}, {"definitions": ["(of vegetables) dug or harvested early in the season"], "examples": [{"text": "new potatoes"}], "id": "m_en_gbus0687710.013"}]}, {"definitions": ["already existing but seen, experienced, or acquired recently or now for the first time"], "examples": [{"text": "her new bike"}], "id": "m_en_gbus0687710.016", "subsenses": [{"definitions": ["unfamiliar or strange to (someone)"], "examples": [{"text": "a way of living that was new to me"}], "id": "m_en_gbus0687710.017"}, {"definitions": ["(of a person) inexperienced at or unaccustomed to doing (something)"], "examples": [{"text": "I'm quite new to gardening"}], "id": "m_en_gbus0687710.018"}, {"definitions": ["different from a recent previous one"], "examples": [{"text": "I have a new assistant"}, {"text": "this would be her new home"}], "id": "m_en_gbus0687710.019"}, {"definitions": ["in addition to another or others already existing"], "examples": [{"text": "recruiting new pilots overseas"}], "id": "m_en_gbus0687710.020"}, {"definitions": ["(in place names) discovered or founded later than and named after"], "examples": [{"text": "New York"}], "id": "m_en_gbus0687710.021"}]}, {"definitions": ["just beginning or beginning anew and regarded as better than what went before"], "examples": [{"text": "starting a new life"}, {"text": "the new South Africa"}], "id": "m_en_gbus0687710.024", "subsenses": [{"definitions": ["(of a person) reinvigorated or restored"], "examples": [{"text": "a bottle of pills would make him a new man"}], "id": "m_en_gbus0687710.025"}, {"definitions": ["superseding another or others of the same kind, and advanced in method or theory"], "examples": [{"text": "the new architecture"}], "id": "m_en_gbus0687710.026"}, {"definitions": ["reviving another or others of the same kind"], "examples": [{"text": "the New Bohemians"}], "id": "m_en_gbus0687710.027"}]}]}], "language": "en-us", "lexicalCategory": {"id": "adjective", "text": "Adjective"}, "text": "new"}, {"entries": [{"pronunciations": [{"dialects": ["American English"], "phoneticNotation": "respell", "phoneticSpelling": "no\u035eo"}, {"audioFile": "https://audio.oxforddictionaries.com/en/mp3/pneu__us_1.mp3", "dialects": ["American English"], "phoneticNotation": "IPA", "phoneticSpelling": "nu"}], "senses": [{"definitions": ["newly; recently"], "examples": [{"text": "new-mown hay"}, {"text": "new-fallen snow"}], "id": "m_en_gbus0687710.030"}]}], "language": "en-us", "lexicalCategory": {"id": "adverb", "text": "Adverb"}, "text": "new"}], "type": "headword", "word": "new"}], "word": "new"}













# x = function_to_render_correct_word_meaning('''

# New: this is new




#    old   : this is new old


# blank:iduhfiuh
# bguihg:dkjij
# dsioj:oivfj


# sdjfu:fojij


# ''')
# print(x)

import os
import google.generativeai as genai
import markdown

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
    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    prompt = "What is the meaning of " + word + ", explain with some examples in a sentence."
    response = model.generate_content(prompt)
    finalText = response.text
    finalText = markdown.markdown(response.text)
    # print(finalText)
    # finalText = format_markdown_to_html(finalText)
    return finalText

def format_markdown_to_html(mText):
    count_of_colon = 0
    index_of_first_colon = 0
    index_of_second_colon = 0
    count_of_last_full_stop = 0
    mText = mText.replace('*', '')
    mText = mText.replace('"', '')
    finalText = ""
    for i in range(len(mText)):
        if mText[i] == ".":
            count_of_last_full_stop = i
        if mText[i] == ":":
            count_of_colon = count_of_colon + 1
            if count_of_colon == 1:
                index_of_first_colon = i
            elif count_of_colon == 2:
                index_of_second_colon = i
                break
    finalText = '<p><strong>' + mText[:index_of_first_colon+1] +'</strong></p>' + mText[index_of_first_colon+1:count_of_last_full_stop+1] + '<p><strong>' + mText[count_of_last_full_stop+1:index_of_second_colon+1] +'</strong></p>' + mText[index_of_second_colon+1:]        
    finalText = finalText.replace('.', '.<br>')
    return finalText
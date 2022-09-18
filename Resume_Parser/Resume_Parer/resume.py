import pdfminer # pdf to text
import spacy #fro natural language processing # comes with pre trained models, without training ou own model
import re #regex for pattern search

import os #os file path , file manipulation
import pandas as pd #output csv

import pdf2txt

#converting pdf to text

def convert_pdf(f):
    output_filename = os.path.basename(os.path.splitext(f)[0]) + ".txt"
    output_filepath = os.path.join("output/txt/",output_filename)
    pdf2txt.main(args=[f, "--outfile",output_filepath]) #pdf to text and save it in the provided location
    print(output_filepath + " saved Successfully")
    return open(output_filepath).read()

#load the lang model
nlp = spacy.load("en_core_web_sm")

result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []} 
names = []
phones = []
emails = []
skills = []

def parse_content(text):
    skillset = re.compile('python|javascript|sql|hadoop|tableau|cpp|data')
    phone_num = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ == 'PERSON'][0]
    email = [word for word in doc if word.like_email == True][0]
    phone = str(re.findall(phone_num,text.lower()))# convert in string and lower case
    skills_list = re.findall(skillset,text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Resume Extraction completed successfully!!!")

# print(os.listdir('automate2/Resumes/'))
for file in os.listdir('Resumes/'):
    if file.endswith('.pdf'):
        print('Reading : ' + file)
        txt = convert_pdf(os.path.join('Resumes/',file))
        parse_content(txt)



result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills

result_df = pd.DataFrame(result_dict) # data frame to help convert it into csv

result_df.to_csv('output/csv/parsed_resumes.csv')























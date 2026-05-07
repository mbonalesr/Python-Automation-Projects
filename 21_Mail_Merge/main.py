
#Avoid C:\Users\mawic\OneDrive\Documentos\Python-Automation-Projects\21_Mail_Merge\Input\Names\invited_names.txt

with open(r'../Python-Automation-Projects/21_Mail_Merge/Input/Names/invited_names.txt',
           mode='r') as names_file:
    all_names = names_file.readlines()

with open(r'../Python-Automation-Projects/21_Mail_Merge/Input/Letters/starting_letter.txt',
           mode='r') as letter_file:
    letter = letter_file.read()

for name in all_names:
    clean_name = name.strip().title()
    with open(f'../Python-Automation-Projects/21_Mail_Merge/Output/ReadyToSend/letter_for_{clean_name}.txt', 
              mode='w') as custom_invitation:
        new_letter = letter.replace('[name]', clean_name)
        custom_invitation.write(new_letter)

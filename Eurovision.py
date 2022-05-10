import random
answers1 = ['Albania', 'Armenia', 'Austria', 'Bulgaria', 'Croatia', 'Denmark', 'Greece', 'Iceland', 'Latvia',
            'Lithuania', 'Moldova', 'The Netherlands', 'Norway', 'Portugal', 'Slovenia', 'Switzerland', 'Ukraine']
answers2 = ['Australia', 'Azerbaijan', 'Belgium', 'Cyprus', 'Czech Republic', 'Estonia', 'Finland', 'Georgia',
            'Ireland', 'Israel', 'Malta', 'Montenegro', 'North Macedonia', 'Poland', 'Romania', 'San Marino',
            'Serbia', 'Sweden']

print('Hello. I''m a magical ball and I can predict Eurovision results.')
name = input('What is your name? ')
print(f'Hello {name}')

again = 'y'
while again.lower() == 'y':
    question = input('Which semifinal is interested you? one/two ')
    if question.lower() == 'one':
        print('The qualifier from semifinal 1 is: ', *random.sample(answers1, 10))
    elif question.lower() == 'two':
        print('The qualifier from semifinal 2 is: ', *random.sample(answers2, 10))
    again = input('Do you want to try again? Y/N ')

print('See you next time!')
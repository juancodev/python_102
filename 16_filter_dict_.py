matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

#print(matches)

#print(len(matches))


def wins(obj):
  for i in obj:
    if i['home_team_result'] == 'Win':
      print(i)


wins(matches)

only_wins = list(
    filter(lambda item: item['home_team_result'] == 'Win', matches))

print(only_wins)

# ejercicio

def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda letter: len(letter) >= 4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)
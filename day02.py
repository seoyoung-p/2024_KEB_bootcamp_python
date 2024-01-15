x = 2
y = x + 5
print(y)

print(type(3.14)) #float
print(type(3.14) == float) #True
print(isinstance(3.14, float)) #True
print(isinstance("Inha", float)) #False
print(isinstance(55, float)) #False

artists = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artists
artists[2] = '세븐틴'
print(artists, groups)
artists[2] = '세븐틴'
print(artists, groups)
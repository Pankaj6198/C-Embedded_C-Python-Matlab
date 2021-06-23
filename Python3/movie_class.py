class Movie:
    ''' Movie class for demo purpose '''
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def disp(self):
        print(" Movie Name :",self.title)
        print(" Hero Name :",self.hero)
        print(" Heroine Name :",self.heroine)
list_of_movies=[]
while True:
    title=input("  Enter Movie Name: ")
    hero=input("  Enter Hero Name: ")
    heroine=input("  Enter Heroine Name: ")
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print(" Movie Added Successfully !!!! ")
    option=input("\n  Do u want to continue !!! [Yes/No] :")
    print()
    if option.lower()=='no':
        break
    
print("\t\t All Movies Information :\n")
for movie in list_of_movies:
    movie.disp()
    print()

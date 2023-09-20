# Write your solution here:


class Series: 
    def __init__(self, title: str, seasons: int, genre:list):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.ratings = []
        
    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
            
        
    def __str__(self):
        if len(self.ratings) > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genre)} \n{len(self.ratings)} ratings, average {sum(self.ratings)/len(self.ratings):.1f} points"
        else: 
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genre)} \nno ratings"

        
def minimum_grade(rating: float, series_list: list):
    min_grade = []
    for i in series_list:
        if sum(i.ratings)/len(i.ratings) >= rating:
            min_grade.append(i)
    return min_grade

def includes_genre(genre: str, series_list: list):
    genre_in_s = []
    for i in series_list:
        if genre in i.genre:
            genre_in_s.append(i)
    return genre_in_s
              
    
# dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# print(dexter)
        
        
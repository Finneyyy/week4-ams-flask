from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game=Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to the database"

@app.route('/read')
def read():
    all_games=Games.query.all()
    games_string=""
    for game in all_games:
        games_string+="<br>"+game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game=Games.query.first()
    first_game.name=name
    db.session.commit()
    return first_game.name

@app.route('/delete')
def delete():
    game_to_delete=Games.query.first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return "Deleted first game in the database"
    
@app.route('/list')
def games_list():
    list_games=Games.query.count()
    return f"There are {list_games} games in the database"

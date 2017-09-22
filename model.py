from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    Game.query.delete()

    portal = Game(game_id=1, name="Portal", description="Puzzle game with a cuddly companion cube.")
    rail_baron = Game(game_id=2, name="Rail Baron", description="Dominate railroad enterprise in America!")
    reigns = Game(game_id=3, name="Reigns", description="Rule a kingdom, keep everyone happy... or else.")

    db.session.add_all([portal, rail_baron, reigns])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."

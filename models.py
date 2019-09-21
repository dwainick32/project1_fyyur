from app import db
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Shows', backref='venue', passive_deletes=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    #implemented the shows field 
     

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    #the phone can be changed to a number 
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Shows', backref='artist', passive_deletes=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # implemented the shows field 

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
#will have to make a show class which will have a one to many relationship with the artist class. For every one show, there is one artist. An artist will have more than one show
#every venue will have multiple shows 
#There is also a one to many relationship with the venue. Every show will have one venue but every artist will have more than one show
class Shows(db.Model):
  __tablename__ = 'Shows'
  id = db.Column(db.Integer, primary_key=True)
  show_time = db.Column(db.DateTime, nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))
  #to get the venue name, I can apparently write a select statement that selects it. I, however, don't
  #think that is the best way to do it 
  #select name from artist where id = artist_id
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))

db.create_all()
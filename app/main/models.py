from app import db

class PackDay(db.Model):
    __tablename__ = 'packday'
    id = db.Column(db.Integer, primary_key=True)
    packege = db.Column(db.Integer)

    # pr = db.relationship('ToursInfo', backref='packday', uselist=False)
    #
    # def __repr__(self):
    #     return f'<ToursCat_id {ToursCat.id}>'


class ToursCat(db.Model):
    __tablename__ = 'tourscat'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    en_cat = db.Column(db.String(100), nullable=False)
    ru_cat = db.Column(db.String(100), nullable=False)
    uz_cat = db.Column(db.String(100), nullable=False)
    day_pack = db.Column(db.Integer)

    # pr = db.relationship('ToursInfo', backref='tourscat', uselist=False)
    #
    # def __repr__(self):
    #     return f'<ToursCat_id {ToursCat.id}>'


class ToursInfo(db.Model):
    __tablename__ = 'toursinfo'
    id = db.Column(db.Integer, primary_key=True)
    ru_loc = db.Column(db.String(100), nullable=False) #location
    en_loc = db.Column(db.String(100), nullable=False)
    uz_loc = db.Column(db.String(100), nullable=False)
    adult_pr = db.Column(db.Integer) # adult price
    kids_pr = db.Column(db.Integer) # price for kids
    photos = db.Column(db.String(255), nullable=False) #photos for tours
    ru_des = db.Column(db.Text, nullable=False)  # Descriptions
    en_des = db.Column(db.Text, nullable=False)
    uz_des = db.Column(db.Text, nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('tourscat.id')) # Foreign key for catigories from ToursCat table
    pack_id = db.Column(db.Integer, db.ForeignKey('packday.id')) # Foreign key for packeges from PackDay table
    reviews = db.Column(db.Integer)


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    job = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(50), nullable=False)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    psw = db.Column(db.String(50), nullable=False)


class Travlio(db.Model):
    __tablename__ = 'travlio'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    ru_address = db.Column(db.String(255), nullable=False)
    uz_address = db.Column(db.String(255), nullable=False)
    en_address = db.Column(db.String(255), nullable=False)
    tel1 = db.Column(db.Integer)
    tel2 = db.Column(db.Integer)
    ru_about = db.Column(db.String(255), nullable=False) #in the About page text wich contains info about company
    en_about = db.Column(db.String(255), nullable=False)
    uz_about = db.Column(db.String(255), nullable=False)
    facebook = db.Column(db.String(255), nullable=False) #links for social media
    telegram = db.Column(db.String(255), nullable=False)
    instagram = db.Column(db.String(255), nullable=False)
    youtube = db.Column(db.String(255), nullable=False)
    usd = db.Column(db.Integer)
    eur = db.Column(db.Integer)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    ru_ques = db.Column(db.String(255), nullable=False)
    en_ques = db.Column(db.String(255), nullable=False)
    uz_ques = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer) # different betweeen categories of questions

    # pr = db.relationship('Answer', backref='question', uselist=False)
    #
    # def __repr__(self):
    #     return f"<Question {Question.id}>"


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    ru_ans = db.Column(db.String(255), nullable=False)
    en_ans = db.Column(db.String(255), nullable=False)
    uz_ans = db.Column(db.String(255), nullable=False)
    que_id = db.Column(db.Integer, db.ForeignKey('question.id')) # choise the answer of wich question


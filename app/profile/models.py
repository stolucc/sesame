from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates

from app import db
from app.auth.models import User

from datetime import date

class Researcher(db.Model):

    __tablename__ = "researchers"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    user = db.relationship("User", backref=db.backref("researcher", uselist=False))


    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable=False)
    job_title = db.Column(db.String, nullable=False)
    prefix = db.Column(db.String, nullable=False)

    suffix = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=True)
    phone_ext = db.Column(db.String, nullable=True)
    orcid = db.Column(db.String, nullable=True)
    

class Education(db.Model):

    __tablename__ = "educations"
    
    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="education")
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    degree = db.Column(db.String, nullable=True)
    field_of_study = db.Column(db.String, nullable=True)
    institution = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    degree_award_year = db.Column(db.String, nullable=True)

class Employment(db.Model):

    __tablename__ = "employments"
    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="employment")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    institution = db.Column(db.String)
    location = db.Column(db.String)
    years = db.Column(db.Integer)
    
class Membership(db.Model):
    """The same as professional societies"""

    __tablename__ = "memberships"
    
    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="membership")
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    start_date  = db.Column(db.Date)
    end_date = db.Column(db.Date)
    society_name = db.Column(db.String)
    membership_type = db.Column(db.String)

    @hybrid_property
    def status(self):
        today = date.today()
        return (today > self.start_date) and (today < self.end_date)

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        if type(end_date) == date:
            return end_date
        else:
            end_date_input = end_date.split("-")
            end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return end_date


class Award(db.Model):

    __tablename__ = "awards"
    
    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="award")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    year = db.Column(db.Integer)
    awarding_body = db.Column(db.String)
    details = db.Column(db.String)
    team_member_name = db.Column(db.String)

class FundingDiversification(db.Model):

    __tablename__ = "funding_diversification"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="funding_diversification")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    amount = db.Column(db.Integer)
    funding_body = db.Column(db.String)
    funding_programme = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

    @hybrid_property
    def status(self):
        today = date.today()
        return (today > start_date) and (today < end_date)

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        if type(end_date) == date:
            return end_date
        else:
            end_date_input = end_date.split("-")
            end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return end_date


class TeamMember(db.Model):

    __tablename__ = "team_member"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="team_member")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    start_date = db.Column(db.Date)
    departure_date = db.Column(db.Date)
    name = db.Column(db.String)
    position = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("departure_date")
    def validate_departure_date(self, key, departure_date):
        if type(departure_date) == date:
            return departure_date
        else:
            departure_date_input = end_date.split("-")
            departure_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return departure_date


class Impact(db.Model):

    __tablename__ = "impacts"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="impact")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    title = db.Column(db.String)
    category = db.Column(db.String)
    primary_beneficiary = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))


class Innovation(db.Model):

    __tablename__ = "inovations_and_commercialisation"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="innovation")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    year = db.Column(db.Integer)
    innovation_type = db.Column(db.String)
    title = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

class Publication(db.Model):

    __tablename__ = "publications"
    
    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="publication")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    year = db.Column(db.Integer)

    original_article = db.Column(db.String)
    review_article = db.Column(db.String)
    conference_paper = db.Column(db.String)
    book = db.Column(db.String)
    technical_report = db.Column(db.String)

    title = db.Column(db.String)
    journal_name = db.Column(db.String)

    is_published = db.Column(db.Boolean)
    in_press = db.Column(db.Boolean)
    DOI = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

class Presentation(db.Model):

    __tablename__ = "presentations"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="presentation")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    year = db.Column(db.Integer)
    title = db.Column(db.String)

    conference = db.Column(db.String)
    invited_seminar = db.Column(db.String)
    keynote = db.Column(db.String)
    organizing_body = db.Column(db.String)
    location = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

class AcademicCollaboration(db.Model):

    __tablename__ = "academic_collaborations"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="academic_collaboration")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    institution = db.Column(db.String)
    institution_dept = db.Column(db.String)
    location = db.Column(db.String)
    collaborator_name = db.Column(db.String)
    primary_goal = db.Column(db.String)
    interaction_frequency = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        if type(end_date) == date:
            return end_date
        else:
            end_date_input = end_date.split("-")
            end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return end_date


class NonAcademicCollaboration(db.Model):

    __tablename__ = "non_academic_collaborations"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="non_academic_collaboration")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    institution = db.Column(db.String)
    institution_dept = db.Column(db.String)
    location = db.Column(db.String)
    collaborator_name = db.Column(db.String)
    primary_goal = db.Column(db.String)
    interaction_frequency = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        if type(end_date) == date:
            return end_date
        else:
            end_date_input = end_date.split("-")
            end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return end_date


class Conference(db.Model):

    __tablename__ = "conferences"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="conference")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    title = db.Column(db.String)
    event_type = db.Column(db.String)
    role = db.Column(db.String)
    location = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        if type(end_date) == date:
            return end_date
        else:
            end_date_input = end_date.split("-")
            end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return end_date


class CommunicationOverview(db.Model):
    
    __tablename__ = "communication_overview"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="communication_overview")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    year = db.Column(db.Integer)
    num_of_public_lectures = db.Column(db.Integer)
    num_of_visits = db.Column(db.Integer)
    num_of_media_interactions = db.Column(db.Integer)

class SFIFundingRatio(db.Model):

    __tablename__ = "sfi_funding_ratios"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="sfi_funding_ratio")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    year = db.Column(db.Integer)
    percentage_of_annual_spend = db.Column(db.Integer)

class EducationAndPublicEngagement(db.Model):

    __tablename__ = "education_and_public_engagement"

    id = db.Column(db.Integer, primary_key=True)
    researcher = db.relationship("Researcher", backref="education_and_public_engagement")     
    researcher_id = db.Column(db.Integer, db.ForeignKey("researchers.user_id"))

    project_name = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    activity_type = db.Column(db.String)
    project_topic = db.Column(db.String)
    target_graphical_area = db.Column(db.String)
    primary_attribution = db.Column(db.Integer, db.ForeignKey("calls.id"))

    @validates("start_date")
    def validates_start_date(self, key, start_date):
        if type(start_date) == date:
            return start_date
        else:
            start_date_input = start_date.split("-")
            start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
            return start_date

    @validates("end_date")
    def validate_end_date(self, key, end_date):
        if type(end_date) == date:
            return end_date
        else:
            end_date_input = end_date.split("-")
            end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
            return end_date










class TeamMembers(db.Model):

    __tablename__ = 'team_members'
    
    member_id = db.Column(db.Integer, primary_key=True) #ID in team, not out of all members 
    start_date= db.Column(db.Date,nullable=True)  ##When inserting, datetime.date i think, not .datetime
    end_date = db.Column(db.Date,nullable=True)   ##
    name = db.Column(db.String(20),nullable=False)
    position = db.Column(db.String(80),nullable=False)
    primary_attribute = db.Column(db.String(12),nullable=True)
    researcher_id = db.Column(db.Integer, db.ForeignKey('researchers.user_id'), nullable = False)

    def __str__(self):
        return list(start_date, end_date, name, position, primary_attribute, researcher_id)


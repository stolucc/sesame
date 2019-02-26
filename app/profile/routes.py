from .forms import *
from . import profile
from .models import *
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from datetime import datetime, date
from sqlalchemy import inspect

@profile.route("add/education", methods=["GET", "POST"])
@login_required
def addEducation():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = EducationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        education = Education(researcher_id=researcher.user_id, degree=form.degree.data, field_of_study=form.field_of_study.data,
                              institution=form.institution.data, location=form.location.data, degree_award_year=form.degree_award_year.data)
        db.session.add(education)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addEducation"))
    return render_template("profile/add.html", form=form, title="Education")

@profile.route("add/employment", methods=["GET", "POST"])
def addEmployment():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = EmploymentForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        employment = Employment(researcher_id=researcher.user_id, institution=form.institution.data,
                                location=form.location.data, years=form.years.data)
        db.session.add(employment)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addEmployment"))
    return render_template("profile/add.html", form=form, title="Employment")

@profile.route("add/membership", methods=["GET", "POST"])
def addMembership():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = MembershipForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.end_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))

        membership = Membership(researcher_id=researcher.user_id, start_date=start_date,
                                end_date=end_date, society_name=form.society_name.data,
                                membership_type=form.membership_type.data)
        db.session.add(membership)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addMembership"))
    return render_template("profile/add.html", form=form, title="Membership")

@profile.route("add/award", methods=["GET", "POST"])
def addAward():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = AwardForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        award = Award(researcher_id=researcher.user_id, year=form.year.data,
                      awarding_body=form.awarding_body.data, details=form.details.data,
                      team_member_name=form.team_member_name.data)
        db.session.add(award)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addAward"))
    return render_template("profile/add.html", form=form, title="Award")

@profile.route("add/funding_diversification")
def addFundingDiversification():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = FundingDiversificationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.end_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))

        funding_diversification = FundingDiversification(researcher_id=researcher.user_id,
                                                         start_date=start_date,
                                                         end_date=end_date,
                                                         amount=form.amount.data,
                                                         funding_body=form.funding_body.data,
                                                         funding_programme=form.funding_programme.data,
                                                         primary_attribution=form.primary_attribution.data)
        db.session.add(funding_diversification)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addFundingDiversification"))
    return render_template("profile/add.html", form=form, title="Funding Diversification")

@profile.route("add/team_member", methods=["GET", "POST"])
def addTeamMember():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = TeamMemberForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.departure_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))

        team_member = TeamMember(researcher_id=researcher.user_id, start_date=start_date,
                                 departure_date=end_date, name=form.name.data,
                                 position=form.position.data, primary_attribution=form.primary_attribution.data)
        db.session.add(team_member)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addTeamMember"))
    return render_template("profile/add.html", form=form, title="Team Members")

@profile.route("add/impact", methods=["GET", "POST"])
def addImpact():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = ImpactForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        impact = Impact(researcher_id=researcher.user_id, title=form.title.data,
                        category=form.category.data, primary_beneficiary=form.primary_beneficiary.data,
                        primary_attribution=form.primary_attribution.data)
        db.session.add(impact)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addImpact"))
    return render_template("profile/add.html", form=form, title="Impact")

@profile.route("add/innovation", methods=["GET", "POST"])
def addInnovation():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = InnovationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        innovation = Innovation(researcher_id=researcher.user_id, year=form.year.data,
                                innovation_type=form.innovation_type.data, title=form.title.data,
                                primary_attribution=form.primary_attribution.data)
        db.session.add(innovation)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addInnovation"))
    return render_template("profile/add.html", form=form, title="Innovation")

@profile.route("add/publication", methods=["GET", "POST"])
def addPublication():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = PublicationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        publication = Publication(researcher_id=researcher.user_id, year=form.year.data,
                                  original_article=form.original_article.data, review_article=form.review_article.data,
                                  conference_paper=form.conference_paper.data,
                                  book=form.book.data, technical_report=form.technical_report.data,
                                  title=form.title.data, journal_name=form.journal_name.data,
                                  is_published=form.is_published.data, in_press=form.in_press.data,
                                  DOI=form.DOI.data, primary_attribution=form.primary_attribution.data)
        db.session.add(publication)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addPublication"))
    return render_template("profile/add.html", form=form, title="Publication")

@profile.route("add/presentation", methods=["GET", "POST"])
def addPresentation():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = PresentationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher

        presentation = Presentation(researcher_id=researcher.user_id, year=form.year.data,
                                    title=form.title.data, conference=form.conference.data,
                                    invited_seminar=form.invited_seminar.data,
                                    keynote=form.keynote.data,
                                    organising_body=form.invited_seminar.data,
                                    location=form.location.data,
                                    primary_attribution=form.primary_attribution.data)
        db.session.add(presentation)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addPresentation"))
    return render_template("profile/add.html", form=form, title="Presentation")

@profile.route("add/academic_collaboration", methods=["GET", "POST"])
def addAcademicCollaboration():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = AcademicCollaborationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.end_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
        academic_collaboration = AcademicCollaboration(researcher_id=researcher.id, start_date=start_date, end_date=end_date, institution=form.institution.data, location=form.location.data, collaborator_name=form.collaborator.data,
                                                              primary_goal=form.primary_goal.data, interaction_frequency=form.interaction_frequency.data, primary_attribution=form.primary_attribution.data)
        db.session.add(academic_collaboration)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addAcademicCollaboration"))
    return render_template("profile/add.html", form=form)

@profile.route("add/non_academic_collaboration", methods=["GET", "POST"])
def addNonAcademicCollaboration():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = NonAcademicCollaborationForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.end_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
        non_academic_collaboration = NonAcademicCollaboration(researcher_id=researcher.id, start_date=start_date, end_date=end_date, institution=form.institution.data, location=form.location.data, collaborator_name=form.collaborator.data,
                                                              primary_goal=form.primary_goal.data, interaction_frequency=form.interaction_frequency.data, primary_attribution=form.primary_attribution.data)
        db.session.add(non_academic_collaboration)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addNonAcademicCollaboration"))
    return render_template("profile/add.html", form=form)

@profile.route("add/conference", methods=["GET", "POST"])
def addConference():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = ConferenceForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.end_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))
        conference = Conference(researcher_id=researcher.id, start_date=start_date, end_date=end_date, title=form.title.data, event_type=form.event_type.data,
                                role=form.role.data, location=form.location.data, primary_attribution=form.primary_attribution.data)
        db.session.add(conference)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addConference"))
    return render_template("profile/add.html", form=form, title="Conference")

@profile.route("add/communication_overview")
def addCommunicationOverview():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = CommunicationOverviewForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        comm_overview = CommunicationOverview(researcher_id=researcher.id, year=form.year.data, num_of_public_lectures=form.num_of_public_lectures.data, num_of_visits=form)
        db.session.add(conference)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addCommuicationOverview"))
    return render_template("profile/add.html", form=form, title="Communication Overview")

@profile.route("add/sfi_funding_ratio", methods=["GET", "POST"])
def addSFIFundingRatio():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = SFIFundingRatioForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        fr = SFIFundingRatio(researcher_id=researcher.id, year=form.year.data, percentage_of_annual_spend=form.percentage_of_annual_spend.data) 
        db.session.add(fr)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addSFIFundingRatio"))
    return render_template("profile/add.html", form=form, title="SFI Funding Ratio")

@profile.route("add/educaiton_and_public_engagement", methods=["GET", "POST"])
def addEducationAndPublicEngagement():
    if current_user.role != "RESEARCHER":
        abort(403)
    form = EducationAndPublicEngagementForm()
    if request.method == "POST" and form.validate():
        researcher = current_user.researcher
        
        start_date_input = form.start_date.data.split("-")
        start_date = date(int(start_date_input[0]), int(start_date_input[1]), int(start_date_input[2]))
        end_date_input = form.end_date.data
        end_date = date(int(end_date_input[0]), int(end_date_input[1]), int(end_date_input[2]))

        epe = EducationAndPublicEngagement(researcher_id=researcher.id, project_name=form.project_name.data, start_date=start_date, end_date=end_date, activity_type=form.activity_type.data,
                                           project_topic=form.project_topic.data, target_graphical_area=form.target_graphical_area.data, primary_attribution=form.primary_attribution.data)
        db.session.add(epe)
        db.session.commit()
        flash("Your profile has been updated")
        return redirect(url_for("profile.addEducaitonAndPublicEngagement"))
    return render_template("profile/add.html", form=form, title="Education and Public Engagement")


@profile.route("view/<section>")
def view(section):
    
    sections = {"education": Education, "employment": Employment, "membership": Membership, "award": Award, "funding_diversification": FundingDiversification, "team_member": TeamMember, "impact": Impact, "innovation": Innovation, "publication": Publication, "presentation": Presentation, "academic_collaboration": AcademicCollaboration, "non_academic_collaboration": NonAcademicCollaboration, "conference": Conference, "communicaiton_overview": CommunicationOverview, "sfi_funding_ratio": SFIFundingRatio, "education_and_public_engagemnt": EducationAndPublicEngagement}
    if section not in sections:
        abort(404)
    labels = {'id': 'Id', 'researcher': 'Researcher', 'researcher_id': 'Researcher id', 'degree': 'Degree', 'field_of_study': 'Field of study', 'institution': 'Institution', 'location': 'Location', 'degree_award_year': 'Degree award year', 'years': 'Years', 'start_date': 'Start date', 'end_date': 'End date', 'society_name': 'Society name', 'membership_type': 'Membership type', 'year': 'Year', 'awarding_body': 'Awarding body', 'details': 'Details', 'team_member_name': 'Team member name', 'amount': 'Amount', 'funding_body': 'Funding body', 'funding_programme': 'Funding programme', 'primary_attribution': 'Primary attribution', 'departure_date': 'Departure date', 'name': 'Name', 'position': 'Position', 'title': 'Title', 'category': 'Category', 'primary_beneficiary': 'Primary beneficiary', 'innovation_type': 'Innovation type', 'original_article': 'Original article', 'review_article': 'Review article',
        'conference_paper': 'Conference paper', 'book': 'Book', 'technical_report': 'Technical report', 'journal_name': 'Journal name', 'is_published': 'Is published', 'in_press': 'In press', 'DOI': 'DOI', 'conference': 'Conference', 'invited_seminar': 'Invited seminar', 'keynote': 'Keynote', 'organizing_body': 'Organizing body', 'institution_dept': 'Institution departmentt', 'collaborator_name': 'Collaborator name', 'primary_goal': 'Primary goal', 'interaction_frequency': 'Interaction frequency', 'event_type': 'Event type', 'role': 'Role', 'num_of_public_lectures': 'Number of public lectures', 'num_of_visits': 'Number of visits', 'num_of_media_interactions': 'Number of media interactions', 'percentage_of_annual_spend': 'Percentage of annual spend', 'project_name': 'Project name', 'activity_type': 'Activity type', 'project_topic': 'Project topic', 'target_graphical_area': 'Target graphical area'}

    researcher = current_user.researcher
    models = getattr(researcher, section)
    mapper = inspect(sections[section])
    columns = mapper.attrs.items()

    data = []
    for obj in models:  
        data.append(dict())
        for c in columns:
            if c[0] not in ["researcher", "id", "researcher_id"]:
                data[-1][labels[c[0]]] = getattr(obj, c[0])  # data[the last dict in data][labels dict[column][name of column]] = the value of column in the section instance
    
    return render_template("profile/view.html", section=section, data=data)





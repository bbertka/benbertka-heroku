# try something like
from mitrend import Mitrend

def index():
    response.title = 'MiTrend Quickly'
    response.subtitle = 'Symmetrix Assessments Made Easy'
    return dict(form=form())

def createAssessment():
        try:
            # these are hardcoded variables for now
            device_type = 'Symmetrix'
            country='United States'
            timezone='US Eastern'
            city = 'Boston'
            state = 'MA'
            tags = ['MiTrend Mobile']

            files = request.vars['files'].split(',')
            attributes = {'origin':'mitrend.cfapps.io'}
            M = Mitrend(username=request.vars['username'],
                    password=request.vars['password'],
                    company=request.vars['company'],
                    assessment_name=request.vars['assessment_name'],
                    city=city,
                    country=country,
                    state=state,
                    timezone=timezone,
                    tags=tags,
                    attributes=attributes,
                    device_type=device_type,
                    files=files )

            M.create_submission()
            M.add_files()
            M.submit()
            if M.submission:
                response.flash="Success!"
            else:
                response.flash="Failure"
        except Exception as e:
            request.flash=e

def form():
    form=FORM(TABLE(TR("Mitrend Username:",INPUT(_type="text",_name="username",requires=IS_NOT_EMPTY())),
                    TR("Mitrend Password",INPUT(_type="password",_name="password",requires=IS_NOT_EMPTY())),
                    TR("Assessment Name:",INPUT(_type="text",_name="assessment_name",requires=IS_NOT_EMPTY())),
                    TR("Company:",INPUT(_type="text",_name="company",requires=IS_NOT_EMPTY())),
                    TR("Files (Comma Seperated FTP URL):",INPUT(_type="text",_name="files",requires=IS_NOT_EMPTY())),
                    TR("",INPUT(_type="submit",_value="SUBMIT"))))
    if form.accepts(request,session):
        createAssessment()
    elif form.errors:
        pass
        #response.flash="form is invalid"
    else:
        pass
        #response.flash="please fill the form"
    return dict(form=form)

from coach.models import Training_session 
def addimg(img):
    session=Training_session(img=img)
    session.save()
    return session
    
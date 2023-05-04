from server import models,schemas
from sqlalchemy.orm import Session

## For creating a New user
def create(request: schemas.CreateUser, db: Session):

    new_user = models.User(
                            name = request.name,
                            age = request.age,
                            sex = request.sex,
                            mobile = request.mobile,
                            govtID = request.govtID,
                            guardian = request.guardian,
                            email = request.email,
                            emergencyNumber = request.emergencyNumber,
                            address = request.address,
                            state = request.state,
                            city = request.city,
                            country = request.country,
                            pincode = request.pincode,
                            occupation = request.occupation,
                            religion = request.religion,
                            maritalStatus = request.maritalStatus,
                            bloodGroup = request.bloodGroup,
                            nationality = request.nationality
                            )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

## For getting the all the user details 
def get_all_user_profile(db: Session):
    users = db.query(models.User).all()
    return users
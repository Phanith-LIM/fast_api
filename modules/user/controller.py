from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from core.database import get_db
from modules.user.entity import User
from modules.user.model import UserModel

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get('')
def gets(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get('/{item_id}')
def get(item_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == item_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f'User with id {item_id} not found')
    return user


@router.put('/{item_id}')
def update(item_id: int, item: UserModel, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == item_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f'User with id {item_id} not found')

    for attr, value in item.model_dump().items():
        setattr(user, attr, value)

    db.commit()
    db.refresh(user)
    return user


@router.post('')
def create(item: UserModel, db: Session = Depends(get_db)):
    new_user = User(**item.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f'create new user {item}'


@router.delete('/{item_id}')
def delete(item_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == item_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f'User with id {item_id} not found')

    db.delete(user)
    db.commit()
    return {"message": f"User with id {item_id} has been deleted"}

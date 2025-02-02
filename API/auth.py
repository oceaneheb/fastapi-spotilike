from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

router = APIRouter(
	prefix="/auth",
	tags=["auth"]
)

SECRET_KEY = '3Z6gpUkVI4wvE5WL8X3KVpT7uRgfl341'
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

class CreateUserRequest(BaseModel):
	name: str
	email: str
	password: str

class Token(BaseModel):
	access_token: str
	token_type: str

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

db_dependencies = Annotated[Session, Depends(get_db)]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependencies, create_user_request: CreateUserRequest):
	create_user_model = User(name=create_user_request.name, email=create_user_request.email, password=bcrypt_context.hash(create_user_request.password))
	db.add(create_user_model)
	db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependencies):
	user = authenticate_user(form_data.username, form_data.password, db)
	if not user:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
	token = create_access_token(user.email, user.id, timedelta(minutes=30))
	return {"access_token": token, "token_type": "bearer"}

def authenticate_user(email: str, password: str, db):
	user = db.query(User).filter(User.email == email).first()
	if not user:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email")
	if not bcrypt_context.verify(password, user.password):
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
	return user

def create_access_token(email: str, user_id: int, expires_delta: timedelta):
	to_encode = {"sub": email, "user_id": user_id, "exp": datetime.utcnow() + expires_delta}
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		email: str = payload.get("sub")
		user_id: int = payload.get("user_id")
		if email is None or user_id is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
		return {"email": email, "user_id": user_id}
	except JWTError:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")

from datetime import datetime, timezone
from typing import List, Optional

from sqlmodel import Session, select

from app.auth import get_password_hash, verify_password
from app.models import (
    Project, 
    ProjectCreate, 
    ProjectUpdate, 
    User, 
    UserCreate,
    UserRole
)


# User CRUD operations
def get_user(db: Session, user_id: int) -> Optional[User]:
    """Get a user by ID."""
    return db.get(User, user_id)


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """Get a user by username."""
    return db.exec(select(User).where(User.username == username)).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """Get a list of users."""
    return db.exec(select(User).offset(skip).limit(limit)).all()


def create_user(db: Session, user: UserCreate) -> User:
    """Create a new user."""
    db_user = User(
        username=user.username,
        hashed_password=get_password_hash(user.password),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """Authenticate a user by username and password."""
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


# Project CRUD operations
def get_project(db: Session, project_id: int) -> Optional[Project]:
    """Get a project by ID."""
    return db.get(Project, project_id)


def get_projects(db: Session, skip: int = 0, limit: int = 100) -> List[Project]:
    """Get a list of projects."""
    return db.exec(select(Project).offset(skip).limit(limit)).all()


def get_user_projects(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Project]:
    """Get projects for a specific user."""
    return db.exec(
        select(Project)
        .where(Project.owner_id == user_id)
        .offset(skip)
        .limit(limit)
    ).all()


def create_project(db: Session, project: ProjectCreate, user_id: int) -> Project:
    """Create a new project."""
    db_project = Project(**project.model_dump(), owner_id=user_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def update_project(db: Session, project_id: int, project_update: ProjectUpdate) -> Optional[Project]:
    """Update a project."""
    db_project = get_project(db, project_id)
    if not db_project:
        return None
    
    project_data = project_update.model_dump(exclude_unset=True)
    for key, value in project_data.items():
        setattr(db_project, key, value)
    
    db_project.updated_at = datetime.now(timezone.utc)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int) -> bool:
    """Delete a project."""
    db_project = get_project(db, project_id)
    if not db_project:
        return False
    
    db.delete(db_project)
    db.commit()
    return True
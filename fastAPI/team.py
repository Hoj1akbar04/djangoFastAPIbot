from fastapi import APIRouter, HTTPException, status, Depends
from database import ENGINE, session
from models import User, Team
from fastapi.encoders import jsonable_encoder
from schemas import TeamM
from fastapi_jwt_auth import AuthJWT


session = session(bind=ENGINE)
team_router = APIRouter(prefix="/team")


@team_router.get("/")
def get_team(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    teams = session.query(Team).all()
    context = [
        {
            "id": team.id,
            "name": team.name,
            "slug": team.slug,
            "image": team.image,
            "title": team.title,
            "staff_type": team.staff_type

        }
        for team in teams
    ]

    return jsonable_encoder(context)


@team_router.post("/create")
def create_team(team: TeamM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        new_team = Team(
            name=team.name,
            slug=team.slug,
            image=team.image,
            title = team.title,
            staff_type = team.staff_type
        )

        session.add(new_team)
        session.commit()

        context = {
            "status_code": status.HTTP_201_CREATED,
            "msg": "Team created",
            "data": {
                "id": new_team.id,
                "name": new_team.name,
                "slug": new_team.slug,
                "image": new_team.image,
                "title": new_team.title,
                "staff_type": new_team.staff_type
            }
        }
        return context
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to create team")


@team_router.get("/{id}")
async def get_team_id(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    check_team = session.query(Team).filter(Team.id == id).first()
    if check_team:
        context = [
            {
                "id": check_team.id,
                "name": check_team.name,
                "slug": check_team.slug,
                "image": check_team.image,
                "title": check_team.title,
                "staff_type": check_team.staff_type,
            }
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="team not found")


@team_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, data: TeamM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        team = session.query(Team).filter(Team.id == id).first()
        if team:

            for key, value in data.dict(exclude_unset=True).items():
                setattr(team, key, value)

            session.commit()
            context = {
                    "status_code": 200,
                    "msg": "Team updated"
                }
            return jsonable_encoder(context)
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to update Team data for you")


@team_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_team(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        team = session.query(Team).filter(Team.id == id).first()
        if not team:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="bLOG not found")

        session.delete(team)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Team deleted"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to delete team data for you")


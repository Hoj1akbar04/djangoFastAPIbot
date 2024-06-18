from fastapi import APIRouter, HTTPException, status, Depends
from database import ENGINE, session
from models import Product, User, Comment, Blog
from fastapi.encoders import jsonable_encoder
from schemas import BlogM
from fastapi_jwt_auth import AuthJWT


session = session(bind=ENGINE)
blog_router = APIRouter(prefix="/blog")


@blog_router.get("/")
def get_blog(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    blogs = session.query(Blog).all()
    context = [
        {
            "id": blog.id,
            "name": blog.name,
            "slug": blog.slug,
            "image": blog.image,
            "who": blog.who,

        }
        for blog in blogs
    ]

    return jsonable_encoder(context)


@blog_router.post("/create")
def create_product(blog: BlogM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        new_blog = Blog(
            name=blog.name,
            slug=blog.slug,
            image=blog.image,
            who = blog.who
        )

        session.add(new_blog)
        session.commit()

        context = {
            "status_code": status.HTTP_201_CREATED,
            "msg": "Blog created",
            "data": {
                "id": new_blog.id,
                "name": new_blog.name,
                "slug": new_blog.slug,
                "image": new_blog.image,
                "who": new_blog.who
            }
        }
        return context
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to create blog")


@blog_router.get("/{id}")
async def get_blog_id(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    check_blog = session.query(Blog).filter(Blog.id == id).first()
    if check_blog:
        context = [
            {
                "id": check_blog.id,
                "name": check_blog.name,
                "slug": check_blog.slug,
                "image": check_blog.image,
                "who": check_blog.who,
            }
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="blog not found")


@blog_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, data: BlogM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        blog = session.query(Blog).filter(Blog.id == id).first()
        if blog:

            for key, value in data.dict(exclude_unset=True).items():
                setattr(blog, key, value)

            session.commit()
            context = {
                    "status_code": 200,
                    "msg": "Blog updated"
                }
            return jsonable_encoder(context)
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to update BLOG data for you")


@blog_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_BLOG(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        blog = session.query(Blog).filter(Blog.id == id).first()
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="bLOG not found")

        session.delete(blog)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Blog deleted"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to delete blog data for you")


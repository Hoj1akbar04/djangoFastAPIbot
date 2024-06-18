from fastapi import APIRouter, HTTPException, status, Depends
from database import ENGINE, session
from models import Product, User, Comment
from fastapi.encoders import jsonable_encoder
from schemas import ProductM, CommentM
from fastapi_jwt_auth import AuthJWT


session = session(bind=ENGINE)
comment_router = APIRouter(prefix="/comment")


@comment_router.get("/")
def get_comment(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    comments = session.query(Comment).all()
    context = [
        {
            "id": comment.id,
            "name": comment.name,
            "comment": comment.comment,
            "product_id": comment.product_id,
            "slug": comment.slug,
            "image": comment.image
        }
        for comment in comments
    ]

    return jsonable_encoder(context)


@comment_router.post("/create")
def create_comment(comment: CommentM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        # Check if product_id exists in products table
        product_exists = session.query(Product).filter(Product.id == comment.product_id).first()
        if not product_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product does not exist")

        new_comment = Comment(
            name=comment.name,
            comment=comment.comment,
            product_id=comment.product_id,
            slug=comment.slug,
            image=comment.image
        )

        session.add(new_comment)
        session.commit()

        context = {
            "status_code": status.HTTP_201_CREATED,
            "msg": "Comment created",
            "data": {
                "id": new_comment.id,
                "name": new_comment.name,
                "comment": new_comment.comment,
                "product_id": new_comment.product_id,
                "slug": new_comment.slug,
                "image": new_comment.image
            }
        }
        return context
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to create comment")


@comment_router.get("/{id}")
async def get_comment_id(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    check_comment = session.query(Comment).filter(Comment.id == id).first()
    if check_comment:
        context = [
            {
                "id": check_comment.id,
                "name": check_comment.name,
                "comment": check_comment.comment,
                "product_id": check_comment.product_id,
                "slug": check_comment.slug,
                "image": check_comment.image
            }
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="comment not found")


@comment_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_comment(id: int, data: CommentM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        comment = session.query(Comment).filter(Comment.id == id).first()
        if comment:

            for key, value in data.dict(exclude_unset=True).items():
                setattr(comment, key, value)

            session.commit()
            context = {
                    "status_code": 200,
                    "msg": "Comment updated"
                }
            return jsonable_encoder(context)
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to update comment data for you")


@comment_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_comment(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        comment = session.query(Comment).filter(Comment.id == id).first()
        if not comment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

        session.delete(comment)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Comment deleted"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to delete comment data for you")


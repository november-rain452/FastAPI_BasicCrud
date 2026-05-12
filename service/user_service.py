from repository import user_repo

def add_new_user(user_data,db):
    return user_repo.create_user(user_data,db)

def get_user_by_id(user_id,db):
    return user_repo.get_user_by_id(user_id,db)
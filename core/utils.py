
def get_usuario_upload_path(instance, filename):
    return 'usuarios/{user_id}/{filename}'.format(user_id=instance.user.id, filename=filename)

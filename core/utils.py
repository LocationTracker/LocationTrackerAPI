
def get_usuario_upload_path(instance, filename):
    return 'usuarios/{filename}'.format(user_id=instance.pk, filename=filename)

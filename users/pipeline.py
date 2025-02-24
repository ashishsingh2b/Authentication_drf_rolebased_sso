def store_user_role(backend, details, response, request, user=None, *args, **kwargs):
    role = request.GET.get('role')
    if role and user:
        user.profile.role = role  # Assuming you have a 'role' field in the User Profile model
        user.profile.save()

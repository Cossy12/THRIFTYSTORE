from django.contrib.auth.decorators import user_passes_test, login_required


def customer_required(view_func):
    active_required = user_passes_test(lambda u: u.is_active and u.is_customer, login_url='/accounts/signup/customer/', )
    decorated_view_func = login_required(active_required(view_func))
    return decorated_view_func


def manager_required(view_func):
    active_required = user_passes_test(lambda u: u.is_active and u.is_manager, login_url='/accounts/signup/plugmanager/', )
    decorated_view_func = login_required(active_required(view_func))
    return decorated_view_func

#http://127.0.0.1:8000/accounts/login/?next=/plugmanager/test/
#http://127.0.0.1:8000/accounts/signup/customer/?next=/plugmanager/test/
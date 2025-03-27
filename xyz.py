from django.contrib.auth.models import User
from service_requests.models import Customer

# Loop over all users and create a Customer if it doesn't exist
for user in User.objects.all():
    if not hasattr(user, 'customer'):
        Customer.objects.create(user=user)
        print(f"Customer created for user: {user.username}")

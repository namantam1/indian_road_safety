from django.contrib.auth.tokens import PasswordResetTokenGenerator \
     as tokengenerator


class EmailActivationTokenGenerator(tokengenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + 
            str(timestamp) + 
            str(user.is_active)
        )

emailactivationtokengenarator = EmailActivationTokenGenerator()
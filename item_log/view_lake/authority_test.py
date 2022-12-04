from django.contrib.auth.mixins import UserPassesTestMixin

class AuthorityTestMixin(UserPassesTestMixin):
    def test_func(self) -> bool:
        return self.request.user.is_superuser or self.request.user.is_staff
        
class SuperUserTestMixin(UserPassesTestMixin):
    def test_func(self) -> bool:
        return self.request.user.is_superuser
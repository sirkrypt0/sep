from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group


class UserProfileManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, first_name=None, last_name=None):
        if not username:
            raise ValueError(_('Users must have a username'))

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email=None, first_name=None, last_name=None):
        user = self.create_user(
            username=username,
            password=password,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.is_superuser = True
        user.is_staff = True
        user.save()
        # user.groups.add(Group.objects.get(name="Manager"))
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, verbose_name=_('username'))

    # null=True because certain external users don't have an address
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True, verbose_name=_('email address'))

    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Title"))
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("first name"))
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("last name"))

    language = models.CharField(max_length=8, blank=True, null=True, verbose_name=_("language"))

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name=_("active"))

    class Meta:
        ordering = ('last_name', 'first_name', 'username')
        verbose_name = _('user')
        verbose_name_plural = _('users')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff

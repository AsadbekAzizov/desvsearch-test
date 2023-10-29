from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='devsearch-test/profiles/',
        default='devsearch-test/profiles/user-default.png',
        null=True,
        blank=True)
    social_github = models.URLField(max_length=200, null=True, blank=True)
    social_facebook = models.URLField(max_length=200, null=True, blank=True)
    social_instagram = models.URLField(max_length=200, null=True, blank=True)
    social_telegram = models.URLField(max_length=200, null=True, blank=True)
    social_website = models.URLField(max_length=200, null=True, blank=True)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.user.username}"  # Ulug'bek Umaraliyev


class Project(models.Model):
    # OneToMany -> One profile - many projects
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='devsearch-test/projects/',
        default='devsearch-test/projects/project-default.jpg',
        null=True,
        blank=True
    )
    tags = models.ManyToManyField(to='Tag', blank=True)
    source_link = models.URLField(max_length=200, null=True, blank=True)
    demo_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    # OneToMany -> one profile - many skills
    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # OneToMany rel-ship -> one profile - many comments
    owner = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True)

    # OneToMany rel-ship -> one project - many comments
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} - {self.project.title} - {self.body[:30]} ...'
        #        Asadbek Azizov - DevSearch project - Hey ! Cool project, I was exci ...


class Tag(models.Model):
    # ManyToMany -> Many tags -> many project
    # Ex. One tag can be used in multiple projects and one project can use multiple tags
    # Ex. One parent can have multiple child objects and one child can have multiple parents
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



# Foreign Key
# OneToOne
# ManyToMany

# Profile
# Project
# Foreign Key (OneToMany)
# profile.project_set.all()


# Profile
# User
# OneToOne
# profile.user


# Project (Devsearch -> html, css, js, bootstrap, python, django)
# Tag
# ManyToMany
# project.tag.all()


















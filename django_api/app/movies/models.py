import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        db_table = 'content"."genre'
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class FilmType(models.TextChoices):
        MOVIE = "movie", _("Film")
        TV_SHOW = "tv_show", _("TV-show")

    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    creation_date = models.DateField(_("creation date"), blank=True)
    rating = models.FloatField(
        _("rating"),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    type = models.TextField(
        _("type"), choices=FilmType.choices, default=FilmType.MOVIE
    )
    genres = models.ManyToManyField(Genre, through="GenreFilmwork")
    persons = models.ManyToManyField("Person", through="PersonFilmwork")
    file_path = models.FileField(
        _("file"), blank=True, null=True, upload_to="movies/"
    )

    class Meta:
        db_table = 'content"."film_work'
        verbose_name = _("Filmwork")
        verbose_name_plural = _("Filmworks")

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey(Filmwork, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."genre_film_work'
        verbose_name = _("Genre filmwork")
        verbose_name_plural = _("Genres filmworks")


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.CharField(_("full name"), max_length=255)

    class Meta:
        db_table = 'content"."person'
        verbose_name = _("Person filmwork")
        verbose_name_plural = _("Persons filmworks")

    def __str__(self):
        return self.full_name


class Role(models.TextChoices):
    ACTOR = "actor", _("actor")
    DIRECTOR = "director", _("director")
    WRITER = "writer", _("writer")


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey(Filmwork, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(
        _("role"),
        max_length=10,
        choices=Role.choices,
        default=Role.ACTOR
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."person_film_work'
        constraints = [
            models.UniqueConstraint(
                fields=["film_work", "person", "role"],
                name="film_work_person_role_idx",
            ),
        ]
        verbose_name = _("Person - Filmwork")
        verbose_name_plural = _("Persons - Filmworks")

    def __str__(self):
        return "{film} - {person}".format(
            film=self.film_work.title, person=self.person.full_name
        )

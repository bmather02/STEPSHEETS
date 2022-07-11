from django.db import models
from django.urls import reverse
# Create your models here.
LEVELS = (
    (1, 'Absolute Beginner'),
    (2, 'Beginner'),
    (3, 'Improver'),
    (4, 'Improver/Intermediate'),
    (5, 'Intermediate'),
    (6, 'Intermediate/Advanced'),
    (7, 'Advanced'),
    (8, 'Advanced+'),
)

STYLES = (
    ('n/a', 'Not Specified'),
    ('cc', 'Cha Cha'),
    ('chl', 'Charleston'),
    ('cont', 'Contemporary'),
    ('ecs', 'East Coast Swing'),
    ('fox', 'Foxtrot'),
    ('hh', 'Hip-Hop'),
    ('dsc', 'Hustle/Disco'),
    ('nc2', 'Nightclub Two Step'),
    ('plk', 'Polka'),
    ('qs', 'Quickstep'),
    ('rmba', 'Rumba'),
    ('sal', 'Salsa/Mambo'),
    ('sba', 'Samba'),
    ('tgo', 'Tango'),
    ('2st', 'Two Step'),
    ('vw', 'Viennese Waltz'),
    ('wtz', 'Waltz'),
    ('wcs', 'West Coast Swing'),
    ('oth', 'Other'),
)

class Sheet(models.Model):
    title = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=4, choices=LEVELS, default=LEVELS[0][0])
    counts = models.IntegerField()
    walls = models.IntegerField()
    style = models.CharField(max_length=10, choices=STYLES, default=STYLES[0][0])
    content = models.TextField()

    def __str__(self):
        return self.title
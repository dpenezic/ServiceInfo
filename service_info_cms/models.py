from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

ICON_CATALOG = 'http://materializecss.com/icons.html'
RATING_CHOICES = [(1, '1 star'),
                  (2, '2 stars'),
                  (3, '3 stars'),
                  (4, '4 stars'),
                  (5, '5 stars')
                  ]

class IconNameExtension(PageExtension):
    icon_name = models.CharField(
        _('Materialize icon name'), max_length=80, null=False, blank=False,
        help_text=_('Choose an icon at ' + ICON_CATALOG))

extension_pool.register(IconNameExtension)


class RatingExtension(PageExtension):
    include_rating = models.BooleanField(default=False)

extension_pool.register(RatingExtension)


class PageRating(PageExtension):
    average_rating = models.DecimalField(default=False)
    num_ratings = IntegerField()
    rating_total = IntegerField()
    page_id = IntegerField()

    def update_rating_average(self):
        """find the average number of stars for this
           page and round to the closest integer"""
        return 3  # <<< TODO: calculate average

from django.core.exceptions import ImproperlyConfigured

class SelectRelatedMixin(object):
    """
    Mixin allows you to provide a tuple or list of related models to
    perform a select_related on.
    """
    select_related = None  # Default related fields to none

    def get_queryset(self):
        if self.select_related is None:
            # If no fields were provided, raise a configuration error
            raise ImproperlyConfigured(
                '{0} is missing the select_related property. This must be '
                'a tuple or list.'.format(self.__class__.__name__))

        if not isinstance(self.select_related, (tuple, list)):
            # If the select_related argument is *not* a tuple or list,
            # raise a configuration error.
            raise ImproperlyConfigured(
                "{0}'s select_related property must be a tuple or "
                "list.".format(self.__class__.__name__))

        # Get the current queryset of the view
        queryset = super(SelectRelatedMixin, self).get_queryset()

        if not self.select_related:
            warnings.warn('The select_related attribute is empty')
            return queryset

        return queryset.select_related(*self.select_related)

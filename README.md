# CMS Lab Members

CMS Lab Members is A Django app to extend [django-lab-members](https://github.com/mfcovington/django-lab-members) with django CMS-specific features.

## Quick start

- Ignore instructions for [django-lab-members](https://github.com/mfcovington/django-lab-members), the non-django CMS app that this app extends.

- [Install django CMS and start a project](http://docs.django-cms.org/en/latest/introduction/install.html), if one doesn't already exist.


- Unless you use this app as part of [djangocms-lab-site](https://github.com/mfcovington/djangocms-lab-site) or plan to style the app from scratch, you will want to choose the `Use Twitter Bootstrap Theme` option (when running `djangocms`) and then edit the resulting `templates/base.html`.

    - This will add style that looks like Bootstrap 2. To use Bootstrap 3 styling, remove the following line for the `bootstrap-theme.min.css` stylesheet from `templates/base.html`:

        ```python
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.x.x/css/bootstrap-theme.min.css">
        ```

    - The default menu settings for django CMS using Bootstrap will allow the user to access specific lab members via a dropdown menu, but will not give easy access to the summary page of all lab member. To fix this do one of the following:

        - In `templates/base.html`, change `{% show_menu 0 1 100 100 "menu.html" %}` to `{% show_menu 0 0 100 100 "menu.html" %}`, or

        - Use a split button dropdowns by changing that line to `{% show_menu 0 100 1 1 '_menu.html' %}` and populate `_menu.html` as done in [djangocms-lab-site](https://github.com/mfcovington/djangocms-lab-site/blob/develop/cms_lab_site/templates/_menu.html).

- Edit the project's `settings.py` file.

    - Add `cms_lab_members` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'cms_lab_members',
            'cms_lab_publications',
            'easy_thumbnails',
            'filer',
            'friendlytagloader',
            'lab_members',
            'taggit',
        )
        ```

    - Add `easy_thumbnail` settings: 

        ```python
        # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
        THUMBNAIL_HIGH_RESOLUTION = True
        THUMBNAIL_QUALITY = 95
        THUMBNAIL_PROCESSORS = (
            'easy_thumbnails.processors.colorspace',
            'easy_thumbnails.processors.autocrop',
            'filer.thumbnail_processors.scale_and_crop_with_subject_location',
            'easy_thumbnails.processors.filters',
        )
        THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
        THUMBNAIL_SUBDIR = 'versions'
        ```

    - Pre-populate placeholder content for research/personal interests and sidebar:

        ```python
        # Pre-populate placeholder content
        CMS_PLACEHOLDER_CONF = {
            # ...
            'research interests': {
                'default_plugins': [
                    {
                        'plugin_type': 'TextPlugin',
                        'values': {
                            'body':"<p><em>[Enter 'Edit Mode' and double-click here to add your research interests.]</em></p>",
                        },
                    },
                ],
            },
            'personal interests': {
                'default_plugins': [
                    {
                        'plugin_type': 'TextPlugin',
                        'values': {
                            'body':"<p><em>[Enter 'Edit Mode' and double-click here to add your personal interests.]</em></p>",
                        },
                    },
                ],
            },
            'scientist sidebar': {
                'default_plugins': [
                    {
                        'plugin_type': 'TextPlugin',
                        'values': {
                            'body':"<p><em>[Enter 'Edit Mode' and double-click here to add sidebar content.]</em></p>",
                        },
                    },
                ],
            },
        }
        ```

- Run `python manage.py makemigrations cms_lab_members` to create the cms_lab_members migrations.

- Run `python manage.py makemigrations lab_members` to create the lab_members migrations.

- Run `python manage.py makemigrations cms_lab_publications` to create the cms_lab_publications migrations.

- Run `python manage.py migrate` to create the lab_members models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and attach the `Lab Members App` under `Advanced Settings` for the page.

*Version 0.1.5*

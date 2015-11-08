# CMS Lab Members

CMS Lab Members is A Django app to extend [django-lab-members](https://github.com/mfcovington/django-lab-members) with django CMS-specific features.

## Quick start

- Edit the project's `settings.py` file.

    - Add `cms_lab_members` and its dependencies to your `INSTALLED_APPS` setting:

        ```python
        INSTALLED_APPS = (
            ...
            'lab_members',
            'cms_lab_members',
            'easy_thumbnails',
            'filer',
            'mptt',
            'friendlytagloader',
        )
        ```

    - Specify your media settings, if not already specified:

        ```python
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
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
            ...
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

- Run `python manage.py migrate` to create the lab_members models.

- Start the development server (`python manage.py runserver`) and visit http://127.0.0.1:8000/

- Create a CMS page and attach the `Lab Members App` under `Advanced Settings` for the page.

*Version 0.1.5*

<!-- @file Instructions for subtheming using the CDN Starterkit. -->
<!-- @defgroup subtheme_cdn -->
<!-- @ingroup subtheme -->
# gbifBootstrap

gbifBootStrap is the customised subtheme of Bootstrap for Drupal 7.

### References
- Drupal 7 Bootstrap development tutorial videos by Drupal Legoland Playlist: https://goo.gl/8qp7kl


### Modules

These modules were added or changed
- Font Awesome 7.x-3.10
- Empty Front Page 7.x-1.0
- Block languages 7.x-1.13 (activate)
- disable module comment
- Empty front Page

### Installation
These settings are needed after activating the theme
- Set CONTAINER to `fluid container`
- Uncheck `Logo`, `Site name`, `Site slogan` and `Short icon`

## CDN Starterkit

The CDN Starterkit is rather simple to set up. You don't have to do anything
until you wish to override the default [Drupal Bootstrap] base theme settings
or provide additional custom CSS.

- [Prerequisite](#prerequisite)
- [Override Styles](#styles)
- [Override Settings](#settings)
- [Override Templates and Theme Functions](#registry)

## Prerequisite
Read the @link subtheme Sub-theming @endlink parent topic.

## Override Styles {#styles}
Open `./subtheme/css/style.css` and modify the file to your liking.

## Override Settings {#settings}
Please refer to the @link subtheme_settings Sub-theme Settings @endlink topic.

## Override Templates and Theme Functions {#registry}
Please refer to the @link registry Theme Registry @endlink topic.

[Drupal Bootstrap]: https://www.drupal.org/project/bootstrap
[Bootstrap Framework]: https://getbootstrap.com/docs/3.4/
[jsDelivr CDN]: https://www.jsdelivr.com

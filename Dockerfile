FROM quay.io/numigi/odoo-public:11.0
MAINTAINER numigi <contact@numigi.com>

USER odoo
COPY hr_working_space /mnt/extra-addons/hr_working_space
COPY hr_event /mnt/extra-addons/hr_event

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo

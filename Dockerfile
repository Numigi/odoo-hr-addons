FROM quay.io/numigi/odoo-public:11.0
MAINTAINER numigi <contact@numigi.com>

USER root

COPY .docker_files/test-requirements.txt .
RUN pip3 install -r test-requirements.txt

USER odoo
COPY hr_event /mnt/extra-addons/hr_event
COPY hr_holidays_half_day /mnt/extra-addons/hr_holidays_half_day
COPY hr_working_space /mnt/extra-addons/hr_working_space

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo
